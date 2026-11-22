from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_keywords_body_keywords_item_kind import (
    CreateKeywordsBodyKeywordsItemKind,
)
from ..models.create_keywords_body_keywords_item_platforms_type_0_item import (
    CreateKeywordsBodyKeywordsItemPlatformsType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_keywords_body_keywords_item_cap_type_0 import (
        CreateKeywordsBodyKeywordsItemCapType0,
    )
    from ..models.create_keywords_body_keywords_item_comments import (
        CreateKeywordsBodyKeywordsItemComments,
    )
    from ..models.create_keywords_body_keywords_item_display import (
        CreateKeywordsBodyKeywordsItemDisplay,
    )
    from ..models.create_keywords_body_keywords_item_matching import (
        CreateKeywordsBodyKeywordsItemMatching,
    )


T = TypeVar("T", bound="CreateKeywordsBodyKeywordsItem")


@_attrs_define
class CreateKeywordsBodyKeywordsItem:
    """One keyword, as POST /v1/keywords takes it, without reviewSources and feeds (add those to the keyword afterwards).

    Attributes:
        term (str | Unset): The word or phrase to track, case-insensitive. Required unless `query` is sent. A multi-word
            term matches as the phrase or as its words close together (see matching.exactPhrase); wrap it in double quotes
            for the exact phrase only.
        query (str | Unset): The keyword as one boolean query instead of term and matching, like "acme cloud" AND
            (pricing OR price*) -jobs ([Keywords](/guides/keywords#write-it-as-a-query)):

            - Phrases, words, AND, OR, NOT or -word, parentheses, word-end *
            - Compiled into term and the term rules; never sent with them (400).
            - Each alternative starts with the term; else 400 query_needs_one_term.
        kind (CreateKeywordsBodyKeywordsItemKind | Unset): brand: your own names. competitor: theirs. topic: the space.
            Drives share of voice and segments. Default: CreateKeywordsBodyKeywordsItemKind.BRAND.
        platforms (list[CreateKeywordsBodyKeywordsItemPlatformsType0Item] | None | Unset): Platforms to search the term
            on; omit or null for every platform. [] searches it nowhere: a keyword that only collects reviews or reads
            feeds, which then needs reviewSources or feeds.
        context (None | str | Unset): A sentence the classifier reads for this keyword only, on top of the company
            profile or group description: what the term means here, what to ignore. "Arc is our browser; ignore the geometry
            word." Null clears it.
        matching (CreateKeywordsBodyKeywordsItemMatching | Unset): Omitted fields are untouched; an empty list clears
            one.
        cap (CreateKeywordsBodyKeywordsItemCapType0 | None | Unset): A mention cap per day, week or month (per, default
            month); omit or null for none.
        comments (CreateKeywordsBodyKeywordsItemComments | Unset): Comments under this keyword's mentions; omitted
            fields are untouched (on create: off, 20 per post).
        display (CreateKeywordsBodyKeywordsItemDisplay | Unset): Which of this keyword's mentions you see, by language
            and country; each list is replaced when sent, kept when omitted. Hidden mentions are still billed.
        group_id (str | Unset): The group to track it in (grp_...); omit for the workspace's default group. A term may
            be tracked once per group.
        reads_workspace_feeds (bool | Unset): Whether the keyword also reads the workspace's feeds (GET /v1/feeds);
            default true. A new keyword reading them gets the look-back of the 8 most recently connected.
    """

    term: str | Unset = UNSET
    query: str | Unset = UNSET
    kind: CreateKeywordsBodyKeywordsItemKind | Unset = (
        CreateKeywordsBodyKeywordsItemKind.BRAND
    )
    platforms: list[CreateKeywordsBodyKeywordsItemPlatformsType0Item] | None | Unset = (
        UNSET
    )
    context: None | str | Unset = UNSET
    matching: CreateKeywordsBodyKeywordsItemMatching | Unset = UNSET
    cap: CreateKeywordsBodyKeywordsItemCapType0 | None | Unset = UNSET
    comments: CreateKeywordsBodyKeywordsItemComments | Unset = UNSET
    display: CreateKeywordsBodyKeywordsItemDisplay | Unset = UNSET
    group_id: str | Unset = UNSET
    reads_workspace_feeds: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_keywords_body_keywords_item_cap_type_0 import (
            CreateKeywordsBodyKeywordsItemCapType0,
        )

        term = self.term

        query = self.query

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
        elif isinstance(self.cap, CreateKeywordsBodyKeywordsItemCapType0):
            cap = self.cap.to_dict()
        else:
            cap = self.cap

        comments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        display: dict[str, Any] | Unset = UNSET
        if not isinstance(self.display, Unset):
            display = self.display.to_dict()

        group_id = self.group_id

        reads_workspace_feeds = self.reads_workspace_feeds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if query is not UNSET:
            field_dict["query"] = query
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
        if display is not UNSET:
            field_dict["display"] = display
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if reads_workspace_feeds is not UNSET:
            field_dict["readsWorkspaceFeeds"] = reads_workspace_feeds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_keywords_body_keywords_item_cap_type_0 import (
            CreateKeywordsBodyKeywordsItemCapType0,
        )
        from ..models.create_keywords_body_keywords_item_comments import (
            CreateKeywordsBodyKeywordsItemComments,
        )
        from ..models.create_keywords_body_keywords_item_display import (
            CreateKeywordsBodyKeywordsItemDisplay,
        )
        from ..models.create_keywords_body_keywords_item_matching import (
            CreateKeywordsBodyKeywordsItemMatching,
        )

        d = dict(src_dict)
        term = d.pop("term", UNSET)

        query = d.pop("query", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: CreateKeywordsBodyKeywordsItemKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = CreateKeywordsBodyKeywordsItemKind(_kind)

        def _parse_platforms(
            data: object,
        ) -> list[CreateKeywordsBodyKeywordsItemPlatformsType0Item] | None | Unset:
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
                    platforms_type_0_item = (
                        CreateKeywordsBodyKeywordsItemPlatformsType0Item(
                            platforms_type_0_item_data
                        )
                    )

                    platforms_type_0.append(platforms_type_0_item)

                return platforms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CreateKeywordsBodyKeywordsItemPlatformsType0Item] | None | Unset,
                data,
            )

        platforms = _parse_platforms(d.pop("platforms", UNSET))

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        _matching = d.pop("matching", UNSET)
        matching: CreateKeywordsBodyKeywordsItemMatching | Unset
        if isinstance(_matching, Unset):
            matching = UNSET
        else:
            matching = CreateKeywordsBodyKeywordsItemMatching.from_dict(_matching)

        def _parse_cap(
            data: object,
        ) -> CreateKeywordsBodyKeywordsItemCapType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cap_type_0 = CreateKeywordsBodyKeywordsItemCapType0.from_dict(data)

                return cap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateKeywordsBodyKeywordsItemCapType0 | None | Unset, data)

        cap = _parse_cap(d.pop("cap", UNSET))

        _comments = d.pop("comments", UNSET)
        comments: CreateKeywordsBodyKeywordsItemComments | Unset
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = CreateKeywordsBodyKeywordsItemComments.from_dict(_comments)

        _display = d.pop("display", UNSET)
        display: CreateKeywordsBodyKeywordsItemDisplay | Unset
        if isinstance(_display, Unset):
            display = UNSET
        else:
            display = CreateKeywordsBodyKeywordsItemDisplay.from_dict(_display)

        group_id = d.pop("groupId", UNSET)

        reads_workspace_feeds = d.pop("readsWorkspaceFeeds", UNSET)

        create_keywords_body_keywords_item = cls(
            term=term,
            query=query,
            kind=kind,
            platforms=platforms,
            context=context,
            matching=matching,
            cap=cap,
            comments=comments,
            display=display,
            group_id=group_id,
            reads_workspace_feeds=reads_workspace_feeds,
        )

        create_keywords_body_keywords_item.additional_properties = d
        return create_keywords_body_keywords_item

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
