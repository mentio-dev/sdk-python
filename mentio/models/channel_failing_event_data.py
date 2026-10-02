from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.channel_failing_event_data_channel import (
        ChannelFailingEventDataChannel,
    )


T = TypeVar("T", bound="ChannelFailingEventData")


@_attrs_define
class ChannelFailingEventData:
    """
    Attributes:
        attention_id (str): The attention item (att_...): GET /v1/attention lists it, POST /v1/attention/{id}/dismiss
            puts it away.
        url (str): Where to look in the dashboard.
        channel (ChannelFailingEventDataChannel): The channel whose sends fail.
        failures (int): Failed sends in a row within the last 24 hours.
        last_error (None | str): The newest failure, as the transport reported it.
        since (str): The oldest of those failures.
    """

    attention_id: str
    url: str
    channel: ChannelFailingEventDataChannel
    failures: int
    last_error: None | str
    since: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attention_id = self.attention_id

        url = self.url

        channel = self.channel.to_dict()

        failures = self.failures

        last_error: None | str
        last_error = self.last_error

        since = self.since

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attentionId": attention_id,
                "url": url,
                "channel": channel,
                "failures": failures,
                "lastError": last_error,
                "since": since,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.channel_failing_event_data_channel import (
            ChannelFailingEventDataChannel,
        )

        d = dict(src_dict)
        attention_id = d.pop("attentionId")

        url = d.pop("url")

        channel = ChannelFailingEventDataChannel.from_dict(d.pop("channel"))

        failures = d.pop("failures")

        def _parse_last_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_error = _parse_last_error(d.pop("lastError"))

        since = d.pop("since")

        channel_failing_event_data = cls(
            attention_id=attention_id,
            url=url,
            channel=channel,
            failures=failures,
            last_error=last_error,
            since=since,
        )

        channel_failing_event_data.additional_properties = d
        return channel_failing_event_data

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
