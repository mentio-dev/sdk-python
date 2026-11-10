from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_platforms_item_platform import SearchPlatformsItemPlatform
from ..models.search_platforms_item_reason import SearchPlatformsItemReason
from ..models.search_platforms_item_status import SearchPlatformsItemStatus

T = TypeVar("T", bound="SearchPlatformsItem")


@_attrs_define
class SearchPlatformsItem:
    """
    Attributes:
        platform (SearchPlatformsItemPlatform): Platform: bluesky, hackernews, github, stackoverflow, devto, reddit, x,
            youtube, news, linkedin, tiktok, instagram, facebook, appstore (App Store reviews), googleplay (Google Play
            reviews), trustpilot (Trustpilot reviews), googlemaps (Google reviews of a place), rss (RSS and Atom feeds a
            keyword reads).
        status (SearchPlatformsItemStatus): queued: not read yet. running: being read or scored. done: read and scored.
            skipped: not read (see reason). failed: the read failed (see reason).
        reason (SearchPlatformsItemReason): Why a platform was skipped or failed: unsupported (no term search on it),
            credentials (not connected on this deployment), budget (its monthly vendor budget is spent), rate_limited,
            error, timeout. null otherwise.
        results (int): Results stored for this platform, at most 25.
        relevant (int): Of them, scored relevant (40 or more).
    """

    platform: SearchPlatformsItemPlatform
    status: SearchPlatformsItemStatus
    reason: SearchPlatformsItemReason
    results: int
    relevant: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        status = self.status.value

        reason = self.reason.value

        results = self.results

        relevant = self.relevant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "status": status,
                "reason": reason,
                "results": results,
                "relevant": relevant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        platform = SearchPlatformsItemPlatform(d.pop("platform"))

        status = SearchPlatformsItemStatus(d.pop("status"))

        reason = SearchPlatformsItemReason(d.pop("reason"))

        results = d.pop("results")

        relevant = d.pop("relevant")

        search_platforms_item = cls(
            platform=platform,
            status=status,
            reason=reason,
            results=results,
            relevant=relevant,
        )

        search_platforms_item.additional_properties = d
        return search_platforms_item

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
