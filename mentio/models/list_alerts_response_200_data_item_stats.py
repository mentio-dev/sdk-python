from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListAlertsResponse200DataItemStats")


@_attrs_define
class ListAlertsResponse200DataItemStats:
    """Computed over this workspace's deliveries.

    Attributes:
        sent_last_7_d (int): Deliveries in the last 7 days, across channels.
        last_sent_at (None | str): ISO 8601 timestamp, UTC.
        next_run_at (None | str): Daily alerts: the next digest; null when disabled or instant.
    """

    sent_last_7_d: int
    last_sent_at: None | str
    next_run_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sent_last_7_d = self.sent_last_7_d

        last_sent_at: None | str
        last_sent_at = self.last_sent_at

        next_run_at: None | str
        next_run_at = self.next_run_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sentLast7d": sent_last_7_d,
                "lastSentAt": last_sent_at,
                "nextRunAt": next_run_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sent_last_7_d = d.pop("sentLast7d")

        def _parse_last_sent_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_sent_at = _parse_last_sent_at(d.pop("lastSentAt"))

        def _parse_next_run_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_run_at = _parse_next_run_at(d.pop("nextRunAt"))

        list_alerts_response_200_data_item_stats = cls(
            sent_last_7_d=sent_last_7_d,
            last_sent_at=last_sent_at,
            next_run_at=next_run_at,
        )

        list_alerts_response_200_data_item_stats.additional_properties = d
        return list_alerts_response_200_data_item_stats

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
