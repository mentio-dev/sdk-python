from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_schedule_cadence import ExportScheduleCadence
from ..models.export_schedule_format import ExportScheduleFormat
from ..models.export_schedule_weekday import ExportScheduleWeekday

if TYPE_CHECKING:
    from ..models.export_schedule_destination_type_0 import (
        ExportScheduleDestinationType0,
    )
    from ..models.export_schedule_destination_type_1 import (
        ExportScheduleDestinationType1,
    )
    from ..models.export_schedule_filter import ExportScheduleFilter


T = TypeVar("T", bound="ExportSchedule")


@_attrs_define
class ExportSchedule:
    """
    Attributes:
        id (str): Schedule id (exs_...).
        name (str): Schedule name, unique in the workspace.
        enabled (bool): false: kept, never run.
        format_ (ExportScheduleFormat): csv: the spreadsheet columns of GET /v1/mentions/export.csv, text cut at 1,000
            characters. jsonl: one whole Mention object per line (newline-delimited JSON), as GET /v1/mentions returns it.
        filter_ (ExportScheduleFilter): Which mentions: every filter of GET /v1/mentions except the window (range, from,
            to): each run exports the mentions matched since the previous run.
        cadence (ExportScheduleCadence): hourly: at five past each UTC hour, the hour before. daily: at hour (UTC), the
            24 hours before. weekly: on weekday at hour (UTC), the week before.
        hour (int): UTC hour daily and weekly runs start.
        weekday (ExportScheduleWeekday): Weekly runs: the day; null otherwise.
        destination (ExportScheduleDestinationType0 | ExportScheduleDestinationType1): Where each run goes.
        next_run_at (None | str): When it runs next; null while disabled.
        last_run_at (None | str): When it last ran.
        last_export_id (None | str): The export its last run made (exp_...).
        last_error (None | str): Why the last run or delivery failed; null after one that worked.
        created_at (str): ISO 8601 timestamp, UTC.
        updated_at (str): ISO 8601 timestamp, UTC.
    """

    id: str
    name: str
    enabled: bool
    format_: ExportScheduleFormat
    filter_: ExportScheduleFilter
    cadence: ExportScheduleCadence
    hour: int
    weekday: ExportScheduleWeekday
    destination: ExportScheduleDestinationType0 | ExportScheduleDestinationType1
    next_run_at: None | str
    last_run_at: None | str
    last_export_id: None | str
    last_error: None | str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.export_schedule_destination_type_0 import (
            ExportScheduleDestinationType0,
        )

        id = self.id

        name = self.name

        enabled = self.enabled

        format_ = self.format_.value

        filter_ = self.filter_.to_dict()

        cadence = self.cadence.value

        hour = self.hour

        weekday = self.weekday.value

        destination: dict[str, Any]
        if isinstance(self.destination, ExportScheduleDestinationType0):
            destination = self.destination.to_dict()
        else:
            destination = self.destination.to_dict()

        next_run_at: None | str
        next_run_at = self.next_run_at

        last_run_at: None | str
        last_run_at = self.last_run_at

        last_export_id: None | str
        last_export_id = self.last_export_id

        last_error: None | str
        last_error = self.last_error

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "enabled": enabled,
                "format": format_,
                "filter": filter_,
                "cadence": cadence,
                "hour": hour,
                "weekday": weekday,
                "destination": destination,
                "nextRunAt": next_run_at,
                "lastRunAt": last_run_at,
                "lastExportId": last_export_id,
                "lastError": last_error,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.export_schedule_destination_type_0 import (
            ExportScheduleDestinationType0,
        )
        from ..models.export_schedule_destination_type_1 import (
            ExportScheduleDestinationType1,
        )
        from ..models.export_schedule_filter import ExportScheduleFilter

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        enabled = d.pop("enabled")

        format_ = ExportScheduleFormat(d.pop("format"))

        filter_ = ExportScheduleFilter.from_dict(d.pop("filter"))

        cadence = ExportScheduleCadence(d.pop("cadence"))

        hour = d.pop("hour")

        weekday = ExportScheduleWeekday(d.pop("weekday"))

        def _parse_destination(
            data: object,
        ) -> ExportScheduleDestinationType0 | ExportScheduleDestinationType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                destination_type_0 = ExportScheduleDestinationType0.from_dict(data)

                return destination_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            destination_type_1 = ExportScheduleDestinationType1.from_dict(data)

            return destination_type_1

        destination = _parse_destination(d.pop("destination"))

        def _parse_next_run_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_run_at = _parse_next_run_at(d.pop("nextRunAt"))

        def _parse_last_run_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_run_at = _parse_last_run_at(d.pop("lastRunAt"))

        def _parse_last_export_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_export_id = _parse_last_export_id(d.pop("lastExportId"))

        def _parse_last_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_error = _parse_last_error(d.pop("lastError"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        export_schedule = cls(
            id=id,
            name=name,
            enabled=enabled,
            format_=format_,
            filter_=filter_,
            cadence=cadence,
            hour=hour,
            weekday=weekday,
            destination=destination,
            next_run_at=next_run_at,
            last_run_at=last_run_at,
            last_export_id=last_export_id,
            last_error=last_error,
            created_at=created_at,
            updated_at=updated_at,
        )

        export_schedule.additional_properties = d
        return export_schedule

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
