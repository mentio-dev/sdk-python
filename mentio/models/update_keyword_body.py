from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_keyword_body_platforms_type_0_item import (
    UpdateKeywordBodyPlatformsType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateKeywordBody")


@_attrs_define
class UpdateKeywordBody:
    """Omitted fields are untouched.

    Attributes:
        muted (bool | Unset): A muted keyword stops polling and matching; its mentions stay.
        platforms (list[UpdateKeywordBodyPlatformsType0Item] | None | Unset): Replaces the platform list; null means
            every platform.
    """

    muted: bool | Unset = UNSET
    platforms: list[UpdateKeywordBodyPlatformsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        muted = self.muted

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
        field_dict.update({})
        if muted is not UNSET:
            field_dict["muted"] = muted
        if platforms is not UNSET:
            field_dict["platforms"] = platforms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        muted = d.pop("muted", UNSET)

        def _parse_platforms(
            data: object,
        ) -> list[UpdateKeywordBodyPlatformsType0Item] | None | Unset:
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
                    platforms_type_0_item = UpdateKeywordBodyPlatformsType0Item(
                        platforms_type_0_item_data
                    )

                    platforms_type_0.append(platforms_type_0_item)

                return platforms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateKeywordBodyPlatformsType0Item] | None | Unset, data)

        platforms = _parse_platforms(d.pop("platforms", UNSET))

        update_keyword_body = cls(
            muted=muted,
            platforms=platforms,
        )

        update_keyword_body.additional_properties = d
        return update_keyword_body

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
