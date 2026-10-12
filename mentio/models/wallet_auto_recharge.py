from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WalletAutoRecharge")


@_attrs_define
class WalletAutoRecharge:
    """
    Attributes:
        available (bool): This deployment can charge saved cards; false hides the setting.
        enabled (bool): Charge the saved card automatically when the balance runs low.
        threshold_cents (int): Charge when the effective balance drops under this.
        amount_cents (int): How much to add per automatic charge (same bounds as a manual top-up).
        weekly_limit_cents (int | None): Most the saved card may be charged automatically over any 7 days, before tax;
            null = no limit.
        spent_this_week_cents (int): What counts against the weekly limit over the last 7 days, before tax: automatic
            charges made plus any still settling.
        last_run_at (None | str): Newest successful automatic charge.
        last_error (None | str): Why the last automatic charge failed; null after a success.
    """

    available: bool
    enabled: bool
    threshold_cents: int
    amount_cents: int
    weekly_limit_cents: int | None
    spent_this_week_cents: int
    last_run_at: None | str
    last_error: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        enabled = self.enabled

        threshold_cents = self.threshold_cents

        amount_cents = self.amount_cents

        weekly_limit_cents: int | None
        weekly_limit_cents = self.weekly_limit_cents

        spent_this_week_cents = self.spent_this_week_cents

        last_run_at: None | str
        last_run_at = self.last_run_at

        last_error: None | str
        last_error = self.last_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available": available,
                "enabled": enabled,
                "thresholdCents": threshold_cents,
                "amountCents": amount_cents,
                "weeklyLimitCents": weekly_limit_cents,
                "spentThisWeekCents": spent_this_week_cents,
                "lastRunAt": last_run_at,
                "lastError": last_error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        available = d.pop("available")

        enabled = d.pop("enabled")

        threshold_cents = d.pop("thresholdCents")

        amount_cents = d.pop("amountCents")

        def _parse_weekly_limit_cents(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        weekly_limit_cents = _parse_weekly_limit_cents(d.pop("weeklyLimitCents"))

        spent_this_week_cents = d.pop("spentThisWeekCents")

        def _parse_last_run_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_run_at = _parse_last_run_at(d.pop("lastRunAt"))

        def _parse_last_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_error = _parse_last_error(d.pop("lastError"))

        wallet_auto_recharge = cls(
            available=available,
            enabled=enabled,
            threshold_cents=threshold_cents,
            amount_cents=amount_cents,
            weekly_limit_cents=weekly_limit_cents,
            spent_this_week_cents=spent_this_week_cents,
            last_run_at=last_run_at,
            last_error=last_error,
        )

        wallet_auto_recharge.additional_properties = d
        return wallet_auto_recharge

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
