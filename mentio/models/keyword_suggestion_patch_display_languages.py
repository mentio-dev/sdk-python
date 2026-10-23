from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_suggestion_patch_display_languages_excluded_item import (
    KeywordSuggestionPatchDisplayLanguagesExcludedItem,
)
from ..models.keyword_suggestion_patch_display_languages_only_item import (
    KeywordSuggestionPatchDisplayLanguagesOnlyItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordSuggestionPatchDisplayLanguages")


@_attrs_define
class KeywordSuggestionPatchDisplayLanguages:
    """By the language of the post (ISO 639-1); omitted: untouched.

    Attributes:
        only (list[KeywordSuggestionPatchDisplayLanguagesOnlyItem] | Unset): Replaces the list; [] clears it.
        excluded (list[KeywordSuggestionPatchDisplayLanguagesExcludedItem] | Unset): Replaces the list; [] clears it.
    """

    only: list[KeywordSuggestionPatchDisplayLanguagesOnlyItem] | Unset = UNSET
    excluded: list[KeywordSuggestionPatchDisplayLanguagesExcludedItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        only: list[str] | Unset = UNSET
        if not isinstance(self.only, Unset):
            only = []
            for only_item_data in self.only:
                only_item = only_item_data.value
                only.append(only_item)

        excluded: list[str] | Unset = UNSET
        if not isinstance(self.excluded, Unset):
            excluded = []
            for excluded_item_data in self.excluded:
                excluded_item = excluded_item_data.value
                excluded.append(excluded_item)

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
        _only = d.pop("only", UNSET)
        only: list[KeywordSuggestionPatchDisplayLanguagesOnlyItem] | Unset = UNSET
        if _only is not UNSET:
            only = []
            for only_item_data in _only:
                only_item = KeywordSuggestionPatchDisplayLanguagesOnlyItem(
                    only_item_data
                )

                only.append(only_item)

        _excluded = d.pop("excluded", UNSET)
        excluded: list[KeywordSuggestionPatchDisplayLanguagesExcludedItem] | Unset = (
            UNSET
        )
        if _excluded is not UNSET:
            excluded = []
            for excluded_item_data in _excluded:
                excluded_item = KeywordSuggestionPatchDisplayLanguagesExcludedItem(
                    excluded_item_data
                )

                excluded.append(excluded_item)

        keyword_suggestion_patch_display_languages = cls(
            only=only,
            excluded=excluded,
        )

        keyword_suggestion_patch_display_languages.additional_properties = d
        return keyword_suggestion_patch_display_languages

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
