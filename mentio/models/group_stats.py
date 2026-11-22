from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GroupStats")


@_attrs_define
class GroupStats:
    """Computed over the group's keywords.

    Attributes:
        keywords (int): Keywords in the group, muted ones included.
        active (int): Keywords in the group that are tracking (not muted).
        accounts (int): Tracked accounts in the group; a delete takes them too.
    """

    keywords: int
    active: int
    accounts: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        active = self.active

        accounts = self.accounts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keywords": keywords,
                "active": active,
                "accounts": accounts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keywords = d.pop("keywords")

        active = d.pop("active")

        accounts = d.pop("accounts")

        group_stats = cls(
            keywords=keywords,
            active=active,
            accounts=accounts,
        )

        group_stats.additional_properties = d
        return group_stats

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
