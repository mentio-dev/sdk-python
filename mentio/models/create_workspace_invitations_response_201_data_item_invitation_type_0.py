from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_workspace_invitations_response_201_data_item_invitation_type_0_role import (
    CreateWorkspaceInvitationsResponse201DataItemInvitationType0Role,
)

if TYPE_CHECKING:
    from ..models.create_workspace_invitations_response_201_data_item_invitation_type_0_invited_by_type_0 import (
        CreateWorkspaceInvitationsResponse201DataItemInvitationType0InvitedByType0,
    )


T = TypeVar("T", bound="CreateWorkspaceInvitationsResponse201DataItemInvitationType0")


@_attrs_define
class CreateWorkspaceInvitationsResponse201DataItemInvitationType0:
    """The open invitation; null when the person is already a member.

    Attributes:
        id (str): Invitation id (inv_...).
        email (str): The invited address, lowercased.
        role (CreateWorkspaceInvitationsResponse201DataItemInvitationType0Role): The role they join with.
        invited_by (CreateWorkspaceInvitationsResponse201DataItemInvitationType0InvitedByType0 | None): Who sent it; an
            API key invites on behalf of the oldest owner.
        expires_at (str): Invitations last 48 hours; an expired one is no longer listed.
        created_at (str): When the invitation was sent.
    """

    id: str
    email: str
    role: CreateWorkspaceInvitationsResponse201DataItemInvitationType0Role
    invited_by: (
        CreateWorkspaceInvitationsResponse201DataItemInvitationType0InvitedByType0
        | None
    )
    expires_at: str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_workspace_invitations_response_201_data_item_invitation_type_0_invited_by_type_0 import (
            CreateWorkspaceInvitationsResponse201DataItemInvitationType0InvitedByType0,
        )

        id = self.id

        email = self.email

        role = self.role.value

        invited_by: dict[str, Any] | None
        if isinstance(
            self.invited_by,
            CreateWorkspaceInvitationsResponse201DataItemInvitationType0InvitedByType0,
        ):
            invited_by = self.invited_by.to_dict()
        else:
            invited_by = self.invited_by

        expires_at = self.expires_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "role": role,
                "invitedBy": invited_by,
                "expiresAt": expires_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_workspace_invitations_response_201_data_item_invitation_type_0_invited_by_type_0 import (
            CreateWorkspaceInvitationsResponse201DataItemInvitationType0InvitedByType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        role = CreateWorkspaceInvitationsResponse201DataItemInvitationType0Role(
            d.pop("role")
        )

        def _parse_invited_by(
            data: object,
        ) -> (
            CreateWorkspaceInvitationsResponse201DataItemInvitationType0InvitedByType0
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invited_by_type_0 = CreateWorkspaceInvitationsResponse201DataItemInvitationType0InvitedByType0.from_dict(
                    data
                )

                return invited_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateWorkspaceInvitationsResponse201DataItemInvitationType0InvitedByType0
                | None,
                data,
            )

        invited_by = _parse_invited_by(d.pop("invitedBy"))

        expires_at = d.pop("expiresAt")

        created_at = d.pop("createdAt")

        create_workspace_invitations_response_201_data_item_invitation_type_0 = cls(
            id=id,
            email=email,
            role=role,
            invited_by=invited_by,
            expires_at=expires_at,
            created_at=created_at,
        )

        create_workspace_invitations_response_201_data_item_invitation_type_0.additional_properties = d
        return create_workspace_invitations_response_201_data_item_invitation_type_0

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
