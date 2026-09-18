from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertScheduleType0")


@_attrs_define
class AlertScheduleType0:
    """Daily and weekly alerts only.

    Attributes:
        hour (int):
        timezone (str):
        minute (int | Unset):  Default: 0.
        skip_empty (bool | Unset):  Default: True.
        weekday (int | Unset): Weekly rules: the day it sends, 0 Sunday to 6 Saturday. Required for mode weekly; ignored
            on daily rules.
    """

    hour: int
    timezone: str
    minute: int | Unset = 0
    skip_empty: bool | Unset = True
    weekday: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hour = self.hour

        timezone = self.timezone

        minute = self.minute

        skip_empty = self.skip_empty

        weekday = self.weekday

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hour": hour,
                "timezone": timezone,
            }
        )
        if minute is not UNSET:
            field_dict["minute"] = minute
        if skip_empty is not UNSET:
            field_dict["skipEmpty"] = skip_empty
        if weekday is not UNSET:
            field_dict["weekday"] = weekday

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hour = d.pop("hour")

        timezone = d.pop("timezone")

        minute = d.pop("minute", UNSET)

        skip_empty = d.pop("skipEmpty", UNSET)

        weekday = d.pop("weekday", UNSET)

        alert_schedule_type_0 = cls(
            hour=hour,
            timezone=timezone,
            minute=minute,
            skip_empty=skip_empty,
            weekday=weekday,
        )

        alert_schedule_type_0.additional_properties = d
        return alert_schedule_type_0

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
