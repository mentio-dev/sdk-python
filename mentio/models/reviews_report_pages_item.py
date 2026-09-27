from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reviews_report_pages_item_platform import ReviewsReportPagesItemPlatform

if TYPE_CHECKING:
    from ..models.reviews_report_pages_item_distribution import (
        ReviewsReportPagesItemDistribution,
    )
    from ..models.reviews_report_pages_item_previous_type_0 import (
        ReviewsReportPagesItemPreviousType0,
    )
    from ..models.reviews_report_pages_item_series_item import (
        ReviewsReportPagesItemSeriesItem,
    )


T = TypeVar("T", bound="ReviewsReportPagesItem")


@_attrs_define
class ReviewsReportPagesItem:
    """
    Attributes:
        reviews (int): Reviews published in the window; a review matched by two keywords counts once.
        average_rating (float | None): Average stars, one decimal; null with no reviews.
        distribution (ReviewsReportPagesItemDistribution): Reviews per star rating.
        responded (int): Reviews carrying the owner's or developer's reply (the App Store's feed has none).
        open_negative (int): 1 and 2 star reviews nobody has marked done or ignored yet.
        platform (ReviewsReportPagesItemPlatform): appstore (Apple App Store), googleplay (Google Play), trustpilot (a
            company's Trustpilot page) or googlemaps (a place's Google reviews).
        id (str): The page's id: app id, package name, Trustpilot domain, Place ID or cid.
        url (str): The review page.
        series (list[ReviewsReportPagesItemSeriesItem]): Reviews and average stars per bucket, oldest first, every
            bucket present.
        previous (None | ReviewsReportPagesItemPreviousType0): The period of the same length right before the window,
            with compare=true; else null.
    """

    reviews: int
    average_rating: float | None
    distribution: ReviewsReportPagesItemDistribution
    responded: int
    open_negative: int
    platform: ReviewsReportPagesItemPlatform
    id: str
    url: str
    series: list[ReviewsReportPagesItemSeriesItem]
    previous: None | ReviewsReportPagesItemPreviousType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.reviews_report_pages_item_previous_type_0 import (
            ReviewsReportPagesItemPreviousType0,
        )

        reviews = self.reviews

        average_rating: float | None
        average_rating = self.average_rating

        distribution = self.distribution.to_dict()

        responded = self.responded

        open_negative = self.open_negative

        platform = self.platform.value

        id = self.id

        url = self.url

        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        previous: dict[str, Any] | None
        if isinstance(self.previous, ReviewsReportPagesItemPreviousType0):
            previous = self.previous.to_dict()
        else:
            previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reviews": reviews,
                "averageRating": average_rating,
                "distribution": distribution,
                "responded": responded,
                "openNegative": open_negative,
                "platform": platform,
                "id": id,
                "url": url,
                "series": series,
                "previous": previous,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.reviews_report_pages_item_distribution import (
            ReviewsReportPagesItemDistribution,
        )
        from ..models.reviews_report_pages_item_previous_type_0 import (
            ReviewsReportPagesItemPreviousType0,
        )
        from ..models.reviews_report_pages_item_series_item import (
            ReviewsReportPagesItemSeriesItem,
        )

        d = dict(src_dict)
        reviews = d.pop("reviews")

        def _parse_average_rating(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        average_rating = _parse_average_rating(d.pop("averageRating"))

        distribution = ReviewsReportPagesItemDistribution.from_dict(
            d.pop("distribution")
        )

        responded = d.pop("responded")

        open_negative = d.pop("openNegative")

        platform = ReviewsReportPagesItemPlatform(d.pop("platform"))

        id = d.pop("id")

        url = d.pop("url")

        series = []
        _series = d.pop("series")
        for series_item_data in _series:
            series_item = ReviewsReportPagesItemSeriesItem.from_dict(series_item_data)

            series.append(series_item)

        def _parse_previous(data: object) -> None | ReviewsReportPagesItemPreviousType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                previous_type_0 = ReviewsReportPagesItemPreviousType0.from_dict(data)

                return previous_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReviewsReportPagesItemPreviousType0, data)

        previous = _parse_previous(d.pop("previous"))

        reviews_report_pages_item = cls(
            reviews=reviews,
            average_rating=average_rating,
            distribution=distribution,
            responded=responded,
            open_negative=open_negative,
            platform=platform,
            id=id,
            url=url,
            series=series,
            previous=previous,
        )

        reviews_report_pages_item.additional_properties = d
        return reviews_report_pages_item

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
