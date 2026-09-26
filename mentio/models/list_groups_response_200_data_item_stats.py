from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListGroupsResponse200DataItemStats")


@_attrs_define
class ListGroupsResponse200DataItemStats:
    """Computed over the group's keywords.

    Attributes:
        keywords (int): Keywords in the group, muted ones included.
        active (int): Keywords in the group that are tracking (not muted).
    """

    keywords: int
    active: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keywords": keywords,
                "active": active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keywords = d.pop("keywords")

        active = d.pop("active")

        list_groups_response_200_data_item_stats = cls(
            keywords=keywords,
            active=active,
        )

        list_groups_response_200_data_item_stats.additional_properties = d
        return list_groups_response_200_data_item_stats

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
