from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_api_key_body_scope import CreateApiKeyBodyScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateApiKeyBody")


@_attrs_define
class CreateApiKeyBody:
    """
    Attributes:
        name (str | Unset): A label for the key; "default" when omitted.
        scope (CreateApiKeyBodyScope | Unset): read: GET only. write: everything. Default: CreateApiKeyBodyScope.WRITE.
    """

    name: str | Unset = UNSET
    scope: CreateApiKeyBodyScope | Unset = CreateApiKeyBodyScope.WRITE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: CreateApiKeyBodyScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = CreateApiKeyBodyScope(_scope)

        create_api_key_body = cls(
            name=name,
            scope=scope,
        )

        create_api_key_body.additional_properties = d
        return create_api_key_body

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
