from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.filter_group_keyword_kinds_item import FilterGroupKeywordKindsItem
from ..models.filter_group_kind import FilterGroupKind
from ..models.filter_group_not_platforms_item import FilterGroupNotPlatformsItem
from ..models.filter_group_not_sentiments_item import FilterGroupNotSentimentsItem
from ..models.filter_group_platforms_item import FilterGroupPlatformsItem
from ..models.filter_group_sentiments_item import FilterGroupSentimentsItem
from ..models.filter_group_status import FilterGroupStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterGroup")


@_attrs_define
class FilterGroup:
    """A group of conditions, all of which must hold: the vocabulary of a view filter, without anyOf.

    Attributes:
        q (str | Unset): Substring in the post text or the author's name.
        keyword_ids (list[str] | Unset): Only matches of any of these keywords.
        not_keyword_ids (list[str] | Unset): Never matches of these keywords.
        keyword_kinds (list[FilterGroupKeywordKindsItem] | Unset): Only matches of keywords of any of these kinds:
            brand, competitor, topic.
        group_ids (list[str] | Unset): Only matches of keywords in any of these groups (grp_...).
        not_group_ids (list[str] | Unset): Never matches of keywords in these groups.
        platforms (list[FilterGroupPlatformsItem] | Unset): Only posts from any of these platforms.
        not_platforms (list[FilterGroupNotPlatformsItem] | Unset): Never posts from these platforms.
        status (FilterGroupStatus | Unset): Only mentions in this status: open, ignored, done.
        relevant (bool | Unset): true: only mentions the classifier scored relevant; false: only the rest.
        min_relevance (int | Unset): Only mentions scored at least this.
        min_confidence (float | Unset): Only mentions whose classifier confidence is at least this.
        sentiments (list[FilterGroupSentimentsItem] | Unset): Only these sentiments.
        not_sentiments (list[FilterGroupNotSentimentsItem] | Unset): Never these sentiments; an unscored mention still
            passes.
        intents (list[str] | Unset): Only mentions carrying any of these intent or topic tags.
        not_intents (list[str] | Unset): Never mentions carrying these tags.
        automated (bool | Unset): true: only posts that read as machine-made; false: only the rest.
        languages (list[str] | Unset): Only posts in any of these languages (ISO 639-1).
        not_languages (list[str] | Unset): Never posts in these languages; an unknown language still passes.
        tags (list[str] | Unset): Only authors your workspace tagged with any of these.
        not_tags (list[str] | Unset): Never authors tagged with any of these.
        link_hosts (list[str] | Unset): Only posts linking to any of these hosts, the host itself or a subdomain of it.
        not_link_hosts (list[str] | Unset): Never posts linking to these hosts.
        subreddits (list[str] | Unset): Only Reddit posts from any of these subreddits (names without the r/, any case);
            every other post fails it.
        not_subreddits (list[str] | Unset): Never Reddit posts from these subreddits; posts from other platforms still
            pass.
        min_followers (int | Unset): Only authors with at least this many followers; unknown reach never passes.
        max_followers (int | Unset): Only authors with at most this many followers; unknown reach never passes.
        is_reply (bool | Unset): true: only replies and comments; false: only top-level posts.
        kind (FilterGroupKind | Unset): Only posts (post) or only comments (comment).
        exclude_authors (list[str] | Unset): Never these authors: display names, handles or profile URLs.
        ratings (list[int] | Unset): Only app store reviews with any of these star ratings; every other post fails it.
        not_ratings (list[int] | Unset): Never reviews with these star ratings; posts that are not reviews still pass.
        min_likes (int | Unset): Only posts with at least this many likes (upvotes, reactions), as the platform reported
            them when the post was found. A post without that count never passes.
        min_reposts (int | Unset): Only posts with at least this many reposts (shares, retweets), as the platform
            reported them when the post was found. A post without that count never passes.
        min_replies (int | Unset): Only posts with at least this many replies (comments), as the platform reported them
            when the post was found. A post without that count never passes.
        min_quotes (int | Unset): Only posts with at least this many quotes, as the platform reported them when the post
            was found. A post without that count never passes.
        min_views (int | Unset): Only posts with at least this many views (plays), as the platform reported them when
            the post was found. A post without that count never passes.
        min_bookmarks (int | Unset): Only posts with at least this many bookmarks (saves), as the platform reported them
            when the post was found. A post without that count never passes.
    """

    q: str | Unset = UNSET
    keyword_ids: list[str] | Unset = UNSET
    not_keyword_ids: list[str] | Unset = UNSET
    keyword_kinds: list[FilterGroupKeywordKindsItem] | Unset = UNSET
    group_ids: list[str] | Unset = UNSET
    not_group_ids: list[str] | Unset = UNSET
    platforms: list[FilterGroupPlatformsItem] | Unset = UNSET
    not_platforms: list[FilterGroupNotPlatformsItem] | Unset = UNSET
    status: FilterGroupStatus | Unset = UNSET
    relevant: bool | Unset = UNSET
    min_relevance: int | Unset = UNSET
    min_confidence: float | Unset = UNSET
    sentiments: list[FilterGroupSentimentsItem] | Unset = UNSET
    not_sentiments: list[FilterGroupNotSentimentsItem] | Unset = UNSET
    intents: list[str] | Unset = UNSET
    not_intents: list[str] | Unset = UNSET
    automated: bool | Unset = UNSET
    languages: list[str] | Unset = UNSET
    not_languages: list[str] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    not_tags: list[str] | Unset = UNSET
    link_hosts: list[str] | Unset = UNSET
    not_link_hosts: list[str] | Unset = UNSET
    subreddits: list[str] | Unset = UNSET
    not_subreddits: list[str] | Unset = UNSET
    min_followers: int | Unset = UNSET
    max_followers: int | Unset = UNSET
    is_reply: bool | Unset = UNSET
    kind: FilterGroupKind | Unset = UNSET
    exclude_authors: list[str] | Unset = UNSET
    ratings: list[int] | Unset = UNSET
    not_ratings: list[int] | Unset = UNSET
    min_likes: int | Unset = UNSET
    min_reposts: int | Unset = UNSET
    min_replies: int | Unset = UNSET
    min_quotes: int | Unset = UNSET
    min_views: int | Unset = UNSET
    min_bookmarks: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        q = self.q

        keyword_ids: list[str] | Unset = UNSET
        if not isinstance(self.keyword_ids, Unset):
            keyword_ids = self.keyword_ids

        not_keyword_ids: list[str] | Unset = UNSET
        if not isinstance(self.not_keyword_ids, Unset):
            not_keyword_ids = self.not_keyword_ids

        keyword_kinds: list[str] | Unset = UNSET
        if not isinstance(self.keyword_kinds, Unset):
            keyword_kinds = []
            for keyword_kinds_item_data in self.keyword_kinds:
                keyword_kinds_item = keyword_kinds_item_data.value
                keyword_kinds.append(keyword_kinds_item)

        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        not_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.not_group_ids, Unset):
            not_group_ids = self.not_group_ids

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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        relevant = self.relevant

        min_relevance = self.min_relevance

        min_confidence = self.min_confidence

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

        intents: list[str] | Unset = UNSET
        if not isinstance(self.intents, Unset):
            intents = self.intents

        not_intents: list[str] | Unset = UNSET
        if not isinstance(self.not_intents, Unset):
            not_intents = self.not_intents

        automated = self.automated

        languages: list[str] | Unset = UNSET
        if not isinstance(self.languages, Unset):
            languages = self.languages

        not_languages: list[str] | Unset = UNSET
        if not isinstance(self.not_languages, Unset):
            not_languages = self.not_languages

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        not_tags: list[str] | Unset = UNSET
        if not isinstance(self.not_tags, Unset):
            not_tags = self.not_tags

        link_hosts: list[str] | Unset = UNSET
        if not isinstance(self.link_hosts, Unset):
            link_hosts = self.link_hosts

        not_link_hosts: list[str] | Unset = UNSET
        if not isinstance(self.not_link_hosts, Unset):
            not_link_hosts = self.not_link_hosts

        subreddits: list[str] | Unset = UNSET
        if not isinstance(self.subreddits, Unset):
            subreddits = self.subreddits

        not_subreddits: list[str] | Unset = UNSET
        if not isinstance(self.not_subreddits, Unset):
            not_subreddits = self.not_subreddits

        min_followers = self.min_followers

        max_followers = self.max_followers

        is_reply = self.is_reply

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        exclude_authors: list[str] | Unset = UNSET
        if not isinstance(self.exclude_authors, Unset):
            exclude_authors = self.exclude_authors

        ratings: list[int] | Unset = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = self.ratings

        not_ratings: list[int] | Unset = UNSET
        if not isinstance(self.not_ratings, Unset):
            not_ratings = self.not_ratings

        min_likes = self.min_likes

        min_reposts = self.min_reposts

        min_replies = self.min_replies

        min_quotes = self.min_quotes

        min_views = self.min_views

        min_bookmarks = self.min_bookmarks

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if q is not UNSET:
            field_dict["q"] = q
        if keyword_ids is not UNSET:
            field_dict["keywordIds"] = keyword_ids
        if not_keyword_ids is not UNSET:
            field_dict["notKeywordIds"] = not_keyword_ids
        if keyword_kinds is not UNSET:
            field_dict["keywordKinds"] = keyword_kinds
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if not_group_ids is not UNSET:
            field_dict["notGroupIds"] = not_group_ids
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if not_platforms is not UNSET:
            field_dict["notPlatforms"] = not_platforms
        if status is not UNSET:
            field_dict["status"] = status
        if relevant is not UNSET:
            field_dict["relevant"] = relevant
        if min_relevance is not UNSET:
            field_dict["minRelevance"] = min_relevance
        if min_confidence is not UNSET:
            field_dict["minConfidence"] = min_confidence
        if sentiments is not UNSET:
            field_dict["sentiments"] = sentiments
        if not_sentiments is not UNSET:
            field_dict["notSentiments"] = not_sentiments
        if intents is not UNSET:
            field_dict["intents"] = intents
        if not_intents is not UNSET:
            field_dict["notIntents"] = not_intents
        if automated is not UNSET:
            field_dict["automated"] = automated
        if languages is not UNSET:
            field_dict["languages"] = languages
        if not_languages is not UNSET:
            field_dict["notLanguages"] = not_languages
        if tags is not UNSET:
            field_dict["tags"] = tags
        if not_tags is not UNSET:
            field_dict["notTags"] = not_tags
        if link_hosts is not UNSET:
            field_dict["linkHosts"] = link_hosts
        if not_link_hosts is not UNSET:
            field_dict["notLinkHosts"] = not_link_hosts
        if subreddits is not UNSET:
            field_dict["subreddits"] = subreddits
        if not_subreddits is not UNSET:
            field_dict["notSubreddits"] = not_subreddits
        if min_followers is not UNSET:
            field_dict["minFollowers"] = min_followers
        if max_followers is not UNSET:
            field_dict["maxFollowers"] = max_followers
        if is_reply is not UNSET:
            field_dict["isReply"] = is_reply
        if kind is not UNSET:
            field_dict["kind"] = kind
        if exclude_authors is not UNSET:
            field_dict["excludeAuthors"] = exclude_authors
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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        q = d.pop("q", UNSET)

        keyword_ids = cast(list[str], d.pop("keywordIds", UNSET))

        not_keyword_ids = cast(list[str], d.pop("notKeywordIds", UNSET))

        _keyword_kinds = d.pop("keywordKinds", UNSET)
        keyword_kinds: list[FilterGroupKeywordKindsItem] | Unset = UNSET
        if _keyword_kinds is not UNSET:
            keyword_kinds = []
            for keyword_kinds_item_data in _keyword_kinds:
                keyword_kinds_item = FilterGroupKeywordKindsItem(
                    keyword_kinds_item_data
                )

                keyword_kinds.append(keyword_kinds_item)

        group_ids = cast(list[str], d.pop("groupIds", UNSET))

        not_group_ids = cast(list[str], d.pop("notGroupIds", UNSET))

        _platforms = d.pop("platforms", UNSET)
        platforms: list[FilterGroupPlatformsItem] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = FilterGroupPlatformsItem(platforms_item_data)

                platforms.append(platforms_item)

        _not_platforms = d.pop("notPlatforms", UNSET)
        not_platforms: list[FilterGroupNotPlatformsItem] | Unset = UNSET
        if _not_platforms is not UNSET:
            not_platforms = []
            for not_platforms_item_data in _not_platforms:
                not_platforms_item = FilterGroupNotPlatformsItem(
                    not_platforms_item_data
                )

                not_platforms.append(not_platforms_item)

        _status = d.pop("status", UNSET)
        status: FilterGroupStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FilterGroupStatus(_status)

        relevant = d.pop("relevant", UNSET)

        min_relevance = d.pop("minRelevance", UNSET)

        min_confidence = d.pop("minConfidence", UNSET)

        _sentiments = d.pop("sentiments", UNSET)
        sentiments: list[FilterGroupSentimentsItem] | Unset = UNSET
        if _sentiments is not UNSET:
            sentiments = []
            for sentiments_item_data in _sentiments:
                sentiments_item = FilterGroupSentimentsItem(sentiments_item_data)

                sentiments.append(sentiments_item)

        _not_sentiments = d.pop("notSentiments", UNSET)
        not_sentiments: list[FilterGroupNotSentimentsItem] | Unset = UNSET
        if _not_sentiments is not UNSET:
            not_sentiments = []
            for not_sentiments_item_data in _not_sentiments:
                not_sentiments_item = FilterGroupNotSentimentsItem(
                    not_sentiments_item_data
                )

                not_sentiments.append(not_sentiments_item)

        intents = cast(list[str], d.pop("intents", UNSET))

        not_intents = cast(list[str], d.pop("notIntents", UNSET))

        automated = d.pop("automated", UNSET)

        languages = cast(list[str], d.pop("languages", UNSET))

        not_languages = cast(list[str], d.pop("notLanguages", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        not_tags = cast(list[str], d.pop("notTags", UNSET))

        link_hosts = cast(list[str], d.pop("linkHosts", UNSET))

        not_link_hosts = cast(list[str], d.pop("notLinkHosts", UNSET))

        subreddits = cast(list[str], d.pop("subreddits", UNSET))

        not_subreddits = cast(list[str], d.pop("notSubreddits", UNSET))

        min_followers = d.pop("minFollowers", UNSET)

        max_followers = d.pop("maxFollowers", UNSET)

        is_reply = d.pop("isReply", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: FilterGroupKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = FilterGroupKind(_kind)

        exclude_authors = cast(list[str], d.pop("excludeAuthors", UNSET))

        ratings = cast(list[int], d.pop("ratings", UNSET))

        not_ratings = cast(list[int], d.pop("notRatings", UNSET))

        min_likes = d.pop("minLikes", UNSET)

        min_reposts = d.pop("minReposts", UNSET)

        min_replies = d.pop("minReplies", UNSET)

        min_quotes = d.pop("minQuotes", UNSET)

        min_views = d.pop("minViews", UNSET)

        min_bookmarks = d.pop("minBookmarks", UNSET)

        filter_group = cls(
            q=q,
            keyword_ids=keyword_ids,
            not_keyword_ids=not_keyword_ids,
            keyword_kinds=keyword_kinds,
            group_ids=group_ids,
            not_group_ids=not_group_ids,
            platforms=platforms,
            not_platforms=not_platforms,
            status=status,
            relevant=relevant,
            min_relevance=min_relevance,
            min_confidence=min_confidence,
            sentiments=sentiments,
            not_sentiments=not_sentiments,
            intents=intents,
            not_intents=not_intents,
            automated=automated,
            languages=languages,
            not_languages=not_languages,
            tags=tags,
            not_tags=not_tags,
            link_hosts=link_hosts,
            not_link_hosts=not_link_hosts,
            subreddits=subreddits,
            not_subreddits=not_subreddits,
            min_followers=min_followers,
            max_followers=max_followers,
            is_reply=is_reply,
            kind=kind,
            exclude_authors=exclude_authors,
            ratings=ratings,
            not_ratings=not_ratings,
            min_likes=min_likes,
            min_reposts=min_reposts,
            min_replies=min_replies,
            min_quotes=min_quotes,
            min_views=min_views,
            min_bookmarks=min_bookmarks,
        )

        return filter_group
