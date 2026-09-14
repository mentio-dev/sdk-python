from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsSummarySentiment")


@_attrs_define
class AnalyticsSummarySentiment:
    """Matched mentions by classifier sentiment.

    Attributes:
        positive (int): Classified positive.
        neutral (int): Classified neutral.
        negative (int): Classified negative.
        unclassified (int): Not scored: still queued, or the classifier failed on it.
    """

    positive: int
    neutral: int
    negative: int
    unclassified: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        positive = self.positive

        neutral = self.neutral

        negative = self.negative

        unclassified = self.unclassified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        positive = d.pop("positive")

        neutral = d.pop("neutral")

        negative = d.pop("negative")

        unclassified = d.pop("unclassified")

        analytics_summary_sentiment = cls(
            positive=positive,
            neutral=neutral,
            negative=negative,
            unclassified=unclassified,
        )

        analytics_summary_sentiment.additional_properties = d
        return analytics_summary_sentiment

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
