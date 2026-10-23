from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_keyword_body_display_countries import (
        UpdateKeywordBodyDisplayCountries,
    )
    from ..models.update_keyword_body_display_languages import (
        UpdateKeywordBodyDisplayLanguages,
    )


T = TypeVar("T", bound="UpdateKeywordBodyDisplay")


@_attrs_define
class UpdateKeywordBodyDisplay:
    """Which of this keyword's mentions you see, by language and country; each list is replaced when sent, kept when
    omitted. Hidden mentions are still billed.

        Attributes:
            languages (UpdateKeywordBodyDisplayLanguages | Unset): By the language of the post (ISO 639-1); omitted:
                untouched.
            countries (UpdateKeywordBodyDisplayCountries | Unset): By where the author is (ISO 3166-1 alpha-2); omitted:
                untouched.
    """

    languages: UpdateKeywordBodyDisplayLanguages | Unset = UNSET
    countries: UpdateKeywordBodyDisplayCountries | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        languages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.languages, Unset):
            languages = self.languages.to_dict()

        countries: dict[str, Any] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if languages is not UNSET:
            field_dict["languages"] = languages
        if countries is not UNSET:
            field_dict["countries"] = countries

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_keyword_body_display_countries import (
            UpdateKeywordBodyDisplayCountries,
        )
        from ..models.update_keyword_body_display_languages import (
            UpdateKeywordBodyDisplayLanguages,
        )

        d = dict(src_dict)
        _languages = d.pop("languages", UNSET)
        languages: UpdateKeywordBodyDisplayLanguages | Unset
        if isinstance(_languages, Unset):
            languages = UNSET
        else:
            languages = UpdateKeywordBodyDisplayLanguages.from_dict(_languages)

        _countries = d.pop("countries", UNSET)
        countries: UpdateKeywordBodyDisplayCountries | Unset
        if isinstance(_countries, Unset):
            countries = UNSET
        else:
            countries = UpdateKeywordBodyDisplayCountries.from_dict(_countries)

        update_keyword_body_display = cls(
            languages=languages,
            countries=countries,
        )

        update_keyword_body_display.additional_properties = d
        return update_keyword_body_display

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
