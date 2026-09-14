from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analytics_breakdown_by import AnalyticsBreakdownBy

if TYPE_CHECKING:
    from ..models.analytics_breakdown_data_item import AnalyticsBreakdownDataItem
    from ..models.analytics_breakdown_window import AnalyticsBreakdownWindow


T = TypeVar("T", bound="AnalyticsBreakdown")


@_attrs_define
class AnalyticsBreakdown:
    """
    Attributes:
        window (AnalyticsBreakdownWindow): The window the report covers.
        by (AnalyticsBreakdownBy): The dimension the rows are grouped by.
        data (list[AnalyticsBreakdownDataItem]): Most matched first, at most 50 groups. by=hour is chronological and
            unlimited (168 cells at most).
    """

    window: AnalyticsBreakdownWindow
    by: AnalyticsBreakdownBy
    data: list[AnalyticsBreakdownDataItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        window = self.window.to_dict()

        by = self.by.value

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window": window,
                "by": by,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analytics_breakdown_data_item import (
            AnalyticsBreakdownDataItem,
        )
        from ..models.analytics_breakdown_window import (
            AnalyticsBreakdownWindow,
        )

        d = dict(src_dict)
        window = AnalyticsBreakdownWindow.from_dict(d.pop("window"))

        by = AnalyticsBreakdownBy(d.pop("by"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = AnalyticsBreakdownDataItem.from_dict(data_item_data)

            data.append(data_item)

        analytics_breakdown = cls(
            window=window,
            by=by,
            data=data,
        )

        analytics_breakdown.additional_properties = d
        return analytics_breakdown

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
