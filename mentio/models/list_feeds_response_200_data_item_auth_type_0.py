from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_feeds_response_200_data_item_auth_type_0_type import (
    ListFeedsResponse200DataItemAuthType0Type,
)

T = TypeVar("T", bound="ListFeedsResponse200DataItemAuthType0")


@_attrs_define
class ListFeedsResponse200DataItemAuthType0:
    """The sign-in the feed is read with, or null for a public feed. PATCH { auth } replaces it, { auth: null } removes it.

    Attributes:
        type_ (ListFeedsResponse200DataItemAuthType0Type): cookie or header. The value is never shown.
    """

    type_: ListFeedsResponse200DataItemAuthType0Type
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = ListFeedsResponse200DataItemAuthType0Type(d.pop("type"))

        list_feeds_response_200_data_item_auth_type_0 = cls(
            type_=type_,
        )

        list_feeds_response_200_data_item_auth_type_0.additional_properties = d
        return list_feeds_response_200_data_item_auth_type_0

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
