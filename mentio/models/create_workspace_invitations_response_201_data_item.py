from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_workspace_invitations_response_201_data_item_status import (
    CreateWorkspaceInvitationsResponse201DataItemStatus,
)

if TYPE_CHECKING:
    from ..models.create_workspace_invitations_response_201_data_item_invitation_type_0 import (
        CreateWorkspaceInvitationsResponse201DataItemInvitationType0,
    )


T = TypeVar("T", bound="CreateWorkspaceInvitationsResponse201DataItem")


@_attrs_define
class CreateWorkspaceInvitationsResponse201DataItem:
    """
    Attributes:
        workspace_id (str): The child workspace (org_...).
        status (CreateWorkspaceInvitationsResponse201DataItemStatus): invited: a new invitation went out.
            already_invited: the address held one already, returned as it is. already_member: nothing to do.
        invitation (CreateWorkspaceInvitationsResponse201DataItemInvitationType0 | None): The open invitation; null when
            the person is already a member.
    """

    workspace_id: str
    status: CreateWorkspaceInvitationsResponse201DataItemStatus
    invitation: CreateWorkspaceInvitationsResponse201DataItemInvitationType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_workspace_invitations_response_201_data_item_invitation_type_0 import (
            CreateWorkspaceInvitationsResponse201DataItemInvitationType0,
        )

        workspace_id = self.workspace_id

        status = self.status.value

        invitation: dict[str, Any] | None
        if isinstance(
            self.invitation,
            CreateWorkspaceInvitationsResponse201DataItemInvitationType0,
        ):
            invitation = self.invitation.to_dict()
        else:
            invitation = self.invitation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspaceId": workspace_id,
                "status": status,
                "invitation": invitation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_workspace_invitations_response_201_data_item_invitation_type_0 import (
            CreateWorkspaceInvitationsResponse201DataItemInvitationType0,
        )

        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        status = CreateWorkspaceInvitationsResponse201DataItemStatus(d.pop("status"))

        def _parse_invitation(
            data: object,
        ) -> CreateWorkspaceInvitationsResponse201DataItemInvitationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invitation_type_0 = CreateWorkspaceInvitationsResponse201DataItemInvitationType0.from_dict(
                    data
                )

                return invitation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateWorkspaceInvitationsResponse201DataItemInvitationType0 | None,
                data,
            )

        invitation = _parse_invitation(d.pop("invitation"))

        create_workspace_invitations_response_201_data_item = cls(
            workspace_id=workspace_id,
            status=status,
            invitation=invitation,
        )

        create_workspace_invitations_response_201_data_item.additional_properties = d
        return create_workspace_invitations_response_201_data_item

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
