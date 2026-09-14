from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ShareOfVoiceDataItemPreviousType0")


@_attrs_define
class ShareOfVoiceDataItemPreviousType0:
    """The same keyword over the period right before the window; null unless compare=true.

    Attributes:
        matched (int): Matches of this keyword then.
    """

    matched: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matched = self.matched

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matched": matched,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        matched = d.pop("matched")

        share_of_voice_data_item_previous_type_0 = cls(
            matched=matched,
        )

        share_of_voice_data_item_previous_type_0.additional_properties = d
        return share_of_voice_data_item_previous_type_0

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
