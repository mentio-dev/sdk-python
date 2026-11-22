from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_export_body_filter_countries_item import (
    CreateExportBodyFilterCountriesItem,
)
from ..models.create_export_body_filter_emotions_item import (
    CreateExportBodyFilterEmotionsItem,
)
from ..models.create_export_body_filter_keyword_kinds_item import (
    CreateExportBodyFilterKeywordKindsItem,
)
from ..models.create_export_body_filter_kind import CreateExportBodyFilterKind
from ..models.create_export_body_filter_not_countries_item import (
    CreateExportBodyFilterNotCountriesItem,
)
from ..models.create_export_body_filter_not_emotions_item import (
    CreateExportBodyFilterNotEmotionsItem,
)
from ..models.create_export_body_filter_not_keyword_kinds_item import (
    CreateExportBodyFilterNotKeywordKindsItem,
)
from ..models.create_export_body_filter_not_platforms_item import (
    CreateExportBodyFilterNotPlatformsItem,
)
from ..models.create_export_body_filter_not_sentiments_item import (
    CreateExportBodyFilterNotSentimentsItem,
)
from ..models.create_export_body_filter_platform import CreateExportBodyFilterPlatform
from ..models.create_export_body_filter_platforms_item import (
    CreateExportBodyFilterPlatformsItem,
)
from ..models.create_export_body_filter_range import CreateExportBodyFilterRange
from ..models.create_export_body_filter_sentiment import CreateExportBodyFilterSentiment
from ..models.create_export_body_filter_sentiments_item import (
    CreateExportBodyFilterSentimentsItem,
)
from ..models.create_export_body_filter_status import CreateExportBodyFilterStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateExportBodyFilter")


@_attrs_define
class CreateExportBodyFilter:
    """Which mentions: every filter of GET /v1/mentions, in the same vocabulary (a list as an array or comma-separated),
    viewId and alertId included. {} is every mention the list shows.

        Attributes:
            keyword_id (str | Unset): Deprecated: use keywordIds. Only matches of this keyword; combines with keywordIds as
                either.
            platform (CreateExportBodyFilterPlatform | Unset): Deprecated: use platforms. Only posts from this platform;
                combines with platforms as either.
            status (CreateExportBodyFilterStatus | Unset): Only mentions in this status. Omit for every status.
            relevant (bool | Unset): true: only mentions the classifier scored relevant; false: only the rest (unclassified
                included).
            sentiment (CreateExportBodyFilterSentiment | Unset): Deprecated: use sentiments. Only this sentiment; combines
                with sentiments as either.
            intent (str | Unset): Deprecated: use intents. Only mentions carrying this intent or topic tag, combined with
                intents as either (buy_intent, question, complaint, praise, comparison, churn_intent, bug_report, pricing,
                hiring, event, promotional, testimonial, industry_insight, launch, feedback).
            automated (bool | Unset): true: only mentions that read as machine-made (a bot account, a scheduled or templated
                post, AI-written text); false: only the rest, mentions judged before this existed included. Omitted: everything.
            organization (bool | Unset): true: only posts by companies, brands and organizations (a LinkedIn company page, a
                GitHub organization, a business account); false: only posts by people, mentions judged before this existed
                included. Omitted: everything.
            person_id (str | Unset): Only this person (an id from /v1/people), merged accounts included. Implies
                includeMuted.
            include_muted (bool | Unset): true: include mentions by people you muted, hidden by default: muted for the
                workspace, or for the mention's own keyword group.
            include_hidden (bool | Unset): true: include mentions their keyword's display lists hide (a language or country
                it does not show), hidden by default.
            include_duplicates (bool | Unset): true: list cross-posts (a mention whose duplicateOf is set) as mentions of
                their own. By default each is listed only in its original's duplicates.
            assignee_id (str | Unset): Only mentions assigned to this workspace member (user id).
            snoozed (bool | Unset): true: only mentions currently snoozed. Otherwise snoozed mentions stay out until they
                wake.
            not_authors (list[str] | None | Unset): Hide these authors: display names, handles or profile URLs. Repeatable,
                or one comma-separated value.
            exclude_authors (list[str] | None | Unset): Deprecated: use notAuthors, the same filter. Both may be sent; every
                author named in either is hidden.
            min_relevance (int | None | Unset): Only mentions scored at least this; unclassified ones are excluded.
            min_confidence (float | None | Unset): Only mentions whose classifier confidence is at least this, 0 to 1.
                Mentions without a confidence are excluded.
            min_followers (int | None | Unset): Only authors with at least this many followers. Unknown reach never passes.
            max_followers (int | None | Unset): Only authors with at most this many followers. Unknown reach never passes.
            kind (CreateExportBodyFilterKind | Unset): Only posts (post), only comments (comment) or only GitHub repository
                events (repository). Omitted: all.
            is_reply (bool | Unset): true: only replies and comments (posts answering another post); false: only top-level
                posts. Omitted: both.
            alert_id (str | Unset): Apply an alert rule's filter (an id from GET /v1/alerts) on top of the other filters:
                the same mentions the rule would send, for a feed-shaped export or a preview. Unknown ids are a 404.
            view_id (str | Unset): Apply a saved view's filter (an id from GET /v1/views) on top of the other filters, every
                condition ANDed: exactly what the view selects. Unknown ids are a 404.
            keyword_kinds (list[CreateExportBodyFilterKeywordKindsItem] | Unset): Only matches of keywords of any of these
                kinds: brand, competitor, topic. Repeatable, or comma-separated.
            not_keyword_kinds (list[CreateExportBodyFilterNotKeywordKindsItem] | Unset): Never matches of keywords of these
                kinds. Repeatable, or comma-separated.
            tags (list[str] | None | Unset): Only authors tagged with any of these (exact, case-sensitive), in the
                workspace's tags or those of the mention's own keyword group. Repeatable, or comma-separated.
            link_hosts (list[str] | None | Unset): Only posts linking to any of these hosts, the host itself or a subdomain
                of it (octolens.com also matches blog.octolens.com). Repeatable, or comma-separated.
            platforms (list[CreateExportBodyFilterPlatformsItem] | Unset): Only posts from any of these platforms.
            not_platforms (list[CreateExportBodyFilterNotPlatformsItem] | Unset): Never posts from these platforms.
            keyword_ids (list[str] | None | Unset): Only matches of any of these keywords.
            group_ids (list[str] | None | Unset): Only matches of keywords in any of these groups (grp_...). Repeatable, or
                comma-separated.
            not_group_ids (list[str] | None | Unset): Never matches of keywords in these groups.
            not_keyword_ids (list[str] | None | Unset): Never matches of these keywords.
            sentiments (list[CreateExportBodyFilterSentimentsItem] | Unset): Only these sentiments.
            not_sentiments (list[CreateExportBodyFilterNotSentimentsItem] | Unset): Never these sentiments. A mention the
                classifier has not scored yet still passes.
            emotions (list[CreateExportBodyFilterEmotionsItem] | Unset): Only mentions showing any of these emotions toward
                the keyword (joy, trust, anticipation, surprise, confusion, frustration, anger, fear, sadness, neutral). A
                mention whose emotion was not judged never passes.
            not_emotions (list[CreateExportBodyFilterNotEmotionsItem] | Unset): Never these emotions. A mention whose
                emotion was not judged still passes.
            intents (list[str] | None | Unset): Only mentions carrying any of these intent or topic tags.
            not_intents (list[str] | None | Unset): Never mentions carrying these intent or topic tags.
            not_link_hosts (list[str] | None | Unset): Never posts linking to these hosts, the host itself or a subdomain of
                it.
            subreddits (list[str] | None | Unset): Only Reddit posts from any of these subreddits: subreddits=SaaS,startups
                (names without the r/, any case). Every other post fails it. Repeatable, or comma-separated.
            not_subreddits (list[str] | None | Unset): Never Reddit posts from these subreddits; posts from other platforms
                still pass.
            not_tags (list[str] | None | Unset): Never authors tagged with any of these, in the workspace's tags or those of
                the mention's own keyword group.
            labels (list[str] | None | Unset): Only mentions carrying any of these labels (exact, case-sensitive).
                Repeatable, or comma-separated.
            not_labels (list[str] | None | Unset): Never mentions carrying any of these labels. Repeatable, or comma-
                separated.
            languages (list[str] | Unset): Only posts in any of these languages (ISO 639-1: en, es, de). A post whose
                language is unknown never passes.
            not_languages (list[str] | Unset): Never posts in these languages. A post whose language is unknown still
                passes.
            countries (list[CreateExportBodyFilterCountriesItem] | Unset): Only posts whose author is in any of these
                countries (ISO 3166-1 alpha-2: us, in, de), as the classifier read the author's profile and the post. A post
                whose country is unknown never passes.
            not_countries (list[CreateExportBodyFilterNotCountriesItem] | Unset): Never posts whose author is in these
                countries: notCountries=in. A post whose country is unknown still passes.
            ratings (list[int] | Unset): Only app store reviews with any of these star ratings (1 to 5): ratings=1,2 is the
                unhappy ones. Every other post fails it.
            not_ratings (list[int] | Unset): Never reviews with these star ratings (1 to 5): notRatings=5 hides the five
                star reviews. Posts that are not reviews still pass.
            min_likes (int | None | Unset): Only posts with at least this many likes (upvotes, reactions), as the platform
                reported them when the post was found. A post without that count never passes.
            min_reposts (int | None | Unset): Only posts with at least this many reposts (shares, retweets), as the platform
                reported them when the post was found. A post without that count never passes.
            min_replies (int | None | Unset): Only posts with at least this many replies (comments), as the platform
                reported them when the post was found. A post without that count never passes.
            min_quotes (int | None | Unset): Only posts with at least this many quotes, as the platform reported them when
                the post was found. A post without that count never passes.
            min_views (int | None | Unset): Only posts with at least this many views (plays), as the platform reported them
                when the post was found. A post without that count never passes.
            min_bookmarks (int | None | Unset): Only posts with at least this many bookmarks (saves), as the platform
                reported them when the post was found. A post without that count never passes.
            any_of (str | Unset): OR across groups of conditions, as URL-encoded JSON: a mention passes when one group
                holds, on top of every other filter. Each group holds view-filter conditions, no nesting. See
                [anyOf](/conventions#or-across-groups-anyof).
            q (str | Unset): Substring search in the post text or the author's name.
            range_ (CreateExportBodyFilterRange | Unset): A preset window ending now: 7d is today and the six days before,
                in `timezone`, as in the analytics reports. Ignored when from or to is given. Omit range, from and to for no
                window.
            from_ (str | Unset): Start, inclusive: a day (YYYY-MM-DD, from its first moment in `timezone`) or an instant
                (ISO 8601 with its offset, or epoch ms).
            to (str | Unset): End, inclusive: a day (YYYY-MM-DD, to its last moment in `timezone`) or an instant (ISO 8601
                with its offset, or epoch ms).
            timezone (str | Unset): IANA zone that days in range, from and to are cut in (Europe/Madrid). Default UTC.
            since (datetime.datetime | Unset): Deprecated: use from. Only posts published at or after this instant (ISO
                8601, or epoch ms).
            until (datetime.datetime | Unset): Deprecated: use to. Only posts published at or before this instant (ISO 8601,
                or epoch ms).
    """

    keyword_id: str | Unset = UNSET
    platform: CreateExportBodyFilterPlatform | Unset = UNSET
    status: CreateExportBodyFilterStatus | Unset = UNSET
    relevant: bool | Unset = UNSET
    sentiment: CreateExportBodyFilterSentiment | Unset = UNSET
    intent: str | Unset = UNSET
    automated: bool | Unset = UNSET
    organization: bool | Unset = UNSET
    person_id: str | Unset = UNSET
    include_muted: bool | Unset = UNSET
    include_hidden: bool | Unset = UNSET
    include_duplicates: bool | Unset = UNSET
    assignee_id: str | Unset = UNSET
    snoozed: bool | Unset = UNSET
    not_authors: list[str] | None | Unset = UNSET
    exclude_authors: list[str] | None | Unset = UNSET
    min_relevance: int | None | Unset = UNSET
    min_confidence: float | None | Unset = UNSET
    min_followers: int | None | Unset = UNSET
    max_followers: int | None | Unset = UNSET
    kind: CreateExportBodyFilterKind | Unset = UNSET
    is_reply: bool | Unset = UNSET
    alert_id: str | Unset = UNSET
    view_id: str | Unset = UNSET
    keyword_kinds: list[CreateExportBodyFilterKeywordKindsItem] | Unset = UNSET
    not_keyword_kinds: list[CreateExportBodyFilterNotKeywordKindsItem] | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    link_hosts: list[str] | None | Unset = UNSET
    platforms: list[CreateExportBodyFilterPlatformsItem] | Unset = UNSET
    not_platforms: list[CreateExportBodyFilterNotPlatformsItem] | Unset = UNSET
    keyword_ids: list[str] | None | Unset = UNSET
    group_ids: list[str] | None | Unset = UNSET
    not_group_ids: list[str] | None | Unset = UNSET
    not_keyword_ids: list[str] | None | Unset = UNSET
    sentiments: list[CreateExportBodyFilterSentimentsItem] | Unset = UNSET
    not_sentiments: list[CreateExportBodyFilterNotSentimentsItem] | Unset = UNSET
    emotions: list[CreateExportBodyFilterEmotionsItem] | Unset = UNSET
    not_emotions: list[CreateExportBodyFilterNotEmotionsItem] | Unset = UNSET
    intents: list[str] | None | Unset = UNSET
    not_intents: list[str] | None | Unset = UNSET
    not_link_hosts: list[str] | None | Unset = UNSET
    subreddits: list[str] | None | Unset = UNSET
    not_subreddits: list[str] | None | Unset = UNSET
    not_tags: list[str] | None | Unset = UNSET
    labels: list[str] | None | Unset = UNSET
    not_labels: list[str] | None | Unset = UNSET
    languages: list[str] | Unset = UNSET
    not_languages: list[str] | Unset = UNSET
    countries: list[CreateExportBodyFilterCountriesItem] | Unset = UNSET
    not_countries: list[CreateExportBodyFilterNotCountriesItem] | Unset = UNSET
    ratings: list[int] | Unset = UNSET
    not_ratings: list[int] | Unset = UNSET
    min_likes: int | None | Unset = UNSET
    min_reposts: int | None | Unset = UNSET
    min_replies: int | None | Unset = UNSET
    min_quotes: int | None | Unset = UNSET
    min_views: int | None | Unset = UNSET
    min_bookmarks: int | None | Unset = UNSET
    any_of: str | Unset = UNSET
    q: str | Unset = UNSET
    range_: CreateExportBodyFilterRange | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    timezone: str | Unset = UNSET
    since: datetime.datetime | Unset = UNSET
    until: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword_id = self.keyword_id

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        relevant = self.relevant

        sentiment: str | Unset = UNSET
        if not isinstance(self.sentiment, Unset):
            sentiment = self.sentiment.value

        intent = self.intent

        automated = self.automated

        organization = self.organization

        person_id = self.person_id

        include_muted = self.include_muted

        include_hidden = self.include_hidden

        include_duplicates = self.include_duplicates

        assignee_id = self.assignee_id

        snoozed = self.snoozed

        not_authors: list[str] | None | Unset
        if isinstance(self.not_authors, Unset):
            not_authors = UNSET
        elif isinstance(self.not_authors, list):
            not_authors = self.not_authors

        else:
            not_authors = self.not_authors

        exclude_authors: list[str] | None | Unset
        if isinstance(self.exclude_authors, Unset):
            exclude_authors = UNSET
        elif isinstance(self.exclude_authors, list):
            exclude_authors = self.exclude_authors

        else:
            exclude_authors = self.exclude_authors

        min_relevance: int | None | Unset
        if isinstance(self.min_relevance, Unset):
            min_relevance = UNSET
        else:
            min_relevance = self.min_relevance

        min_confidence: float | None | Unset
        if isinstance(self.min_confidence, Unset):
            min_confidence = UNSET
        else:
            min_confidence = self.min_confidence

        min_followers: int | None | Unset
        if isinstance(self.min_followers, Unset):
            min_followers = UNSET
        else:
            min_followers = self.min_followers

        max_followers: int | None | Unset
        if isinstance(self.max_followers, Unset):
            max_followers = UNSET
        else:
            max_followers = self.max_followers

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        is_reply = self.is_reply

        alert_id = self.alert_id

        view_id = self.view_id

        keyword_kinds: list[str] | Unset = UNSET
        if not isinstance(self.keyword_kinds, Unset):
            keyword_kinds = []
            for keyword_kinds_item_data in self.keyword_kinds:
                keyword_kinds_item = keyword_kinds_item_data.value
                keyword_kinds.append(keyword_kinds_item)

        not_keyword_kinds: list[str] | Unset = UNSET
        if not isinstance(self.not_keyword_kinds, Unset):
            not_keyword_kinds = []
            for not_keyword_kinds_item_data in self.not_keyword_kinds:
                not_keyword_kinds_item = not_keyword_kinds_item_data.value
                not_keyword_kinds.append(not_keyword_kinds_item)

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        link_hosts: list[str] | None | Unset
        if isinstance(self.link_hosts, Unset):
            link_hosts = UNSET
        elif isinstance(self.link_hosts, list):
            link_hosts = self.link_hosts

        else:
            link_hosts = self.link_hosts

        platforms: list[str] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.value
                platforms.append(platforms_item)

        not_platforms: list[str] | Unset = UNSET
        if not isinstance(self.not_platforms, Unset):
            not_platforms = []
            for not_platforms_item_data in self.not_platforms:
                not_platforms_item = not_platforms_item_data.value
                not_platforms.append(not_platforms_item)

        keyword_ids: list[str] | None | Unset
        if isinstance(self.keyword_ids, Unset):
            keyword_ids = UNSET
        elif isinstance(self.keyword_ids, list):
            keyword_ids = self.keyword_ids

        else:
            keyword_ids = self.keyword_ids

        group_ids: list[str] | None | Unset
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        not_group_ids: list[str] | None | Unset
        if isinstance(self.not_group_ids, Unset):
            not_group_ids = UNSET
        elif isinstance(self.not_group_ids, list):
            not_group_ids = self.not_group_ids

        else:
            not_group_ids = self.not_group_ids

        not_keyword_ids: list[str] | None | Unset
        if isinstance(self.not_keyword_ids, Unset):
            not_keyword_ids = UNSET
        elif isinstance(self.not_keyword_ids, list):
            not_keyword_ids = self.not_keyword_ids

        else:
            not_keyword_ids = self.not_keyword_ids

        sentiments: list[str] | Unset = UNSET
        if not isinstance(self.sentiments, Unset):
            sentiments = []
            for sentiments_item_data in self.sentiments:
                sentiments_item = sentiments_item_data.value
                sentiments.append(sentiments_item)

        not_sentiments: list[str] | Unset = UNSET
        if not isinstance(self.not_sentiments, Unset):
            not_sentiments = []
            for not_sentiments_item_data in self.not_sentiments:
                not_sentiments_item = not_sentiments_item_data.value
                not_sentiments.append(not_sentiments_item)

        emotions: list[str] | Unset = UNSET
        if not isinstance(self.emotions, Unset):
            emotions = []
            for emotions_item_data in self.emotions:
                emotions_item = emotions_item_data.value
                emotions.append(emotions_item)

        not_emotions: list[str] | Unset = UNSET
        if not isinstance(self.not_emotions, Unset):
            not_emotions = []
            for not_emotions_item_data in self.not_emotions:
                not_emotions_item = not_emotions_item_data.value
                not_emotions.append(not_emotions_item)

        intents: list[str] | None | Unset
        if isinstance(self.intents, Unset):
            intents = UNSET
        elif isinstance(self.intents, list):
            intents = self.intents

        else:
            intents = self.intents

        not_intents: list[str] | None | Unset
        if isinstance(self.not_intents, Unset):
            not_intents = UNSET
        elif isinstance(self.not_intents, list):
            not_intents = self.not_intents

        else:
            not_intents = self.not_intents

        not_link_hosts: list[str] | None | Unset
        if isinstance(self.not_link_hosts, Unset):
            not_link_hosts = UNSET
        elif isinstance(self.not_link_hosts, list):
            not_link_hosts = self.not_link_hosts

        else:
            not_link_hosts = self.not_link_hosts

        subreddits: list[str] | None | Unset
        if isinstance(self.subreddits, Unset):
            subreddits = UNSET
        elif isinstance(self.subreddits, list):
            subreddits = self.subreddits

        else:
            subreddits = self.subreddits

        not_subreddits: list[str] | None | Unset
        if isinstance(self.not_subreddits, Unset):
            not_subreddits = UNSET
        elif isinstance(self.not_subreddits, list):
            not_subreddits = self.not_subreddits

        else:
            not_subreddits = self.not_subreddits

        not_tags: list[str] | None | Unset
        if isinstance(self.not_tags, Unset):
            not_tags = UNSET
        elif isinstance(self.not_tags, list):
            not_tags = self.not_tags

        else:
            not_tags = self.not_tags

        labels: list[str] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, list):
            labels = self.labels

        else:
            labels = self.labels

        not_labels: list[str] | None | Unset
        if isinstance(self.not_labels, Unset):
            not_labels = UNSET
        elif isinstance(self.not_labels, list):
            not_labels = self.not_labels

        else:
            not_labels = self.not_labels

        languages: list[str] | Unset = UNSET
        if not isinstance(self.languages, Unset):
            languages = self.languages

        not_languages: list[str] | Unset = UNSET
        if not isinstance(self.not_languages, Unset):
            not_languages = self.not_languages

        countries: list[str] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = []
            for countries_item_data in self.countries:
                countries_item = countries_item_data.value
                countries.append(countries_item)

        not_countries: list[str] | Unset = UNSET
        if not isinstance(self.not_countries, Unset):
            not_countries = []
            for not_countries_item_data in self.not_countries:
                not_countries_item = not_countries_item_data.value
                not_countries.append(not_countries_item)

        ratings: list[int] | Unset = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = self.ratings

        not_ratings: list[int] | Unset = UNSET
        if not isinstance(self.not_ratings, Unset):
            not_ratings = self.not_ratings

        min_likes: int | None | Unset
        if isinstance(self.min_likes, Unset):
            min_likes = UNSET
        else:
            min_likes = self.min_likes

        min_reposts: int | None | Unset
        if isinstance(self.min_reposts, Unset):
            min_reposts = UNSET
        else:
            min_reposts = self.min_reposts

        min_replies: int | None | Unset
        if isinstance(self.min_replies, Unset):
            min_replies = UNSET
        else:
            min_replies = self.min_replies

        min_quotes: int | None | Unset
        if isinstance(self.min_quotes, Unset):
            min_quotes = UNSET
        else:
            min_quotes = self.min_quotes

        min_views: int | None | Unset
        if isinstance(self.min_views, Unset):
            min_views = UNSET
        else:
            min_views = self.min_views

        min_bookmarks: int | None | Unset
        if isinstance(self.min_bookmarks, Unset):
            min_bookmarks = UNSET
        else:
            min_bookmarks = self.min_bookmarks

        any_of = self.any_of

        q = self.q

        range_: str | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.value

        from_ = self.from_

        to = self.to

        timezone = self.timezone

        since: str | Unset = UNSET
        if not isinstance(self.since, Unset):
            since = self.since.isoformat()

        until: str | Unset = UNSET
        if not isinstance(self.until, Unset):
            until = self.until.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyword_id is not UNSET:
            field_dict["keywordId"] = keyword_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status
        if relevant is not UNSET:
            field_dict["relevant"] = relevant
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment
        if intent is not UNSET:
            field_dict["intent"] = intent
        if automated is not UNSET:
            field_dict["automated"] = automated
        if organization is not UNSET:
            field_dict["organization"] = organization
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if include_muted is not UNSET:
            field_dict["includeMuted"] = include_muted
        if include_hidden is not UNSET:
            field_dict["includeHidden"] = include_hidden
        if include_duplicates is not UNSET:
            field_dict["includeDuplicates"] = include_duplicates
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if snoozed is not UNSET:
            field_dict["snoozed"] = snoozed
        if not_authors is not UNSET:
            field_dict["notAuthors"] = not_authors
        if exclude_authors is not UNSET:
            field_dict["excludeAuthors"] = exclude_authors
        if min_relevance is not UNSET:
            field_dict["minRelevance"] = min_relevance
        if min_confidence is not UNSET:
            field_dict["minConfidence"] = min_confidence
        if min_followers is not UNSET:
            field_dict["minFollowers"] = min_followers
        if max_followers is not UNSET:
            field_dict["maxFollowers"] = max_followers
        if kind is not UNSET:
            field_dict["kind"] = kind
        if is_reply is not UNSET:
            field_dict["isReply"] = is_reply
        if alert_id is not UNSET:
            field_dict["alertId"] = alert_id
        if view_id is not UNSET:
            field_dict["viewId"] = view_id
        if keyword_kinds is not UNSET:
            field_dict["keywordKinds"] = keyword_kinds
        if not_keyword_kinds is not UNSET:
            field_dict["notKeywordKinds"] = not_keyword_kinds
        if tags is not UNSET:
            field_dict["tags"] = tags
        if link_hosts is not UNSET:
            field_dict["linkHosts"] = link_hosts
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if not_platforms is not UNSET:
            field_dict["notPlatforms"] = not_platforms
        if keyword_ids is not UNSET:
            field_dict["keywordIds"] = keyword_ids
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if not_group_ids is not UNSET:
            field_dict["notGroupIds"] = not_group_ids
        if not_keyword_ids is not UNSET:
            field_dict["notKeywordIds"] = not_keyword_ids
        if sentiments is not UNSET:
            field_dict["sentiments"] = sentiments
        if not_sentiments is not UNSET:
            field_dict["notSentiments"] = not_sentiments
        if emotions is not UNSET:
            field_dict["emotions"] = emotions
        if not_emotions is not UNSET:
            field_dict["notEmotions"] = not_emotions
        if intents is not UNSET:
            field_dict["intents"] = intents
        if not_intents is not UNSET:
            field_dict["notIntents"] = not_intents
        if not_link_hosts is not UNSET:
            field_dict["notLinkHosts"] = not_link_hosts
        if subreddits is not UNSET:
            field_dict["subreddits"] = subreddits
        if not_subreddits is not UNSET:
            field_dict["notSubreddits"] = not_subreddits
        if not_tags is not UNSET:
            field_dict["notTags"] = not_tags
        if labels is not UNSET:
            field_dict["labels"] = labels
        if not_labels is not UNSET:
            field_dict["notLabels"] = not_labels
        if languages is not UNSET:
            field_dict["languages"] = languages
        if not_languages is not UNSET:
            field_dict["notLanguages"] = not_languages
        if countries is not UNSET:
            field_dict["countries"] = countries
        if not_countries is not UNSET:
            field_dict["notCountries"] = not_countries
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if not_ratings is not UNSET:
            field_dict["notRatings"] = not_ratings
        if min_likes is not UNSET:
            field_dict["minLikes"] = min_likes
        if min_reposts is not UNSET:
            field_dict["minReposts"] = min_reposts
        if min_replies is not UNSET:
            field_dict["minReplies"] = min_replies
        if min_quotes is not UNSET:
            field_dict["minQuotes"] = min_quotes
        if min_views is not UNSET:
            field_dict["minViews"] = min_views
        if min_bookmarks is not UNSET:
            field_dict["minBookmarks"] = min_bookmarks
        if any_of is not UNSET:
            field_dict["anyOf"] = any_of
        if q is not UNSET:
            field_dict["q"] = q
        if range_ is not UNSET:
            field_dict["range"] = range_
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if since is not UNSET:
            field_dict["since"] = since
        if until is not UNSET:
            field_dict["until"] = until

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keyword_id = d.pop("keywordId", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: CreateExportBodyFilterPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = CreateExportBodyFilterPlatform(_platform)

        _status = d.pop("status", UNSET)
        status: CreateExportBodyFilterStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateExportBodyFilterStatus(_status)

        relevant = d.pop("relevant", UNSET)

        _sentiment = d.pop("sentiment", UNSET)
        sentiment: CreateExportBodyFilterSentiment | Unset
        if isinstance(_sentiment, Unset):
            sentiment = UNSET
        else:
            sentiment = CreateExportBodyFilterSentiment(_sentiment)

        intent = d.pop("intent", UNSET)

        automated = d.pop("automated", UNSET)

        organization = d.pop("organization", UNSET)

        person_id = d.pop("personId", UNSET)

        include_muted = d.pop("includeMuted", UNSET)

        include_hidden = d.pop("includeHidden", UNSET)

        include_duplicates = d.pop("includeDuplicates", UNSET)

        assignee_id = d.pop("assigneeId", UNSET)

        snoozed = d.pop("snoozed", UNSET)

        def _parse_not_authors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                not_authors_type_0 = cast(list[str], data)

                return not_authors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        not_authors = _parse_not_authors(d.pop("notAuthors", UNSET))

        def _parse_exclude_authors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_authors_type_0 = cast(list[str], data)

                return exclude_authors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude_authors = _parse_exclude_authors(d.pop("excludeAuthors", UNSET))

        def _parse_min_relevance(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_relevance = _parse_min_relevance(d.pop("minRelevance", UNSET))

        def _parse_min_confidence(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_confidence = _parse_min_confidence(d.pop("minConfidence", UNSET))

        def _parse_min_followers(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_followers = _parse_min_followers(d.pop("minFollowers", UNSET))

        def _parse_max_followers(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_followers = _parse_max_followers(d.pop("maxFollowers", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: CreateExportBodyFilterKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = CreateExportBodyFilterKind(_kind)

        is_reply = d.pop("isReply", UNSET)

        alert_id = d.pop("alertId", UNSET)

        view_id = d.pop("viewId", UNSET)

        _keyword_kinds = d.pop("keywordKinds", UNSET)
        keyword_kinds: list[CreateExportBodyFilterKeywordKindsItem] | Unset = UNSET
        if _keyword_kinds is not UNSET:
            keyword_kinds = []
            for keyword_kinds_item_data in _keyword_kinds:
                keyword_kinds_item = CreateExportBodyFilterKeywordKindsItem(
                    keyword_kinds_item_data
                )

                keyword_kinds.append(keyword_kinds_item)

        _not_keyword_kinds = d.pop("notKeywordKinds", UNSET)
        not_keyword_kinds: list[CreateExportBodyFilterNotKeywordKindsItem] | Unset = (
            UNSET
        )
        if _not_keyword_kinds is not UNSET:
            not_keyword_kinds = []
            for not_keyword_kinds_item_data in _not_keyword_kinds:
                not_keyword_kinds_item = CreateExportBodyFilterNotKeywordKindsItem(
                    not_keyword_kinds_item_data
                )

                not_keyword_kinds.append(not_keyword_kinds_item)

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_link_hosts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                link_hosts_type_0 = cast(list[str], data)

                return link_hosts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        link_hosts = _parse_link_hosts(d.pop("linkHosts", UNSET))

        _platforms = d.pop("platforms", UNSET)
        platforms: list[CreateExportBodyFilterPlatformsItem] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = CreateExportBodyFilterPlatformsItem(
                    platforms_item_data
                )

                platforms.append(platforms_item)

        _not_platforms = d.pop("notPlatforms", UNSET)
        not_platforms: list[CreateExportBodyFilterNotPlatformsItem] | Unset = UNSET
        if _not_platforms is not UNSET:
            not_platforms = []
            for not_platforms_item_data in _not_platforms:
                not_platforms_item = CreateExportBodyFilterNotPlatformsItem(
                    not_platforms_item_data
                )

                not_platforms.append(not_platforms_item)

        def _parse_keyword_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keyword_ids_type_0 = cast(list[str], data)

                return keyword_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keyword_ids = _parse_keyword_ids(d.pop("keywordIds", UNSET))

        def _parse_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_ids = _parse_group_ids(d.pop("groupIds", UNSET))

        def _parse_not_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                not_group_ids_type_0 = cast(list[str], data)

                return not_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        not_group_ids = _parse_not_group_ids(d.pop("notGroupIds", UNSET))

        def _parse_not_keyword_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                not_keyword_ids_type_0 = cast(list[str], data)

                return not_keyword_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        not_keyword_ids = _parse_not_keyword_ids(d.pop("notKeywordIds", UNSET))

        _sentiments = d.pop("sentiments", UNSET)
        sentiments: list[CreateExportBodyFilterSentimentsItem] | Unset = UNSET
        if _sentiments is not UNSET:
            sentiments = []
            for sentiments_item_data in _sentiments:
                sentiments_item = CreateExportBodyFilterSentimentsItem(
                    sentiments_item_data
                )

                sentiments.append(sentiments_item)

        _not_sentiments = d.pop("notSentiments", UNSET)
        not_sentiments: list[CreateExportBodyFilterNotSentimentsItem] | Unset = UNSET
        if _not_sentiments is not UNSET:
            not_sentiments = []
            for not_sentiments_item_data in _not_sentiments:
                not_sentiments_item = CreateExportBodyFilterNotSentimentsItem(
                    not_sentiments_item_data
                )

                not_sentiments.append(not_sentiments_item)

        _emotions = d.pop("emotions", UNSET)
        emotions: list[CreateExportBodyFilterEmotionsItem] | Unset = UNSET
        if _emotions is not UNSET:
            emotions = []
            for emotions_item_data in _emotions:
                emotions_item = CreateExportBodyFilterEmotionsItem(emotions_item_data)

                emotions.append(emotions_item)

        _not_emotions = d.pop("notEmotions", UNSET)
        not_emotions: list[CreateExportBodyFilterNotEmotionsItem] | Unset = UNSET
        if _not_emotions is not UNSET:
            not_emotions = []
            for not_emotions_item_data in _not_emotions:
                not_emotions_item = CreateExportBodyFilterNotEmotionsItem(
                    not_emotions_item_data
                )

                not_emotions.append(not_emotions_item)

        def _parse_intents(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                intents_type_0 = cast(list[str], data)

                return intents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        intents = _parse_intents(d.pop("intents", UNSET))

        def _parse_not_intents(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                not_intents_type_0 = cast(list[str], data)

                return not_intents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        not_intents = _parse_not_intents(d.pop("notIntents", UNSET))

        def _parse_not_link_hosts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                not_link_hosts_type_0 = cast(list[str], data)

                return not_link_hosts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        not_link_hosts = _parse_not_link_hosts(d.pop("notLinkHosts", UNSET))

        def _parse_subreddits(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subreddits_type_0 = cast(list[str], data)

                return subreddits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        subreddits = _parse_subreddits(d.pop("subreddits", UNSET))

        def _parse_not_subreddits(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                not_subreddits_type_0 = cast(list[str], data)

                return not_subreddits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        not_subreddits = _parse_not_subreddits(d.pop("notSubreddits", UNSET))

        def _parse_not_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                not_tags_type_0 = cast(list[str], data)

                return not_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        not_tags = _parse_not_tags(d.pop("notTags", UNSET))

        def _parse_labels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                labels_type_0 = cast(list[str], data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_not_labels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                not_labels_type_0 = cast(list[str], data)

                return not_labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        not_labels = _parse_not_labels(d.pop("notLabels", UNSET))

        languages = cast(list[str], d.pop("languages", UNSET))

        not_languages = cast(list[str], d.pop("notLanguages", UNSET))

        _countries = d.pop("countries", UNSET)
        countries: list[CreateExportBodyFilterCountriesItem] | Unset = UNSET
        if _countries is not UNSET:
            countries = []
            for countries_item_data in _countries:
                countries_item = CreateExportBodyFilterCountriesItem(
                    countries_item_data
                )

                countries.append(countries_item)

        _not_countries = d.pop("notCountries", UNSET)
        not_countries: list[CreateExportBodyFilterNotCountriesItem] | Unset = UNSET
        if _not_countries is not UNSET:
            not_countries = []
            for not_countries_item_data in _not_countries:
                not_countries_item = CreateExportBodyFilterNotCountriesItem(
                    not_countries_item_data
                )

                not_countries.append(not_countries_item)

        ratings = cast(list[int], d.pop("ratings", UNSET))

        not_ratings = cast(list[int], d.pop("notRatings", UNSET))

        def _parse_min_likes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_likes = _parse_min_likes(d.pop("minLikes", UNSET))

        def _parse_min_reposts(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_reposts = _parse_min_reposts(d.pop("minReposts", UNSET))

        def _parse_min_replies(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_replies = _parse_min_replies(d.pop("minReplies", UNSET))

        def _parse_min_quotes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_quotes = _parse_min_quotes(d.pop("minQuotes", UNSET))

        def _parse_min_views(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_views = _parse_min_views(d.pop("minViews", UNSET))

        def _parse_min_bookmarks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_bookmarks = _parse_min_bookmarks(d.pop("minBookmarks", UNSET))

        any_of = d.pop("anyOf", UNSET)

        q = d.pop("q", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: CreateExportBodyFilterRange | Unset
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = CreateExportBodyFilterRange(_range_)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        timezone = d.pop("timezone", UNSET)

        _since = d.pop("since", UNSET)
        since: datetime.datetime | Unset
        if isinstance(_since, Unset):
            since = UNSET
        else:
            since = datetime.datetime.fromisoformat(_since)

        _until = d.pop("until", UNSET)
        until: datetime.datetime | Unset
        if isinstance(_until, Unset):
            until = UNSET
        else:
            until = datetime.datetime.fromisoformat(_until)

        create_export_body_filter = cls(
            keyword_id=keyword_id,
            platform=platform,
            status=status,
            relevant=relevant,
            sentiment=sentiment,
            intent=intent,
            automated=automated,
            organization=organization,
            person_id=person_id,
            include_muted=include_muted,
            include_hidden=include_hidden,
            include_duplicates=include_duplicates,
            assignee_id=assignee_id,
            snoozed=snoozed,
            not_authors=not_authors,
            exclude_authors=exclude_authors,
            min_relevance=min_relevance,
            min_confidence=min_confidence,
            min_followers=min_followers,
            max_followers=max_followers,
            kind=kind,
            is_reply=is_reply,
            alert_id=alert_id,
            view_id=view_id,
            keyword_kinds=keyword_kinds,
            not_keyword_kinds=not_keyword_kinds,
            tags=tags,
            link_hosts=link_hosts,
            platforms=platforms,
            not_platforms=not_platforms,
            keyword_ids=keyword_ids,
            group_ids=group_ids,
            not_group_ids=not_group_ids,
            not_keyword_ids=not_keyword_ids,
            sentiments=sentiments,
            not_sentiments=not_sentiments,
            emotions=emotions,
            not_emotions=not_emotions,
            intents=intents,
            not_intents=not_intents,
            not_link_hosts=not_link_hosts,
            subreddits=subreddits,
            not_subreddits=not_subreddits,
            not_tags=not_tags,
            labels=labels,
            not_labels=not_labels,
            languages=languages,
            not_languages=not_languages,
            countries=countries,
            not_countries=not_countries,
            ratings=ratings,
            not_ratings=not_ratings,
            min_likes=min_likes,
            min_reposts=min_reposts,
            min_replies=min_replies,
            min_quotes=min_quotes,
            min_views=min_views,
            min_bookmarks=min_bookmarks,
            any_of=any_of,
            q=q,
            range_=range_,
            from_=from_,
            to=to,
            timezone=timezone,
            since=since,
            until=until,
        )

        create_export_body_filter.additional_properties = d
        return create_export_body_filter

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
