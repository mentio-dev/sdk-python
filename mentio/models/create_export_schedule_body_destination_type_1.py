from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_export_schedule_body_destination_type_1_kind import (
    CreateExportScheduleBodyDestinationType1Kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateExportScheduleBodyDestinationType1")


@_attrs_define
class CreateExportScheduleBodyDestinationType1:
    """
    Attributes:
        kind (CreateExportScheduleBodyDestinationType1Kind): Your own S3-compatible bucket.
        endpoint (str): The S3 API endpoint, https: https://s3.eu-west-1.amazonaws.com,
            https://<account>.r2.cloudflarestorage.com, https://storage.googleapis.com, https://s3.us-
            west-004.backblazeb2.com.
        bucket (str): The bucket name.
        access_key_id (str): Access key id with write access to the bucket.
        region (str | Unset): The region the signature names: auto for R2 and GCS, eu-west-1 and so on for S3. Default:
            'auto'.
        prefix (str | Unset): Prepended to every object key (mentio/ puts the files in a folder). Default: ''.
        path_style (bool | Unset): true: https://endpoint/bucket/key (works everywhere). false:
            https://bucket.endpoint/key. Default: True.
        secret_access_key (str | Unset): Its secret. Write-only: stored encrypted, never shown again. Required unless an
            update keeps the secret already stored.
    """

    kind: CreateExportScheduleBodyDestinationType1Kind
    endpoint: str
    bucket: str
    access_key_id: str
    region: str | Unset = "auto"
    prefix: str | Unset = ""
    path_style: bool | Unset = True
    secret_access_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        endpoint = self.endpoint

        bucket = self.bucket

        access_key_id = self.access_key_id

        region = self.region

        prefix = self.prefix

        path_style = self.path_style

        secret_access_key = self.secret_access_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "endpoint": endpoint,
                "bucket": bucket,
                "accessKeyId": access_key_id,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if path_style is not UNSET:
            field_dict["pathStyle"] = path_style
        if secret_access_key is not UNSET:
            field_dict["secretAccessKey"] = secret_access_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = CreateExportScheduleBodyDestinationType1Kind(d.pop("kind"))

        endpoint = d.pop("endpoint")

        bucket = d.pop("bucket")

        access_key_id = d.pop("accessKeyId")

        region = d.pop("region", UNSET)

        prefix = d.pop("prefix", UNSET)

        path_style = d.pop("pathStyle", UNSET)

        secret_access_key = d.pop("secretAccessKey", UNSET)

        create_export_schedule_body_destination_type_1 = cls(
            kind=kind,
            endpoint=endpoint,
            bucket=bucket,
            access_key_id=access_key_id,
            region=region,
            prefix=prefix,
            path_style=path_style,
            secret_access_key=secret_access_key,
        )

        create_export_schedule_body_destination_type_1.additional_properties = d
        return create_export_schedule_body_destination_type_1

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
