from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_export_schedule_body_cadence import CreateExportScheduleBodyCadence
from ..models.create_export_schedule_body_format import CreateExportScheduleBodyFormat
from ..models.create_export_schedule_body_weekday import CreateExportScheduleBodyWeekday
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_export_schedule_body_destination_type_0 import (
        CreateExportScheduleBodyDestinationType0,
    )
    from ..models.create_export_schedule_body_destination_type_1 import (
        CreateExportScheduleBodyDestinationType1,
    )
    from ..models.create_export_schedule_body_filter import (
        CreateExportScheduleBodyFilter,
    )


T = TypeVar("T", bound="CreateExportScheduleBody")


@_attrs_define
class CreateExportScheduleBody:
    """
    Attributes:
        name (str): Unique per workspace, case-insensitive.
        cadence (CreateExportScheduleBodyCadence): hourly: at five past each UTC hour, the hour before. daily: at hour
            (UTC), the 24 hours before. weekly: on weekday at hour (UTC), the week before.
        destination (CreateExportScheduleBodyDestinationType0 | CreateExportScheduleBodyDestinationType1): Where each
            run goes. link: an export.ready event to your webhook channels, with a signed download link. s3: the file
            written into your own S3-compatible bucket (S3, R2, GCS, B2, MinIO), then the same event.
        enabled (bool | Unset): false saves it without running it. Default: True.
        format_ (CreateExportScheduleBodyFormat | Unset): csv: the spreadsheet columns of GET /v1/mentions/export.csv,
            text cut at 1,000 characters. jsonl: one whole Mention object per line (newline-delimited JSON), as GET
            /v1/mentions returns it. Default: CreateExportScheduleBodyFormat.CSV.
        filter_ (CreateExportScheduleBodyFilter | Unset): Which mentions: every filter of GET /v1/mentions except the
            window (range, from, to): each run exports the mentions matched since the previous run.
        hour (int | Unset): UTC hour daily and weekly runs start, 0 to 23 (default 6). Ignored for hourly. Default: 6.
        weekday (CreateExportScheduleBodyWeekday | Unset): Required for weekly; refused otherwise.
    """

    name: str
    cadence: CreateExportScheduleBodyCadence
    destination: (
        CreateExportScheduleBodyDestinationType0
        | CreateExportScheduleBodyDestinationType1
    )
    enabled: bool | Unset = True
    format_: CreateExportScheduleBodyFormat | Unset = CreateExportScheduleBodyFormat.CSV
    filter_: CreateExportScheduleBodyFilter | Unset = UNSET
    hour: int | Unset = 6
    weekday: CreateExportScheduleBodyWeekday | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_export_schedule_body_destination_type_0 import (
            CreateExportScheduleBodyDestinationType0,
        )

        name = self.name

        cadence = self.cadence.value

        destination: dict[str, Any]
        if isinstance(self.destination, CreateExportScheduleBodyDestinationType0):
            destination = self.destination.to_dict()
        else:
            destination = self.destination.to_dict()

        enabled = self.enabled

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        hour = self.hour

        weekday: str | Unset = UNSET
        if not isinstance(self.weekday, Unset):
            weekday = self.weekday.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "cadence": cadence,
                "destination": destination,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if format_ is not UNSET:
            field_dict["format"] = format_
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if hour is not UNSET:
            field_dict["hour"] = hour
        if weekday is not UNSET:
            field_dict["weekday"] = weekday

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_export_schedule_body_destination_type_0 import (
            CreateExportScheduleBodyDestinationType0,
        )
        from ..models.create_export_schedule_body_destination_type_1 import (
            CreateExportScheduleBodyDestinationType1,
        )
        from ..models.create_export_schedule_body_filter import (
            CreateExportScheduleBodyFilter,
        )

        d = dict(src_dict)
        name = d.pop("name")

        cadence = CreateExportScheduleBodyCadence(d.pop("cadence"))

        def _parse_destination(
            data: object,
        ) -> (
            CreateExportScheduleBodyDestinationType0
            | CreateExportScheduleBodyDestinationType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                destination_type_0 = CreateExportScheduleBodyDestinationType0.from_dict(
                    data
                )

                return destination_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            destination_type_1 = CreateExportScheduleBodyDestinationType1.from_dict(
                data
            )

            return destination_type_1

        destination = _parse_destination(d.pop("destination"))

        enabled = d.pop("enabled", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: CreateExportScheduleBodyFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = CreateExportScheduleBodyFormat(_format_)

        _filter_ = d.pop("filter", UNSET)
        filter_: CreateExportScheduleBodyFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = CreateExportScheduleBodyFilter.from_dict(_filter_)

        hour = d.pop("hour", UNSET)

        _weekday = d.pop("weekday", UNSET)
        weekday: CreateExportScheduleBodyWeekday | Unset
        if isinstance(_weekday, Unset):
            weekday = UNSET
        else:
            weekday = CreateExportScheduleBodyWeekday(_weekday)

        create_export_schedule_body = cls(
            name=name,
            cadence=cadence,
            destination=destination,
            enabled=enabled,
            format_=format_,
            filter_=filter_,
            hour=hour,
            weekday=weekday,
        )

        create_export_schedule_body.additional_properties = d
        return create_export_schedule_body

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
