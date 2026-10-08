from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_keyword_body_kind import CreateKeywordBodyKind
from ..models.create_keyword_body_platforms_type_0_item import (
    CreateKeywordBodyPlatformsType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_keyword_body_cap_type_0 import CreateKeywordBodyCapType0
    from ..models.create_keyword_body_comments import CreateKeywordBodyComments
    from ..models.create_keyword_body_feeds_item import CreateKeywordBodyFeedsItem
    from ..models.create_keyword_body_matching import CreateKeywordBodyMatching
    from ..models.create_keyword_body_review_sources_item import (
        CreateKeywordBodyReviewSourcesItem,
    )


T = TypeVar("T", bound="CreateKeywordBody")


@_attrs_define
class CreateKeywordBody:
    """
    Attributes:
        term (str): The word or phrase to track, case-insensitive. A multi-word term matches as the phrase or as its
            words close together (see matching.exactPhrase); wrap it in double quotes for the exact phrase only.
        kind (CreateKeywordBodyKind | Unset): brand: your own names. competitor: theirs. topic: the space. Drives share
            of voice and segments. Default: CreateKeywordBodyKind.BRAND.
        platforms (list[CreateKeywordBodyPlatformsType0Item] | None | Unset): Platforms to search the term on; omit or
            null for every platform. [] searches it nowhere: a keyword that only collects reviews or reads feeds, which then
            needs reviewSources or feeds.
        context (None | str | Unset): A sentence the classifier reads for this keyword only, on top of the company
            profile or the group's own description (at most 300 characters): what the term means here, what to ignore. "Arc
            is our browser; ignore the geometry word." Null clears it.
        matching (CreateKeywordBodyMatching | Unset): Omitted fields are untouched; an empty list clears one.
        cap (CreateKeywordBodyCapType0 | None | Unset): A monthly mention cap; omit or null for none.
        comments (CreateKeywordBodyComments | Unset): Comments under this keyword's mentions; omitted fields are
            untouched (on create: off, 20 per post).
        group_id (str | Unset): The group to track it in (grp_...); omit for the workspace's default group. A term may
            be tracked once per group.
        review_sources (list[CreateKeywordBodyReviewSourcesItem] | Unset): Review pages this keyword collects, at most
            10: App Store and Google Play apps, Trustpilot pages, Google Maps places. Every new review of one is a mention
            of the keyword, whatever its text says. Polled once a day (per country on the app stores). A newly connected
            page brings its last 30 days, the newest 100 reviews (per country), free and never sent as instant alerts; after
            that each review bills like any mention.
        feeds (list[CreateKeywordBodyFeedsItem] | Unset): RSS or Atom feeds this keyword reads, at most 20, each { url
            }: a feed's URL, or a page's (a forum, a community, a blog), in which case the feed the page advertises is used,
            else a usual address such as /feed or /rss. A URL with no feed behind it is a 400. Each feed is read every hour;
            an item is a mention of this keyword when it holds the term (with the keyword's matching rules), and only of
            keywords that named the feed. A newly connected feed brings its newest 10 items of the last 30 days that hold
            the term, billed like any mention and never sent as instant alerts.
    """

    term: str
    kind: CreateKeywordBodyKind | Unset = CreateKeywordBodyKind.BRAND
    platforms: list[CreateKeywordBodyPlatformsType0Item] | None | Unset = UNSET
    context: None | str | Unset = UNSET
    matching: CreateKeywordBodyMatching | Unset = UNSET
    cap: CreateKeywordBodyCapType0 | None | Unset = UNSET
    comments: CreateKeywordBodyComments | Unset = UNSET
    group_id: str | Unset = UNSET
    review_sources: list[CreateKeywordBodyReviewSourcesItem] | Unset = UNSET
    feeds: list[CreateKeywordBodyFeedsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_keyword_body_cap_type_0 import (
            CreateKeywordBodyCapType0,
        )

        term = self.term

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        platforms: list[str] | None | Unset
        if isinstance(self.platforms, Unset):
            platforms = UNSET
        elif isinstance(self.platforms, list):
            platforms = []
            for platforms_type_0_item_data in self.platforms:
                platforms_type_0_item = platforms_type_0_item_data.value
                platforms.append(platforms_type_0_item)

        else:
            platforms = self.platforms

        context: None | str | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        matching: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matching, Unset):
            matching = self.matching.to_dict()

        cap: dict[str, Any] | None | Unset
        if isinstance(self.cap, Unset):
            cap = UNSET
        elif isinstance(self.cap, CreateKeywordBodyCapType0):
            cap = self.cap.to_dict()
        else:
            cap = self.cap

        comments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        group_id = self.group_id

        review_sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.review_sources, Unset):
            review_sources = []
            for review_sources_item_data in self.review_sources:
                review_sources_item = review_sources_item_data.to_dict()
                review_sources.append(review_sources_item)

        feeds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feeds, Unset):
            feeds = []
            for feeds_item_data in self.feeds:
                feeds_item = feeds_item_data.to_dict()
                feeds.append(feeds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "term": term,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if context is not UNSET:
            field_dict["context"] = context
        if matching is not UNSET:
            field_dict["matching"] = matching
        if cap is not UNSET:
            field_dict["cap"] = cap
        if comments is not UNSET:
            field_dict["comments"] = comments
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if review_sources is not UNSET:
            field_dict["reviewSources"] = review_sources
        if feeds is not UNSET:
            field_dict["feeds"] = feeds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_keyword_body_cap_type_0 import (
            CreateKeywordBodyCapType0,
        )
        from ..models.create_keyword_body_comments import (
            CreateKeywordBodyComments,
        )
        from ..models.create_keyword_body_feeds_item import (
            CreateKeywordBodyFeedsItem,
        )
        from ..models.create_keyword_body_matching import (
            CreateKeywordBodyMatching,
        )
        from ..models.create_keyword_body_review_sources_item import (
            CreateKeywordBodyReviewSourcesItem,
        )

        d = dict(src_dict)
        term = d.pop("term")

        _kind = d.pop("kind", UNSET)
        kind: CreateKeywordBodyKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = CreateKeywordBodyKind(_kind)

        def _parse_platforms(
            data: object,
        ) -> list[CreateKeywordBodyPlatformsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                platforms_type_0 = []
                _platforms_type_0 = data
                for platforms_type_0_item_data in _platforms_type_0:
                    platforms_type_0_item = CreateKeywordBodyPlatformsType0Item(
                        platforms_type_0_item_data
                    )

                    platforms_type_0.append(platforms_type_0_item)

                return platforms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CreateKeywordBodyPlatformsType0Item] | None | Unset, data)

        platforms = _parse_platforms(d.pop("platforms", UNSET))

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        _matching = d.pop("matching", UNSET)
        matching: CreateKeywordBodyMatching | Unset
        if isinstance(_matching, Unset):
            matching = UNSET
        else:
            matching = CreateKeywordBodyMatching.from_dict(_matching)

        def _parse_cap(data: object) -> CreateKeywordBodyCapType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cap_type_0 = CreateKeywordBodyCapType0.from_dict(data)

                return cap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateKeywordBodyCapType0 | None | Unset, data)

        cap = _parse_cap(d.pop("cap", UNSET))

        _comments = d.pop("comments", UNSET)
        comments: CreateKeywordBodyComments | Unset
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = CreateKeywordBodyComments.from_dict(_comments)

        group_id = d.pop("groupId", UNSET)

        _review_sources = d.pop("reviewSources", UNSET)
        review_sources: list[CreateKeywordBodyReviewSourcesItem] | Unset = UNSET
        if _review_sources is not UNSET:
            review_sources = []
            for review_sources_item_data in _review_sources:
                review_sources_item = CreateKeywordBodyReviewSourcesItem.from_dict(
                    review_sources_item_data
                )

                review_sources.append(review_sources_item)

        _feeds = d.pop("feeds", UNSET)
        feeds: list[CreateKeywordBodyFeedsItem] | Unset = UNSET
        if _feeds is not UNSET:
            feeds = []
            for feeds_item_data in _feeds:
                feeds_item = CreateKeywordBodyFeedsItem.from_dict(feeds_item_data)

                feeds.append(feeds_item)

        create_keyword_body = cls(
            term=term,
            kind=kind,
            platforms=platforms,
            context=context,
            matching=matching,
            cap=cap,
            comments=comments,
            group_id=group_id,
            review_sources=review_sources,
            feeds=feeds,
        )

        create_keyword_body.additional_properties = d
        return create_keyword_body

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
