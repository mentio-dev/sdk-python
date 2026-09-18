from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.analytics_series_data_item_keyword_type_0 import (
        AnalyticsSeriesDataItemKeywordType0,
    )
    from ..models.analytics_series_data_item_points_item import (
        AnalyticsSeriesDataItemPointsItem,
    )


T = TypeVar("T", bound="AnalyticsSeriesDataItem")


@_attrs_define
class AnalyticsSeriesDataItem:
    """
    Attributes:
        key (str): Platform name, keyword id, sentiment (positive, neutral, negative, unclassified), "total" for the
            unsplit series, or "other" for the keys beyond the top 20.
        label (str): Readable name: the platform, the keyword term, the sentiment, "Total" or "Other".
        keyword (AnalyticsSeriesDataItemKeywordType0 | None): Set when split by keyword; null otherwise.
        points (list[AnalyticsSeriesDataItemPointsItem]): One point per bucket across the window, oldest first, zero-
            filled.
    """

    key: str
    label: str
    keyword: AnalyticsSeriesDataItemKeywordType0 | None
    points: list[AnalyticsSeriesDataItemPointsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analytics_series_data_item_keyword_type_0 import (
            AnalyticsSeriesDataItemKeywordType0,
        )

        key = self.key

        label = self.label

        keyword: dict[str, Any] | None
        if isinstance(self.keyword, AnalyticsSeriesDataItemKeywordType0):
            keyword = self.keyword.to_dict()
        else:
            keyword = self.keyword

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "keyword": keyword,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analytics_series_data_item_keyword_type_0 import (
            AnalyticsSeriesDataItemKeywordType0,
        )
        from ..models.analytics_series_data_item_points_item import (
            AnalyticsSeriesDataItemPointsItem,
        )

        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        def _parse_keyword(data: object) -> AnalyticsSeriesDataItemKeywordType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_type_0 = AnalyticsSeriesDataItemKeywordType0.from_dict(data)

                return keyword_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnalyticsSeriesDataItemKeywordType0 | None, data)

        keyword = _parse_keyword(d.pop("keyword"))

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = AnalyticsSeriesDataItemPointsItem.from_dict(points_item_data)

            points.append(points_item)

        analytics_series_data_item = cls(
            key=key,
            label=label,
            keyword=keyword,
            points=points,
        )

        analytics_series_data_item.additional_properties = d
        return analytics_series_data_item

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
