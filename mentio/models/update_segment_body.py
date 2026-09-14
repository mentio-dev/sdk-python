from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_segment_body_filter import UpdateSegmentBodyFilter


T = TypeVar("T", bound="UpdateSegmentBody")


@_attrs_define
class UpdateSegmentBody:
    """Omitted fields are untouched.

    Attributes:
        name (str | Unset):
        description (str | Unset):
        filter_ (UpdateSegmentBodyFilter | Unset): Replaces the whole filter.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    filter_: UpdateSegmentBodyFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_segment_body_filter import (
            UpdateSegmentBodyFilter,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: UpdateSegmentBodyFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = UpdateSegmentBodyFilter.from_dict(_filter_)

        update_segment_body = cls(
            name=name,
            description=description,
            filter_=filter_,
        )

        update_segment_body.additional_properties = d
        return update_segment_body

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
