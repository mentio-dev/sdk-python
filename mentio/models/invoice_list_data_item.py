from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InvoiceListDataItem")


@_attrs_define
class InvoiceListDataItem:
    """
    Attributes:
        id (str): The Polar order id; what GET /v1/billing/invoices/{id}/url takes.
        created_at (str): When the order was placed (ISO 8601).
        status (str): The order status as Polar reports it (paid, refunded, ...).
        paid (bool): Whether the order was paid.
        total_amount (int): What was charged, in minor units of `currency`, tax included.
        currency (str): ISO 4217 currency of the order (usd).
        billing_reason (None | str): Why the order exists, as Polar reports it (purchase, subscription_cycle, ...); null
            when it does not say.
    """

    id: str
    created_at: str
    status: str
    paid: bool
    total_amount: int
    currency: str
    billing_reason: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        status = self.status

        paid = self.paid

        total_amount = self.total_amount

        currency = self.currency

        billing_reason: None | str
        billing_reason = self.billing_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "status": status,
                "paid": paid,
                "totalAmount": total_amount,
                "currency": currency,
                "billingReason": billing_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("createdAt")

        status = d.pop("status")

        paid = d.pop("paid")

        total_amount = d.pop("totalAmount")

        currency = d.pop("currency")

        def _parse_billing_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billing_reason = _parse_billing_reason(d.pop("billingReason"))

        invoice_list_data_item = cls(
            id=id,
            created_at=created_at,
            status=status,
            paid=paid,
            total_amount=total_amount,
            currency=currency,
            billing_reason=billing_reason,
        )

        invoice_list_data_item.additional_properties = d
        return invoice_list_data_item

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
