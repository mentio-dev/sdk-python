from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsBreakdownDataItemSlotType0")


@_attrs_define
class AnalyticsBreakdownDataItemSlotType0:
    """by=hour only: the weekday and hour of day in `timezone`; null otherwise.

    Attributes:
        weekday (int): 0 = Sunday through 6 = Saturday.
        hour (int): Hour of day, 0 to 23.
    """

    weekday: int
    hour: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weekday = self.weekday

        hour = self.hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "weekday": weekday,
                "hour": hour,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        weekday = d.pop("weekday")

        hour = d.pop("hour")

        analytics_breakdown_data_item_slot_type_0 = cls(
            weekday=weekday,
            hour=hour,
        )

        analytics_breakdown_data_item_slot_type_0.additional_properties = d
        return analytics_breakdown_data_item_slot_type_0

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
