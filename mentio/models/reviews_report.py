from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reviews_report_pages_item import ReviewsReportPagesItem
    from ..models.reviews_report_previous_type_0 import ReviewsReportPreviousType0
    from ..models.reviews_report_tags_item import ReviewsReportTagsItem
    from ..models.reviews_report_totals import ReviewsReportTotals
    from ..models.reviews_report_window import ReviewsReportWindow


T = TypeVar("T", bound="ReviewsReport")


@_attrs_define
class ReviewsReport:
    """
    Attributes:
        window (ReviewsReportWindow): The window the report covers.
        totals (ReviewsReportTotals):
        tags (list[ReviewsReportTagsItem]): Intent and topic tags on the 1 and 2 star reviews, most frequent first: what
            the unhappy ones are about.
        pages (list[ReviewsReportPagesItem]): One row per review page with reviews in the window, most reviewed first.
        previous (None | ReviewsReportPreviousType0): Totals for the period right before the window, with compare=true;
            else null.
    """

    window: ReviewsReportWindow
    totals: ReviewsReportTotals
    tags: list[ReviewsReportTagsItem]
    pages: list[ReviewsReportPagesItem]
    previous: None | ReviewsReportPreviousType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.reviews_report_previous_type_0 import ReviewsReportPreviousType0

        window = self.window.to_dict()

        totals = self.totals.to_dict()

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        pages = []
        for pages_item_data in self.pages:
            pages_item = pages_item_data.to_dict()
            pages.append(pages_item)

        previous: dict[str, Any] | None
        if isinstance(self.previous, ReviewsReportPreviousType0):
            previous = self.previous.to_dict()
        else:
            previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window": window,
                "totals": totals,
                "tags": tags,
                "pages": pages,
                "previous": previous,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.reviews_report_pages_item import (
            ReviewsReportPagesItem,
        )
        from ..models.reviews_report_previous_type_0 import (
            ReviewsReportPreviousType0,
        )
        from ..models.reviews_report_tags_item import (
            ReviewsReportTagsItem,
        )
        from ..models.reviews_report_totals import ReviewsReportTotals
        from ..models.reviews_report_window import ReviewsReportWindow

        d = dict(src_dict)
        window = ReviewsReportWindow.from_dict(d.pop("window"))

        totals = ReviewsReportTotals.from_dict(d.pop("totals"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = ReviewsReportTagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        pages = []
        _pages = d.pop("pages")
        for pages_item_data in _pages:
            pages_item = ReviewsReportPagesItem.from_dict(pages_item_data)

            pages.append(pages_item)

        def _parse_previous(data: object) -> None | ReviewsReportPreviousType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                previous_type_0 = ReviewsReportPreviousType0.from_dict(data)

                return previous_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReviewsReportPreviousType0, data)

        previous = _parse_previous(d.pop("previous"))

        reviews_report = cls(
            window=window,
            totals=totals,
            tags=tags,
            pages=pages,
            previous=previous,
        )

        reviews_report.additional_properties = d
        return reviews_report

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
