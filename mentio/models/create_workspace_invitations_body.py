from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_workspace_invitations_body_role import (
    CreateWorkspaceInvitationsBodyRole,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWorkspaceInvitationsBody")


@_attrs_define
class CreateWorkspaceInvitationsBody:
    """
    Attributes:
        email (str): The address to invite; it receives one email per workspace with a link to join.
        workspace_ids (list[str]): The child workspaces (org_...) to invite them to.
        role (CreateWorkspaceInvitationsBodyRole | Unset): The role they join each workspace with. Default:
            CreateWorkspaceInvitationsBodyRole.MEMBER.
    """

    email: str
    workspace_ids: list[str]
    role: CreateWorkspaceInvitationsBodyRole | Unset = (
        CreateWorkspaceInvitationsBodyRole.MEMBER
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        workspace_ids = self.workspace_ids

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "workspaceIds": workspace_ids,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        workspace_ids = cast(list[str], d.pop("workspaceIds"))

        _role = d.pop("role", UNSET)
        role: CreateWorkspaceInvitationsBodyRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = CreateWorkspaceInvitationsBodyRole(_role)

        create_workspace_invitations_body = cls(
            email=email,
            workspace_ids=workspace_ids,
            role=role,
        )

        create_workspace_invitations_body.additional_properties = d
        return create_workspace_invitations_body

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
