from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_display_languages_excluded_item import (
    KeywordDisplayLanguagesExcludedItem,
)
from ..models.keyword_display_languages_only_item import KeywordDisplayLanguagesOnlyItem

T = TypeVar("T", bound="KeywordDisplayLanguages")


@_attrs_define
class KeywordDisplayLanguages:
    """By the language the post is written in.

    Attributes:
        only (list[KeywordDisplayLanguagesOnlyItem]): When non-empty, a post whose language (ISO 639-1) is known and not
            listed is hidden, a language (ISO 639-1) the classifier recognises but does not name included. A post whose
            language (ISO 639-1) nobody could tell is always shown.
        excluded (list[KeywordDisplayLanguagesExcludedItem]): A post whose language (ISO 639-1) is listed is hidden.
    """

    only: list[KeywordDisplayLanguagesOnlyItem]
    excluded: list[KeywordDisplayLanguagesExcludedItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        only = []
        for only_item_data in self.only:
            only_item = only_item_data.value
            only.append(only_item)

        excluded = []
        for excluded_item_data in self.excluded:
            excluded_item = excluded_item_data.value
            excluded.append(excluded_item)

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
        only = []
        _only = d.pop("only")
        for only_item_data in _only:
            only_item = KeywordDisplayLanguagesOnlyItem(only_item_data)

            only.append(only_item)

        excluded = []
        _excluded = d.pop("excluded")
        for excluded_item_data in _excluded:
            excluded_item = KeywordDisplayLanguagesExcludedItem(excluded_item_data)

            excluded.append(excluded_item)

        keyword_display_languages = cls(
            only=only,
            excluded=excluded,
        )

        keyword_display_languages.additional_properties = d
        return keyword_display_languages

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
