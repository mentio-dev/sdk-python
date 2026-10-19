from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_feeds_body_feeds_item_auth_type_0_type import (
    ImportFeedsBodyFeedsItemAuthType0Type,
)

T = TypeVar("T", bound="ImportFeedsBodyFeedsItemAuthType0")


@_attrs_define
class ImportFeedsBodyFeedsItemAuthType0:
    """
    Attributes:
        type_ (ImportFeedsBodyFeedsItemAuthType0Type):
        value (str): The Cookie header your browser sends to the forum (devtools, Network, the feed's request, Request
            Headers, cookie).
    """

    type_: ImportFeedsBodyFeedsItemAuthType0Type
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = ImportFeedsBodyFeedsItemAuthType0Type(d.pop("type"))

        value = d.pop("value")

        import_feeds_body_feeds_item_auth_type_0 = cls(
            type_=type_,
            value=value,
        )

        import_feeds_body_feeds_item_auth_type_0.additional_properties = d
        return import_feeds_body_feeds_item_auth_type_0

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
