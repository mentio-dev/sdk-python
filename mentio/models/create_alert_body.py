from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_alert_body_mode import CreateAlertBodyMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_alert_body_filter import CreateAlertBodyFilter
    from ..models.create_alert_body_schedule import CreateAlertBodySchedule


T = TypeVar("T", bound="CreateAlertBody")


@_attrs_define
class CreateAlertBody:
    """
    Attributes:
        name (str):
        enabled (bool | Unset):  Default: True.
        mode (CreateAlertBodyMode | Unset):  Default: CreateAlertBodyMode.INSTANT.
        filter_ (CreateAlertBodyFilter | Unset):
        schedule (CreateAlertBodySchedule | Unset): Required for daily alerts.
        event (None | str | Unset): Custom event name for webhook payloads; null for the mode default.
        channel_ids (list[str] | Unset): Channel ids from GET /v1/channels.
    """

    name: str
    enabled: bool | Unset = True
    mode: CreateAlertBodyMode | Unset = CreateAlertBodyMode.INSTANT
    filter_: CreateAlertBodyFilter | Unset = UNSET
    schedule: CreateAlertBodySchedule | Unset = UNSET
    event: None | str | Unset = UNSET
    channel_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enabled = self.enabled

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        event: None | str | Unset
        if isinstance(self.event, Unset):
            event = UNSET
        else:
            event = self.event

        channel_ids: list[str] | Unset = UNSET
        if not isinstance(self.channel_ids, Unset):
            channel_ids = self.channel_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if mode is not UNSET:
            field_dict["mode"] = mode
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if event is not UNSET:
            field_dict["event"] = event
        if channel_ids is not UNSET:
            field_dict["channelIds"] = channel_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_alert_body_filter import (
            CreateAlertBodyFilter,
        )
        from ..models.create_alert_body_schedule import (
            CreateAlertBodySchedule,
        )

        d = dict(src_dict)
        name = d.pop("name")

        enabled = d.pop("enabled", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: CreateAlertBodyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CreateAlertBodyMode(_mode)

        _filter_ = d.pop("filter", UNSET)
        filter_: CreateAlertBodyFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = CreateAlertBodyFilter.from_dict(_filter_)

        _schedule = d.pop("schedule", UNSET)
        schedule: CreateAlertBodySchedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = CreateAlertBodySchedule.from_dict(_schedule)

        def _parse_event(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event = _parse_event(d.pop("event", UNSET))

        channel_ids = cast(list[str], d.pop("channelIds", UNSET))

        create_alert_body = cls(
            name=name,
            enabled=enabled,
            mode=mode,
            filter_=filter_,
            schedule=schedule,
            event=event,
            channel_ids=channel_ids,
        )

        create_alert_body.additional_properties = d
        return create_alert_body

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
