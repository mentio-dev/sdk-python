from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.teams_channel_config_events_item import TeamsChannelConfigEventsItem

T = TypeVar("T", bound="TeamsChannelConfig")


@_attrs_define
class TeamsChannelConfig:
    """The channel's settings for its kind; secrets are never returned.

    Attributes:
        url_hint (str): The Teams Workflows URL with its signature hidden; the full URL is write-only.
        events (list[TeamsChannelConfigEventsItem]): The attention events this channel receives on its own, no rule
            involved: one short message when an item opens (GET /v1/attention). Empty when it receives none.
    """

    url_hint: str
    events: list[TeamsChannelConfigEventsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url_hint = self.url_hint

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "urlHint": url_hint,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url_hint = d.pop("urlHint")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = TeamsChannelConfigEventsItem(events_item_data)

            events.append(events_item)

        teams_channel_config = cls(
            url_hint=url_hint,
            events=events,
        )

        teams_channel_config.additional_properties = d
        return teams_channel_config

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
