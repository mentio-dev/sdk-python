from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListKeywordsResponse200DataItemMatchingSubreddits")


@_attrs_define
class ListKeywordsResponse200DataItemMatchingSubreddits:
    """Reddit only, for this keyword alone; the workspace filters' own subreddit lists (GET /v1/filters) still apply to
    every keyword, and a post must pass both.

        Attributes:
            only (list[str]): When non-empty, this keyword takes Reddit posts from these subreddits ONLY and `excluded` is
                ignored. r/name or name, stored bare and lowercase.
            excluded (list[str]): Reddit posts from these subreddits are dropped for this keyword. r/name or name.
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

        list_keywords_response_200_data_item_matching_subreddits = cls(
            only=only,
            excluded=excluded,
        )

        list_keywords_response_200_data_item_matching_subreddits.additional_properties = d
        return list_keywords_response_200_data_item_matching_subreddits

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
