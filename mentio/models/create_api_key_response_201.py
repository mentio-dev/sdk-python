from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_api_key_response_201_scope import CreateApiKeyResponse201Scope

T = TypeVar("T", bound="CreateApiKeyResponse201")


@_attrs_define
class CreateApiKeyResponse201:
    """
    Attributes:
        id (str): Key id (key_...).
        name (str):
        prefix (str): The first characters of the key, to tell keys apart.
        scope (CreateApiKeyResponse201Scope): read: GET only. write: everything.
        created_at (str): ISO 8601 timestamp, UTC.
        last_used_at (None | str): ISO 8601 timestamp, UTC.
        key (str): The full key. Shown once; store it now.
    """

    id: str
    name: str
    prefix: str
    scope: CreateApiKeyResponse201Scope
    created_at: str
    last_used_at: None | str
    key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        prefix = self.prefix

        scope = self.scope.value

        created_at = self.created_at

        last_used_at: None | str
        last_used_at = self.last_used_at

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "prefix": prefix,
                "scope": scope,
                "createdAt": created_at,
                "lastUsedAt": last_used_at,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        prefix = d.pop("prefix")

        scope = CreateApiKeyResponse201Scope(d.pop("scope"))

        created_at = d.pop("createdAt")

        def _parse_last_used_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_used_at = _parse_last_used_at(d.pop("lastUsedAt"))

        key = d.pop("key")

        create_api_key_response_201 = cls(
            id=id,
            name=name,
            prefix=prefix,
            scope=scope,
            created_at=created_at,
            last_used_at=last_used_at,
            key=key,
        )

        create_api_key_response_201.additional_properties = d
        return create_api_key_response_201

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
