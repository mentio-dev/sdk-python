from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.analytics_summary_previous_type_0_reach import (
        AnalyticsSummaryPreviousType0Reach,
    )
    from ..models.analytics_summary_previous_type_0_sentiment import (
        AnalyticsSummaryPreviousType0Sentiment,
    )
    from ..models.analytics_summary_previous_type_0_triage import (
        AnalyticsSummaryPreviousType0Triage,
    )


T = TypeVar("T", bound="AnalyticsSummaryPreviousType0")


@_attrs_define
class AnalyticsSummaryPreviousType0:
    """The same counts over the period of the same length right before the window; null unless compare=true.

    Attributes:
        matched (int): Every match in the window, relevant or not: the number usage counts.
        relevant (int): Matches scored at or above the relevance threshold.
        posts (int): Distinct posts behind the matches: a post matching two keywords is two matches, one post.
        people (int): Distinct authors behind the matches.
        sentiment (AnalyticsSummaryPreviousType0Sentiment): Matched mentions by classifier sentiment.
        buy_intent (int): Matches carrying the buy_intent intent.
        questions (int): Matches carrying the question intent.
        reach (AnalyticsSummaryPreviousType0Reach): Estimated reach.
        triage (AnalyticsSummaryPreviousType0Triage): Where the matches stand in your inbox.
    """

    matched: int
    relevant: int
    posts: int
    people: int
    sentiment: AnalyticsSummaryPreviousType0Sentiment
    buy_intent: int
    questions: int
    reach: AnalyticsSummaryPreviousType0Reach
    triage: AnalyticsSummaryPreviousType0Triage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matched = self.matched

        relevant = self.relevant

        posts = self.posts

        people = self.people

        sentiment = self.sentiment.to_dict()

        buy_intent = self.buy_intent

        questions = self.questions

        reach = self.reach.to_dict()

        triage = self.triage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matched": matched,
                "relevant": relevant,
                "posts": posts,
                "people": people,
                "sentiment": sentiment,
                "buyIntent": buy_intent,
                "questions": questions,
                "reach": reach,
                "triage": triage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analytics_summary_previous_type_0_reach import (
            AnalyticsSummaryPreviousType0Reach,
        )
        from ..models.analytics_summary_previous_type_0_sentiment import (
            AnalyticsSummaryPreviousType0Sentiment,
        )
        from ..models.analytics_summary_previous_type_0_triage import (
            AnalyticsSummaryPreviousType0Triage,
        )

        d = dict(src_dict)
        matched = d.pop("matched")

        relevant = d.pop("relevant")

        posts = d.pop("posts")

        people = d.pop("people")

        sentiment = AnalyticsSummaryPreviousType0Sentiment.from_dict(d.pop("sentiment"))

        buy_intent = d.pop("buyIntent")

        questions = d.pop("questions")

        reach = AnalyticsSummaryPreviousType0Reach.from_dict(d.pop("reach"))

        triage = AnalyticsSummaryPreviousType0Triage.from_dict(d.pop("triage"))

        analytics_summary_previous_type_0 = cls(
            matched=matched,
            relevant=relevant,
            posts=posts,
            people=people,
            sentiment=sentiment,
            buy_intent=buy_intent,
            questions=questions,
            reach=reach,
            triage=triage,
        )

        analytics_summary_previous_type_0.additional_properties = d
        return analytics_summary_previous_type_0

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
