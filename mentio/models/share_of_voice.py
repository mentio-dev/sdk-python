from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.share_of_voice_data_item import ShareOfVoiceDataItem
    from ..models.share_of_voice_window import ShareOfVoiceWindow


T = TypeVar("T", bound="ShareOfVoice")


@_attrs_define
class ShareOfVoice:
    """
    Attributes:
        window (ShareOfVoiceWindow): The window the report covers.
        data (list[ShareOfVoiceDataItem]): Every keyword matched in the window, most matched first.
    """

    window: ShareOfVoiceWindow
    data: list[ShareOfVoiceDataItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        window = self.window.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window": window,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.share_of_voice_data_item import (
            ShareOfVoiceDataItem,
        )
        from ..models.share_of_voice_window import ShareOfVoiceWindow

        d = dict(src_dict)
        window = ShareOfVoiceWindow.from_dict(d.pop("window"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ShareOfVoiceDataItem.from_dict(data_item_data)

            data.append(data_item)

        share_of_voice = cls(
            window=window,
            data=data,
        )

        share_of_voice.additional_properties = d
        return share_of_voice

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
