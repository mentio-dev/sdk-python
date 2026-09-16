import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.export_people_csv_keyword_kinds_item import (
    ExportPeopleCsvKeywordKindsItem,
)
from ...models.export_people_csv_never_keyword_kinds_item import (
    ExportPeopleCsvNeverKeywordKindsItem,
)
from ...models.export_people_csv_not_platforms_item import (
    ExportPeopleCsvNotPlatformsItem,
)
from ...models.export_people_csv_platform import ExportPeopleCsvPlatform
from ...models.export_people_csv_platforms_item import ExportPeopleCsvPlatformsItem
from ...models.export_people_csv_sort import ExportPeopleCsvSort
from ...models.export_people_csv_stages_item import ExportPeopleCsvStagesItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform: ExportPeopleCsvPlatform | Unset = UNSET,
    q: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    muted: bool | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    segment_id: str | Unset = UNSET,
    platforms: list[ExportPeopleCsvPlatformsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    min_mentions: int | Unset = UNSET,
    min_negative: int | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_platforms: list[ExportPeopleCsvNotPlatformsItem] | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    keyword_kinds: list[ExportPeopleCsvKeywordKindsItem] | Unset = UNSET,
    never_keyword_kinds: list[ExportPeopleCsvNeverKeywordKindsItem] | Unset = UNSET,
    new_since_days: int | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    stages: list[ExportPeopleCsvStagesItem] | Unset = UNSET,
    owner_ids: list[str] | None | Unset = UNSET,
    sort: ExportPeopleCsvSort | Unset = ExportPeopleCsvSort.MENTIONS,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_platform: str | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform.value

    params["platform"] = json_platform

    params["q"] = q

    params["tag"] = tag

    params["muted"] = muted

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    params["segmentId"] = segment_id

    json_platforms: list[str] | Unset = UNSET
    if not isinstance(platforms, Unset):
        json_platforms = []
        for platforms_item_data in platforms:
            platforms_item = platforms_item_data.value
            json_platforms.append(platforms_item)

    params["platforms"] = json_platforms

    json_tags: list[str] | None | Unset
    if isinstance(tags, Unset):
        json_tags = UNSET
    elif isinstance(tags, list):
        json_tags = tags

    else:
        json_tags = tags
    params["tags"] = json_tags

    json_min_followers: int | None | Unset
    if isinstance(min_followers, Unset):
        json_min_followers = UNSET
    else:
        json_min_followers = min_followers
    params["minFollowers"] = json_min_followers

    json_max_followers: int | None | Unset
    if isinstance(max_followers, Unset):
        json_max_followers = UNSET
    else:
        json_max_followers = max_followers
    params["maxFollowers"] = json_max_followers

    params["minMentions"] = min_mentions

    params["minNegative"] = min_negative

    json_intents: list[str] | None | Unset
    if isinstance(intents, Unset):
        json_intents = UNSET
    elif isinstance(intents, list):
        json_intents = intents

    else:
        json_intents = intents
    params["intents"] = json_intents

    json_not_platforms: list[str] | Unset = UNSET
    if not isinstance(not_platforms, Unset):
        json_not_platforms = []
        for not_platforms_item_data in not_platforms:
            not_platforms_item = not_platforms_item_data.value
            json_not_platforms.append(not_platforms_item)

    params["notPlatforms"] = json_not_platforms

    json_not_tags: list[str] | None | Unset
    if isinstance(not_tags, Unset):
        json_not_tags = UNSET
    elif isinstance(not_tags, list):
        json_not_tags = not_tags

    else:
        json_not_tags = not_tags
    params["notTags"] = json_not_tags

    json_not_intents: list[str] | None | Unset
    if isinstance(not_intents, Unset):
        json_not_intents = UNSET
    elif isinstance(not_intents, list):
        json_not_intents = not_intents

    else:
        json_not_intents = not_intents
    params["notIntents"] = json_not_intents

    json_keyword_kinds: list[str] | Unset = UNSET
    if not isinstance(keyword_kinds, Unset):
        json_keyword_kinds = []
        for keyword_kinds_item_data in keyword_kinds:
            keyword_kinds_item = keyword_kinds_item_data.value
            json_keyword_kinds.append(keyword_kinds_item)

    params["keywordKinds"] = json_keyword_kinds

    json_never_keyword_kinds: list[str] | Unset = UNSET
    if not isinstance(never_keyword_kinds, Unset):
        json_never_keyword_kinds = []
        for never_keyword_kinds_item_data in never_keyword_kinds:
            never_keyword_kinds_item = never_keyword_kinds_item_data.value
            json_never_keyword_kinds.append(never_keyword_kinds_item)

    params["neverKeywordKinds"] = json_never_keyword_kinds

    params["newSinceDays"] = new_since_days

    json_link_hosts: list[str] | None | Unset
    if isinstance(link_hosts, Unset):
        json_link_hosts = UNSET
    elif isinstance(link_hosts, list):
        json_link_hosts = link_hosts

    else:
        json_link_hosts = link_hosts
    params["linkHosts"] = json_link_hosts

    json_stages: list[str] | Unset = UNSET
    if not isinstance(stages, Unset):
        json_stages = []
        for stages_item_data in stages:
            stages_item = stages_item_data.value
            json_stages.append(stages_item)

    params["stages"] = json_stages

    json_owner_ids: list[str] | None | Unset
    if isinstance(owner_ids, Unset):
        json_owner_ids = UNSET
    elif isinstance(owner_ids, list):
        json_owner_ids = owner_ids

    else:
        json_owner_ids = owner_ids
    params["ownerIds"] = json_owner_ids

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/people/export.csv",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    platform: ExportPeopleCsvPlatform | Unset = UNSET,
    q: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    muted: bool | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    segment_id: str | Unset = UNSET,
    platforms: list[ExportPeopleCsvPlatformsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    min_mentions: int | Unset = UNSET,
    min_negative: int | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_platforms: list[ExportPeopleCsvNotPlatformsItem] | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    keyword_kinds: list[ExportPeopleCsvKeywordKindsItem] | Unset = UNSET,
    never_keyword_kinds: list[ExportPeopleCsvNeverKeywordKindsItem] | Unset = UNSET,
    new_since_days: int | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    stages: list[ExportPeopleCsvStagesItem] | Unset = UNSET,
    owner_ids: list[str] | None | Unset = UNSET,
    sort: ExportPeopleCsvSort | Unset = ExportPeopleCsvSort.MENTIONS,
) -> Response[ErrorResponse | str]:
    """Export people as CSV

     The same list as GET /v1/people (segmentId included) as CSV, one row per person with their contact
    columns: handle, followers, email, website, company, location, tags, then outreach stage, owner and
    last contacted. Capped at 5,000 people. At most 6 exports per minute per workspace; a 429 carries
    Retry-After.

    Args:
        platform (ExportPeopleCsvPlatform | Unset): People with an account on this platform.
        q (str | Unset): Matches the display name or the profile handle or URL, case-
            insensitively.
        tag (str | Unset): Only people carrying this tag (exact, case-sensitive).
        muted (bool | Unset): true: only muted people; false: only unmuted; omitted: everyone.
        since (datetime.datetime | Unset): Only people whose first matched mention is at or after
            this instant (ISO 8601, or epoch ms).
        segment_id (str | Unset): A saved segment applied on top of every other filter here.
            Unknown id: 404.
        platforms (list[ExportPeopleCsvPlatformsItem] | Unset): People with an account on any of
            these platforms. Repeatable, or comma-separated.
        tags (list[str] | None | Unset): People carrying any of these tags. Repeatable, or comma-
            separated.
        min_followers (int | None | Unset): At least this many followers. Unknown reach never
            matches.
        max_followers (int | None | Unset): At most this many followers.
        min_mentions (int | Unset): At least this many matched mentions.
        min_negative (int | Unset): At least this many negative mentions.
        intents (list[str] | None | Unset): At least one mention carrying any of these intents.
        not_platforms (list[ExportPeopleCsvNotPlatformsItem] | Unset): Nobody with an account on
            these platforms. Repeatable, or comma-separated.
        not_tags (list[str] | None | Unset): Nobody carrying any of these tags. Repeatable, or
            comma-separated.
        not_intents (list[str] | None | Unset): Nobody whose mentions carry any of these intents.
            Repeatable, or comma-separated.
        keyword_kinds (list[ExportPeopleCsvKeywordKindsItem] | Unset): Mentioned a keyword of any
            of these kinds.
        never_keyword_kinds (list[ExportPeopleCsvNeverKeywordKindsItem] | Unset): Never mentioned
            a keyword of these kinds.
        new_since_days (int | Unset): First seen within this many days.
        link_hosts (list[str] | None | Unset): People with at least one mention linking to any of
            these hosts, the host itself or a subdomain of it. Repeatable, or comma-separated.
        stages (list[ExportPeopleCsvStagesItem] | Unset): People at any of these outreach stages.
            Repeatable, or comma-separated.
        owner_ids (list[str] | None | Unset): People owned by any of these members (user ids);
            `none` matches people nobody owns. Repeatable, or comma-separated.
        sort (ExportPeopleCsvSort | Unset): mentions: most matches first. recent: last seen first.
            reach: most followers first, unknown last. new: first seen most recently first. Default:
            ExportPeopleCsvSort.MENTIONS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | str]
    """

    kwargs = _get_kwargs(
        platform=platform,
        q=q,
        tag=tag,
        muted=muted,
        since=since,
        segment_id=segment_id,
        platforms=platforms,
        tags=tags,
        min_followers=min_followers,
        max_followers=max_followers,
        min_mentions=min_mentions,
        min_negative=min_negative,
        intents=intents,
        not_platforms=not_platforms,
        not_tags=not_tags,
        not_intents=not_intents,
        keyword_kinds=keyword_kinds,
        never_keyword_kinds=never_keyword_kinds,
        new_since_days=new_since_days,
        link_hosts=link_hosts,
        stages=stages,
        owner_ids=owner_ids,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    platform: ExportPeopleCsvPlatform | Unset = UNSET,
    q: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    muted: bool | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    segment_id: str | Unset = UNSET,
    platforms: list[ExportPeopleCsvPlatformsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    min_mentions: int | Unset = UNSET,
    min_negative: int | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_platforms: list[ExportPeopleCsvNotPlatformsItem] | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    keyword_kinds: list[ExportPeopleCsvKeywordKindsItem] | Unset = UNSET,
    never_keyword_kinds: list[ExportPeopleCsvNeverKeywordKindsItem] | Unset = UNSET,
    new_since_days: int | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    stages: list[ExportPeopleCsvStagesItem] | Unset = UNSET,
    owner_ids: list[str] | None | Unset = UNSET,
    sort: ExportPeopleCsvSort | Unset = ExportPeopleCsvSort.MENTIONS,
) -> ErrorResponse | str | None:
    """Export people as CSV

     The same list as GET /v1/people (segmentId included) as CSV, one row per person with their contact
    columns: handle, followers, email, website, company, location, tags, then outreach stage, owner and
    last contacted. Capped at 5,000 people. At most 6 exports per minute per workspace; a 429 carries
    Retry-After.

    Args:
        platform (ExportPeopleCsvPlatform | Unset): People with an account on this platform.
        q (str | Unset): Matches the display name or the profile handle or URL, case-
            insensitively.
        tag (str | Unset): Only people carrying this tag (exact, case-sensitive).
        muted (bool | Unset): true: only muted people; false: only unmuted; omitted: everyone.
        since (datetime.datetime | Unset): Only people whose first matched mention is at or after
            this instant (ISO 8601, or epoch ms).
        segment_id (str | Unset): A saved segment applied on top of every other filter here.
            Unknown id: 404.
        platforms (list[ExportPeopleCsvPlatformsItem] | Unset): People with an account on any of
            these platforms. Repeatable, or comma-separated.
        tags (list[str] | None | Unset): People carrying any of these tags. Repeatable, or comma-
            separated.
        min_followers (int | None | Unset): At least this many followers. Unknown reach never
            matches.
        max_followers (int | None | Unset): At most this many followers.
        min_mentions (int | Unset): At least this many matched mentions.
        min_negative (int | Unset): At least this many negative mentions.
        intents (list[str] | None | Unset): At least one mention carrying any of these intents.
        not_platforms (list[ExportPeopleCsvNotPlatformsItem] | Unset): Nobody with an account on
            these platforms. Repeatable, or comma-separated.
        not_tags (list[str] | None | Unset): Nobody carrying any of these tags. Repeatable, or
            comma-separated.
        not_intents (list[str] | None | Unset): Nobody whose mentions carry any of these intents.
            Repeatable, or comma-separated.
        keyword_kinds (list[ExportPeopleCsvKeywordKindsItem] | Unset): Mentioned a keyword of any
            of these kinds.
        never_keyword_kinds (list[ExportPeopleCsvNeverKeywordKindsItem] | Unset): Never mentioned
            a keyword of these kinds.
        new_since_days (int | Unset): First seen within this many days.
        link_hosts (list[str] | None | Unset): People with at least one mention linking to any of
            these hosts, the host itself or a subdomain of it. Repeatable, or comma-separated.
        stages (list[ExportPeopleCsvStagesItem] | Unset): People at any of these outreach stages.
            Repeatable, or comma-separated.
        owner_ids (list[str] | None | Unset): People owned by any of these members (user ids);
            `none` matches people nobody owns. Repeatable, or comma-separated.
        sort (ExportPeopleCsvSort | Unset): mentions: most matches first. recent: last seen first.
            reach: most followers first, unknown last. new: first seen most recently first. Default:
            ExportPeopleCsvSort.MENTIONS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | str
    """

    return sync_detailed(
        client=client,
        platform=platform,
        q=q,
        tag=tag,
        muted=muted,
        since=since,
        segment_id=segment_id,
        platforms=platforms,
        tags=tags,
        min_followers=min_followers,
        max_followers=max_followers,
        min_mentions=min_mentions,
        min_negative=min_negative,
        intents=intents,
        not_platforms=not_platforms,
        not_tags=not_tags,
        not_intents=not_intents,
        keyword_kinds=keyword_kinds,
        never_keyword_kinds=never_keyword_kinds,
        new_since_days=new_since_days,
        link_hosts=link_hosts,
        stages=stages,
        owner_ids=owner_ids,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    platform: ExportPeopleCsvPlatform | Unset = UNSET,
    q: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    muted: bool | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    segment_id: str | Unset = UNSET,
    platforms: list[ExportPeopleCsvPlatformsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    min_mentions: int | Unset = UNSET,
    min_negative: int | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_platforms: list[ExportPeopleCsvNotPlatformsItem] | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    keyword_kinds: list[ExportPeopleCsvKeywordKindsItem] | Unset = UNSET,
    never_keyword_kinds: list[ExportPeopleCsvNeverKeywordKindsItem] | Unset = UNSET,
    new_since_days: int | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    stages: list[ExportPeopleCsvStagesItem] | Unset = UNSET,
    owner_ids: list[str] | None | Unset = UNSET,
    sort: ExportPeopleCsvSort | Unset = ExportPeopleCsvSort.MENTIONS,
) -> Response[ErrorResponse | str]:
    """Export people as CSV

     The same list as GET /v1/people (segmentId included) as CSV, one row per person with their contact
    columns: handle, followers, email, website, company, location, tags, then outreach stage, owner and
    last contacted. Capped at 5,000 people. At most 6 exports per minute per workspace; a 429 carries
    Retry-After.

    Args:
        platform (ExportPeopleCsvPlatform | Unset): People with an account on this platform.
        q (str | Unset): Matches the display name or the profile handle or URL, case-
            insensitively.
        tag (str | Unset): Only people carrying this tag (exact, case-sensitive).
        muted (bool | Unset): true: only muted people; false: only unmuted; omitted: everyone.
        since (datetime.datetime | Unset): Only people whose first matched mention is at or after
            this instant (ISO 8601, or epoch ms).
        segment_id (str | Unset): A saved segment applied on top of every other filter here.
            Unknown id: 404.
        platforms (list[ExportPeopleCsvPlatformsItem] | Unset): People with an account on any of
            these platforms. Repeatable, or comma-separated.
        tags (list[str] | None | Unset): People carrying any of these tags. Repeatable, or comma-
            separated.
        min_followers (int | None | Unset): At least this many followers. Unknown reach never
            matches.
        max_followers (int | None | Unset): At most this many followers.
        min_mentions (int | Unset): At least this many matched mentions.
        min_negative (int | Unset): At least this many negative mentions.
        intents (list[str] | None | Unset): At least one mention carrying any of these intents.
        not_platforms (list[ExportPeopleCsvNotPlatformsItem] | Unset): Nobody with an account on
            these platforms. Repeatable, or comma-separated.
        not_tags (list[str] | None | Unset): Nobody carrying any of these tags. Repeatable, or
            comma-separated.
        not_intents (list[str] | None | Unset): Nobody whose mentions carry any of these intents.
            Repeatable, or comma-separated.
        keyword_kinds (list[ExportPeopleCsvKeywordKindsItem] | Unset): Mentioned a keyword of any
            of these kinds.
        never_keyword_kinds (list[ExportPeopleCsvNeverKeywordKindsItem] | Unset): Never mentioned
            a keyword of these kinds.
        new_since_days (int | Unset): First seen within this many days.
        link_hosts (list[str] | None | Unset): People with at least one mention linking to any of
            these hosts, the host itself or a subdomain of it. Repeatable, or comma-separated.
        stages (list[ExportPeopleCsvStagesItem] | Unset): People at any of these outreach stages.
            Repeatable, or comma-separated.
        owner_ids (list[str] | None | Unset): People owned by any of these members (user ids);
            `none` matches people nobody owns. Repeatable, or comma-separated.
        sort (ExportPeopleCsvSort | Unset): mentions: most matches first. recent: last seen first.
            reach: most followers first, unknown last. new: first seen most recently first. Default:
            ExportPeopleCsvSort.MENTIONS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | str]
    """

    kwargs = _get_kwargs(
        platform=platform,
        q=q,
        tag=tag,
        muted=muted,
        since=since,
        segment_id=segment_id,
        platforms=platforms,
        tags=tags,
        min_followers=min_followers,
        max_followers=max_followers,
        min_mentions=min_mentions,
        min_negative=min_negative,
        intents=intents,
        not_platforms=not_platforms,
        not_tags=not_tags,
        not_intents=not_intents,
        keyword_kinds=keyword_kinds,
        never_keyword_kinds=never_keyword_kinds,
        new_since_days=new_since_days,
        link_hosts=link_hosts,
        stages=stages,
        owner_ids=owner_ids,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    platform: ExportPeopleCsvPlatform | Unset = UNSET,
    q: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    muted: bool | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    segment_id: str | Unset = UNSET,
    platforms: list[ExportPeopleCsvPlatformsItem] | Unset = UNSET,
    tags: list[str] | None | Unset = UNSET,
    min_followers: int | None | Unset = UNSET,
    max_followers: int | None | Unset = UNSET,
    min_mentions: int | Unset = UNSET,
    min_negative: int | Unset = UNSET,
    intents: list[str] | None | Unset = UNSET,
    not_platforms: list[ExportPeopleCsvNotPlatformsItem] | Unset = UNSET,
    not_tags: list[str] | None | Unset = UNSET,
    not_intents: list[str] | None | Unset = UNSET,
    keyword_kinds: list[ExportPeopleCsvKeywordKindsItem] | Unset = UNSET,
    never_keyword_kinds: list[ExportPeopleCsvNeverKeywordKindsItem] | Unset = UNSET,
    new_since_days: int | Unset = UNSET,
    link_hosts: list[str] | None | Unset = UNSET,
    stages: list[ExportPeopleCsvStagesItem] | Unset = UNSET,
    owner_ids: list[str] | None | Unset = UNSET,
    sort: ExportPeopleCsvSort | Unset = ExportPeopleCsvSort.MENTIONS,
) -> ErrorResponse | str | None:
    """Export people as CSV

     The same list as GET /v1/people (segmentId included) as CSV, one row per person with their contact
    columns: handle, followers, email, website, company, location, tags, then outreach stage, owner and
    last contacted. Capped at 5,000 people. At most 6 exports per minute per workspace; a 429 carries
    Retry-After.

    Args:
        platform (ExportPeopleCsvPlatform | Unset): People with an account on this platform.
        q (str | Unset): Matches the display name or the profile handle or URL, case-
            insensitively.
        tag (str | Unset): Only people carrying this tag (exact, case-sensitive).
        muted (bool | Unset): true: only muted people; false: only unmuted; omitted: everyone.
        since (datetime.datetime | Unset): Only people whose first matched mention is at or after
            this instant (ISO 8601, or epoch ms).
        segment_id (str | Unset): A saved segment applied on top of every other filter here.
            Unknown id: 404.
        platforms (list[ExportPeopleCsvPlatformsItem] | Unset): People with an account on any of
            these platforms. Repeatable, or comma-separated.
        tags (list[str] | None | Unset): People carrying any of these tags. Repeatable, or comma-
            separated.
        min_followers (int | None | Unset): At least this many followers. Unknown reach never
            matches.
        max_followers (int | None | Unset): At most this many followers.
        min_mentions (int | Unset): At least this many matched mentions.
        min_negative (int | Unset): At least this many negative mentions.
        intents (list[str] | None | Unset): At least one mention carrying any of these intents.
        not_platforms (list[ExportPeopleCsvNotPlatformsItem] | Unset): Nobody with an account on
            these platforms. Repeatable, or comma-separated.
        not_tags (list[str] | None | Unset): Nobody carrying any of these tags. Repeatable, or
            comma-separated.
        not_intents (list[str] | None | Unset): Nobody whose mentions carry any of these intents.
            Repeatable, or comma-separated.
        keyword_kinds (list[ExportPeopleCsvKeywordKindsItem] | Unset): Mentioned a keyword of any
            of these kinds.
        never_keyword_kinds (list[ExportPeopleCsvNeverKeywordKindsItem] | Unset): Never mentioned
            a keyword of these kinds.
        new_since_days (int | Unset): First seen within this many days.
        link_hosts (list[str] | None | Unset): People with at least one mention linking to any of
            these hosts, the host itself or a subdomain of it. Repeatable, or comma-separated.
        stages (list[ExportPeopleCsvStagesItem] | Unset): People at any of these outreach stages.
            Repeatable, or comma-separated.
        owner_ids (list[str] | None | Unset): People owned by any of these members (user ids);
            `none` matches people nobody owns. Repeatable, or comma-separated.
        sort (ExportPeopleCsvSort | Unset): mentions: most matches first. recent: last seen first.
            reach: most followers first, unknown last. new: first seen most recently first. Default:
            ExportPeopleCsvSort.MENTIONS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            q=q,
            tag=tag,
            muted=muted,
            since=since,
            segment_id=segment_id,
            platforms=platforms,
            tags=tags,
            min_followers=min_followers,
            max_followers=max_followers,
            min_mentions=min_mentions,
            min_negative=min_negative,
            intents=intents,
            not_platforms=not_platforms,
            not_tags=not_tags,
            not_intents=not_intents,
            keyword_kinds=keyword_kinds,
            never_keyword_kinds=never_keyword_kinds,
            new_since_days=new_since_days,
            link_hosts=link_hosts,
            stages=stages,
            owner_ids=owner_ids,
            sort=sort,
        )
    ).parsed
