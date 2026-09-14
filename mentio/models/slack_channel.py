from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slack_channel_kind import SlackChannelKind

if TYPE_CHECKING:
    from ..models.slack_channel_config import SlackChannelConfig
    from ..models.slack_channel_stats import SlackChannelStats


T = TypeVar("T", bound="SlackChannel")


@_attrs_define
class SlackChannel:
    """
    Attributes:
        id (str): Channel id (dest_...).
        label (str):
        stats (SlackChannelStats): Computed over this workspace's deliveries.
        created_at (str): ISO 8601 timestamp, UTC.
        kind (SlackChannelKind):
        config (SlackChannelConfig):
    """

    id: str
    label: str
    stats: SlackChannelStats
    created_at: str
    kind: SlackChannelKind
    config: SlackChannelConfig
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
        from ..models.slack_channel_config import SlackChannelConfig
        from ..models.slack_channel_stats import SlackChannelStats

        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        stats = SlackChannelStats.from_dict(d.pop("stats"))

        created_at = d.pop("createdAt")

        kind = SlackChannelKind(d.pop("kind"))

        config = SlackChannelConfig.from_dict(d.pop("config"))

        slack_channel = cls(
            id=id,
            label=label,
            stats=stats,
            created_at=created_at,
            kind=kind,
            config=config,
        )

        slack_channel.additional_properties = d
        return slack_channel

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
