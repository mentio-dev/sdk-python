from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsBreakdownDataItemPreviousType0")


@_attrs_define
class AnalyticsBreakdownDataItemPreviousType0:
    """The same group over the period right before the window; null unless compare=true.

    Attributes:
        matched (int): Matches in the group then.
        relevant (int): Relevant matches in the group then.
    """

    matched: int
    relevant: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matched = self.matched

        relevant = self.relevant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matched": matched,
                "relevant": relevant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        matched = d.pop("matched")

        relevant = d.pop("relevant")

        analytics_breakdown_data_item_previous_type_0 = cls(
            matched=matched,
            relevant=relevant,
        )

        analytics_breakdown_data_item_previous_type_0.additional_properties = d
        return analytics_breakdown_data_item_previous_type_0

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
