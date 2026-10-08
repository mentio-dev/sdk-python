from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListKeywordsResponse200DataItemCapType0")


@_attrs_define
class ListKeywordsResponse200DataItemCapType0:
    """The monthly mention cap, or null for none.

    Attributes:
        mentions (int): Charged items allowed per calendar month (UTC): matched mentions plus the thread comments
            delivered under them. Every match counts, relevant or not, the look-back a new keyword gets included, because
            every match bills.
        welcome (bool): Set by Mentio, not you: a workspace on its welcome credit collects at most 200 mentions a
            keyword a month. The first top-up removes it.
        own (int | None): Your own cap. With welcome true, the cap the keyword gets back at the first top-up (null for
            none); otherwise the same as mentions. Sending mentions: 200 back while welcome is true changes nothing.
    """

    mentions: int
    welcome: bool
    own: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mentions = self.mentions

        welcome = self.welcome

        own: int | None
        own = self.own

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mentions": mentions,
                "welcome": welcome,
                "own": own,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mentions = d.pop("mentions")

        welcome = d.pop("welcome")

        def _parse_own(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        own = _parse_own(d.pop("own"))

        list_keywords_response_200_data_item_cap_type_0 = cls(
            mentions=mentions,
            welcome=welcome,
            own=own,
        )

        list_keywords_response_200_data_item_cap_type_0.additional_properties = d
        return list_keywords_response_200_data_item_cap_type_0

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
