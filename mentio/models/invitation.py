from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invitation_role import InvitationRole

if TYPE_CHECKING:
    from ..models.invitation_invited_by_type_0 import InvitationInvitedByType0


T = TypeVar("T", bound="Invitation")


@_attrs_define
class Invitation:
    """
    Attributes:
        id (str): Invitation id (inv_...).
        email (str): The invited address, lowercased.
        role (InvitationRole): The role they join with.
        invited_by (InvitationInvitedByType0 | None): Who sent it; an API key invites on behalf of the oldest owner.
        expires_at (str): Invitations last 48 hours; an expired one is no longer listed.
        created_at (str): When the invitation was sent.
    """

    id: str
    email: str
    role: InvitationRole
    invited_by: InvitationInvitedByType0 | None
    expires_at: str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.invitation_invited_by_type_0 import (
            InvitationInvitedByType0,
        )

        id = self.id

        email = self.email

        role = self.role.value

        invited_by: dict[str, Any] | None
        if isinstance(self.invited_by, InvitationInvitedByType0):
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
        from ..models.invitation_invited_by_type_0 import (
            InvitationInvitedByType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        role = InvitationRole(d.pop("role"))

        def _parse_invited_by(data: object) -> InvitationInvitedByType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invited_by_type_0 = InvitationInvitedByType0.from_dict(data)

                return invited_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvitationInvitedByType0 | None, data)

        invited_by = _parse_invited_by(d.pop("invitedBy"))

        expires_at = d.pop("expiresAt")

        created_at = d.pop("createdAt")

        invitation = cls(
            id=id,
            email=email,
            role=role,
            invited_by=invited_by,
            expires_at=expires_at,
            created_at=created_at,
        )

        invitation.additional_properties = d
        return invitation

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
