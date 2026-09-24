from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTopUpBody")


@_attrs_define
class CreateTopUpBody:
    """
    Attributes:
        amount_cents (int): Amount to add, in USD cents (2000 to 500000). Prefilled at checkout, editable there.
        success_url (str | Unset): Where the customer lands after paying: a page on an origin this deployment trusts
            (the dashboard). Omit it and the dashboard's billing page is used.
    """

    amount_cents: int
    success_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_cents = self.amount_cents

        success_url = self.success_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountCents": amount_cents,
            }
        )
        if success_url is not UNSET:
            field_dict["successUrl"] = success_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount_cents = d.pop("amountCents")

        success_url = d.pop("successUrl", UNSET)

        create_top_up_body = cls(
            amount_cents=amount_cents,
            success_url=success_url,
        )

        create_top_up_body.additional_properties = d
        return create_top_up_body

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
