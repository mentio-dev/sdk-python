from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageBreakdownTotals")


@_attrs_define
class UsageBreakdownTotals:
    """The whole window as one line, the same for every dimension.

    Attributes:
        keyword_days (int): Keyword-days metered in the window.
        keyword_cents (int): The keyword-days at the keyword rate ($5 a month, 500/30 cents a day), rounded once on the
            total.
        matched_mentions (int): Matches recorded in the window, relevant or not.
        billable_mentions (int): Of the matches billed in the window (every scored match, relevant or not), the ones in
            this group.
        unclassified_mentions (int): Matches recorded in the window that are never charged: no score yet (still being
            scored, or classification failed), or a free review from the look-back of a newly connected app. Every other
            match is charged, on the mentions line or, for a comment, on the comments line.
        mention_cents (int): The billed mentions at $0.008 each, rounded once on the total.
        billable_comments (int): Comments billed in the window (the comments line): comments delivered under your
            mentions and comments that matched a keyword, each once per workspace.
        comment_cents (int): The billed comments at $0.008 each, rounded once on the total.
        total_cents (int): keywordCents plus mentionCents plus commentCents.
        ledger_debit_cents (int): What the ledger has debited so far for the days of the window, each debit by the day
            it settled. Mentions settle the morning after their day, so a window ending today lags totalCents by today's
            mentions (and yesterday's before the tick at 00:05 UTC); a closed month differs from totalCents only by
            cumulative rounding.
        unattributed_billable (int): Billed mentions whose match row is gone (deleted keyword), so no platform or
            keyword row can claim them. Charged all the same. Comments carry their keyword and platform on the billed row,
            so they are never unattributed (by=group puts a deleted keyword's comments on the no-group row).
    """

    keyword_days: int
    keyword_cents: int
    matched_mentions: int
    billable_mentions: int
    unclassified_mentions: int
    mention_cents: int
    billable_comments: int
    comment_cents: int
    total_cents: int
    ledger_debit_cents: int
    unattributed_billable: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword_days = self.keyword_days

        keyword_cents = self.keyword_cents

        matched_mentions = self.matched_mentions

        billable_mentions = self.billable_mentions

        unclassified_mentions = self.unclassified_mentions

        mention_cents = self.mention_cents

        billable_comments = self.billable_comments

        comment_cents = self.comment_cents

        total_cents = self.total_cents

        ledger_debit_cents = self.ledger_debit_cents

        unattributed_billable = self.unattributed_billable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keywordDays": keyword_days,
                "keywordCents": keyword_cents,
                "matchedMentions": matched_mentions,
                "billableMentions": billable_mentions,
                "unclassifiedMentions": unclassified_mentions,
                "mentionCents": mention_cents,
                "billableComments": billable_comments,
                "commentCents": comment_cents,
                "totalCents": total_cents,
                "ledgerDebitCents": ledger_debit_cents,
                "unattributedBillable": unattributed_billable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keyword_days = d.pop("keywordDays")

        keyword_cents = d.pop("keywordCents")

        matched_mentions = d.pop("matchedMentions")

        billable_mentions = d.pop("billableMentions")

        unclassified_mentions = d.pop("unclassifiedMentions")

        mention_cents = d.pop("mentionCents")

        billable_comments = d.pop("billableComments")

        comment_cents = d.pop("commentCents")

        total_cents = d.pop("totalCents")

        ledger_debit_cents = d.pop("ledgerDebitCents")

        unattributed_billable = d.pop("unattributedBillable")

        usage_breakdown_totals = cls(
            keyword_days=keyword_days,
            keyword_cents=keyword_cents,
            matched_mentions=matched_mentions,
            billable_mentions=billable_mentions,
            unclassified_mentions=unclassified_mentions,
            mention_cents=mention_cents,
            billable_comments=billable_comments,
            comment_cents=comment_cents,
            total_cents=total_cents,
            ledger_debit_cents=ledger_debit_cents,
            unattributed_billable=unattributed_billable,
        )

        usage_breakdown_totals.additional_properties = d
        return usage_breakdown_totals

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
