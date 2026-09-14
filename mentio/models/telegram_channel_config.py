from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.telegram_channel_config_chat_type import TelegramChannelConfigChatType

T = TypeVar("T", bound="TelegramChannelConfig")


@_attrs_define
class TelegramChannelConfig:
    """
    Attributes:
        chat_id (str): Telegram chat id.
        chat_type (TelegramChannelConfigChatType):
    """

    chat_id: str
    chat_type: TelegramChannelConfigChatType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        chat_type = self.chat_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "chatType": chat_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        chat_id = d.pop("chatId")

        chat_type = TelegramChannelConfigChatType(d.pop("chatType"))

        telegram_channel_config = cls(
            chat_id=chat_id,
            chat_type=chat_type,
        )

        telegram_channel_config.additional_properties = d
        return telegram_channel_config

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
