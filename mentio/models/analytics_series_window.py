from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analytics_series_window_bucket import AnalyticsSeriesWindowBucket

T = TypeVar("T", bound="AnalyticsSeriesWindow")


@_attrs_define
class AnalyticsSeriesWindow:
    """The window the report covers.

    Attributes:
        from_ (str): First day, inclusive.
        to (str): Last day, inclusive.
        days (int): Length of the window in days.
        timezone (str): IANA zone the days were cut in.
        bucket (AnalyticsSeriesWindowBucket): Point granularity used: hour, day, week (Monday to Sunday) or month.
    """

    from_: str
    to: str
    days: int
    timezone: str
    bucket: AnalyticsSeriesWindowBucket
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        days = self.days

        timezone = self.timezone

        bucket = self.bucket.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "days": days,
                "timezone": timezone,
                "bucket": bucket,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        days = d.pop("days")

        timezone = d.pop("timezone")

        bucket = AnalyticsSeriesWindowBucket(d.pop("bucket"))

        analytics_series_window = cls(
            from_=from_,
            to=to,
            days=days,
            timezone=timezone,
            bucket=bucket,
        )

        analytics_series_window.additional_properties = d
        return analytics_series_window

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
