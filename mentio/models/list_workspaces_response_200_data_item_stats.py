from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListWorkspacesResponse200DataItemStats")


@_attrs_define
class ListWorkspacesResponse200DataItemStats:
    """Counts.

    Attributes:
        keywords (int): Keywords in the workspace, running or not.
        members (int): People who are members of this workspace itself (the parent's team reaches it through the
            parent).
    """

    keywords: int
    members: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        members = self.members

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keywords": keywords,
                "members": members,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keywords = d.pop("keywords")

        members = d.pop("members")

        list_workspaces_response_200_data_item_stats = cls(
            keywords=keywords,
            members=members,
        )

        list_workspaces_response_200_data_item_stats.additional_properties = d
        return list_workspaces_response_200_data_item_stats

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
