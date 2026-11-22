from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageBreakdownDataItemWorkspaceType0")


@_attrs_define
class UsageBreakdownDataItemWorkspaceType0:
    """by=workspace only; null otherwise.

    Attributes:
        id (str): Workspace id (org_...): the caller's own, or one of its child workspaces.
        name (str): The workspace name as it reads now.
        parent_id (None | str): The parent (org_...) for a child workspace; null for the caller's own row.
    """

    id: str
    name: str
    parent_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        parent_id: None | str
        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "parentId": parent_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_parent_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_id = _parse_parent_id(d.pop("parentId"))

        usage_breakdown_data_item_workspace_type_0 = cls(
            id=id,
            name=name,
            parent_id=parent_id,
        )

        usage_breakdown_data_item_workspace_type_0.additional_properties = d
        return usage_breakdown_data_item_workspace_type_0

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
