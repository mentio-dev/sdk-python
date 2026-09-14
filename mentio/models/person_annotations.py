from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PersonAnnotations")


@_attrs_define
class PersonAnnotations:
    """What this workspace wrote about the person.

    Attributes:
        tags (list[str]):
        notes (str):
        muted (bool): Their posts stay out of the feed and every channel; ingest and billing are untouched.
    """

    tags: list[str]
    notes: str
    muted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags = self.tags

        notes = self.notes

        muted = self.muted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tags": tags,
                "notes": notes,
                "muted": muted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tags = cast(list[str], d.pop("tags"))

        notes = d.pop("notes")

        muted = d.pop("muted")

        person_annotations = cls(
            tags=tags,
            notes=notes,
            muted=muted,
        )

        person_annotations.additional_properties = d
        return person_annotations

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
