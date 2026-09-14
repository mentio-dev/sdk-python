from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_alerts_response_200_data_item_channels_item_kind import (
    ListAlertsResponse200DataItemChannelsItemKind,
)

T = TypeVar("T", bound="ListAlertsResponse200DataItemChannelsItem")


@_attrs_define
class ListAlertsResponse200DataItemChannelsItem:
    """
    Attributes:
        id (str):
        kind (ListAlertsResponse200DataItemChannelsItemKind):
        label (str):
    """

    id: str
    kind: ListAlertsResponse200DataItemChannelsItemKind
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

        kind = ListAlertsResponse200DataItemChannelsItemKind(d.pop("kind"))

        label = d.pop("label")

        list_alerts_response_200_data_item_channels_item = cls(
            id=id,
            kind=kind,
            label=label,
        )

        list_alerts_response_200_data_item_channels_item.additional_properties = d
        return list_alerts_response_200_data_item_channels_item

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
