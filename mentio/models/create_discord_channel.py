from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_discord_channel_events_item import CreateDiscordChannelEventsItem
from ..models.create_discord_channel_kind import CreateDiscordChannelKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDiscordChannel")


@_attrs_define
class CreateDiscordChannel:
    """
    Attributes:
        kind (CreateDiscordChannelKind): Channel kind.
        url (str): The Discord incoming webhook URL, https://discord.com/api/webhooks/<id>/<token> (in Discord: Channel
            settings, Integrations, Webhooks, Copy Webhook URL). A ?thread_id= posts into a thread. Write-only: reads show
            urlHint.
        label (str | Unset): A name for the channel ("#alerts on our server"); "Discord" when omitted.
        events (list[CreateDiscordChannelEventsItem] | Unset): Attention events and followers.new to receive here, on
            top of whatever rules send. Omit for none.
    """

    kind: CreateDiscordChannelKind
    url: str
    label: str | Unset = UNSET
    events: list[CreateDiscordChannelEventsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        url = self.url

        label = self.label

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "url": url,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = CreateDiscordChannelKind(d.pop("kind"))

        url = d.pop("url")

        label = d.pop("label", UNSET)

        _events = d.pop("events", UNSET)
        events: list[CreateDiscordChannelEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = CreateDiscordChannelEventsItem(events_item_data)

                events.append(events_item)

        create_discord_channel = cls(
            kind=kind,
            url=url,
            label=label,
            events=events,
        )

        create_discord_channel.additional_properties = d
        return create_discord_channel

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
