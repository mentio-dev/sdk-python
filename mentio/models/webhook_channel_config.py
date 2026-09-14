from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        secret (str | Unset): Only on creation and rotation. Signs every body: X-Mentions-Signature is the hex HMAC-
            SHA256 of the raw bytes.
    """

    url: str
    headers: WebhookChannelConfigHeaders
    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        headers = self.headers.to_dict()

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "headers": headers,
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

        secret = d.pop("secret", UNSET)

        webhook_channel_config = cls(
            url=url,
            headers=headers,
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
