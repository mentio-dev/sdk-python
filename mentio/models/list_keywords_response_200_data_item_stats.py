from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_keywords_response_200_data_item_stats_feedback import (
        ListKeywordsResponse200DataItemStatsFeedback,
    )
    from ..models.list_keywords_response_200_data_item_stats_noise import (
        ListKeywordsResponse200DataItemStatsNoise,
    )


T = TypeVar("T", bound="ListKeywordsResponse200DataItemStats")


@_attrs_define
class ListKeywordsResponse200DataItemStats:
    """Computed over this workspace's matches.

    Attributes:
        mentions (int): Every match ever, relevant or not: the number billing counts.
        relevant (int): Matches scored at or above the relevance threshold.
        last7d (int): Matches published in the last 7 days.
        this_month (int): Matches recorded this calendar month (UTC), the count a cap compares against.
        last_mention_at (None | str): Newest matched post; null until the first one.
        feedback (ListKeywordsResponse200DataItemStatsFeedback): Your verdicts on this keyword's mentions (PATCH
            /v1/mentions/{id} relevant).
        noise (ListKeywordsResponse200DataItemStatsNoise): Relevance over the last 14 days of scored matches, so a
            keyword tightened today stops being flagged within two weeks.
    """

    mentions: int
    relevant: int
    last7d: int
    this_month: int
    last_mention_at: None | str
    feedback: ListKeywordsResponse200DataItemStatsFeedback
    noise: ListKeywordsResponse200DataItemStatsNoise
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mentions = self.mentions

        relevant = self.relevant

        last7d = self.last7d

        this_month = self.this_month

        last_mention_at: None | str
        last_mention_at = self.last_mention_at

        feedback = self.feedback.to_dict()

        noise = self.noise.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mentions": mentions,
                "relevant": relevant,
                "last7d": last7d,
                "thisMonth": this_month,
                "lastMentionAt": last_mention_at,
                "feedback": feedback,
                "noise": noise,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_keywords_response_200_data_item_stats_feedback import (
            ListKeywordsResponse200DataItemStatsFeedback,
        )
        from ..models.list_keywords_response_200_data_item_stats_noise import (
            ListKeywordsResponse200DataItemStatsNoise,
        )

        d = dict(src_dict)
        mentions = d.pop("mentions")

        relevant = d.pop("relevant")

        last7d = d.pop("last7d")

        this_month = d.pop("thisMonth")

        def _parse_last_mention_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_mention_at = _parse_last_mention_at(d.pop("lastMentionAt"))

        feedback = ListKeywordsResponse200DataItemStatsFeedback.from_dict(
            d.pop("feedback")
        )

        noise = ListKeywordsResponse200DataItemStatsNoise.from_dict(d.pop("noise"))

        list_keywords_response_200_data_item_stats = cls(
            mentions=mentions,
            relevant=relevant,
            last7d=last7d,
            this_month=this_month,
            last_mention_at=last_mention_at,
            feedback=feedback,
            noise=noise,
        )

        list_keywords_response_200_data_item_stats.additional_properties = d
        return list_keywords_response_200_data_item_stats

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
