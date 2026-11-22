from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_workspaces_response_200_data_item_funding_auto_refill_type_0 import (
        ListWorkspacesResponse200DataItemFundingAutoRefillType0,
    )


T = TypeVar("T", bound="ListWorkspacesResponse200DataItemFunding")


@_attrs_define
class ListWorkspacesResponse200DataItemFunding:
    """How the parent funds this workspace.

    Attributes:
        monthly_limit_cents (int | None): The most the parent moves into this workspace in a UTC calendar month, manual
            and automatic transfers alike; null = no limit.
        transferred_this_month_cents (int): Moved in from the parent this UTC month, what the monthly limit counts.
        auto_refill (ListWorkspacesResponse200DataItemFundingAutoRefillType0 | None): The automatic refill; null when
            off.
        last_refill_at (None | str): When the last automatic refill moved money; null when none ever did.
        last_refill_error (None | str): Why the last automatic refill attempt moved nothing (the parent could not cover
            it, the monthly limit), cleared by the next one that works; null when fine.
    """

    monthly_limit_cents: int | None
    transferred_this_month_cents: int
    auto_refill: ListWorkspacesResponse200DataItemFundingAutoRefillType0 | None
    last_refill_at: None | str
    last_refill_error: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_workspaces_response_200_data_item_funding_auto_refill_type_0 import (
            ListWorkspacesResponse200DataItemFundingAutoRefillType0,
        )

        monthly_limit_cents: int | None
        monthly_limit_cents = self.monthly_limit_cents

        transferred_this_month_cents = self.transferred_this_month_cents

        auto_refill: dict[str, Any] | None
        if isinstance(
            self.auto_refill, ListWorkspacesResponse200DataItemFundingAutoRefillType0
        ):
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
        from ..models.list_workspaces_response_200_data_item_funding_auto_refill_type_0 import (
            ListWorkspacesResponse200DataItemFundingAutoRefillType0,
        )

        d = dict(src_dict)

        def _parse_monthly_limit_cents(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        monthly_limit_cents = _parse_monthly_limit_cents(d.pop("monthlyLimitCents"))

        transferred_this_month_cents = d.pop("transferredThisMonthCents")

        def _parse_auto_refill(
            data: object,
        ) -> ListWorkspacesResponse200DataItemFundingAutoRefillType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auto_refill_type_0 = (
                    ListWorkspacesResponse200DataItemFundingAutoRefillType0.from_dict(
                        data
                    )
                )

                return auto_refill_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListWorkspacesResponse200DataItemFundingAutoRefillType0 | None, data
            )

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

        list_workspaces_response_200_data_item_funding = cls(
            monthly_limit_cents=monthly_limit_cents,
            transferred_this_month_cents=transferred_this_month_cents,
            auto_refill=auto_refill,
            last_refill_at=last_refill_at,
            last_refill_error=last_refill_error,
        )

        list_workspaces_response_200_data_item_funding.additional_properties = d
        return list_workspaces_response_200_data_item_funding

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
