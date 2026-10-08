from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_stats_health import KeywordStatsHealth

if TYPE_CHECKING:
    from ..models.keyword_stats_cost import KeywordStatsCost
    from ..models.keyword_stats_feedback import KeywordStatsFeedback
    from ..models.keyword_stats_noise import KeywordStatsNoise


T = TypeVar("T", bound="KeywordStats")


@_attrs_define
class KeywordStats:
    """Computed over this workspace's matches.

    Attributes:
        mentions (int): Every match ever, relevant or not: the number billing counts.
        relevant (int): Matches scored at or above the relevance threshold.
        last7d (int): Matches published in the last 7 days.
        this_month (int): Matches recorded this calendar month (UTC), plus the thread comments delivered under this
            keyword's mentions: the count a cap compares against.
        last_mention_at (None | str): Newest matched post; null until the first one.
        feedback (KeywordStatsFeedback): Your verdicts on this keyword's mentions (PATCH /v1/mentions/{id} relevant).
        noise (KeywordStatsNoise): Relevance over the last 14 days of scored matches, so a keyword tightened today stops
            being flagged within two weeks.
        health (KeywordStatsHealth): The keyword's health over the same 14 days as `noise`, by the rule GET
            /v1/keywords/{id}/health applies to its own window: paused (muted), capped (at its mention cap), noisy (20 or
            more scored matches, under 30% relevant), new (under 7 days old and not noisy, or changed in the last 7 days
            with under 20 scored matches since), quiet (7 days or older, nothing relevant), else healthy. Judged on the
            matches since the keyword's last change to its matching rules, platforms or context (or its unmute) when that is
            inside the 14 days, so a keyword tightened today is not flagged on the noise the change removed; `noise` itself
            keeps the whole 14 days. Always 14 days, while the endpoint reads 30 by default, so the two can differ for the
            same keyword. The health endpoint says why and what to change.
        cost (KeywordStatsCost): What this keyword has cost this calendar month (UTC) at list price: exactly its row in
            GET /v1/usage/breakdown?month=<this month> (same tables, same rounding). The wallet's ledger, which settles once
            a day, is what can differ from these list-price numbers, and only by cumulative rounding.
    """

    mentions: int
    relevant: int
    last7d: int
    this_month: int
    last_mention_at: None | str
    feedback: KeywordStatsFeedback
    noise: KeywordStatsNoise
    health: KeywordStatsHealth
    cost: KeywordStatsCost
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
        from ..models.keyword_stats_cost import KeywordStatsCost
        from ..models.keyword_stats_feedback import (
            KeywordStatsFeedback,
        )
        from ..models.keyword_stats_noise import KeywordStatsNoise

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

        feedback = KeywordStatsFeedback.from_dict(d.pop("feedback"))

        noise = KeywordStatsNoise.from_dict(d.pop("noise"))

        health = KeywordStatsHealth(d.pop("health"))

        cost = KeywordStatsCost.from_dict(d.pop("cost"))

        keyword_stats = cls(
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

        keyword_stats.additional_properties = d
        return keyword_stats

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
