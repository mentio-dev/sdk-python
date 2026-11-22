from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageSummaryAccounts")


@_attrs_define
class UsageSummaryAccounts:
    """Tracked accounts (followers) against the wallet.

    Attributes:
        active (int): Tracked accounts running, the ones charged daily.
        paused (int): Tracked accounts the wallet paused for lack of balance; a top-up resumes them.
        capped (int): Running accounts at their monthly follower cap: still charged daily, no follower billed until the
            month turns or the cap is raised.
        day_cents (int): What the next day costs for the accounts that pay it: being read, or capped (one not read yet,
            or failing, pays nothing). keywords.dayCents plus this is a day.
    """

    active: int
    paused: int
    capped: int
    day_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        paused = self.paused

        capped = self.capped

        day_cents = self.day_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "paused": paused,
                "capped": capped,
                "dayCents": day_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        active = d.pop("active")

        paused = d.pop("paused")

        capped = d.pop("capped")

        day_cents = d.pop("dayCents")

        usage_summary_accounts = cls(
            active=active,
            paused=paused,
            capped=capped,
            day_cents=day_cents,
        )

        usage_summary_accounts.additional_properties = d
        return usage_summary_accounts

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
