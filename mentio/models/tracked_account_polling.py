from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TrackedAccountPolling")


@_attrs_define
class TrackedAccountPolling:
    """The poller's state.

    Attributes:
        baseline_at (None | str): When the first read ran; until then nothing is new or billed.
        last_polled_at (None | str): When the last read ran.
        next_poll_at (None | str): When the next read is due; null while paused.
        last_error (None | str): Why the last read failed or waited, or null.
    """

    baseline_at: None | str
    last_polled_at: None | str
    next_poll_at: None | str
    last_error: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        baseline_at: None | str
        baseline_at = self.baseline_at

        last_polled_at: None | str
        last_polled_at = self.last_polled_at

        next_poll_at: None | str
        next_poll_at = self.next_poll_at

        last_error: None | str
        last_error = self.last_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baselineAt": baseline_at,
                "lastPolledAt": last_polled_at,
                "nextPollAt": next_poll_at,
                "lastError": last_error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_baseline_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        baseline_at = _parse_baseline_at(d.pop("baselineAt"))

        def _parse_last_polled_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_polled_at = _parse_last_polled_at(d.pop("lastPolledAt"))

        def _parse_next_poll_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_poll_at = _parse_next_poll_at(d.pop("nextPollAt"))

        def _parse_last_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_error = _parse_last_error(d.pop("lastError"))

        tracked_account_polling = cls(
            baseline_at=baseline_at,
            last_polled_at=last_polled_at,
            next_poll_at=next_poll_at,
            last_error=last_error,
        )

        tracked_account_polling.additional_properties = d
        return tracked_account_polling

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
