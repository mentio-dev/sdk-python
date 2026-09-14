from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_slack_channel_kind import CreateSlackChannelKind

T = TypeVar("T", bound="CreateSlackChannel")


@_attrs_define
class CreateSlackChannel:
    """
    Attributes:
        kind (CreateSlackChannelKind):
        channel_id (str): A Slack channel id from the connected workspace.
        channel_name (str): The channel name, for the label.
    """

    kind: CreateSlackChannelKind
    channel_id: str
    channel_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        channel_id = self.channel_id

        channel_name = self.channel_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "channelId": channel_id,
                "channelName": channel_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = CreateSlackChannelKind(d.pop("kind"))

        channel_id = d.pop("channelId")

        channel_name = d.pop("channelName")

        create_slack_channel = cls(
            kind=kind,
            channel_id=channel_id,
            channel_name=channel_name,
        )

        create_slack_channel.additional_properties = d
        return create_slack_channel

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
