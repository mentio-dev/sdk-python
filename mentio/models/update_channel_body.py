from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_channel_body_events_item import UpdateChannelBodyEventsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_channel_body_headers import UpdateChannelBodyHeaders


T = TypeVar("T", bound="UpdateChannelBody")


@_attrs_define
class UpdateChannelBody:
    """Omitted fields are untouched.

    Attributes:
        label (str | Unset):
        url (str | Unset): Webhooks only.
        headers (UpdateChannelBodyHeaders | Unset): Webhooks only; replaces the whole set.
        events (list[UpdateChannelBodyEventsItem] | Unset): Webhooks only; replaces the whole set of account events the
            endpoint receives. An empty list unsubscribes it from all of them.
    """

    label: str | Unset = UNSET
    url: str | Unset = UNSET
    headers: UpdateChannelBodyHeaders | Unset = UNSET
    events: list[UpdateChannelBodyEventsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        url = self.url

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if url is not UNSET:
            field_dict["url"] = url
        if headers is not UNSET:
            field_dict["headers"] = headers
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_channel_body_headers import (
            UpdateChannelBodyHeaders,
        )

        d = dict(src_dict)
        label = d.pop("label", UNSET)

        url = d.pop("url", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: UpdateChannelBodyHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = UpdateChannelBodyHeaders.from_dict(_headers)

        _events = d.pop("events", UNSET)
        events: list[UpdateChannelBodyEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = UpdateChannelBodyEventsItem(events_item_data)

                events.append(events_item)

        update_channel_body = cls(
            label=label,
            url=url,
            headers=headers,
            events=events,
        )

        update_channel_body.additional_properties = d
        return update_channel_body

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
