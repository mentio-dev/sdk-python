from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_keywords_response_200_data_item_display_countries import (
        ListKeywordsResponse200DataItemDisplayCountries,
    )
    from ..models.list_keywords_response_200_data_item_display_languages import (
        ListKeywordsResponse200DataItemDisplayLanguages,
    )


T = TypeVar("T", bound="ListKeywordsResponse200DataItemDisplay")


@_attrs_define
class ListKeywordsResponse200DataItemDisplay:
    """Which of this keyword's mentions you see, by language and country. Both are read by the classifier, so a hidden post
    is still matched, classified and billed like any other; it is kept out of the mentions list, the exports, MCP
    search, alerts and digests (includeHidden=true on GET /v1/mentions shows it). Read when the mentions are read, so
    changing a list applies to older mentions too.

        Attributes:
            languages (ListKeywordsResponse200DataItemDisplayLanguages): By the language the post is written in.
            countries (ListKeywordsResponse200DataItemDisplayCountries): By where the author is, as the classifier read
                their profile and the post.
    """

    languages: ListKeywordsResponse200DataItemDisplayLanguages
    countries: ListKeywordsResponse200DataItemDisplayCountries
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        languages = self.languages.to_dict()

        countries = self.countries.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "languages": languages,
                "countries": countries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_keywords_response_200_data_item_display_countries import (
            ListKeywordsResponse200DataItemDisplayCountries,
        )
        from ..models.list_keywords_response_200_data_item_display_languages import (
            ListKeywordsResponse200DataItemDisplayLanguages,
        )

        d = dict(src_dict)
        languages = ListKeywordsResponse200DataItemDisplayLanguages.from_dict(
            d.pop("languages")
        )

        countries = ListKeywordsResponse200DataItemDisplayCountries.from_dict(
            d.pop("countries")
        )

        list_keywords_response_200_data_item_display = cls(
            languages=languages,
            countries=countries,
        )

        list_keywords_response_200_data_item_display.additional_properties = d
        return list_keywords_response_200_data_item_display

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
