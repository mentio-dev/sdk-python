from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFiltersBodySubreddits")


@_attrs_define
class UpdateFiltersBodySubreddits:
    """Reddit only; an omitted list is untouched.

    Attributes:
        only (list[str] | Unset): Replaces the allowlist; [] clears it.
        excluded (list[str] | Unset): Replaces the deny list; [] clears it.
    """

    only: list[str] | Unset = UNSET
    excluded: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        only: list[str] | Unset = UNSET
        if not isinstance(self.only, Unset):
            only = self.only

        excluded: list[str] | Unset = UNSET
        if not isinstance(self.excluded, Unset):
            excluded = self.excluded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if only is not UNSET:
            field_dict["only"] = only
        if excluded is not UNSET:
            field_dict["excluded"] = excluded

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        only = cast(list[str], d.pop("only", UNSET))

        excluded = cast(list[str], d.pop("excluded", UNSET))

        update_filters_body_subreddits = cls(
            only=only,
            excluded=excluded,
        )

        update_filters_body_subreddits.additional_properties = d
        return update_filters_body_subreddits

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
