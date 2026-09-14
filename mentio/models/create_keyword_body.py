from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_keyword_body_kind import CreateKeywordBodyKind
from ..models.create_keyword_body_platforms_type_0_item import (
    CreateKeywordBodyPlatformsType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKeywordBody")


@_attrs_define
class CreateKeywordBody:
    """
    Attributes:
        term (str): The word or phrase to track, matched case-insensitively as a phrase.
        kind (CreateKeywordBodyKind | Unset): brand: your own names. competitor: theirs. topic: the space. Drives share
            of voice and segments. Default: CreateKeywordBodyKind.BRAND.
        platforms (list[CreateKeywordBodyPlatformsType0Item] | None | Unset): Platforms to track it on; omit or null for
            every platform.
    """

    term: str
    kind: CreateKeywordBodyKind | Unset = CreateKeywordBodyKind.BRAND
    platforms: list[CreateKeywordBodyPlatformsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
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

        create_keyword_body = cls(
            term=term,
            kind=kind,
            platforms=platforms,
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
