/**
 * Writes mentio/_facade.py: `Mentio(api_key).keywords.create(term="acme")`
 * over the generated per-operation modules. Groups and method names follow
 * the CLI's noun:verb rule, so the three surfaces read alike
 * (`mentio keywords:create`, `mentio.keywords.create(...)`,
 * `createKeyword(...)`). Everything the facade needs to know about the
 * generated code (python parameter names, enum class names, response types)
 * is read back from the generated files, so it cannot drift from them.
 */
import { existsSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { commandName } from '../../cli/src/naming';
import { operationsFromDocument, type OpenApiDocument, type OpenApiSchema } from '../../cli/src/operations-from-spec';
import type { CliOperation } from '../../cli/src/operations-types';

const root = fileURLToPath(new URL('..', import.meta.url));
const doc = JSON.parse(readFileSync(`${root}/../sdk/openapi.json`, 'utf8')) as OpenApiDocument;
const operations = operationsFromDocument(doc);

const snake = (s: string): string =>
  s
    .replace(/([a-z0-9])([A-Z])/g, '$1_$2')
    .replace(/[^A-Za-z0-9]+/g, '_')
    .replace(/^_+|_+$/g, '')
    .toLowerCase();
const pascal = (s: string): string =>
  s
    .split(/[^A-Za-z0-9]+/)
    .filter(Boolean)
    .map((w) => w[0]!.toUpperCase() + w.slice(1))
    .join('');

const models = new Set((readFileSync(`${root}/mentio/models/__init__.py`, 'utf8').match(/import (\w+)/g) ?? []).map((m) => m.slice(7)));
const apiDirs = new Set(readdirSync(`${root}/mentio/api`).filter((d) => !d.endsWith('.py')));

interface GeneratedModule {
  dir: string;
  module: string;
  /** Parameter names of _get_kwargs, path parameters first. */
  params: string[];
  /** The success type inside Response[...], ErrorResponse removed. */
  returns: string;
}

function readModule(op: CliOperation): GeneratedModule {
  const dir = snake(op.tag);
  if (!apiDirs.has(dir)) throw new Error(`no generated directory for tag ${op.tag} (looked for mentio/api/${dir})`);
  const module = snake(op.operationId);
  const path = `${root}/mentio/api/${dir}/${module}.py`;
  if (!existsSync(path)) throw new Error(`no generated module for ${op.operationId} at ${path}`);
  const source = readFileSync(path, 'utf8');
  const signature = source.slice(source.indexOf('def _get_kwargs('), source.indexOf(') -> dict[str, Any]:'));
  const params = [...signature.matchAll(/^\s+([a-z_][a-z0-9_]*): /gm)].map((m) => m[1]!);
  const ret = /def sync_detailed\([\s\S]*?\) -> Response\[(.*?)\]:/.exec(source)?.[1] ?? 'Any';
  const returns = ret
    .split('|')
    .map((t) => t.trim())
    .filter((t) => t !== 'ErrorResponse')
    .join(' | ');
  return { dir, module, params, returns: returns === '' ? 'None' : returns };
}

type Coercion = { py: string; fn: '_enum' | '_enum_list' | '_instant'; cls: string | null };

/** How each query parameter's Python value gets into the generated type. */
function coercions(op: CliOperation, generated: GeneratedModule): Coercion[] {
  const raw = doc.paths[op.path]?.[op.method.toLowerCase()];
  const out: Coercion[] = [];
  for (const param of raw?.parameters ?? []) {
    if (param.in !== 'query') continue;
    const py = [snake(param.name), `${snake(param.name)}_`].find((c) => generated.params.includes(c));
    if (!py) continue;
    const schema = param.schema;
    const enumClass = `${pascal(op.operationId)}${pascal(param.name)}`;
    if (schema?.format === 'date-time') out.push({ py, fn: '_instant', cls: null });
    else if (schema?.enum && models.has(enumClass)) out.push({ py, fn: '_enum', cls: enumClass });
    else if (schema?.type === 'array' && schema.items?.enum && models.has(`${enumClass}Item`)) out.push({ py, fn: '_enum_list', cls: `${enumClass}Item` });
  }
  return out;
}

type Body = { kind: 'model'; cls: string } | { kind: 'union'; byKind: Record<string, string> } | null;

function bodyOf(op: CliOperation): Body {
  const raw = doc.paths[op.path]?.[op.method.toLowerCase()];
  const schema = raw?.requestBody?.content?.['application/json']?.schema as (OpenApiSchema & { discriminator?: { mapping?: Record<string, string> } }) | undefined;
  if (!schema) return null;
  if (schema.$ref) return { kind: 'model', cls: schema.$ref.split('/').pop()! };
  if (schema.oneOf && schema.discriminator?.mapping) {
    return { kind: 'union', byKind: Object.fromEntries(Object.entries(schema.discriminator.mapping).map(([k, ref]) => [k, ref.split('/').pop()!])) };
  }
  const inline = `${pascal(op.operationId)}Body`;
  if (models.has(inline)) return { kind: 'model', cls: inline };
  throw new Error(`cannot name the body model of ${op.operationId}`);
}

const q = (s: string): string => JSON.stringify(s);
const indent = (text: string, n: number): string => text.split('\n').map((l) => (l ? ' '.repeat(n) + l : l)).join('\n');

function docstring(op: CliOperation, generated: GeneratedModule, body: Body): string {
  const lines = [op.summary.trim()];
  if (op.description) lines.push('', op.description.trim());
  const params = op.params.filter((p) => p.in === 'query');
  if (params.length > 0) {
    lines.push('', 'Keyword arguments (query):');
    for (const p of params) {
      const py = [snake(p.name), `${snake(p.name)}_`].find((c) => generated.params.includes(c)) ?? snake(p.name);
      lines.push(`  ${py}: ${(p.description ?? '').replace(/\s+/g, ' ').trim()}`.trimEnd());
    }
  }
  if (body && op.body) {
    lines.push('', body.kind === 'union' ? `Body: a dict with \`kind\` (${Object.keys(body.byKind).join(', ')}) or a model; fields may also be passed as keyword arguments:` : 'Body: a dict, a model, or the fields as keyword arguments:');
    for (const f of op.body.fields) lines.push(`  ${f.name}${f.required ? ' (required)' : ''}: ${(f.description ?? '').replace(/\s+/g, ' ').trim()}`.trimEnd());
  }
  return lines.join('\n').replace(/\\/g, '\\\\').replace(/"""/g, '\\"\\"\\"');
}

function bodyExpr(body: Exclude<Body, null>): string {
  if (body.kind === 'model') return `_m.${body.cls}`;
  return `{${Object.entries(body.byKind)
    .map(([k, cls]) => `${q(k)}: _m.${cls}`)
    .join(', ')}}`;
}

function methodSource(op: CliOperation, isAsync: boolean): string {
  const generated = readModule(op);
  const [, verb] = commandName(op).split(':') as [string, string];
  const name = snake(verb);
  const pathParams = op.params.filter((p) => p.in === 'path').map((p) => snake(p.name));
  const body = bodyOf(op);
  const coerce = coercions(op, generated);
  const fn = `_ops.${generated.dir}.${generated.module}.${isAsync ? 'asyncio_detailed' : 'sync_detailed'}`;
  const call = (args: string): string => (isAsync ? `_result(await ${fn}(${args}))` : `_result(${fn}(${args}))`);
  const returns = generated.returns
    .split(' | ')
    .map((t) => (t === 'Any' || t === 'None' || t === 'str' ? t : `_m.${t}`))
    .join(' | ');
  const head = isAsync ? 'async def' : 'def';
  const pathArgs = pathParams.map((p) => `${p}: str`).join(', ');
  const doc = `"""${docstring(op, generated, body)}"""`;
  const lines: string[] = [];
  if (body) {
    const bodyType = body.kind === 'model' ? `dict[str, Any] | _m.${body.cls} | None` : `dict[str, Any] | ${Object.values(body.byKind).map((c) => `_m.${c}`).join(' | ')} | None`;
    lines.push(`${head} ${name}(self${pathArgs ? `, ${pathArgs}` : ''}, body: ${bodyType} = None, **fields: Any) -> ${returns}:`);
    lines.push(indent(doc, 4));
    lines.push(`    return ${call(`${pathParams.join(', ')}${pathParams.length ? ', ' : ''}client=self._client, body=_body(${bodyExpr(body)}, body, fields)`)}`);
  } else {
    const hasQuery = op.params.some((p) => p.in === 'query');
    lines.push(`${head} ${name}(self${pathArgs ? `, ${pathArgs}` : ''}${hasQuery ? ', **params: Any' : ''}) -> ${returns}:`);
    lines.push(indent(doc, 4));
    if (coerce.length > 0) {
      lines.push(`    _coerce(params, {${coerce.map((c) => `${q(c.py)}: (${c.fn}, ${c.cls ? `_m.${c.cls}` : 'None'})`).join(', ')}})`);
    }
    lines.push(`    return ${call(`${pathParams.join(', ')}${pathParams.length ? ', ' : ''}client=self._client${hasQuery ? ', **params' : ''}`)}`);
  }
  return lines.join('\n');
}

const groups = new Map<string, CliOperation[]>();
for (const op of operations) {
  const [noun] = commandName(op).split(':') as [string, string];
  groups.set(noun, [...(groups.get(noun) ?? []), op]);
}
const groupOrder = ['keywords', 'mentions', 'people', 'segments', 'alerts', 'channels', 'company', 'analytics', 'api-keys', 'system'].filter((g) => groups.has(g));
for (const g of groups.keys()) if (!groupOrder.includes(g)) groupOrder.push(g);

function groupClass(noun: string, isAsync: boolean): string {
  const cls = `_${isAsync ? 'Async' : ''}${pascal(noun)}`;
  const ops = (groups.get(noun) ?? []).sort((a, b) => commandName(a).localeCompare(commandName(b)));
  const methods = ops.map((op) => indent(methodSource(op, isAsync), 4)).join('\n\n');
  return `class ${cls}:\n    """${noun}: ${ops.map((op) => snake(commandName(op).split(':')[1]!)).join(', ')}."""\n\n    def __init__(self, client: AuthenticatedClient) -> None:\n        self._client = client\n\n${methods}\n`;
}

function clientClass(isAsync: boolean): string {
  const name = isAsync ? 'AsyncMentio' : 'Mentio';
  const attrs = groupOrder.map((g) => `        self.${snake(g)} = _${isAsync ? 'Async' : ''}${pascal(g)}(self.client)`).join('\n');
  const enter = isAsync
    ? `    async def __aenter__(self) -> "AsyncMentio":\n        await self.client.__aenter__()\n        return self\n\n    async def __aexit__(self, *args: Any) -> None:\n        await self.client.__aexit__(*args)\n`
    : `    def __enter__(self) -> "Mentio":\n        self.client.__enter__()\n        return self\n\n    def __exit__(self, *args: Any) -> None:\n        self.client.__exit__(*args)\n`;
  return `class ${name}:
    """The Mentio API${isAsync ? ', awaitable' : ''}: one object, one call per endpoint, grouped by resource.

    ${isAsync ? 'client = AsyncMentio(api_key)\n    mentions = await client.mentions.search(platform="reddit", relevant=True)' : 'client = Mentio(api_key)\n    mentions = client.mentions.search(platform="reddit", relevant=True)'}

    Every call returns the parsed response (the generated model, a str for CSV
    exports, None for a 204) or raises MentioError with the API's status, code
    and message. Enum-valued arguments take plain strings, instants take a
    datetime, an ISO 8601 string or epoch milliseconds, bodies take a dict, a
    model, or their fields as keyword arguments. \`client\` is the underlying
    AuthenticatedClient for anything the facade does not cover.
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float | None = 30.0,
        headers: dict[str, str] | None = None,
        httpx_args: dict[str, Any] | None = None,
    ) -> None:
        self.client = AuthenticatedClient(
            base_url=base_url.rstrip("/"),
            token=api_key,
            prefix="Bearer",
            headers=headers or {},
            timeout=httpx.Timeout(timeout) if timeout is not None else None,
            httpx_args=httpx_args or {},
        )
${attrs}

${enter}`;
}

const header = `"""Convenience layer over the generated client: one object, one call per endpoint.

Generated by scripts/generate-facade.ts from the OpenAPI document; do not edit.
Groups and method names follow the CLI's noun:verb rule.
"""

from __future__ import annotations

import datetime as _dt
from typing import Any

import httpx

from . import api as _ops
from . import models as _m
from .client import AuthenticatedClient
from .types import UNSET, Response

DEFAULT_BASE_URL = "https://api.mentio.dev"


class MentioError(Exception):
    """A non-2xx answer: the HTTP \`status\`, the API's stable \`code\`, and its \`message\`."""

    def __init__(self, status: int, code: str, message: str) -> None:
        super().__init__(f"{code}: {message} (HTTP {status})")
        self.status = status
        self.code = code
        self.message = message


def _result(response: Response[Any]) -> Any:
    status = int(response.status_code)
    if 200 <= status < 300:
        return response.parsed
    parsed = response.parsed
    if isinstance(parsed, _m.ErrorResponse):
        raise MentioError(status, parsed.error.code, parsed.error.message)
    raise MentioError(status, f"http_{status}", response.content[:300].decode(errors="replace"))


def _enum(cls: type, value: Any) -> Any:
    if value is UNSET or value is None or isinstance(value, cls):
        return value
    return cls(value)


def _enum_list(cls: type, values: Any) -> Any:
    if values is UNSET or values is None:
        return values
    return [_enum(cls, v) for v in values]


def _instant(_cls: Any, value: Any) -> Any:
    if value is UNSET or value is None or isinstance(value, _dt.datetime):
        return value
    if isinstance(value, (int, float)):
        return _dt.datetime.fromtimestamp(value / 1000, tz=_dt.timezone.utc)
    if isinstance(value, _dt.date):
        return _dt.datetime(value.year, value.month, value.day, tzinfo=_dt.timezone.utc)
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    parsed = _dt.datetime.fromisoformat(text)
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=_dt.timezone.utc)


def _coerce(params: dict[str, Any], table: dict[str, tuple[Any, Any]]) -> None:
    for name, (fn, cls) in table.items():
        if name in params:
            params[name] = fn(cls, params[name])


def _body(target: Any, body: Any, fields: dict[str, Any]) -> Any:
    data = body if body is not None else fields
    if not isinstance(data, dict):
        return data
    if isinstance(target, dict):
        kind = data.get("kind")
        cls = target.get(kind)
        if cls is None:
            raise ValueError(f"kind must be one of: {', '.join(target)}")
        return cls.from_dict(data)
    return target.from_dict(data)


`;

// api/__init__.py is empty in the generated code; import the tag modules explicitly.
const imports = [...new Set(operations.map((op) => `${snake(op.tag)}.${snake(op.operationId)}`))]
  .sort()
  .map((m) => `import mentio.api.${m}  # noqa: F401`)
  .join('\n');

const body = [
  header.replace("from . import api as _ops\n", `from . import api as _ops  # noqa: F401\n`),
  imports,
  '',
  '',
  ...groupOrder.map((g) => groupClass(g, false)),
  ...groupOrder.map((g) => groupClass(g, true)),
  clientClass(false),
  clientClass(true),
].join('\n');

writeFileSync(`${root}/mentio/_facade.py`, body);
console.log(`Wrote mentio/_facade.py (${operations.length} operations in ${groupOrder.length} groups, sync and async)`);
