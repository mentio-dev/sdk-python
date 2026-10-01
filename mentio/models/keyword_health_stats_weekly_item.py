from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordHealthStatsWeeklyItem")


@_attrs_define
class KeywordHealthStatsWeeklyItem:
    """
    Attributes:
        from_ (str): First day of the 7, YYYY-MM-DD (counted from the window's first day).
        matches (int): Matches in those 7 days.
        relevant (int): Of those, relevant.
    """

    from_: str
    matches: int
    relevant: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        matches = self.matches

        relevant = self.relevant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "matches": matches,
                "relevant": relevant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        from_ = d.pop("from")

        matches = d.pop("matches")

        relevant = d.pop("relevant")

        keyword_health_stats_weekly_item = cls(
            from_=from_,
            matches=matches,
            relevant=relevant,
        )

        keyword_health_stats_weekly_item.additional_properties = d
        return keyword_health_stats_weekly_item

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
