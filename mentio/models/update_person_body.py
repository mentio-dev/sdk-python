from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_person_body_stage import UpdatePersonBodyStage
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePersonBody")


@_attrs_define
class UpdatePersonBody:
    """Omitted fields are untouched.

    Attributes:
        tags (list[str] | Unset): Replaces the whole list.
        notes (str | Unset):
        muted (bool | Unset):
        owner_id (None | str | Unset): The member who owns the contact (user id); null clears.
        stage (UpdatePersonBodyStage | Unset): Where your workspace stands with the person: not_contacted, contacted,
            replied, in_talks, customer or not_a_fit.
    """

    tags: list[str] | Unset = UNSET
    notes: str | Unset = UNSET
    muted: bool | Unset = UNSET
    owner_id: None | str | Unset = UNSET
    stage: UpdatePersonBodyStage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        notes = self.notes

        muted = self.muted

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        stage: str | Unset = UNSET
        if not isinstance(self.stage, Unset):
            stage = self.stage.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if notes is not UNSET:
            field_dict["notes"] = notes
        if muted is not UNSET:
            field_dict["muted"] = muted
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if stage is not UNSET:
            field_dict["stage"] = stage

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tags = cast(list[str], d.pop("tags", UNSET))

        notes = d.pop("notes", UNSET)

        muted = d.pop("muted", UNSET)

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("ownerId", UNSET))

        _stage = d.pop("stage", UNSET)
        stage: UpdatePersonBodyStage | Unset
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = UpdatePersonBodyStage(_stage)

        update_person_body = cls(
            tags=tags,
            notes=notes,
            muted=muted,
            owner_id=owner_id,
            stage=stage,
        )

        update_person_body.additional_properties = d
        return update_person_body

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
