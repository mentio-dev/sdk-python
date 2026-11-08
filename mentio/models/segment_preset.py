from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.segment_preset_filter import SegmentPresetFilter


T = TypeVar("T", bound="SegmentPreset")


@_attrs_define
class SegmentPreset:
    """
    Attributes:
        key (str): Stable id of the preset (influencers, champions, ...).
        name (str): Suggested segment name.
        description (str): What the segment holds, in one sentence.
        filter_ (SegmentPresetFilter): The filter to save with POST /v1/segments.
    """

    key: str
    name: str
    description: str
    filter_: SegmentPresetFilter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        description = self.description

        filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "description": description,
                "filter": filter_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.segment_preset_filter import SegmentPresetFilter

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        description = d.pop("description")

        filter_ = SegmentPresetFilter.from_dict(d.pop("filter"))

        segment_preset = cls(
            key=key,
            name=name,
            description=description,
            filter_=filter_,
        )

        segment_preset.additional_properties = d
        return segment_preset

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
