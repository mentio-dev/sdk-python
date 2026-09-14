from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_channel_stats_last_7d import WebhookChannelStatsLast7D


T = TypeVar("T", bound="WebhookChannelStats")


@_attrs_define
class WebhookChannelStats:
    """Computed over this workspace's deliveries.

    Attributes:
        alerts (int): Alerts sending to this channel.
        active_alerts (int): Of those, enabled ones; 0 means the channel receives nothing right now.
        last_delivery_at (None | str): Newest delivery attempt, successful or not.
        last7d (WebhookChannelStatsLast7D): Deliveries in the last 7 days.
    """

    alerts: int
    active_alerts: int
    last_delivery_at: None | str
    last7d: WebhookChannelStatsLast7D
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alerts = self.alerts

        active_alerts = self.active_alerts

        last_delivery_at: None | str
        last_delivery_at = self.last_delivery_at

        last7d = self.last7d.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alerts": alerts,
                "activeAlerts": active_alerts,
                "lastDeliveryAt": last_delivery_at,
                "last7d": last7d,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_channel_stats_last_7d import (
            WebhookChannelStatsLast7D,
        )

        d = dict(src_dict)
        alerts = d.pop("alerts")

        active_alerts = d.pop("activeAlerts")

        def _parse_last_delivery_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_delivery_at = _parse_last_delivery_at(d.pop("lastDeliveryAt"))

        last7d = WebhookChannelStatsLast7D.from_dict(d.pop("last7d"))

        webhook_channel_stats = cls(
            alerts=alerts,
            active_alerts=active_alerts,
            last_delivery_at=last_delivery_at,
            last7d=last7d,
        )

        webhook_channel_stats.additional_properties = d
        return webhook_channel_stats

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
