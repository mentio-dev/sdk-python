from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageSummaryFollowers")


@_attrs_define
class UsageSummaryFollowers:
    """New followers of tracked accounts, billed like mentions.

    Attributes:
        today (int): New followers billed today (UTC), every tracked account.
        last30d (int): New followers billed in the last 30 days.
    """

    today: int
    last30d: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        today = self.today

        last30d = self.last30d

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "today": today,
                "last30d": last30d,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        today = d.pop("today")

        last30d = d.pop("last30d")

        usage_summary_followers = cls(
            today=today,
            last30d=last30d,
        )

        usage_summary_followers.additional_properties = d
        return usage_summary_followers

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
