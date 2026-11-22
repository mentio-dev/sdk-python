from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_export_body_format import CreateExportBodyFormat
from ..models.create_export_body_resource import CreateExportBodyResource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_export_body_filter import CreateExportBodyFilter


T = TypeVar("T", bound="CreateExportBody")


@_attrs_define
class CreateExportBody:
    """
    Attributes:
        resource (CreateExportBodyResource | Unset): What is exported: mentions. Default:
            CreateExportBodyResource.MENTIONS.
        format_ (CreateExportBodyFormat | Unset): csv: the spreadsheet columns of GET /v1/mentions/export.csv, text cut
            at 1,000 characters. jsonl: one whole Mention object per line (newline-delimited JSON), as GET /v1/mentions
            returns it. Default: CreateExportBodyFormat.CSV.
        filter_ (CreateExportBodyFilter | Unset): Which mentions: every filter of GET /v1/mentions, in the same
            vocabulary (a list as an array or comma-separated), viewId and alertId included. {} is every mention the list
            shows.
        max_rows (int | Unset): Stop after this many rows, newest matched first. At most 1,000,000, the default.
    """

    resource: CreateExportBodyResource | Unset = CreateExportBodyResource.MENTIONS
    format_: CreateExportBodyFormat | Unset = CreateExportBodyFormat.CSV
    filter_: CreateExportBodyFilter | Unset = UNSET
    max_rows: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource: str | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.value

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        max_rows = self.max_rows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource is not UNSET:
            field_dict["resource"] = resource
        if format_ is not UNSET:
            field_dict["format"] = format_
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if max_rows is not UNSET:
            field_dict["maxRows"] = max_rows

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_export_body_filter import CreateExportBodyFilter

        d = dict(src_dict)
        _resource = d.pop("resource", UNSET)
        resource: CreateExportBodyResource | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = CreateExportBodyResource(_resource)

        _format_ = d.pop("format", UNSET)
        format_: CreateExportBodyFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = CreateExportBodyFormat(_format_)

        _filter_ = d.pop("filter", UNSET)
        filter_: CreateExportBodyFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = CreateExportBodyFilter.from_dict(_filter_)

        max_rows = d.pop("maxRows", UNSET)

        create_export_body = cls(
            resource=resource,
            format_=format_,
            filter_=filter_,
            max_rows=max_rows,
        )

        create_export_body.additional_properties = d
        return create_export_body

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
