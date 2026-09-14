# Mentio Python SDK

[![PyPI](https://img.shields.io/pypi/v/mentio?label=pypi)](https://pypi.org/project/mentio/)
[![Python](https://img.shields.io/pypi/pyversions/mentio)](https://pypi.org/project/mentio/)
[![license](https://img.shields.io/pypi/l/mentio)](./LICENSE)
[![docs](https://img.shields.io/badge/docs-docs.mentio.dev-1421b9)](https://docs.mentio.dev/sdks/python)

Social listening for developers, in Python. [Mentio](https://mentio.dev) watches Reddit, Hacker News, X, GitHub, Bluesky, LinkedIn, Stack Overflow, DEV, YouTube and news for your keywords and scores every mention for relevance, sentiment and intent. This package is the official Python client for its API: one object, one call per endpoint, generated from the OpenAPI document and regenerated whenever the API changes, so it is always complete. Python 3.11+, sync and async, typed.

## Installation

```bash
pip install mentio
```

## Quick start

```python
from mentio import Mentio

mentio = Mentio(api_key="mk_live_...")

# Track a keyword on two platforms.
keyword = mentio.keywords.create(term="acme cloud", kind="brand", platforms=["reddit", "x"])

# Read what arrived, relevant posts only, newest first.
for mention in mentio.mentions.search(platform="reddit", relevant=True, limit=25).data:
    print(mention.post.platform.value, mention.classification.relevance, mention.post.url)
```

An API key comes from the dashboard (Settings, API keys) or from `mentio.api_keys.create(...)` with an existing key. Every account starts with $5.80 of credit and no card.

## Configuration

```python
mentio = Mentio(
    api_key="mk_live_...",                # required
    base_url="https://api.mentio.dev",    # another deployment's host, if you run one
    timeout=30.0,                         # seconds, or None for no timeout
)
```

Enum-valued arguments take plain strings (`platform="reddit"`). Instants take a `datetime`, an ISO 8601 string, or epoch milliseconds. Bodies take a dict, a model, or their fields as keyword arguments.

## Examples

### Page through every mention of the last week

```python
from datetime import datetime, timedelta, timezone

since = datetime.now(timezone.utc) - timedelta(days=7)
cursor = None
while True:
    page = mentio.mentions.search(since=since, relevant=True, limit=100, cursor=cursor)
    for mention in page.data:
        print(mention.post.url)
    cursor = page.next_cursor
    if not cursor:
        break
```

### Filter by intent and sentiment

```python
hot = mentio.mentions.search(intent="buy_intent", sentiment="negative", min_followers=1000, sort="priority")
```

Intents are `buy_intent`, `question`, `complaint`, `praise` and `comparison`. `sort="priority"` puts fresh, relevant, high-reach posts first.

### Triage

```python
mentio.mentions.update("mm_7f3a...", status="done", note="replied 2026-09-14")
mentio.mentions.update("mm_9c1b...", status="ignored")
```

### An instant Slack alert for buying signals on Reddit

```python
slack = next(c for c in mentio.channels.list().data if c.type == "slack")

mentio.alerts.create(
    name="Reddit buying signals",
    mode="instant",
    filter={"platforms": ["reddit"], "intents": ["buy_intent"], "minRelevance": 40},
    channel_ids=[slack.id],
)
```

Slack, Telegram, email and webhook channels are created with `mentio.channels.create(...)`; `mentio.alerts.test(id)` sends a sample; `mentio.alerts.run(id)` sends a daily alert's last 24 hours now.

### Analytics

```python
summary = mentio.analytics.summary(range_="30d", compare=True, timezone="Europe/Madrid")
by_platform = mentio.analytics.breakdown(range_="30d", dimension="platform")
sov = mentio.analytics.share_of_voice(range_="90d")
```

### People

```python
people = mentio.people.list(platforms=["x"], min_followers=5000)
mentio.people.update(people.data[0].id, tags=["influencer"], muted=False)
```

### CSV export

```python
csv_text = mentio.mentions.export(since="2026-09-01T00:00:00Z")
```

## Async

`AsyncMentio` mirrors every call for `asyncio`:

```python
import asyncio
from mentio import AsyncMentio

async def main() -> None:
    mentio = AsyncMentio(api_key="mk_live_...")
    page = await mentio.mentions.search(relevant=True, limit=10)
    for mention in page.data:
        print(mention.post.url)

asyncio.run(main())
```

## Error handling

A non-2xx raises `MentioError` with the API's `status`, `code` and `message`:

```python
from mentio import Mentio, MentioError

try:
    mentio.keywords.create(term="acme", kind="brand")
except MentioError as err:
    if err.code == "duplicate_keyword":
        pass                          # already tracked
    elif err.code == "insufficient_balance":
        print("top up from Billing")
    elif err.code == "rate_limited":
        print("slow down")
    else:
        raise
```

The full catalog, with status and meaning, is at [docs.mentio.dev/errors](https://docs.mentio.dev/errors). Common codes: `unauthorized`, `forbidden`, `read_only_key`, `validation_error`, `not_found`, `invalid_cursor`, `rate_limited`, `duplicate_keyword`, `insufficient_balance`, `keyword_limit_reached`, `upstream_unavailable`, `internal_error`.

## SDK reference

| Resource | Methods |
| --- | --- |
| `mentio.keywords` | `create`, `list`, `get`, `update`, `delete` |
| `mentio.mentions` | `search`, `get`, `update`, `export` |
| `mentio.people` | `list`, `get`, `update`, `merge`, `split`, `export` |
| `mentio.segments` | `list`, `create`, `get`, `update`, `delete` |
| `mentio.alerts` | `list`, `create`, `get`, `update`, `delete`, `test`, `run` |
| `mentio.channels` | `list`, `create`, `get`, `update`, `delete`, `test`, `rotate_secret`, `deliveries` |
| `mentio.analytics` | `summary`, `series`, `breakdown`, `share_of_voice` |
| `mentio.company` | `get`, `update` |
| `mentio.api_keys` | `create`, `list`, `revoke` |
| `mentio.system` | `health` |

The generated low-level client and models live under `mentio.api` and `mentio.models` for anything the facade does not cover.

## MCP server

The same API is available to Claude Code, Cursor, Codex, claude.ai and ChatGPT as tools:

```bash
claude mcp add --transport http mentio https://mcp.mentio.dev/mcp
```

Guide: [docs.mentio.dev/mcp](https://docs.mentio.dev/mcp).

## Requirements

- Python 3.11+
- A Mentio API key

## Links

- [Documentation](https://docs.mentio.dev) and the [Python guide](https://docs.mentio.dev/sdks/python)
- [API reference](https://docs.mentio.dev/api/keywords/create-keyword) and the [OpenAPI document](https://api.mentio.dev/v1/openapi.json)
- [Dashboard](https://app.mentio.dev)
- [TypeScript SDK](https://github.com/mentio-dev/sdk), [CLI](https://github.com/mentio-dev/cli), [Claude Code skills](https://github.com/mentio-dev/claude-skills)

This repository is published from the Mentio monorepo on every release; regenerate from a checkout with `pnpm --filter @mentio-dev/sdk-python generate` (needs `uv`).

## License

MIT.
