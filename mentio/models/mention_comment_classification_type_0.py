from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_comment_classification_type_0_sentiment import (
    MentionCommentClassificationType0Sentiment,
)

T = TypeVar("T", bound="MentionCommentClassificationType0")


@_attrs_define
class MentionCommentClassificationType0:
    """A light read of the comment (sentiment and intent tags); null until it is scored, usually minutes after the thread
    arrives.

        Attributes:
            sentiment (MentionCommentClassificationType0Sentiment): Classifier sentiment.
            intents (list[str]): Intent and topic tags, the same vocabulary as a mention's.
    """

    sentiment: MentionCommentClassificationType0Sentiment
    intents: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sentiment = self.sentiment.value

        intents = self.intents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sentiment": sentiment,
                "intents": intents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sentiment = MentionCommentClassificationType0Sentiment(d.pop("sentiment"))

        intents = cast(list[str], d.pop("intents"))

        mention_comment_classification_type_0 = cls(
            sentiment=sentiment,
            intents=intents,
        )

        mention_comment_classification_type_0.additional_properties = d
        return mention_comment_classification_type_0

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
