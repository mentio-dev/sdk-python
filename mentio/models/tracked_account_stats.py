from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TrackedAccountStats")


@_attrs_define
class TrackedAccountStats:
    """Counts about the account.

    Attributes:
        followers (int | None): Its follower count on the platform, as the last poll read it.
        tracked (int): Followers Mentio has seen, the baseline included.
        this_month (int): New followers billed this UTC month.
    """

    followers: int | None
    tracked: int
    this_month: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        followers: int | None
        followers = self.followers

        tracked = self.tracked

        this_month = self.this_month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "followers": followers,
                "tracked": tracked,
                "thisMonth": this_month,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_followers(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        followers = _parse_followers(d.pop("followers"))

        tracked = d.pop("tracked")

        this_month = d.pop("thisMonth")

        tracked_account_stats = cls(
            followers=followers,
            tracked=tracked,
            this_month=this_month,
        )

        tracked_account_stats.additional_properties = d
        return tracked_account_stats

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
