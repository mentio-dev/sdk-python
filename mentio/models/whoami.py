from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.whoami_auth import WhoamiAuth
    from ..models.whoami_user_type_0 import WhoamiUserType0
    from ..models.whoami_workspace import WhoamiWorkspace


T = TypeVar("T", bound="Whoami")


@_attrs_define
class Whoami:
    """
    Attributes:
        workspace (WhoamiWorkspace): The workspace this credential acts on.
        auth (WhoamiAuth): The credential.
        user (None | WhoamiUserType0): The person behind an OAuth token or a session; null for an API key, which has no
            person behind it.
    """

    workspace: WhoamiWorkspace
    auth: WhoamiAuth
    user: None | WhoamiUserType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.whoami_user_type_0 import WhoamiUserType0

        workspace = self.workspace.to_dict()

        auth = self.auth.to_dict()

        user: dict[str, Any] | None
        if isinstance(self.user, WhoamiUserType0):
            user = self.user.to_dict()
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace": workspace,
                "auth": auth,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.whoami_auth import WhoamiAuth
        from ..models.whoami_user_type_0 import WhoamiUserType0
        from ..models.whoami_workspace import WhoamiWorkspace

        d = dict(src_dict)
        workspace = WhoamiWorkspace.from_dict(d.pop("workspace"))

        auth = WhoamiAuth.from_dict(d.pop("auth"))

        def _parse_user(data: object) -> None | WhoamiUserType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = WhoamiUserType0.from_dict(data)

                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WhoamiUserType0, data)

        user = _parse_user(d.pop("user"))

        whoami = cls(
            workspace=workspace,
            auth=auth,
            user=user,
        )

        whoami.additional_properties = d
        return whoami

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
