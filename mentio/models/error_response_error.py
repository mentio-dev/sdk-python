from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_response_error_code import ErrorResponseErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponseError")


@_attrs_define
class ErrorResponseError:
    """The error.

    Attributes:
        code (ErrorResponseErrorCode): Stable machine-readable code; branch on this, never on the message. Codes are
            additive: a client should treat one it does not know as a generic failure of the same status.
        message (str): Human-readable detail; may change between releases.
        request_id (str | Unset): The id of this request (also the X-Request-Id response header); quote it to support.
        retry_after_seconds (int | Unset): For rate_limited and other retryable errors: how long to wait before retrying
            (mirrors the Retry-After header).
    """

    code: ErrorResponseErrorCode
    message: str
    request_id: str | Unset = UNSET
    retry_after_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        request_id = self.request_id

        retry_after_seconds = self.retry_after_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if retry_after_seconds is not UNSET:
            field_dict["retryAfterSeconds"] = retry_after_seconds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = ErrorResponseErrorCode(d.pop("code"))

        message = d.pop("message")

        request_id = d.pop("requestId", UNSET)

        retry_after_seconds = d.pop("retryAfterSeconds", UNSET)

        error_response_error = cls(
            code=code,
            message=message,
            request_id=request_id,
            retry_after_seconds=retry_after_seconds,
        )

        error_response_error.additional_properties = d
        return error_response_error

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
