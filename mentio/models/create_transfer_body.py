from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_transfer_body_direction import CreateTransferBodyDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTransferBody")


@_attrs_define
class CreateTransferBody:
    """
    Attributes:
        amount_cents (int): How much to move, in USD cents (1 to 500000).
        direction (CreateTransferBodyDirection | Unset): to_workspace: from the parent into the child workspace.
            to_parent: from the child back to the parent. Default: CreateTransferBodyDirection.TO_WORKSPACE.
        note (str | Unset): Free text kept on both ledger rows, up to 200 characters.
    """

    amount_cents: int
    direction: CreateTransferBodyDirection | Unset = (
        CreateTransferBodyDirection.TO_WORKSPACE
    )
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_cents = self.amount_cents

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountCents": amount_cents,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount_cents = d.pop("amountCents")

        _direction = d.pop("direction", UNSET)
        direction: CreateTransferBodyDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = CreateTransferBodyDirection(_direction)

        note = d.pop("note", UNSET)

        create_transfer_body = cls(
            amount_cents=amount_cents,
            direction=direction,
            note=note,
        )

        create_transfer_body.additional_properties = d
        return create_transfer_body

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
