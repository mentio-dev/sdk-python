from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MentionBatchResult")


@_attrs_define
class MentionBatchResult:
    """
    Attributes:
        updated (list[str]): The ids changed, in the order sent. A pending mention given only a status is not changed:
            it is in pending alone.
        not_found (list[str]): The ids this workspace has no mention by, in the order sent; nothing was done to them.
        pending (list[str]): Of the updated ids, those still waiting for the classifier: they took the labels and the
            assignee, but their status stays until they are scored. Empty unless the update set a status.
    """

    updated: list[str]
    not_found: list[str]
    pending: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated = self.updated

        not_found = self.not_found

        pending = self.pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updated": updated,
                "notFound": not_found,
                "pending": pending,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        updated = cast(list[str], d.pop("updated"))

        not_found = cast(list[str], d.pop("notFound"))

        pending = cast(list[str], d.pop("pending"))

        mention_batch_result = cls(
            updated=updated,
            not_found=not_found,
            pending=pending,
        )

        mention_batch_result.additional_properties = d
        return mention_batch_result

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
