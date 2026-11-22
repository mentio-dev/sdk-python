from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordEstimateTermsItemPlatformsItemSampleType0")


@_attrs_define
class KeywordEstimateTermsItemPlatformsItemSampleType0:
    """What the number rests on; null without a number.

    Attributes:
        read (int): Posts read (index: posts counted).
        matched (int): Of them, holding the term and passing the rules.
        days (float): The span of time they cover, in days.
    """

    read: int
    matched: int
    days: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read = self.read

        matched = self.matched

        days = self.days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "read": read,
                "matched": matched,
                "days": days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        read = d.pop("read")

        matched = d.pop("matched")

        days = d.pop("days")

        keyword_estimate_terms_item_platforms_item_sample_type_0 = cls(
            read=read,
            matched=matched,
            days=days,
        )

        keyword_estimate_terms_item_platforms_item_sample_type_0.additional_properties = d
        return keyword_estimate_terms_item_platforms_item_sample_type_0

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
