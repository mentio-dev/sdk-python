from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_failing_event_data_channel_kind import (
    ChannelFailingEventDataChannelKind,
)

T = TypeVar("T", bound="ChannelFailingEventDataChannel")


@_attrs_define
class ChannelFailingEventDataChannel:
    """The channel whose sends fail.

    Attributes:
        id (str): Channel id (dest_...).
        kind (ChannelFailingEventDataChannelKind): slack, email, webhook or telegram.
        label (str): The channel's label.
    """

    id: str
    kind: ChannelFailingEventDataChannelKind
    label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        kind = ChannelFailingEventDataChannelKind(d.pop("kind"))

        label = d.pop("label")

        channel_failing_event_data_channel = cls(
            id=id,
            kind=kind,
            label=label,
        )

        channel_failing_event_data_channel.additional_properties = d
        return channel_failing_event_data_channel

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
