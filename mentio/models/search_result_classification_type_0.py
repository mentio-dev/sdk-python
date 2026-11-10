from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_result_classification_type_0_sentiment import (
    SearchResultClassificationType0Sentiment,
)

T = TypeVar("T", bound="SearchResultClassificationType0")


@_attrs_define
class SearchResultClassificationType0:
    """The verdict, judged against your company profile; null while the result waits for the classifier.

    Attributes:
        relevance (int | None): 0 to 100; null only when classification failed.
        sentiment (SearchResultClassificationType0Sentiment): positive, neutral or negative; null when classification
            failed.
        intents (list[str]): Intent and topic tags:

            - buy_intent, question, complaint, praise, comparison, bug_report, pricing, hiring, event, promotional.
            - churn_intent: leaving or replacing the keyword.
            - testimonial: a customer vouching for it from their own use.
            - industry_insight: analysis or data about the field.
            - launch: a product or feature launch announcement.
            - feedback: a suggestion or request about it.
        automated (bool): The post reads as machine-made (a bot or app account, a scheduled or templated post, an AI-
            written summary). A label only: it stays in the feed, delivered and billed as usual. false while unjudged.
        language (None | str): The language the post is written in, as an ISO 639-1 code (en, es, de); null when
            unknown, not one of the 20 the classifier names, or classified before languages were recorded.
        confidence (float | None): How sure the classifier is of its relevance verdict, 0 to 1. null when the verdict
            came without one: the fallback model judged, or the row was scored before confidence was recorded.
        note (None | str): One sentence from the classifier explaining the score.
        failed (bool): true when the model could not score this post; it is not billed.
    """

    relevance: int | None
    sentiment: SearchResultClassificationType0Sentiment
    intents: list[str]
    automated: bool
    language: None | str
    confidence: float | None
    note: None | str
    failed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relevance: int | None
        relevance = self.relevance

        sentiment = self.sentiment.value

        intents = self.intents

        automated = self.automated

        language: None | str
        language = self.language

        confidence: float | None
        confidence = self.confidence

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
                "automated": automated,
                "language": language,
                "confidence": confidence,
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

        sentiment = SearchResultClassificationType0Sentiment(d.pop("sentiment"))

        intents = cast(list[str], d.pop("intents"))

        automated = d.pop("automated")

        def _parse_language(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        language = _parse_language(d.pop("language"))

        def _parse_confidence(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        confidence = _parse_confidence(d.pop("confidence"))

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        failed = d.pop("failed")

        search_result_classification_type_0 = cls(
            relevance=relevance,
            sentiment=sentiment,
            intents=intents,
            automated=automated,
            language=language,
            confidence=confidence,
            note=note,
            failed=failed,
        )

        search_result_classification_type_0.additional_properties = d
        return search_result_classification_type_0

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
