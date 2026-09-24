from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordStatsCost")


@_attrs_define
class KeywordStatsCost:
    """What this keyword has cost this calendar month (UTC) at list price: exactly its row in GET
    /v1/usage/breakdown?month=<this month> (same tables, same rounding). The wallet's ledger, which settles once a day,
    is what can differ from these list-price numbers, and only by cumulative rounding.

        Attributes:
            keyword_days (int): Days this month the keyword was charged for: unmuted at the daily tick. A keyword created
                today reads 0 until tomorrow's tick.
            keyword_cents (int): Those days at the keyword rate ($5 a month, 500/30 cents a day), rounded once on the total.
            billable_mentions (int): Matches billed this month, counted when they were scored (the clock the ledger settles
                by), so it can trail thisMonth by the matches still being scored and never counts one that failed to score.
            mention_cents (int): Those matches at $0.008 each, rounded once on the total.
            total_cents (int): keywordCents plus mentionCents: what this keyword has cost this month, in USD cents.
    """

    keyword_days: int
    keyword_cents: int
    billable_mentions: int
    mention_cents: int
    total_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword_days = self.keyword_days

        keyword_cents = self.keyword_cents

        billable_mentions = self.billable_mentions

        mention_cents = self.mention_cents

        total_cents = self.total_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keywordDays": keyword_days,
                "keywordCents": keyword_cents,
                "billableMentions": billable_mentions,
                "mentionCents": mention_cents,
                "totalCents": total_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keyword_days = d.pop("keywordDays")

        keyword_cents = d.pop("keywordCents")

        billable_mentions = d.pop("billableMentions")

        mention_cents = d.pop("mentionCents")

        total_cents = d.pop("totalCents")

        keyword_stats_cost = cls(
            keyword_days=keyword_days,
            keyword_cents=keyword_cents,
            billable_mentions=billable_mentions,
            mention_cents=mention_cents,
            total_cents=total_cents,
        )

        keyword_stats_cost.additional_properties = d
        return keyword_stats_cost

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
