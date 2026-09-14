from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.analytics_series_data_item import AnalyticsSeriesDataItem
    from ..models.analytics_series_previous_type_0_item import (
        AnalyticsSeriesPreviousType0Item,
    )
    from ..models.analytics_series_window import AnalyticsSeriesWindow


T = TypeVar("T", bound="AnalyticsSeries")


@_attrs_define
class AnalyticsSeries:
    """
    Attributes:
        window (AnalyticsSeriesWindow): The window the report covers.
        data (list[AnalyticsSeriesDataItem]): One item per series, most matched first; a single "total" item when not
            split.
        previous (list[AnalyticsSeriesPreviousType0Item] | None): The same items over the period right before the
            window, in the same order, points aligned by index with `data` (the last bucket may be missing when weeks split
            differently); null unless compare=true.
    """

    window: AnalyticsSeriesWindow
    data: list[AnalyticsSeriesDataItem]
    previous: list[AnalyticsSeriesPreviousType0Item] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        window = self.window.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        previous: list[dict[str, Any]] | None
        if isinstance(self.previous, list):
            previous = []
            for previous_type_0_item_data in self.previous:
                previous_type_0_item = previous_type_0_item_data.to_dict()
                previous.append(previous_type_0_item)

        else:
            previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window": window,
                "data": data,
                "previous": previous,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analytics_series_data_item import (
            AnalyticsSeriesDataItem,
        )
        from ..models.analytics_series_previous_type_0_item import (
            AnalyticsSeriesPreviousType0Item,
        )
        from ..models.analytics_series_window import (
            AnalyticsSeriesWindow,
        )

        d = dict(src_dict)
        window = AnalyticsSeriesWindow.from_dict(d.pop("window"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = AnalyticsSeriesDataItem.from_dict(data_item_data)

            data.append(data_item)

        def _parse_previous(
            data: object,
        ) -> list[AnalyticsSeriesPreviousType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                previous_type_0 = []
                _previous_type_0 = data
                for previous_type_0_item_data in _previous_type_0:
                    previous_type_0_item = AnalyticsSeriesPreviousType0Item.from_dict(
                        previous_type_0_item_data
                    )

                    previous_type_0.append(previous_type_0_item)

                return previous_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AnalyticsSeriesPreviousType0Item] | None, data)

        previous = _parse_previous(d.pop("previous"))

        analytics_series = cls(
            window=window,
            data=data,
            previous=previous,
        )

        analytics_series.additional_properties = d
        return analytics_series

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
