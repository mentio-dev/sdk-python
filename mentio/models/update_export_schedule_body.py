from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_export_schedule_body_cadence import UpdateExportScheduleBodyCadence
from ..models.update_export_schedule_body_format import UpdateExportScheduleBodyFormat
from ..models.update_export_schedule_body_weekday import UpdateExportScheduleBodyWeekday
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_export_schedule_body_destination_type_0 import (
        UpdateExportScheduleBodyDestinationType0,
    )
    from ..models.update_export_schedule_body_destination_type_1 import (
        UpdateExportScheduleBodyDestinationType1,
    )
    from ..models.update_export_schedule_body_filter import (
        UpdateExportScheduleBodyFilter,
    )


T = TypeVar("T", bound="UpdateExportScheduleBody")


@_attrs_define
class UpdateExportScheduleBody:
    """
    Attributes:
        name (str | Unset): Schedule name, unique in the workspace.
        enabled (bool | Unset): false stops it; true starts it again from the next run.
        format_ (UpdateExportScheduleBodyFormat | Unset): csv: the spreadsheet columns of GET /v1/mentions/export.csv,
            text cut at 1,000 characters. jsonl: one whole Mention object per line (newline-delimited JSON), as GET
            /v1/mentions returns it.
        filter_ (UpdateExportScheduleBodyFilter | Unset): Replaces the whole filter.
        cadence (UpdateExportScheduleBodyCadence | Unset): hourly: at five past each UTC hour, the hour before. daily:
            at hour (UTC), the 24 hours before. weekly: on weekday at hour (UTC), the week before.
        hour (int | Unset): UTC hour daily and weekly runs start, 0 to 23 (default 6). Ignored for hourly.
        weekday (UpdateExportScheduleBodyWeekday | Unset): Weekly runs: the day; null clears it (only when the cadence
            is no longer weekly).
        destination (Unset | UpdateExportScheduleBodyDestinationType0 | UpdateExportScheduleBodyDestinationType1):
            Replaces the destination. An s3 one may leave secretAccessKey out to keep the stored secret.
    """

    name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    format_: UpdateExportScheduleBodyFormat | Unset = UNSET
    filter_: UpdateExportScheduleBodyFilter | Unset = UNSET
    cadence: UpdateExportScheduleBodyCadence | Unset = UNSET
    hour: int | Unset = UNSET
    weekday: UpdateExportScheduleBodyWeekday | Unset = UNSET
    destination: (
        Unset
        | UpdateExportScheduleBodyDestinationType0
        | UpdateExportScheduleBodyDestinationType1
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_export_schedule_body_destination_type_0 import (
            UpdateExportScheduleBodyDestinationType0,
        )

        name = self.name

        enabled = self.enabled

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        cadence: str | Unset = UNSET
        if not isinstance(self.cadence, Unset):
            cadence = self.cadence.value

        hour = self.hour

        weekday: str | Unset = UNSET
        if not isinstance(self.weekday, Unset):
            weekday = self.weekday.value

        destination: dict[str, Any] | Unset
        if isinstance(self.destination, Unset):
            destination = UNSET
        elif isinstance(self.destination, UpdateExportScheduleBodyDestinationType0):
            destination = self.destination.to_dict()
        else:
            destination = self.destination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if format_ is not UNSET:
            field_dict["format"] = format_
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if cadence is not UNSET:
            field_dict["cadence"] = cadence
        if hour is not UNSET:
            field_dict["hour"] = hour
        if weekday is not UNSET:
            field_dict["weekday"] = weekday
        if destination is not UNSET:
            field_dict["destination"] = destination

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_export_schedule_body_destination_type_0 import (
            UpdateExportScheduleBodyDestinationType0,
        )
        from ..models.update_export_schedule_body_destination_type_1 import (
            UpdateExportScheduleBodyDestinationType1,
        )
        from ..models.update_export_schedule_body_filter import (
            UpdateExportScheduleBodyFilter,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: UpdateExportScheduleBodyFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = UpdateExportScheduleBodyFormat(_format_)

        _filter_ = d.pop("filter", UNSET)
        filter_: UpdateExportScheduleBodyFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = UpdateExportScheduleBodyFilter.from_dict(_filter_)

        _cadence = d.pop("cadence", UNSET)
        cadence: UpdateExportScheduleBodyCadence | Unset
        if isinstance(_cadence, Unset):
            cadence = UNSET
        else:
            cadence = UpdateExportScheduleBodyCadence(_cadence)

        hour = d.pop("hour", UNSET)

        _weekday = d.pop("weekday", UNSET)
        weekday: UpdateExportScheduleBodyWeekday | Unset
        if isinstance(_weekday, Unset):
            weekday = UNSET
        else:
            weekday = UpdateExportScheduleBodyWeekday(_weekday)

        def _parse_destination(
            data: object,
        ) -> (
            Unset
            | UpdateExportScheduleBodyDestinationType0
            | UpdateExportScheduleBodyDestinationType1
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                destination_type_0 = UpdateExportScheduleBodyDestinationType0.from_dict(
                    data
                )

                return destination_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            destination_type_1 = UpdateExportScheduleBodyDestinationType1.from_dict(
                data
            )

            return destination_type_1

        destination = _parse_destination(d.pop("destination", UNSET))

        update_export_schedule_body = cls(
            name=name,
            enabled=enabled,
            format_=format_,
            filter_=filter_,
            cadence=cadence,
            hour=hour,
            weekday=weekday,
            destination=destination,
        )

        update_export_schedule_body.additional_properties = d
        return update_export_schedule_body

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
