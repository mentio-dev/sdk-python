from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsSummaryTriage")


@_attrs_define
class AnalyticsSummaryTriage:
    """Where the matches stand in your inbox.

    Attributes:
        open_ (int): Status open.
        ignored (int): Status ignored.
        done (int): Status done.
        waiting (int): Relevant, still open, and matched more than 24 hours ago.
        handled_rate (float | None): done divided by relevant, 0 to 1; null when nothing was relevant.
        median_time_to_done_ms (float | None): Median milliseconds from match to done; null when nothing was done.
    """

    open_: int
    ignored: int
    done: int
    waiting: int
    handled_rate: float | None
    median_time_to_done_ms: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_

        ignored = self.ignored

        done = self.done

        waiting = self.waiting

        handled_rate: float | None
        handled_rate = self.handled_rate

        median_time_to_done_ms: float | None
        median_time_to_done_ms = self.median_time_to_done_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "open": open_,
                "ignored": ignored,
                "done": done,
                "waiting": waiting,
                "handledRate": handled_rate,
                "medianTimeToDoneMs": median_time_to_done_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        open_ = d.pop("open")

        ignored = d.pop("ignored")

        done = d.pop("done")

        waiting = d.pop("waiting")

        def _parse_handled_rate(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        handled_rate = _parse_handled_rate(d.pop("handledRate"))

        def _parse_median_time_to_done_ms(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        median_time_to_done_ms = _parse_median_time_to_done_ms(
            d.pop("medianTimeToDoneMs")
        )

        analytics_summary_triage = cls(
            open_=open_,
            ignored=ignored,
            done=done,
            waiting=waiting,
            handled_rate=handled_rate,
            median_time_to_done_ms=median_time_to_done_ms,
        )

        analytics_summary_triage.additional_properties = d
        return analytics_summary_triage

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
