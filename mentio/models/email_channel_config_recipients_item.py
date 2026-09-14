from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmailChannelConfigRecipientsItem")


@_attrs_define
class EmailChannelConfigRecipientsItem:
    """
    Attributes:
        email (str):
        confirmed_at (None | str): Null until the address confirmed through its link; unconfirmed addresses receive
            nothing.
    """

    email: str
    confirmed_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        confirmed_at: None | str
        confirmed_at = self.confirmed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "confirmedAt": confirmed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        def _parse_confirmed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        confirmed_at = _parse_confirmed_at(d.pop("confirmedAt"))

        email_channel_config_recipients_item = cls(
            email=email,
            confirmed_at=confirmed_at,
        )

        email_channel_config_recipients_item.additional_properties = d
        return email_channel_config_recipients_item

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
