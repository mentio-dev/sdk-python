from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_delivery_type_0_kind import ExportDeliveryType0Kind
from ..models.export_delivery_type_0_status import ExportDeliveryType0Status

T = TypeVar("T", bound="ExportDeliveryType0")


@_attrs_define
class ExportDeliveryType0:
    """A scheduled run: where the file goes and how that went. null for a one-off export.

    Attributes:
        kind (ExportDeliveryType0Kind): link: an export.ready webhook event. s3: the file written into your bucket.
        status (ExportDeliveryType0Status): pending, delivered or failed.
        key (None | str): s3: the object key written.
        error (None | str): Why the last attempt failed.
        delivered_at (None | str): When it was delivered.
    """

    kind: ExportDeliveryType0Kind
    status: ExportDeliveryType0Status
    key: None | str
    error: None | str
    delivered_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        status = self.status.value

        key: None | str
        key = self.key

        error: None | str
        error = self.error

        delivered_at: None | str
        delivered_at = self.delivered_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "status": status,
                "key": key,
                "error": error,
                "deliveredAt": delivered_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = ExportDeliveryType0Kind(d.pop("kind"))

        status = ExportDeliveryType0Status(d.pop("status"))

        def _parse_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key = _parse_key(d.pop("key"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        def _parse_delivered_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        delivered_at = _parse_delivered_at(d.pop("deliveredAt"))

        export_delivery_type_0 = cls(
            kind=kind,
            status=status,
            key=key,
            error=error,
            delivered_at=delivered_at,
        )

        export_delivery_type_0.additional_properties = d
        return export_delivery_type_0

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
