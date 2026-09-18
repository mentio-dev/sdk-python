from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.usage_summary_balance import UsageSummaryBalance
    from ..models.usage_summary_burn import UsageSummaryBurn
    from ..models.usage_summary_keywords import UsageSummaryKeywords
    from ..models.usage_summary_mentions import UsageSummaryMentions


T = TypeVar("T", bound="UsageSummary")


@_attrs_define
class UsageSummary:
    """
    Attributes:
        balance (UsageSummaryBalance): The prepaid wallet.
        burn (UsageSummaryBurn): How fast the balance goes.
        keywords (UsageSummaryKeywords): Keywords against the wallet.
        mentions (UsageSummaryMentions): Matched mentions, the other thing that bills.
        stopped (bool): The wallet paused tracking; a top-up that covers a day of every keyword resumes it.
        low_balance (bool): Running, and the effective balance is at or under 20 percent of the last credit.
        last_top_up_at (None | str): Newest paid top-up; null before the first.
    """

    balance: UsageSummaryBalance
    burn: UsageSummaryBurn
    keywords: UsageSummaryKeywords
    mentions: UsageSummaryMentions
    stopped: bool
    low_balance: bool
    last_top_up_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance = self.balance.to_dict()

        burn = self.burn.to_dict()

        keywords = self.keywords.to_dict()

        mentions = self.mentions.to_dict()

        stopped = self.stopped

        low_balance = self.low_balance

        last_top_up_at: None | str
        last_top_up_at = self.last_top_up_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balance": balance,
                "burn": burn,
                "keywords": keywords,
                "mentions": mentions,
                "stopped": stopped,
                "lowBalance": low_balance,
                "lastTopUpAt": last_top_up_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_summary_balance import UsageSummaryBalance
        from ..models.usage_summary_burn import UsageSummaryBurn
        from ..models.usage_summary_keywords import (
            UsageSummaryKeywords,
        )
        from ..models.usage_summary_mentions import (
            UsageSummaryMentions,
        )

        d = dict(src_dict)
        balance = UsageSummaryBalance.from_dict(d.pop("balance"))

        burn = UsageSummaryBurn.from_dict(d.pop("burn"))

        keywords = UsageSummaryKeywords.from_dict(d.pop("keywords"))

        mentions = UsageSummaryMentions.from_dict(d.pop("mentions"))

        stopped = d.pop("stopped")

        low_balance = d.pop("lowBalance")

        def _parse_last_top_up_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_top_up_at = _parse_last_top_up_at(d.pop("lastTopUpAt"))

        usage_summary = cls(
            balance=balance,
            burn=burn,
            keywords=keywords,
            mentions=mentions,
            stopped=stopped,
            low_balance=low_balance,
            last_top_up_at=last_top_up_at,
        )

        usage_summary.additional_properties = d
        return usage_summary

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
