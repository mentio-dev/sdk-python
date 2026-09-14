from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_classification_type_0_sentiment import (
    MentionClassificationType0Sentiment,
)

T = TypeVar("T", bound="MentionClassificationType0")


@_attrs_define
class MentionClassificationType0:
    """The classifier verdict; null while the post is still queued for classification.

    Attributes:
        relevance (int | None): 0 to 100; null only when classification failed.
        sentiment (MentionClassificationType0Sentiment): Classifier sentiment.
        intents (list[str]): Detected intents: buy_intent, question, complaint, praise, comparison.
        note (None | str): One sentence from the classifier explaining the score.
        failed (bool): true when the model could not score this post; it stays in the feed and is not billed.
    """

    relevance: int | None
    sentiment: MentionClassificationType0Sentiment
    intents: list[str]
    note: None | str
    failed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relevance: int | None
        relevance = self.relevance

        sentiment = self.sentiment.value

        intents = self.intents

        note: None | str
        note = self.note

        failed = self.failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relevance": relevance,
                "sentiment": sentiment,
                "intents": intents,
                "note": note,
                "failed": failed,
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

        sentiment = MentionClassificationType0Sentiment(d.pop("sentiment"))

        intents = cast(list[str], d.pop("intents"))

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        failed = d.pop("failed")

        mention_classification_type_0 = cls(
            relevance=relevance,
            sentiment=sentiment,
            intents=intents,
            note=note,
            failed=failed,
        )

        mention_classification_type_0.additional_properties = d
        return mention_classification_type_0

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
