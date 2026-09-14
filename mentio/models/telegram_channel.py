from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.telegram_channel_kind import TelegramChannelKind

if TYPE_CHECKING:
    from ..models.telegram_channel_config import TelegramChannelConfig
    from ..models.telegram_channel_stats import TelegramChannelStats


T = TypeVar("T", bound="TelegramChannel")


@_attrs_define
class TelegramChannel:
    """
    Attributes:
        id (str): Channel id (dest_...).
        label (str):
        stats (TelegramChannelStats): Computed over this workspace's deliveries.
        created_at (str): ISO 8601 timestamp, UTC.
        kind (TelegramChannelKind):
        config (TelegramChannelConfig):
    """

    id: str
    label: str
    stats: TelegramChannelStats
    created_at: str
    kind: TelegramChannelKind
    config: TelegramChannelConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        stats = self.stats.to_dict()

        created_at = self.created_at

        kind = self.kind.value

        config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "stats": stats,
                "createdAt": created_at,
                "kind": kind,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.telegram_channel_config import (
            TelegramChannelConfig,
        )
        from ..models.telegram_channel_stats import (
            TelegramChannelStats,
        )

        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        stats = TelegramChannelStats.from_dict(d.pop("stats"))

        created_at = d.pop("createdAt")

        kind = TelegramChannelKind(d.pop("kind"))

        config = TelegramChannelConfig.from_dict(d.pop("config"))

        telegram_channel = cls(
            id=id,
            label=label,
            stats=stats,
            created_at=created_at,
            kind=kind,
            config=config,
        )

        telegram_channel.additional_properties = d
        return telegram_channel

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
