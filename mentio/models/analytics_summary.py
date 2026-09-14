from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.analytics_summary_previous_type_0 import AnalyticsSummaryPreviousType0
    from ..models.analytics_summary_reach import AnalyticsSummaryReach
    from ..models.analytics_summary_sentiment import AnalyticsSummarySentiment
    from ..models.analytics_summary_triage import AnalyticsSummaryTriage
    from ..models.analytics_summary_window import AnalyticsSummaryWindow


T = TypeVar("T", bound="AnalyticsSummary")


@_attrs_define
class AnalyticsSummary:
    """
    Attributes:
        window (AnalyticsSummaryWindow): The window the report covers.
        matched (int): Every match in the window, relevant or not: the number usage counts.
        relevant (int): Matches scored at or above the relevance threshold.
        posts (int): Distinct posts behind the matches: a post matching two keywords is two matches, one post.
        people (int): Distinct authors behind the matches.
        sentiment (AnalyticsSummarySentiment): Matched mentions by classifier sentiment.
        buy_intent (int): Matches carrying the buy_intent intent.
        questions (int): Matches carrying the question intent.
        reach (AnalyticsSummaryReach): Estimated reach.
        triage (AnalyticsSummaryTriage): Where the matches stand in your inbox.
        previous (AnalyticsSummaryPreviousType0 | None): The same counts over the period of the same length right before
            the window; null unless compare=true.
    """

    window: AnalyticsSummaryWindow
    matched: int
    relevant: int
    posts: int
    people: int
    sentiment: AnalyticsSummarySentiment
    buy_intent: int
    questions: int
    reach: AnalyticsSummaryReach
    triage: AnalyticsSummaryTriage
    previous: AnalyticsSummaryPreviousType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analytics_summary_previous_type_0 import (
            AnalyticsSummaryPreviousType0,
        )

        window = self.window.to_dict()

        matched = self.matched

        relevant = self.relevant

        posts = self.posts

        people = self.people

        sentiment = self.sentiment.to_dict()

        buy_intent = self.buy_intent

        questions = self.questions

        reach = self.reach.to_dict()

        triage = self.triage.to_dict()

        previous: dict[str, Any] | None
        if isinstance(self.previous, AnalyticsSummaryPreviousType0):
            previous = self.previous.to_dict()
        else:
            previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window": window,
                "matched": matched,
                "relevant": relevant,
                "posts": posts,
                "people": people,
                "sentiment": sentiment,
                "buyIntent": buy_intent,
                "questions": questions,
                "reach": reach,
                "triage": triage,
                "previous": previous,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analytics_summary_previous_type_0 import (
            AnalyticsSummaryPreviousType0,
        )
        from ..models.analytics_summary_reach import (
            AnalyticsSummaryReach,
        )
        from ..models.analytics_summary_sentiment import (
            AnalyticsSummarySentiment,
        )
        from ..models.analytics_summary_triage import (
            AnalyticsSummaryTriage,
        )
        from ..models.analytics_summary_window import (
            AnalyticsSummaryWindow,
        )

        d = dict(src_dict)
        window = AnalyticsSummaryWindow.from_dict(d.pop("window"))

        matched = d.pop("matched")

        relevant = d.pop("relevant")

        posts = d.pop("posts")

        people = d.pop("people")

        sentiment = AnalyticsSummarySentiment.from_dict(d.pop("sentiment"))

        buy_intent = d.pop("buyIntent")

        questions = d.pop("questions")

        reach = AnalyticsSummaryReach.from_dict(d.pop("reach"))

        triage = AnalyticsSummaryTriage.from_dict(d.pop("triage"))

        def _parse_previous(data: object) -> AnalyticsSummaryPreviousType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                previous_type_0 = AnalyticsSummaryPreviousType0.from_dict(data)

                return previous_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnalyticsSummaryPreviousType0 | None, data)

        previous = _parse_previous(d.pop("previous"))

        analytics_summary = cls(
            window=window,
            matched=matched,
            relevant=relevant,
            posts=posts,
            people=people,
            sentiment=sentiment,
            buy_intent=buy_intent,
            questions=questions,
            reach=reach,
            triage=triage,
            previous=previous,
        )

        analytics_summary.additional_properties = d
        return analytics_summary

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
