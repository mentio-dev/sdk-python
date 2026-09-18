from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageSummaryKeywords")


@_attrs_define
class UsageSummaryKeywords:
    """Keywords against the wallet.

    Attributes:
        active (int): Unmuted keywords, the ones charged daily.
        paused (int): Keywords the wallet paused for lack of balance; a top-up resumes them.
        limit (int): How many keywords the workspace may run right now: the self-serve ceiling when the balance covers
            one more keyword-day, else 0.
        day_cents (int): What one more day of the active keywords costs.
    """

    active: int
    paused: int
    limit: int
    day_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        paused = self.paused

        limit = self.limit

        day_cents = self.day_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "paused": paused,
                "limit": limit,
                "dayCents": day_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        active = d.pop("active")

        paused = d.pop("paused")

        limit = d.pop("limit")

        day_cents = d.pop("dayCents")

        usage_summary_keywords = cls(
            active=active,
            paused=paused,
            limit=limit,
            day_cents=day_cents,
        )

        usage_summary_keywords.additional_properties = d
        return usage_summary_keywords

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
