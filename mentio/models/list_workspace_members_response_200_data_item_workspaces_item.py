from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_workspace_members_response_200_data_item_workspaces_item_role import (
    ListWorkspaceMembersResponse200DataItemWorkspacesItemRole,
)

T = TypeVar("T", bound="ListWorkspaceMembersResponse200DataItemWorkspacesItem")


@_attrs_define
class ListWorkspaceMembersResponse200DataItemWorkspacesItem:
    """
    Attributes:
        id (str): Workspace id (org_...): the parent or one of its children.
        name (str): The workspace name.
        member_id (str): The membership id (mem_...) in that workspace.
        role (ListWorkspaceMembersResponse200DataItemWorkspacesItemRole): owner: everything, billing included. admin:
            manages the team. member: works the feed.
    """

    id: str
    name: str
    member_id: str
    role: ListWorkspaceMembersResponse200DataItemWorkspacesItemRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        member_id = self.member_id

        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "memberId": member_id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        member_id = d.pop("memberId")

        role = ListWorkspaceMembersResponse200DataItemWorkspacesItemRole(d.pop("role"))

        list_workspace_members_response_200_data_item_workspaces_item = cls(
            id=id,
            name=name,
            member_id=member_id,
            role=role,
        )

        list_workspace_members_response_200_data_item_workspaces_item.additional_properties = d
        return list_workspace_members_response_200_data_item_workspaces_item

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
