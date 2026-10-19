from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_feeds_response_200_data_item_error_type_0_code import (
    ImportFeedsResponse200DataItemErrorType0Code,
)

T = TypeVar("T", bound="ImportFeedsResponse200DataItemErrorType0")


@_attrs_define
class ImportFeedsResponse200DataItemErrorType0:
    """Why it was not connected; null unless failed.

    Attributes:
        code (ImportFeedsResponse200DataItemErrorType0Code): The same code POST /v1/feeds answers for this address:
            feed_login_required (send it again with auth), feed_login_expired (a fresh cookie), feed_unreadable (no feed, or
            the site blocks readers), feed_limit_reached, feed_auth_not_configured, validation_error (an address that is not
            one), internal_error (ours: send it again).
        message (str): What was seen, for a person.
    """

    code: ImportFeedsResponse200DataItemErrorType0Code
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = ImportFeedsResponse200DataItemErrorType0Code(d.pop("code"))

        message = d.pop("message")

        import_feeds_response_200_data_item_error_type_0 = cls(
            code=code,
            message=message,
        )

        import_feeds_response_200_data_item_error_type_0.additional_properties = d
        return import_feeds_response_200_data_item_error_type_0

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
