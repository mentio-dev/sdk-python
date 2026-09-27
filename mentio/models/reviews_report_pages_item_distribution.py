from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReviewsReportPagesItemDistribution")


@_attrs_define
class ReviewsReportPagesItemDistribution:
    """Reviews per star rating.

    Attributes:
        field_1 (int):
        field_2 (int):
        field_3 (int):
        field_4 (int):
        field_5 (int):
    """

    field_1: int
    field_2: int
    field_3: int
    field_4: int
    field_5: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_1 = self.field_1

        field_2 = self.field_2

        field_3 = self.field_3

        field_4 = self.field_4

        field_5 = self.field_5

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "1": field_1,
                "2": field_2,
                "3": field_3,
                "4": field_4,
                "5": field_5,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        field_1 = d.pop("1")

        field_2 = d.pop("2")

        field_3 = d.pop("3")

        field_4 = d.pop("4")

        field_5 = d.pop("5")

        reviews_report_pages_item_distribution = cls(
            field_1=field_1,
            field_2=field_2,
            field_3=field_3,
            field_4=field_4,
            field_5=field_5,
        )

        reviews_report_pages_item_distribution.additional_properties = d
        return reviews_report_pages_item_distribution

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
