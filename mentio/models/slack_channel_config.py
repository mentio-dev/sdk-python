from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slack_channel_config_events_item import SlackChannelConfigEventsItem

T = TypeVar("T", bound="SlackChannelConfig")


@_attrs_define
class SlackChannelConfig:
    """
    Attributes:
        channel_id (str): Slack channel id.
        channel_name (str): Slack channel name, without the #.
        events (list[SlackChannelConfigEventsItem]): The attention events this channel receives on its own, no rule
            involved: one short message when an item opens (GET /v1/attention). Empty when it receives none.
    """

    channel_id: str
    channel_name: str
    events: list[SlackChannelConfigEventsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        channel_name = self.channel_name

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelId": channel_id,
                "channelName": channel_name,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel_id = d.pop("channelId")

        channel_name = d.pop("channelName")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = SlackChannelConfigEventsItem(events_item_data)

            events.append(events_item)

        slack_channel_config = cls(
            channel_id=channel_id,
            channel_name=channel_name,
            events=events,
        )

        slack_channel_config.additional_properties = d
        return slack_channel_config

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
