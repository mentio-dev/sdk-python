from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.discord_channel import DiscordChannel
    from ..models.email_channel import EmailChannel
    from ..models.slack_channel import SlackChannel
    from ..models.teams_channel import TeamsChannel
    from ..models.telegram_channel import TelegramChannel
    from ..models.webhook_channel import WebhookChannel


T = TypeVar("T", bound="ListChannelsResponse200")


@_attrs_define
class ListChannelsResponse200:
    """
    Attributes:
        data (list[DiscordChannel | EmailChannel | SlackChannel | TeamsChannel | TelegramChannel | WebhookChannel]):
            Every channel of the workspace.
    """

    data: list[
        DiscordChannel
        | EmailChannel
        | SlackChannel
        | TeamsChannel
        | TelegramChannel
        | WebhookChannel
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.discord_channel import DiscordChannel
        from ..models.email_channel import EmailChannel
        from ..models.slack_channel import SlackChannel
        from ..models.telegram_channel import TelegramChannel
        from ..models.webhook_channel import WebhookChannel

        data = []
        for data_item_data in self.data:
            data_item: dict[str, Any]
            if (
                isinstance(data_item_data, SlackChannel)
                or isinstance(data_item_data, EmailChannel)
                or isinstance(data_item_data, WebhookChannel)
                or isinstance(data_item_data, TelegramChannel)
                or isinstance(data_item_data, DiscordChannel)
            ):
                data_item = data_item_data.to_dict()
            else:
                data_item = data_item_data.to_dict()

            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.discord_channel import DiscordChannel
        from ..models.email_channel import EmailChannel
        from ..models.slack_channel import SlackChannel
        from ..models.teams_channel import TeamsChannel
        from ..models.telegram_channel import TelegramChannel
        from ..models.webhook_channel import WebhookChannel

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:

            def _parse_data_item(
                data: object,
            ) -> (
                DiscordChannel
                | EmailChannel
                | SlackChannel
                | TeamsChannel
                | TelegramChannel
                | WebhookChannel
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_0 = SlackChannel.from_dict(data)

                    return data_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = EmailChannel.from_dict(data)

                    return data_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_2 = WebhookChannel.from_dict(data)

                    return data_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_3 = TelegramChannel.from_dict(data)

                    return data_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_4 = DiscordChannel.from_dict(data)

                    return data_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                data_item_type_5 = TeamsChannel.from_dict(data)

                return data_item_type_5

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)

        list_channels_response_200 = cls(
            data=data,
        )

        list_channels_response_200.additional_properties = d
        return list_channels_response_200

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
