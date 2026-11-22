from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TopicClusterEventDataBaseline")


@_attrs_define
class TopicClusterEventDataBaseline:
    """What the keyword usually gets.

    Attributes:
        count (int): Posts carrying it in the 7 days before the window.
        per_day (float): The usual daily count, smoothed so a tag the keyword never had still needs a crowd.
    """

    count: int
    per_day: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        per_day = self.per_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "perDay": per_day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count")

        per_day = d.pop("perDay")

        topic_cluster_event_data_baseline = cls(
            count=count,
            per_day=per_day,
        )

        topic_cluster_event_data_baseline.additional_properties = d
        return topic_cluster_event_data_baseline

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
