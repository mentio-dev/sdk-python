from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.email_channel_config_recipients_item import (
        EmailChannelConfigRecipientsItem,
    )


T = TypeVar("T", bound="EmailChannelConfig")


@_attrs_define
class EmailChannelConfig:
    """
    Attributes:
        recipients (list[EmailChannelConfigRecipientsItem]): Every address on the list and whether it confirmed.
    """

    recipients: list[EmailChannelConfigRecipientsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recipients = []
        for recipients_item_data in self.recipients:
            recipients_item = recipients_item_data.to_dict()
            recipients.append(recipients_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recipients": recipients,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.email_channel_config_recipients_item import (
            EmailChannelConfigRecipientsItem,
        )

        d = dict(src_dict)
        recipients = []
        _recipients = d.pop("recipients")
        for recipients_item_data in _recipients:
            recipients_item = EmailChannelConfigRecipientsItem.from_dict(
                recipients_item_data
            )

            recipients.append(recipients_item)

        email_channel_config = cls(
            recipients=recipients,
        )

        email_channel_config.additional_properties = d
        return email_channel_config

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
