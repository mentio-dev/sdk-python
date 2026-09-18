from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.usage_summary_balance_currency import UsageSummaryBalanceCurrency

T = TypeVar("T", bound="UsageSummaryBalance")


@_attrs_define
class UsageSummaryBalance:
    """The prepaid wallet.

    Attributes:
        cents (int): Ledger balance: every credit minus every settled debit.
        pending_cents (int): Mentions matched since the last daily settlement, priced but not yet debited.
        effective_cents (int): cents minus pendingCents: what the stop rule and the keyword gate look at.
        currency (UsageSummaryBalanceCurrency):
    """

    cents: int
    pending_cents: int
    effective_cents: int
    currency: UsageSummaryBalanceCurrency
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cents = self.cents

        pending_cents = self.pending_cents

        effective_cents = self.effective_cents

        currency = self.currency.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cents": cents,
                "pendingCents": pending_cents,
                "effectiveCents": effective_cents,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cents = d.pop("cents")

        pending_cents = d.pop("pendingCents")

        effective_cents = d.pop("effectiveCents")

        currency = UsageSummaryBalanceCurrency(d.pop("currency"))

        usage_summary_balance = cls(
            cents=cents,
            pending_cents=pending_cents,
            effective_cents=effective_cents,
            currency=currency,
        )

        usage_summary_balance.additional_properties = d
        return usage_summary_balance

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
