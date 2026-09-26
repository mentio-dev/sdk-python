from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analytics_breakdown_data_item_person_type_0_platform import (
    AnalyticsBreakdownDataItemPersonType0Platform,
)

T = TypeVar("T", bound="AnalyticsBreakdownDataItemPersonType0")


@_attrs_define
class AnalyticsBreakdownDataItemPersonType0:
    """by=person only; null otherwise.

    Attributes:
        id (None | str): Person id (aut_...); null for posts ingested before people were linked.
        name (None | str): Display name as the platform shows it.
        platform (AnalyticsBreakdownDataItemPersonType0Platform): Platform: bluesky, hackernews, github, stackoverflow,
            devto, reddit, x, youtube, news, linkedin, tiktok.
        url (None | str): Profile URL.
        avatar_url (None | str): Avatar image URL, when the platform gave one.
        followers (int | None): From the audience profile; null when unknown.
    """

    id: None | str
    name: None | str
    platform: AnalyticsBreakdownDataItemPersonType0Platform
    url: None | str
    avatar_url: None | str
    followers: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        name: None | str
        name = self.name

        platform = self.platform.value

        url: None | str
        url = self.url

        avatar_url: None | str
        avatar_url = self.avatar_url

        followers: int | None
        followers = self.followers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "platform": platform,
                "url": url,
                "avatarUrl": avatar_url,
                "followers": followers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        platform = AnalyticsBreakdownDataItemPersonType0Platform(d.pop("platform"))

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        def _parse_avatar_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl"))

        def _parse_followers(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        followers = _parse_followers(d.pop("followers"))

        analytics_breakdown_data_item_person_type_0 = cls(
            id=id,
            name=name,
            platform=platform,
            url=url,
            avatar_url=avatar_url,
            followers=followers,
        )

        analytics_breakdown_data_item_person_type_0.additional_properties = d
        return analytics_breakdown_data_item_person_type_0

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
