from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_batch_result_data_item_keyword_type_0_stats_health import (
    KeywordBatchResultDataItemKeywordType0StatsHealth,
)

if TYPE_CHECKING:
    from ..models.keyword_batch_result_data_item_keyword_type_0_stats_cost import (
        KeywordBatchResultDataItemKeywordType0StatsCost,
    )
    from ..models.keyword_batch_result_data_item_keyword_type_0_stats_feedback import (
        KeywordBatchResultDataItemKeywordType0StatsFeedback,
    )
    from ..models.keyword_batch_result_data_item_keyword_type_0_stats_noise import (
        KeywordBatchResultDataItemKeywordType0StatsNoise,
    )


T = TypeVar("T", bound="KeywordBatchResultDataItemKeywordType0Stats")


@_attrs_define
class KeywordBatchResultDataItemKeywordType0Stats:
    """Computed over this workspace's matches.

    Attributes:
        mentions (int): Every match ever, relevant or not: the number billing counts.
        relevant (int): Matches scored at or above the relevance threshold.
        last7d (int): Matches published in the last 7 days.
        this_month (int): Matches recorded this calendar month (UTC), plus the thread comments delivered under this
            keyword's mentions: the count a cap compares against.
        last_mention_at (None | str): Newest matched post; null until the first one.
        feedback (KeywordBatchResultDataItemKeywordType0StatsFeedback): Your verdicts on this keyword's mentions (PATCH
            /v1/mentions/{id} relevant).
        noise (KeywordBatchResultDataItemKeywordType0StatsNoise): Relevance over the last 14 days of scored matches, so
            a keyword tightened today stops being flagged within two weeks.
        health (KeywordBatchResultDataItemKeywordType0StatsHealth): The first status that applies over the last 14 days;
            see [Keyword health](/guides/keyword-health).

            - paused: muted.
            - capped: at its mention cap.
            - noisy: 20 or more scored matches, under 30% relevant.
            - new: under 7 days old, or changed lately with few scored matches.
            - quiet: 7 days or older, nothing relevant.
            - healthy: none of the above.
        cost (KeywordBatchResultDataItemKeywordType0StatsCost): What this keyword has cost this calendar month (UTC) at
            list price: its row in GET /v1/usage/breakdown?month=<this month>. The ledger differs only by cumulative
            rounding.
    """

    mentions: int
    relevant: int
    last7d: int
    this_month: int
    last_mention_at: None | str
    feedback: KeywordBatchResultDataItemKeywordType0StatsFeedback
    noise: KeywordBatchResultDataItemKeywordType0StatsNoise
    health: KeywordBatchResultDataItemKeywordType0StatsHealth
    cost: KeywordBatchResultDataItemKeywordType0StatsCost
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

        health = self.health.value

        cost = self.cost.to_dict()

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
                "health": health,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_batch_result_data_item_keyword_type_0_stats_cost import (
            KeywordBatchResultDataItemKeywordType0StatsCost,
        )
        from ..models.keyword_batch_result_data_item_keyword_type_0_stats_feedback import (
            KeywordBatchResultDataItemKeywordType0StatsFeedback,
        )
        from ..models.keyword_batch_result_data_item_keyword_type_0_stats_noise import (
            KeywordBatchResultDataItemKeywordType0StatsNoise,
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

        feedback = KeywordBatchResultDataItemKeywordType0StatsFeedback.from_dict(
            d.pop("feedback")
        )

        noise = KeywordBatchResultDataItemKeywordType0StatsNoise.from_dict(
            d.pop("noise")
        )

        health = KeywordBatchResultDataItemKeywordType0StatsHealth(d.pop("health"))

        cost = KeywordBatchResultDataItemKeywordType0StatsCost.from_dict(d.pop("cost"))

        keyword_batch_result_data_item_keyword_type_0_stats = cls(
            mentions=mentions,
            relevant=relevant,
            last7d=last7d,
            this_month=this_month,
            last_mention_at=last_mention_at,
            feedback=feedback,
            noise=noise,
            health=health,
            cost=cost,
        )

        keyword_batch_result_data_item_keyword_type_0_stats.additional_properties = d
        return keyword_batch_result_data_item_keyword_type_0_stats

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
