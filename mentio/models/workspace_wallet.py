from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkspaceWallet")


@_attrs_define
class WorkspaceWallet:
    """The child's own wallet. A child spends only what it holds; nothing is pooled with the parent.

    Attributes:
        balance_cents (int): The workspace's own balance: every credit and transfer in, minus every debit and transfer
            out.
        effective_cents (int): The balance minus usage not settled yet: what a transfer back to the parent may take, and
            what the stop rules read.
        active_keywords (int): Keywords running (each costs a keyword-day a day).
        paused_keywords (int): Keywords the wallet paused for lack of balance; they resume once a day of every keyword
            is covered.
    """

    balance_cents: int
    effective_cents: int
    active_keywords: int
    paused_keywords: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance_cents = self.balance_cents

        effective_cents = self.effective_cents

        active_keywords = self.active_keywords

        paused_keywords = self.paused_keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balanceCents": balance_cents,
                "effectiveCents": effective_cents,
                "activeKeywords": active_keywords,
                "pausedKeywords": paused_keywords,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        balance_cents = d.pop("balanceCents")

        effective_cents = d.pop("effectiveCents")

        active_keywords = d.pop("activeKeywords")

        paused_keywords = d.pop("pausedKeywords")

        workspace_wallet = cls(
            balance_cents=balance_cents,
            effective_cents=effective_cents,
            active_keywords=active_keywords,
            paused_keywords=paused_keywords,
        )

        workspace_wallet.additional_properties = d
        return workspace_wallet

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
