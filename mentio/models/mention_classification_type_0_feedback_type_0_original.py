from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_classification_type_0_feedback_type_0_original_sentiment import (
    MentionClassificationType0FeedbackType0OriginalSentiment,
)

T = TypeVar("T", bound="MentionClassificationType0FeedbackType0Original")


@_attrs_define
class MentionClassificationType0FeedbackType0Original:
    """The classifier values your feedback replaced.

    Attributes:
        relevance (int | None): What the classifier scored before your verdict; null if it had not scored it.
        sentiment (MentionClassificationType0FeedbackType0OriginalSentiment): The sentiment the classifier gave before
            your correction.
    """

    relevance: int | None
    sentiment: MentionClassificationType0FeedbackType0OriginalSentiment
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relevance: int | None
        relevance = self.relevance

        sentiment = self.sentiment.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relevance": relevance,
                "sentiment": sentiment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_relevance(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        relevance = _parse_relevance(d.pop("relevance"))

        sentiment = MentionClassificationType0FeedbackType0OriginalSentiment(
            d.pop("sentiment")
        )

        mention_classification_type_0_feedback_type_0_original = cls(
            relevance=relevance,
            sentiment=sentiment,
        )

        mention_classification_type_0_feedback_type_0_original.additional_properties = d
        return mention_classification_type_0_feedback_type_0_original

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
