from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.analytics_series_previous_type_0_item_keyword_type_0 import (
        AnalyticsSeriesPreviousType0ItemKeywordType0,
    )
    from ..models.analytics_series_previous_type_0_item_points_item import (
        AnalyticsSeriesPreviousType0ItemPointsItem,
    )


T = TypeVar("T", bound="AnalyticsSeriesPreviousType0Item")


@_attrs_define
class AnalyticsSeriesPreviousType0Item:
    """
    Attributes:
        key (str): Platform name, keyword id, "total" for the unsplit series, or "other" for the keys beyond the top 20.
        label (str): Readable name: the platform, the keyword term, "Total" or "Other".
        keyword (AnalyticsSeriesPreviousType0ItemKeywordType0 | None): Set when split by keyword; null otherwise.
        points (list[AnalyticsSeriesPreviousType0ItemPointsItem]): One point per bucket across the window, oldest first,
            zero-filled.
    """

    key: str
    label: str
    keyword: AnalyticsSeriesPreviousType0ItemKeywordType0 | None
    points: list[AnalyticsSeriesPreviousType0ItemPointsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analytics_series_previous_type_0_item_keyword_type_0 import (
            AnalyticsSeriesPreviousType0ItemKeywordType0,
        )

        key = self.key

        label = self.label

        keyword: dict[str, Any] | None
        if isinstance(self.keyword, AnalyticsSeriesPreviousType0ItemKeywordType0):
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
        from ..models.analytics_series_previous_type_0_item_keyword_type_0 import (
            AnalyticsSeriesPreviousType0ItemKeywordType0,
        )
        from ..models.analytics_series_previous_type_0_item_points_item import (
            AnalyticsSeriesPreviousType0ItemPointsItem,
        )

        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        def _parse_keyword(
            data: object,
        ) -> AnalyticsSeriesPreviousType0ItemKeywordType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_type_0 = AnalyticsSeriesPreviousType0ItemKeywordType0.from_dict(
                    data
                )

                return keyword_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnalyticsSeriesPreviousType0ItemKeywordType0 | None, data)

        keyword = _parse_keyword(d.pop("keyword"))

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = AnalyticsSeriesPreviousType0ItemPointsItem.from_dict(
                points_item_data
            )

            points.append(points_item)

        analytics_series_previous_type_0_item = cls(
            key=key,
            label=label,
            keyword=keyword,
            points=points,
        )

        analytics_series_previous_type_0_item.additional_properties = d
        return analytics_series_previous_type_0_item

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
