from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_channel_config_events_item import WebhookChannelConfigEventsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_channel_config_headers import WebhookChannelConfigHeaders


T = TypeVar("T", bound="WebhookChannelConfig")


@_attrs_define
class WebhookChannelConfig:
    """
    Attributes:
        url (str): Where the signed POSTs go.
        headers (WebhookChannelConfigHeaders): Extra request headers you configured.
        events (list[WebhookChannelConfigEventsItem]): The account events this endpoint receives on its own, no rule
            involved: keyword and wallet state changes. Empty when it receives none; mention and digest deliveries come
            through rules as before.
        secret (str | Unset): Only on creation and rotation. Signs every request: X-Mentions-Signature-V2 is v2= plus
            the hex HMAC-SHA256 of "<X-Mentions-Timestamp>.<raw body>" (reject a timestamp older than a few minutes);
            X-Mentions-Signature, the hex HMAC-SHA256 of the raw body alone, stays for older verifiers.
    """

    url: str
    headers: WebhookChannelConfigHeaders
    events: list[WebhookChannelConfigEventsItem]
    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        headers = self.headers.to_dict()

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "headers": headers,
                "events": events,
            }
        )
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_channel_config_headers import (
            WebhookChannelConfigHeaders,
        )

        d = dict(src_dict)
        url = d.pop("url")

        headers = WebhookChannelConfigHeaders.from_dict(d.pop("headers"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = WebhookChannelConfigEventsItem(events_item_data)

            events.append(events_item)

        secret = d.pop("secret", UNSET)

        webhook_channel_config = cls(
            url=url,
            headers=headers,
            events=events,
            secret=secret,
        )

        webhook_channel_config.additional_properties = d
        return webhook_channel_config

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
