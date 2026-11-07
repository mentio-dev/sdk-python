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
    """Which of this keyword's mentions you see, by language and country. A hidden post is still matched, classified and
    billed, but kept out of lists, exports, search, alerts and digests (includeHidden=true shows it). See
    [Keywords](/guides/keywords#show-only-some-languages-or-countries).

        Attributes:
            languages (ListKeywordsResponse200DataItemDisplayLanguages): By the language the post is written in (ISO 639-1).
            countries (ListKeywordsResponse200DataItemDisplayCountries): By where the author is (ISO 3166-1 alpha-2), as the
                classifier read their profile and the post.
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
