from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_mode import AlertMode

if TYPE_CHECKING:
    from ..models.alert_channels_item import AlertChannelsItem
    from ..models.alert_filter import AlertFilter
    from ..models.alert_schedule_type_0 import AlertScheduleType0
    from ..models.alert_stats import AlertStats


T = TypeVar("T", bound="Alert")


@_attrs_define
class Alert:
    """
    Attributes:
        id (str): Alert id (feed_...).
        name (str):
        enabled (bool):
        mode (AlertMode): instant: each matching mention as it happens. daily: one digest at the scheduled local time.
            weekly: one digest a week, on schedule.weekday.
        filter_ (AlertFilter):
        schedule (AlertScheduleType0 | None): Daily and weekly alerts only.
        event (str): Event name carried in webhook payloads; the mode default unless you set one.
        channels (list[AlertChannelsItem]): Where it sends.
        stats (AlertStats): Computed over this workspace's deliveries.
        created_at (str): ISO 8601 timestamp, UTC.
    """

    id: str
    name: str
    enabled: bool
    mode: AlertMode
    filter_: AlertFilter
    schedule: AlertScheduleType0 | None
    event: str
    channels: list[AlertChannelsItem]
    stats: AlertStats
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alert_schedule_type_0 import AlertScheduleType0

        id = self.id

        name = self.name

        enabled = self.enabled

        mode = self.mode.value

        filter_ = self.filter_.to_dict()

        schedule: dict[str, Any] | None
        if isinstance(self.schedule, AlertScheduleType0):
            schedule = self.schedule.to_dict()
        else:
            schedule = self.schedule

        event = self.event

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)

        stats = self.stats.to_dict()

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "enabled": enabled,
                "mode": mode,
                "filter": filter_,
                "schedule": schedule,
                "event": event,
                "channels": channels,
                "stats": stats,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_channels_item import AlertChannelsItem
        from ..models.alert_filter import AlertFilter
        from ..models.alert_schedule_type_0 import AlertScheduleType0
        from ..models.alert_stats import AlertStats

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        enabled = d.pop("enabled")

        mode = AlertMode(d.pop("mode"))

        filter_ = AlertFilter.from_dict(d.pop("filter"))

        def _parse_schedule(data: object) -> AlertScheduleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_type_0 = AlertScheduleType0.from_dict(data)

                return schedule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertScheduleType0 | None, data)

        schedule = _parse_schedule(d.pop("schedule"))

        event = d.pop("event")

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = AlertChannelsItem.from_dict(channels_item_data)

            channels.append(channels_item)

        stats = AlertStats.from_dict(d.pop("stats"))

        created_at = d.pop("createdAt")

        alert = cls(
            id=id,
            name=name,
            enabled=enabled,
            mode=mode,
            filter_=filter_,
            schedule=schedule,
            event=event,
            channels=channels,
            stats=stats,
            created_at=created_at,
        )

        alert.additional_properties = d
        return alert

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
