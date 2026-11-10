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
        unclassified_mentions (int): Matches in the window that are never charged: not scored yet, classification
            failed, or a free review from a new app's look-back. Every other match is charged, on the mentions or comments
            line.
        mention_cents (int): The billed mentions at $0.008 each, rounded once on the total.
        billable_comments (int): Comments billed in the window (the comments line): comments delivered under your
            mentions and comments that matched a keyword, each once per workspace.
        comment_cents (int): The billed comments at $0.008 each, rounded once on the total.
        total_cents (int): keywordCents, mentionCents and commentCents, plus searchCents when the report is not
            filtered: then the window's whole list price. The rows carry keyword spend only.
        ledger_debit_cents (int): What the ledger has debited for the window's days, by the day each debit settled, for
            the whole workspace whatever the filters, on-demand searches included. Lags totalCents by unsettled mentions;
            see [The ledger](/billing#the-ledger).
        search_results (int): On-demand search results billed in the window (scored then), for the whole workspace
            whatever the filters.
        search_cents (int): searchResults at $0.008 each, in totals.totalCents when the report is not filtered (never in
            a row: rows are keyword spend).
        unattributed_billable (int): Billed mentions whose match row is gone (deleted keyword), so no platform or
            keyword row claims them; charged all the same. Comments never are (by=group puts a deleted keyword's comments on
            the no-group row).
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
    search_results: int
    search_cents: int
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

        search_results = self.search_results

        search_cents = self.search_cents

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
                "searchResults": search_results,
                "searchCents": search_cents,
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

        search_results = d.pop("searchResults")

        search_cents = d.pop("searchCents")

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
            search_results=search_results,
            search_cents=search_cents,
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
