# mentio

Python client for the [Mentio API](https://docs.mentio.dev): social listening across Bluesky, Hacker News, Reddit, X, GitHub, Stack Overflow, DEV, YouTube, LinkedIn and news. Generated from the API's OpenAPI document and regenerated whenever the API changes, so it is always complete. Python 3.11+, sync and async, typed.

```bash
pip install mentio
```

```python
from mentio import Mentio

mentio = Mentio(api_key="mk_live_...")

for mention in mentio.mentions.search(platform="reddit", relevant=True, limit=25).data:
    print(mention.post.platform.value, mention.classification.relevance, mention.post.url)

keyword = mentio.keywords.create(term="acme", kind="brand")
mentio.mentions.update("mm_7f3a...", status="done")
summary = mentio.analytics.summary(range_="7d", compare=True, timezone="Europe/Madrid")
```

One object, one call per endpoint, grouped by resource: `keywords`, `mentions`, `people`, `segments`, `alerts`, `channels`, `company`, `analytics`, `api_keys`, `system`. Enum-valued arguments take plain strings, instants take a `datetime`, an ISO 8601 string or epoch milliseconds, bodies take a dict, a model or their fields as keyword arguments. A non-2xx raises `MentioError` with the API's `status`, `code` and `message`. `AsyncMentio` mirrors every call for `asyncio`.

The full guide is at [docs.mentio.dev/sdks/python](https://docs.mentio.dev/sdks/python).
