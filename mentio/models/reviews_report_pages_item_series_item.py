from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReviewsReportPagesItemSeriesItem")


@_attrs_define
class ReviewsReportPagesItemSeriesItem:
    """
    Attributes:
        date (str): Bucket start, YYYY-MM-DD.
        reviews (int):
        average_rating (float | None): Average stars, one decimal; null with no reviews.
    """

    date: str
    reviews: int
    average_rating: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        reviews = self.reviews

        average_rating: float | None
        average_rating = self.average_rating

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "reviews": reviews,
                "averageRating": average_rating,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = d.pop("date")

        reviews = d.pop("reviews")

        def _parse_average_rating(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        average_rating = _parse_average_rating(d.pop("averageRating"))

        reviews_report_pages_item_series_item = cls(
            date=date,
            reviews=reviews,
            average_rating=average_rating,
        )

        reviews_report_pages_item_series_item.additional_properties = d
        return reviews_report_pages_item_series_item

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
