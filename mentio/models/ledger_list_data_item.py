from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ledger_list_data_item_kind import LedgerListDataItemKind

T = TypeVar("T", bound="LedgerListDataItem")


@_attrs_define
class LedgerListDataItem:
    """
    Attributes:
        id (str): Ledger entry id (led_...).
        kind (LedgerListDataItemKind): signup_credit, topup, refund, debit_keyword_days, debit_mentions or adjustment.
        amount_cents (int): Integer USD cents; credits positive, debits negative.
        day (None | str): Debit rows: the last UTC day the row settled (YYYY-MM-DD).
        units (int | None): Debit rows: cumulative units (mentions or keyword-days) settled up to this row.
        note (None | str): Free text on credits and adjustments.
        polar_order_id (None | str): Top-ups and refunds: the Polar order.
        created_at (str): ISO 8601 timestamp, UTC.
    """

    id: str
    kind: LedgerListDataItemKind
    amount_cents: int
    day: None | str
    units: int | None
    note: None | str
    polar_order_id: None | str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        amount_cents = self.amount_cents

        day: None | str
        day = self.day

        units: int | None
        units = self.units

        note: None | str
        note = self.note

        polar_order_id: None | str
        polar_order_id = self.polar_order_id

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "amountCents": amount_cents,
                "day": day,
                "units": units,
                "note": note,
                "polarOrderId": polar_order_id,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        kind = LedgerListDataItemKind(d.pop("kind"))

        amount_cents = d.pop("amountCents")

        def _parse_day(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        day = _parse_day(d.pop("day"))

        def _parse_units(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        units = _parse_units(d.pop("units"))

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        def _parse_polar_order_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        polar_order_id = _parse_polar_order_id(d.pop("polarOrderId"))

        created_at = d.pop("createdAt")

        ledger_list_data_item = cls(
            id=id,
            kind=kind,
            amount_cents=amount_cents,
            day=day,
            units=units,
            note=note,
            polar_order_id=polar_order_id,
            created_at=created_at,
        )

        ledger_list_data_item.additional_properties = d
        return ledger_list_data_item

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
