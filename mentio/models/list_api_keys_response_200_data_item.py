from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_api_keys_response_200_data_item_scope import (
    ListApiKeysResponse200DataItemScope,
)

T = TypeVar("T", bound="ListApiKeysResponse200DataItem")


@_attrs_define
class ListApiKeysResponse200DataItem:
    """
    Attributes:
        id (str): Key id (key_...).
        name (str):
        prefix (str): The first characters of the key, to tell keys apart.
        scope (ListApiKeysResponse200DataItemScope): read: GET only. write: everything.
        created_at (str): ISO 8601 timestamp, UTC.
        last_used_at (None | str): ISO 8601 timestamp, UTC.
        expires_at (None | str): When the key stops working; null for a key that never expires. An expired key stays
            listed until revoked.
    """

    id: str
    name: str
    prefix: str
    scope: ListApiKeysResponse200DataItemScope
    created_at: str
    last_used_at: None | str
    expires_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        prefix = self.prefix

        scope = self.scope.value

        created_at = self.created_at

        last_used_at: None | str
        last_used_at = self.last_used_at

        expires_at: None | str
        expires_at = self.expires_at

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
                "expiresAt": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        prefix = d.pop("prefix")

        scope = ListApiKeysResponse200DataItemScope(d.pop("scope"))

        created_at = d.pop("createdAt")

        def _parse_last_used_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_used_at = _parse_last_used_at(d.pop("lastUsedAt"))

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        list_api_keys_response_200_data_item = cls(
            id=id,
            name=name,
            prefix=prefix,
            scope=scope,
            created_at=created_at,
            last_used_at=last_used_at,
            expires_at=expires_at,
        )

        list_api_keys_response_200_data_item.additional_properties = d
        return list_api_keys_response_200_data_item

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
