from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_suggestion_patch_review_sources_item_platform import (
    KeywordSuggestionPatchReviewSourcesItemPlatform,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordSuggestionPatchReviewSourcesItem")


@_attrs_define
class KeywordSuggestionPatchReviewSourcesItem:
    """A review page whose reviews become this keyword's mentions: its link, or the platform and the id.

    Attributes:
        url (str | Unset): The review page's link: an App Store or Google Play app
            (https://apps.apple.com/us/app/notion/id1232780281, https://play.google.com/store/apps/details?id=notion.id), a
            Trustpilot page (https://www.trustpilot.com/review/notion.so) or a Google Maps place (its full link, or a
            maps.app.goo.gl share link). Or give platform and id.
        platform (KeywordSuggestionPatchReviewSourcesItemPlatform | Unset): appstore (Apple App Store), googleplay
            (Google Play), trustpilot (a company's Trustpilot page) or googlemaps (a place's Google reviews).
        id (str | Unset): The id on the platform: the digits after "id" on the App Store, the package name on Google
            Play, the company's domain on Trustpilot (notion.so), a Place ID (ChIJ...) on Google Maps.
        countries (list[str] | Unset): App Store and Google Play only: storefronts to read, two-letter codes, at most
            20. Default: the one in the link, else us. Each is one more poll a day; the same review seen in two storefronts
            is one mention. Trustpilot and Google Maps have one page for everyone and take none.
        language (str | Unset): Google Play only: the language of the reviews to read (en, es, de, pt-BR); Google Play
            answers one language at a time. Default: the link's hl, else en.
    """

    url: str | Unset = UNSET
    platform: KeywordSuggestionPatchReviewSourcesItemPlatform | Unset = UNSET
    id: str | Unset = UNSET
    countries: list[str] | Unset = UNSET
    language: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        id = self.id

        countries: list[str] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if platform is not UNSET:
            field_dict["platform"] = platform
        if id is not UNSET:
            field_dict["id"] = id
        if countries is not UNSET:
            field_dict["countries"] = countries
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: KeywordSuggestionPatchReviewSourcesItemPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = KeywordSuggestionPatchReviewSourcesItemPlatform(_platform)

        id = d.pop("id", UNSET)

        countries = cast(list[str], d.pop("countries", UNSET))

        language = d.pop("language", UNSET)

        keyword_suggestion_patch_review_sources_item = cls(
            url=url,
            platform=platform,
            id=id,
            countries=countries,
            language=language,
        )

        keyword_suggestion_patch_review_sources_item.additional_properties = d
        return keyword_suggestion_patch_review_sources_item

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
