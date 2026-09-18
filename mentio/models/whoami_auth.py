from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.whoami_auth_kind import WhoamiAuthKind
from ..models.whoami_auth_scope import WhoamiAuthScope

T = TypeVar("T", bound="WhoamiAuth")


@_attrs_define
class WhoamiAuth:
    """The credential.

    Attributes:
        kind (WhoamiAuthKind): How the request authenticated: an API key, an OAuth access token (MCP sign-in), or the
            dashboard session.
        scope (WhoamiAuthScope): What the credential may do: read (GET only) or write.
        api_key_id (None | str): The key id (key_...) when authenticated with an API key; null otherwise.
        expires_at (None | str): When an API key stops working; null for a key that never expires, an OAuth token or a
            session.
    """

    kind: WhoamiAuthKind
    scope: WhoamiAuthScope
    api_key_id: None | str
    expires_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        scope = self.scope.value

        api_key_id: None | str
        api_key_id = self.api_key_id

        expires_at: None | str
        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "scope": scope,
                "apiKeyId": api_key_id,
                "expiresAt": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = WhoamiAuthKind(d.pop("kind"))

        scope = WhoamiAuthScope(d.pop("scope"))

        def _parse_api_key_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        api_key_id = _parse_api_key_id(d.pop("apiKeyId"))

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        whoami_auth = cls(
            kind=kind,
            scope=scope,
            api_key_id=api_key_id,
            expires_at=expires_at,
        )

        whoami_auth.additional_properties = d
        return whoami_auth

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
