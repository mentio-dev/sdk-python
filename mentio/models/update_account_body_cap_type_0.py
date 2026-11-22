from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateAccountBodyCapType0")


@_attrs_define
class UpdateAccountBodyCapType0:
    """Set the monthly follower cap; null removes it.

    Attributes:
        followers (int): New followers billed in a UTC calendar month at most; past it the account stops being read
            until the 1st.
    """

    followers: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        followers = self.followers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "followers": followers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        followers = d.pop("followers")

        update_account_body_cap_type_0 = cls(
            followers=followers,
        )

        update_account_body_cap_type_0.additional_properties = d
        return update_account_body_cap_type_0

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
