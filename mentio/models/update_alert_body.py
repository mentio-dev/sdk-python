from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_alert_body_mode import UpdateAlertBodyMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_alert_body_filter import UpdateAlertBodyFilter
    from ..models.update_alert_body_schedule_type_0 import UpdateAlertBodyScheduleType0


T = TypeVar("T", bound="UpdateAlertBody")


@_attrs_define
class UpdateAlertBody:
    """Omitted fields are untouched.

    Attributes:
        name (str | Unset):
        enabled (bool | Unset):
        mode (UpdateAlertBodyMode | Unset):
        filter_ (UpdateAlertBodyFilter | Unset): Replaces the whole filter.
        schedule (None | Unset | UpdateAlertBodyScheduleType0):
        event (None | str | Unset):
        channel_ids (list[str] | Unset): Replaces the whole list.
    """

    name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    mode: UpdateAlertBodyMode | Unset = UNSET
    filter_: UpdateAlertBodyFilter | Unset = UNSET
    schedule: None | Unset | UpdateAlertBodyScheduleType0 = UNSET
    event: None | str | Unset = UNSET
    channel_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_alert_body_schedule_type_0 import (
            UpdateAlertBodyScheduleType0,
        )

        name = self.name

        enabled = self.enabled

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        schedule: dict[str, Any] | None | Unset
        if isinstance(self.schedule, Unset):
            schedule = UNSET
        elif isinstance(self.schedule, UpdateAlertBodyScheduleType0):
            schedule = self.schedule.to_dict()
        else:
            schedule = self.schedule

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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.update_alert_body_filter import (
            UpdateAlertBodyFilter,
        )
        from ..models.update_alert_body_schedule_type_0 import (
            UpdateAlertBodyScheduleType0,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: UpdateAlertBodyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = UpdateAlertBodyMode(_mode)

        _filter_ = d.pop("filter", UNSET)
        filter_: UpdateAlertBodyFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = UpdateAlertBodyFilter.from_dict(_filter_)

        def _parse_schedule(
            data: object,
        ) -> None | Unset | UpdateAlertBodyScheduleType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_type_0 = UpdateAlertBodyScheduleType0.from_dict(data)

                return schedule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAlertBodyScheduleType0, data)

        schedule = _parse_schedule(d.pop("schedule", UNSET))

        def _parse_event(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event = _parse_event(d.pop("event", UNSET))

        channel_ids = cast(list[str], d.pop("channelIds", UNSET))

        update_alert_body = cls(
            name=name,
            enabled=enabled,
            mode=mode,
            filter_=filter_,
            schedule=schedule,
            event=event,
            channel_ids=channel_ids,
        )

        update_alert_body.additional_properties = d
        return update_alert_body

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
