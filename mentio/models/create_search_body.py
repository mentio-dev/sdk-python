from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_search_body_kind import CreateSearchBodyKind
from ..models.create_search_body_platforms_item import CreateSearchBodyPlatformsItem
from ..models.create_search_body_range import CreateSearchBodyRange
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSearchBody")


@_attrs_define
class CreateSearchBody:
    """
    Attributes:
        term (str): The word or phrase to search, case-insensitive, matched as the phrase (written joined or as a
            hashtag counts). Quotes are not needed.
        range_ (CreateSearchBodyRange | Unset): How far back the search reads, ending now: 24h, 7d or 30d. Instagram
            reads at most its last 7 days whatever the range. Default: CreateSearchBodyRange.VALUE_1.
        platforms (list[CreateSearchBodyPlatformsItem] | Unset): The platforms to read; omit for every platform that can
            search a term back in time (bluesky, hackernews, github, stackoverflow, reddit, x, youtube, linkedin, tiktok,
            instagram, facebook). devto and news have no search and are reported as skipped.
        kind (CreateSearchBodyKind | Unset): What the term is to you, as on a keyword: brand (your company or product),
            competitor, or topic (the default). The classifier judges relevance with it. Default:
            CreateSearchBodyKind.TOPIC.
        context (str | Unset): A sentence the classifier reads for this search only, on top of the company profile: what
            the term means here, what to ignore.
    """

    term: str
    range_: CreateSearchBodyRange | Unset = CreateSearchBodyRange.VALUE_1
    platforms: list[CreateSearchBodyPlatformsItem] | Unset = UNSET
    kind: CreateSearchBodyKind | Unset = CreateSearchBodyKind.TOPIC
    context: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        range_: str | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.value

        platforms: list[str] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.value
                platforms.append(platforms_item)

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "term": term,
            }
        )
        if range_ is not UNSET:
            field_dict["range"] = range_
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if kind is not UNSET:
            field_dict["kind"] = kind
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        term = d.pop("term")

        _range_ = d.pop("range", UNSET)
        range_: CreateSearchBodyRange | Unset
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = CreateSearchBodyRange(_range_)

        _platforms = d.pop("platforms", UNSET)
        platforms: list[CreateSearchBodyPlatformsItem] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = CreateSearchBodyPlatformsItem(platforms_item_data)

                platforms.append(platforms_item)

        _kind = d.pop("kind", UNSET)
        kind: CreateSearchBodyKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = CreateSearchBodyKind(_kind)

        context = d.pop("context", UNSET)

        create_search_body = cls(
            term=term,
            range_=range_,
            platforms=platforms,
            kind=kind,
            context=context,
        )

        create_search_body.additional_properties = d
        return create_search_body

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
