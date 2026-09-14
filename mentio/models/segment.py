from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.segment_filter import SegmentFilter


T = TypeVar("T", bound="Segment")


@_attrs_define
class Segment:
    """
    Attributes:
        id (str): Segment id (seg_...).
        name (str):
        description (str):
        filter_ (SegmentFilter):
        count (int): People in the segment right now; it is evaluated on every read.
        created_at (str): ISO 8601 timestamp, UTC.
        updated_at (str): ISO 8601 timestamp, UTC.
    """

    id: str
    name: str
    description: str
    filter_: SegmentFilter
    count: int
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        filter_ = self.filter_.to_dict()

        count = self.count

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "filter": filter_,
                "count": count,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.segment_filter import SegmentFilter

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        filter_ = SegmentFilter.from_dict(d.pop("filter"))

        count = d.pop("count")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        segment = cls(
            id=id,
            name=name,
            description=description,
            filter_=filter_,
            count=count,
            created_at=created_at,
            updated_at=updated_at,
        )

        segment.additional_properties = d
        return segment

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
