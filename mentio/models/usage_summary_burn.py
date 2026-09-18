from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageSummaryBurn")


@_attrs_define
class UsageSummaryBurn:
    """How fast the balance goes.

    Attributes:
        per_day_cents (int): Average daily debit over the last 7 days (or since the workspace was created).
        days_left (int | None): effectiveCents divided by perDayCents; null when nothing is burning.
    """

    per_day_cents: int
    days_left: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        per_day_cents = self.per_day_cents

        days_left: int | None
        days_left = self.days_left

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "perDayCents": per_day_cents,
                "daysLeft": days_left,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        per_day_cents = d.pop("perDayCents")

        def _parse_days_left(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_left = _parse_days_left(d.pop("daysLeft"))

        usage_summary_burn = cls(
            per_day_cents=per_day_cents,
            days_left=days_left,
        )

        usage_summary_burn.additional_properties = d
        return usage_summary_burn

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
