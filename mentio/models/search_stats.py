from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SearchStats")


@_attrs_define
class SearchStats:
    """Counts across platforms.

    Attributes:
        results (int): Results stored.
        scored (int): Results scored (the rest wait or failed).
        relevant (int): Results scored relevant (40 or more).
    """

    results: int
    scored: int
    relevant: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = self.results

        scored = self.scored

        relevant = self.relevant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "scored": scored,
                "relevant": relevant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        results = d.pop("results")

        scored = d.pop("scored")

        relevant = d.pop("relevant")

        search_stats = cls(
            results=results,
            scored=scored,
            relevant=relevant,
        )

        search_stats.additional_properties = d
        return search_stats

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
