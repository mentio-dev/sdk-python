from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_schedule_destination_type_1_kind import (
    ExportScheduleDestinationType1Kind,
)

T = TypeVar("T", bound="ExportScheduleDestinationType1")


@_attrs_define
class ExportScheduleDestinationType1:
    """
    Attributes:
        kind (ExportScheduleDestinationType1Kind): Your own S3-compatible bucket.
        endpoint (str): The S3 API endpoint.
        bucket (str): The bucket name.
        region (str): The region the signature names.
        prefix (str): Prepended to every object key.
        path_style (bool): Path-style (true) or virtual-hosted (false) addressing.
        access_key_id (str): The access key id.
        secret_set (bool): Always true: the secret is stored encrypted and never shown.
    """

    kind: ExportScheduleDestinationType1Kind
    endpoint: str
    bucket: str
    region: str
    prefix: str
    path_style: bool
    access_key_id: str
    secret_set: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        endpoint = self.endpoint

        bucket = self.bucket

        region = self.region

        prefix = self.prefix

        path_style = self.path_style

        access_key_id = self.access_key_id

        secret_set = self.secret_set

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "endpoint": endpoint,
                "bucket": bucket,
                "region": region,
                "prefix": prefix,
                "pathStyle": path_style,
                "accessKeyId": access_key_id,
                "secretSet": secret_set,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = ExportScheduleDestinationType1Kind(d.pop("kind"))

        endpoint = d.pop("endpoint")

        bucket = d.pop("bucket")

        region = d.pop("region")

        prefix = d.pop("prefix")

        path_style = d.pop("pathStyle")

        access_key_id = d.pop("accessKeyId")

        secret_set = d.pop("secretSet")

        export_schedule_destination_type_1 = cls(
            kind=kind,
            endpoint=endpoint,
            bucket=bucket,
            region=region,
            prefix=prefix,
            path_style=path_style,
            access_key_id=access_key_id,
            secret_set=secret_set,
        )

        export_schedule_destination_type_1.additional_properties = d
        return export_schedule_destination_type_1

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
