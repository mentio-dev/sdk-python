from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_classification_type_0_sentiment import (
    MentionClassificationType0Sentiment,
)

if TYPE_CHECKING:
    from ..models.mention_classification_type_0_feedback_type_0 import (
        MentionClassificationType0FeedbackType0,
    )


T = TypeVar("T", bound="MentionClassificationType0")


@_attrs_define
class MentionClassificationType0:
    """The classifier verdict, as corrected by your feedback; null while the post is still queued for classification.

    Attributes:
        relevance (int | None): 0 to 100; null only when classification failed.
        sentiment (MentionClassificationType0Sentiment): Classifier sentiment.
        intents (list[str]): Intent and topic tags: buy_intent, question, complaint, praise, comparison, churn_intent
            (leaving or replacing the keyword), bug_report, pricing, hiring, event, promotional.
        automated (bool): The post reads as machine-made: a bot or app account, a scheduled or templated post, an
            obvious AI-written summary. A label only: automated mentions stay in the feed, are delivered as usual and are
            billed like any other match. false while unjudged.
        language (None | str): The language the post is written in, as an ISO 639-1 code (en, es, de); null when unknown
            or classified before languages were recorded.
        confidence (float | None): How sure the classifier is of its relevance verdict, 0 to 1. null when the verdict
            came without one: the fallback model judged, or the row was scored before confidence was recorded.
        uncertain (bool): The verdict deserves a human look: confidence under 0.4, or the model that wrote the note
            disagreed with the verdict. A flag for reviewers; it never hides a mention.
        note (None | str): One sentence from the classifier explaining the score.
        failed (bool): true when the model could not score this post; it stays in the feed and is not billed.
        feedback (MentionClassificationType0FeedbackType0 | None): A person's correction of the verdict, or null. A
            relevance verdict sets `relevance` to 100 or 0 and `relevant` with it; a corrected sentiment replaces
            `sentiment`. Every list, filter, digest and report reads the corrected values.
    """

    relevance: int | None
    sentiment: MentionClassificationType0Sentiment
    intents: list[str]
    automated: bool
    language: None | str
    confidence: float | None
    uncertain: bool
    note: None | str
    failed: bool
    feedback: MentionClassificationType0FeedbackType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mention_classification_type_0_feedback_type_0 import (
            MentionClassificationType0FeedbackType0,
        )

        relevance: int | None
        relevance = self.relevance

        sentiment = self.sentiment.value

        intents = self.intents

        automated = self.automated

        language: None | str
        language = self.language

        confidence: float | None
        confidence = self.confidence

        uncertain = self.uncertain

        note: None | str
        note = self.note

        failed = self.failed

        feedback: dict[str, Any] | None
        if isinstance(self.feedback, MentionClassificationType0FeedbackType0):
            feedback = self.feedback.to_dict()
        else:
            feedback = self.feedback

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
                "uncertain": uncertain,
                "note": note,
                "failed": failed,
                "feedback": feedback,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mention_classification_type_0_feedback_type_0 import (
            MentionClassificationType0FeedbackType0,
        )

        d = dict(src_dict)

        def _parse_relevance(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        relevance = _parse_relevance(d.pop("relevance"))

        sentiment = MentionClassificationType0Sentiment(d.pop("sentiment"))

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

        uncertain = d.pop("uncertain")

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        failed = d.pop("failed")

        def _parse_feedback(
            data: object,
        ) -> MentionClassificationType0FeedbackType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feedback_type_0 = MentionClassificationType0FeedbackType0.from_dict(
                    data
                )

                return feedback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionClassificationType0FeedbackType0 | None, data)

        feedback = _parse_feedback(d.pop("feedback"))

        mention_classification_type_0 = cls(
            relevance=relevance,
            sentiment=sentiment,
            intents=intents,
            automated=automated,
            language=language,
            confidence=confidence,
            uncertain=uncertain,
            note=note,
            failed=failed,
            feedback=feedback,
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
