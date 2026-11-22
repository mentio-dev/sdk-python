from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workspace_funding_auto_refill_type_0 import (
        WorkspaceFundingAutoRefillType0,
    )


T = TypeVar("T", bound="WorkspaceFunding")


@_attrs_define
class WorkspaceFunding:
    """How the parent funds this workspace.

    Attributes:
        monthly_limit_cents (int | None): The most the parent moves into this workspace in a UTC calendar month, manual
            and automatic transfers alike; null = no limit.
        transferred_this_month_cents (int): Moved in from the parent this UTC month, what the monthly limit counts.
        auto_refill (None | WorkspaceFundingAutoRefillType0): The automatic refill; null when off.
        last_refill_at (None | str): When the last automatic refill moved money; null when none ever did.
        last_refill_error (None | str): Why the last automatic refill attempt moved nothing (the parent could not cover
            it, the monthly limit), cleared by the next one that works; null when fine.
    """

    monthly_limit_cents: int | None
    transferred_this_month_cents: int
    auto_refill: None | WorkspaceFundingAutoRefillType0
    last_refill_at: None | str
    last_refill_error: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workspace_funding_auto_refill_type_0 import (
            WorkspaceFundingAutoRefillType0,
        )

        monthly_limit_cents: int | None
        monthly_limit_cents = self.monthly_limit_cents

        transferred_this_month_cents = self.transferred_this_month_cents

        auto_refill: dict[str, Any] | None
        if isinstance(self.auto_refill, WorkspaceFundingAutoRefillType0):
            auto_refill = self.auto_refill.to_dict()
        else:
            auto_refill = self.auto_refill

        last_refill_at: None | str
        last_refill_at = self.last_refill_at

        last_refill_error: None | str
        last_refill_error = self.last_refill_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monthlyLimitCents": monthly_limit_cents,
                "transferredThisMonthCents": transferred_this_month_cents,
                "autoRefill": auto_refill,
                "lastRefillAt": last_refill_at,
                "lastRefillError": last_refill_error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workspace_funding_auto_refill_type_0 import (
            WorkspaceFundingAutoRefillType0,
        )

        d = dict(src_dict)

        def _parse_monthly_limit_cents(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        monthly_limit_cents = _parse_monthly_limit_cents(d.pop("monthlyLimitCents"))

        transferred_this_month_cents = d.pop("transferredThisMonthCents")

        def _parse_auto_refill(data: object) -> None | WorkspaceFundingAutoRefillType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auto_refill_type_0 = WorkspaceFundingAutoRefillType0.from_dict(data)

                return auto_refill_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WorkspaceFundingAutoRefillType0, data)

        auto_refill = _parse_auto_refill(d.pop("autoRefill"))

        def _parse_last_refill_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_refill_at = _parse_last_refill_at(d.pop("lastRefillAt"))

        def _parse_last_refill_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_refill_error = _parse_last_refill_error(d.pop("lastRefillError"))

        workspace_funding = cls(
            monthly_limit_cents=monthly_limit_cents,
            transferred_this_month_cents=transferred_this_month_cents,
            auto_refill=auto_refill,
            last_refill_at=last_refill_at,
            last_refill_error=last_refill_error,
        )

        workspace_funding.additional_properties = d
        return workspace_funding

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
