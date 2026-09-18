from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsSeriesDataItemPointsItem")


@_attrs_define
class AnalyticsSeriesDataItemPointsItem:
    """
    Attributes:
        date (str): The bucket start in `timezone`: the day (YYYY-MM-DD), the Monday of the week, the first of the
            month, or the hour as YYYY-MM-DDTHH:00.
        matched (int): Every match published in the bucket.
        relevant (int): Of those, scored at or above the relevance threshold.
        positive (int): Classified positive.
        neutral (int): Classified neutral.
        negative (int): Classified negative.
        unclassified (int): Not scored: still queued, or the classifier failed on it.
    """

    date: str
    matched: int
    relevant: int
    positive: int
    neutral: int
    negative: int
    unclassified: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        matched = self.matched

        relevant = self.relevant

        positive = self.positive

        neutral = self.neutral

        negative = self.negative

        unclassified = self.unclassified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "matched": matched,
                "relevant": relevant,
                "positive": positive,
                "neutral": neutral,
                "negative": negative,
                "unclassified": unclassified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = d.pop("date")

        matched = d.pop("matched")

        relevant = d.pop("relevant")

        positive = d.pop("positive")

        neutral = d.pop("neutral")

        negative = d.pop("negative")

        unclassified = d.pop("unclassified")

        analytics_series_data_item_points_item = cls(
            date=date,
            matched=matched,
            relevant=relevant,
            positive=positive,
            neutral=neutral,
            negative=negative,
            unclassified=unclassified,
        )

        analytics_series_data_item_points_item.additional_properties = d
        return analytics_series_data_item_points_item

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
