from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_teams_channel_events_item import CreateTeamsChannelEventsItem
from ..models.create_teams_channel_kind import CreateTeamsChannelKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTeamsChannel")


@_attrs_define
class CreateTeamsChannel:
    """
    Attributes:
        kind (CreateTeamsChannelKind): Channel kind.
        url (str): The Teams Workflows webhook URL (in Teams: the channel's menu, Workflows, "Send webhook alerts to a
            channel", then copy the URL it gives). Office 365 connector URLs (webhook.office.com), retired by Microsoft in
            2026, are refused. Write-only: reads show urlHint.
        label (str | Unset): A name for the channel ("Marketing > Mentions"); "Teams" when omitted.
        events (list[CreateTeamsChannelEventsItem] | Unset): Attention events to receive here, on top of whatever rules
            send. Omit for none.
    """

    kind: CreateTeamsChannelKind
    url: str
    label: str | Unset = UNSET
    events: list[CreateTeamsChannelEventsItem] | Unset = UNSET
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
        kind = CreateTeamsChannelKind(d.pop("kind"))

        url = d.pop("url")

        label = d.pop("label", UNSET)

        _events = d.pop("events", UNSET)
        events: list[CreateTeamsChannelEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = CreateTeamsChannelEventsItem(events_item_data)

                events.append(events_item)

        create_teams_channel = cls(
            kind=kind,
            url=url,
            label=label,
            events=events,
        )

        create_teams_channel.additional_properties = d
        return create_teams_channel

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
