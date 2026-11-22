from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordEstimateTermsItemPlatformsItemMonthlyType0")


@_attrs_define
class KeywordEstimateTermsItemPlatformsItemMonthlyType0:
    """Expected matched mentions a month on this platform; null without a number.

    Attributes:
        low (int): Low end of the expected matched mentions a month.
        high (int): High end of the expected matched mentions a month.
    """

    low: int
    high: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        low = self.low

        high = self.high

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "low": low,
                "high": high,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        low = d.pop("low")

        high = d.pop("high")

        keyword_estimate_terms_item_platforms_item_monthly_type_0 = cls(
            low=low,
            high=high,
        )

        keyword_estimate_terms_item_platforms_item_monthly_type_0.additional_properties = d
        return keyword_estimate_terms_item_platforms_item_monthly_type_0

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
