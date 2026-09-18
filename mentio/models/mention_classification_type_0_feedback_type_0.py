from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_classification_type_0_feedback_type_0_sentiment import (
    MentionClassificationType0FeedbackType0Sentiment,
)

if TYPE_CHECKING:
    from ..models.mention_classification_type_0_feedback_type_0_original import (
        MentionClassificationType0FeedbackType0Original,
    )


T = TypeVar("T", bound="MentionClassificationType0FeedbackType0")


@_attrs_define
class MentionClassificationType0FeedbackType0:
    """A person's correction of the verdict, or null. A relevance verdict sets `relevance` to 100 or 0 and `relevant` with
    it; a corrected sentiment replaces `sentiment`. Every list, filter, digest and report reads the corrected values.

        Attributes:
            relevant (bool | None): Your verdict on relevance, or null when you only corrected the sentiment.
            sentiment (MentionClassificationType0FeedbackType0Sentiment): Your corrected sentiment, or null when you only
                judged relevance.
            at (str): When the last verdict was given.
            original (MentionClassificationType0FeedbackType0Original): The classifier values your feedback replaced.
    """

    relevant: bool | None
    sentiment: MentionClassificationType0FeedbackType0Sentiment
    at: str
    original: MentionClassificationType0FeedbackType0Original
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relevant: bool | None
        relevant = self.relevant

        sentiment = self.sentiment.value

        at = self.at

        original = self.original.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relevant": relevant,
                "sentiment": sentiment,
                "at": at,
                "original": original,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mention_classification_type_0_feedback_type_0_original import (
            MentionClassificationType0FeedbackType0Original,
        )

        d = dict(src_dict)

        def _parse_relevant(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        relevant = _parse_relevant(d.pop("relevant"))

        sentiment = MentionClassificationType0FeedbackType0Sentiment(d.pop("sentiment"))

        at = d.pop("at")

        original = MentionClassificationType0FeedbackType0Original.from_dict(
            d.pop("original")
        )

        mention_classification_type_0_feedback_type_0 = cls(
            relevant=relevant,
            sentiment=sentiment,
            at=at,
            original=original,
        )

        mention_classification_type_0_feedback_type_0.additional_properties = d
        return mention_classification_type_0_feedback_type_0

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
