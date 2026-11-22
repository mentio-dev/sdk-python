from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExportDownloadType0")


@_attrs_define
class ExportDownloadType0:
    """Once it succeeded: a signed download link, valid for an hour. null before, after the file expired, or when this
    deployment cannot sign links.

        Attributes:
            url (str): Signed link to the file; works without a key until expiresAt. GET /v1/exports/{id}/file downloads it
                with a key.
            expires_at (str): When this link stops working; read the export again for a fresh one.
    """

    url: str
    expires_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "expiresAt": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url")

        expires_at = d.pop("expiresAt")

        export_download_type_0 = cls(
            url=url,
            expires_at=expires_at,
        )

        export_download_type_0.additional_properties = d
        return export_download_type_0

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
