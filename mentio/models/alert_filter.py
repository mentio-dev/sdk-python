from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_filter_platforms_item import AlertFilterPlatformsItem
from ..models.alert_filter_sentiments_item import AlertFilterSentimentsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_group import FilterGroup


T = TypeVar("T", bound="AlertFilter")


@_attrs_define
class AlertFilter:
    """
    Attributes:
        keyword_ids (list[str] | Unset): Only these keywords.
        group_ids (list[str] | Unset): Only keywords in these groups (grp_...): one rule per customer, say.
        platforms (list[AlertFilterPlatformsItem] | Unset): Only posts from these platforms.
        min_relevance (int | Unset): The rule's relevance floor. Absent, it sends relevant mentions only (scored 40 and
            up, the classifier's line); lower, down to 0, it also receives the matches the classifier scored as noise;
            higher, it hears less. Email channels keep the 40 line whatever the rule says. Unclassified mentions never pass.
        min_confidence (float | Unset): Only mentions whose classifier confidence is at least this, 0 to 1. A mention
            without a confidence never passes.
        sentiments (list[AlertFilterSentimentsItem] | Unset): Only these sentiments.
        intents (list[str] | Unset): At least one of these intent or topic tags.
        exclude_authors (list[str] | Unset): Never these authors: display names, handles or profile URLs.
        min_followers (int | Unset): Only authors with at least this many followers. Unknown reach never passes.
        tags (list[str] | Unset): Only authors your workspace tagged with any of these.
        link_hosts (list[str] | Unset): Only posts linking to any of these hosts, the host itself or a subdomain of it
            (octolens.com also matches blog.octolens.com). A post with no links never passes.
        languages (list[str] | Unset): Only posts in any of these languages (ISO 639-1: en, es, de). A post whose
            language is unknown never passes.
        automated (bool | Unset): true: only posts that read as machine-made (bots, templated posts); false: only the
            rest. Omit for both.
        ratings (list[int] | Unset): Only app store reviews with any of these star ratings (1 to 5): [1, 2] sends the
            unhappy ones. Every other post fails it.
        not_ratings (list[int] | Unset): Never reviews with these star ratings (1 to 5): [5] keeps the five star reviews
            out. Posts that are not reviews still pass.
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
        any_of (list[FilterGroup] | Unset): OR across groups: a mention passes when it meets every condition of at least
            one group (1 to 10 groups). The other conditions still apply to every mention: the whole filter is (other
            conditions) AND (group 1 OR group 2 ...). A group takes the conditions of a view filter (platforms, sentiments,
            intents, keywordKinds, the not lists ...), with no anyOf of its own.
    """

    keyword_ids: list[str] | Unset = UNSET
    group_ids: list[str] | Unset = UNSET
    platforms: list[AlertFilterPlatformsItem] | Unset = UNSET
    min_relevance: int | Unset = UNSET
    min_confidence: float | Unset = UNSET
    sentiments: list[AlertFilterSentimentsItem] | Unset = UNSET
    intents: list[str] | Unset = UNSET
    exclude_authors: list[str] | Unset = UNSET
    min_followers: int | Unset = UNSET
    tags: list[str] | Unset = UNSET
    link_hosts: list[str] | Unset = UNSET
    languages: list[str] | Unset = UNSET
    automated: bool | Unset = UNSET
    ratings: list[int] | Unset = UNSET
    not_ratings: list[int] | Unset = UNSET
    min_likes: int | Unset = UNSET
    min_reposts: int | Unset = UNSET
    min_replies: int | Unset = UNSET
    min_quotes: int | Unset = UNSET
    min_views: int | Unset = UNSET
    min_bookmarks: int | Unset = UNSET
    any_of: list[FilterGroup] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword_ids: list[str] | Unset = UNSET
        if not isinstance(self.keyword_ids, Unset):
            keyword_ids = self.keyword_ids

        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        platforms: list[str] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.value
                platforms.append(platforms_item)

        min_relevance = self.min_relevance

        min_confidence = self.min_confidence

        sentiments: list[str] | Unset = UNSET
        if not isinstance(self.sentiments, Unset):
            sentiments = []
            for sentiments_item_data in self.sentiments:
                sentiments_item = sentiments_item_data.value
                sentiments.append(sentiments_item)

        intents: list[str] | Unset = UNSET
        if not isinstance(self.intents, Unset):
            intents = self.intents

        exclude_authors: list[str] | Unset = UNSET
        if not isinstance(self.exclude_authors, Unset):
            exclude_authors = self.exclude_authors

        min_followers = self.min_followers

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        link_hosts: list[str] | Unset = UNSET
        if not isinstance(self.link_hosts, Unset):
            link_hosts = self.link_hosts

        languages: list[str] | Unset = UNSET
        if not isinstance(self.languages, Unset):
            languages = self.languages

        automated = self.automated

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

        any_of: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.any_of, Unset):
            any_of = []
            for any_of_item_data in self.any_of:
                any_of_item = any_of_item_data.to_dict()
                any_of.append(any_of_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyword_ids is not UNSET:
            field_dict["keywordIds"] = keyword_ids
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if min_relevance is not UNSET:
            field_dict["minRelevance"] = min_relevance
        if min_confidence is not UNSET:
            field_dict["minConfidence"] = min_confidence
        if sentiments is not UNSET:
            field_dict["sentiments"] = sentiments
        if intents is not UNSET:
            field_dict["intents"] = intents
        if exclude_authors is not UNSET:
            field_dict["excludeAuthors"] = exclude_authors
        if min_followers is not UNSET:
            field_dict["minFollowers"] = min_followers
        if tags is not UNSET:
            field_dict["tags"] = tags
        if link_hosts is not UNSET:
            field_dict["linkHosts"] = link_hosts
        if languages is not UNSET:
            field_dict["languages"] = languages
        if automated is not UNSET:
            field_dict["automated"] = automated
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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_group import FilterGroup

        d = dict(src_dict)
        keyword_ids = cast(list[str], d.pop("keywordIds", UNSET))

        group_ids = cast(list[str], d.pop("groupIds", UNSET))

        _platforms = d.pop("platforms", UNSET)
        platforms: list[AlertFilterPlatformsItem] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = AlertFilterPlatformsItem(platforms_item_data)

                platforms.append(platforms_item)

        min_relevance = d.pop("minRelevance", UNSET)

        min_confidence = d.pop("minConfidence", UNSET)

        _sentiments = d.pop("sentiments", UNSET)
        sentiments: list[AlertFilterSentimentsItem] | Unset = UNSET
        if _sentiments is not UNSET:
            sentiments = []
            for sentiments_item_data in _sentiments:
                sentiments_item = AlertFilterSentimentsItem(sentiments_item_data)

                sentiments.append(sentiments_item)

        intents = cast(list[str], d.pop("intents", UNSET))

        exclude_authors = cast(list[str], d.pop("excludeAuthors", UNSET))

        min_followers = d.pop("minFollowers", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        link_hosts = cast(list[str], d.pop("linkHosts", UNSET))

        languages = cast(list[str], d.pop("languages", UNSET))

        automated = d.pop("automated", UNSET)

        ratings = cast(list[int], d.pop("ratings", UNSET))

        not_ratings = cast(list[int], d.pop("notRatings", UNSET))

        min_likes = d.pop("minLikes", UNSET)

        min_reposts = d.pop("minReposts", UNSET)

        min_replies = d.pop("minReplies", UNSET)

        min_quotes = d.pop("minQuotes", UNSET)

        min_views = d.pop("minViews", UNSET)

        min_bookmarks = d.pop("minBookmarks", UNSET)

        _any_of = d.pop("anyOf", UNSET)
        any_of: list[FilterGroup] | Unset = UNSET
        if _any_of is not UNSET:
            any_of = []
            for any_of_item_data in _any_of:
                any_of_item = FilterGroup.from_dict(any_of_item_data)

                any_of.append(any_of_item)

        alert_filter = cls(
            keyword_ids=keyword_ids,
            group_ids=group_ids,
            platforms=platforms,
            min_relevance=min_relevance,
            min_confidence=min_confidence,
            sentiments=sentiments,
            intents=intents,
            exclude_authors=exclude_authors,
            min_followers=min_followers,
            tags=tags,
            link_hosts=link_hosts,
            languages=languages,
            automated=automated,
            ratings=ratings,
            not_ratings=not_ratings,
            min_likes=min_likes,
            min_reposts=min_reposts,
            min_replies=min_replies,
            min_quotes=min_quotes,
            min_views=min_views,
            min_bookmarks=min_bookmarks,
            any_of=any_of,
        )

        alert_filter.additional_properties = d
        return alert_filter

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
