from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_keyword_body_review_sources_item_platform import (
    UpdateKeywordBodyReviewSourcesItemPlatform,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateKeywordBodyReviewSourcesItem")


@_attrs_define
class UpdateKeywordBodyReviewSourcesItem:
    """An app whose reviews become this keyword's mentions: a store link, or the platform and the app id.

    Attributes:
        url (str | Unset): The app's store link: https://apps.apple.com/us/app/notion/id1232780281 or
            https://play.google.com/store/apps/details?id=notion.id. Or give platform and id.
        platform (UpdateKeywordBodyReviewSourcesItemPlatform | Unset): appstore (Apple App Store) or googleplay (Google
            Play).
        id (str | Unset): The store's app id: the digits after "id" on the App Store, the package name on Google Play.
        countries (list[str] | Unset): Storefronts to read, two-letter codes, at most 20. Default: the one in the link,
            else us. Each is one more poll a day; the same review seen in two storefronts is one mention.
        language (str | Unset): Google Play only: the language of the reviews to read (en, es, de, pt-BR); Google Play
            answers one language at a time. Default: the link's hl, else en.
    """

    url: str | Unset = UNSET
    platform: UpdateKeywordBodyReviewSourcesItemPlatform | Unset = UNSET
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
        platform: UpdateKeywordBodyReviewSourcesItemPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = UpdateKeywordBodyReviewSourcesItemPlatform(_platform)

        id = d.pop("id", UNSET)

        countries = cast(list[str], d.pop("countries", UNSET))

        language = d.pop("language", UNSET)

        update_keyword_body_review_sources_item = cls(
            url=url,
            platform=platform,
            id=id,
            countries=countries,
            language=language,
        )

        update_keyword_body_review_sources_item.additional_properties = d
        return update_keyword_body_review_sources_item

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
