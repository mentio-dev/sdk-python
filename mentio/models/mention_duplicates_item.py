from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_duplicates_item_platform import MentionDuplicatesItemPlatform

T = TypeVar("T", bound="MentionDuplicatesItem")


@_attrs_define
class MentionDuplicatesItem:
    """
    Attributes:
        id (str): The copy's mention id (mm_...).
        platform (MentionDuplicatesItemPlatform): Platform: bluesky, hackernews, github, stackoverflow, devto, reddit,
            x, youtube, news, linkedin, tiktok, instagram, appstore (App Store reviews), googleplay (Google Play reviews),
            trustpilot (Trustpilot reviews), googlemaps (Google reviews of a place), rss (RSS and Atom feeds a keyword
            reads).
        url (str): Link to the copy.
        published_at (str): When the copy was published.
    """

    id: str
    platform: MentionDuplicatesItemPlatform
    url: str
    published_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        platform = self.platform.value

        url = self.url

        published_at = self.published_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "platform": platform,
                "url": url,
                "publishedAt": published_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        platform = MentionDuplicatesItemPlatform(d.pop("platform"))

        url = d.pop("url")

        published_at = d.pop("publishedAt")

        mention_duplicates_item = cls(
            id=id,
            platform=platform,
            url=url,
            published_at=published_at,
        )

        mention_duplicates_item.additional_properties = d
        return mention_duplicates_item

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
