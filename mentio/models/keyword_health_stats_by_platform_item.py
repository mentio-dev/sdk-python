from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_health_stats_by_platform_item_platform import (
    KeywordHealthStatsByPlatformItemPlatform,
)

T = TypeVar("T", bound="KeywordHealthStatsByPlatformItem")


@_attrs_define
class KeywordHealthStatsByPlatformItem:
    """
    Attributes:
        platform (KeywordHealthStatsByPlatformItemPlatform): Platform: bluesky, hackernews, github, stackoverflow,
            devto, reddit, x, youtube, news, linkedin, tiktok, instagram, appstore (App Store reviews), googleplay (Google
            Play reviews), trustpilot (Trustpilot reviews), googlemaps (Google reviews of a place), rss (RSS and Atom feeds
            a keyword reads).
        matches (int): Matches on this platform in the window.
        relevant (int): Of those, scored at or above the relevance line (40).
        filtered (int): Of those, scored under the line: the noise.
        noise_share (float | None): filtered / (relevant + filtered); null with nothing scored.
    """

    platform: KeywordHealthStatsByPlatformItemPlatform
    matches: int
    relevant: int
    filtered: int
    noise_share: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        matches = self.matches

        relevant = self.relevant

        filtered = self.filtered

        noise_share: float | None
        noise_share = self.noise_share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "matches": matches,
                "relevant": relevant,
                "filtered": filtered,
                "noiseShare": noise_share,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        platform = KeywordHealthStatsByPlatformItemPlatform(d.pop("platform"))

        matches = d.pop("matches")

        relevant = d.pop("relevant")

        filtered = d.pop("filtered")

        def _parse_noise_share(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        noise_share = _parse_noise_share(d.pop("noiseShare"))

        keyword_health_stats_by_platform_item = cls(
            platform=platform,
            matches=matches,
            relevant=relevant,
            filtered=filtered,
            noise_share=noise_share,
        )

        keyword_health_stats_by_platform_item.additional_properties = d
        return keyword_health_stats_by_platform_item

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
