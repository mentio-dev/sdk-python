from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkspaceFiltersSubreddits")


@_attrs_define
class WorkspaceFiltersSubreddits:
    """Reddit only.

    Attributes:
        only (list[str]): When non-empty, ONLY Reddit posts from these subreddits pass and `excluded` is ignored. r/name
            or name.
        excluded (list[str]): Reddit posts from these subreddits are dropped. r/name or name.
    """

    only: list[str]
    excluded: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        only = self.only

        excluded = self.excluded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "only": only,
                "excluded": excluded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        only = cast(list[str], d.pop("only"))

        excluded = cast(list[str], d.pop("excluded"))

        workspace_filters_subreddits = cls(
            only=only,
            excluded=excluded,
        )

        workspace_filters_subreddits.additional_properties = d
        return workspace_filters_subreddits

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
