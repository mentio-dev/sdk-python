from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_webhook_channel_kind import CreateWebhookChannelKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_webhook_channel_headers import CreateWebhookChannelHeaders


T = TypeVar("T", bound="CreateWebhookChannel")


@_attrs_define
class CreateWebhookChannel:
    """
    Attributes:
        kind (CreateWebhookChannelKind):
        url (str): Where the signed POSTs go. https in production.
        label (str | Unset): A name for the channel; the host of the URL when omitted.
        headers (CreateWebhookChannelHeaders | Unset): Extra request headers to send, for your own auth.
    """

    kind: CreateWebhookChannelKind
    url: str
    label: str | Unset = UNSET
    headers: CreateWebhookChannelHeaders | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        url = self.url

        label = self.label

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

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
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_webhook_channel_headers import (
            CreateWebhookChannelHeaders,
        )

        d = dict(src_dict)
        kind = CreateWebhookChannelKind(d.pop("kind"))

        url = d.pop("url")

        label = d.pop("label", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: CreateWebhookChannelHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = CreateWebhookChannelHeaders.from_dict(_headers)

        create_webhook_channel = cls(
            kind=kind,
            url=url,
            label=label,
            headers=headers,
        )

        create_webhook_channel.additional_properties = d
        return create_webhook_channel

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
