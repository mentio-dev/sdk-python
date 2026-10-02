from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MentionSpikeEventDataBaseline")


@_attrs_define
class MentionSpikeEventDataBaseline:
    """What the keyword usually gets.

    Attributes:
        mean_per_hour (float): Fresh matches per hour over the baseline.
        stddev_per_hour (float): Their standard deviation.
        hours (int): Hours in the baseline: the week before the window, or since the keyword started listening.
    """

    mean_per_hour: float
    stddev_per_hour: float
    hours: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mean_per_hour = self.mean_per_hour

        stddev_per_hour = self.stddev_per_hour

        hours = self.hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meanPerHour": mean_per_hour,
                "stddevPerHour": stddev_per_hour,
                "hours": hours,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mean_per_hour = d.pop("meanPerHour")

        stddev_per_hour = d.pop("stddevPerHour")

        hours = d.pop("hours")

        mention_spike_event_data_baseline = cls(
            mean_per_hour=mean_per_hour,
            stddev_per_hour=stddev_per_hour,
            hours=hours,
        )

        mention_spike_event_data_baseline.additional_properties = d
        return mention_spike_event_data_baseline

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
