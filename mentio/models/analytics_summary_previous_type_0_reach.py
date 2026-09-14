from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsSummaryPreviousType0Reach")


@_attrs_define
class AnalyticsSummaryPreviousType0Reach:
    """Estimated reach.

    Attributes:
        followers (int): Followers summed over the distinct authors whose count is known: an estimate of the feeds the
            posts landed in.
        people (int): How many of `people` have a known follower count.
    """

    followers: int
    people: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        followers = self.followers

        people = self.people

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "followers": followers,
                "people": people,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        followers = d.pop("followers")

        people = d.pop("people")

        analytics_summary_previous_type_0_reach = cls(
            followers=followers,
            people=people,
        )

        analytics_summary_previous_type_0_reach.additional_properties = d
        return analytics_summary_previous_type_0_reach

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
