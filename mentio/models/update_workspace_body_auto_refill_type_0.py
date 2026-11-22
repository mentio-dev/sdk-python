from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateWorkspaceBodyAutoRefillType0")


@_attrs_define
class UpdateWorkspaceBodyAutoRefillType0:
    """The automatic refill; null turns it off.

    Attributes:
        threshold_cents (int): Refill when the child's effective balance (balance minus usage not settled yet) drops
            under this, in USD cents.
        amount_cents (int): How much each refill moves from the parent, in USD cents (100 to 500000).
    """

    threshold_cents: int
    amount_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        threshold_cents = self.threshold_cents

        amount_cents = self.amount_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thresholdCents": threshold_cents,
                "amountCents": amount_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        threshold_cents = d.pop("thresholdCents")

        amount_cents = d.pop("amountCents")

        update_workspace_body_auto_refill_type_0 = cls(
            threshold_cents=threshold_cents,
            amount_cents=amount_cents,
        )

        update_workspace_body_auto_refill_type_0.additional_properties = d
        return update_workspace_body_auto_refill_type_0

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
