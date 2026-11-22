from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_workspace_members_response_200_data_item_workspaces_item import (
        ListWorkspaceMembersResponse200DataItemWorkspacesItem,
    )


T = TypeVar("T", bound="ListWorkspaceMembersResponse200DataItem")


@_attrs_define
class ListWorkspaceMembersResponse200DataItem:
    """
    Attributes:
        user_id (str): The person's user id.
        email (str): The account's email address.
        name (None | str): The name on the account; null when they never set one.
        workspaces (list[ListWorkspaceMembersResponse200DataItemWorkspacesItem]): Every workspace of the agency (the
            parent and its children) the person is a member of.
    """

    user_id: str
    email: str
    name: None | str
    workspaces: list[ListWorkspaceMembersResponse200DataItemWorkspacesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        email = self.email

        name: None | str
        name = self.name

        workspaces = []
        for workspaces_item_data in self.workspaces:
            workspaces_item = workspaces_item_data.to_dict()
            workspaces.append(workspaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "email": email,
                "name": name,
                "workspaces": workspaces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_workspace_members_response_200_data_item_workspaces_item import (
            ListWorkspaceMembersResponse200DataItemWorkspacesItem,
        )

        d = dict(src_dict)
        user_id = d.pop("userId")

        email = d.pop("email")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        workspaces = []
        _workspaces = d.pop("workspaces")
        for workspaces_item_data in _workspaces:
            workspaces_item = (
                ListWorkspaceMembersResponse200DataItemWorkspacesItem.from_dict(
                    workspaces_item_data
                )
            )

            workspaces.append(workspaces_item)

        list_workspace_members_response_200_data_item = cls(
            user_id=user_id,
            email=email,
            name=name,
            workspaces=workspaces,
        )

        list_workspace_members_response_200_data_item.additional_properties = d
        return list_workspace_members_response_200_data_item

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
