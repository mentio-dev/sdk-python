from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_polling_item_platform import KeywordPollingItemPlatform

T = TypeVar("T", bound="KeywordPollingItem")


@_attrs_define
class KeywordPollingItem:
    """
    Attributes:
        platform (KeywordPollingItemPlatform): Platform: bluesky, hackernews, github, stackoverflow, devto, reddit, x,
            youtube, news, linkedin.
        last_polled_at (None | str): Newest poll of this platform for the term; null until the first one.
        empty_polls (int): Consecutive polls that found nothing new; the scheduler slows down as it grows.
    """

    platform: KeywordPollingItemPlatform
    last_polled_at: None | str
    empty_polls: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        last_polled_at: None | str
        last_polled_at = self.last_polled_at

        empty_polls = self.empty_polls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "lastPolledAt": last_polled_at,
                "emptyPolls": empty_polls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        platform = KeywordPollingItemPlatform(d.pop("platform"))

        def _parse_last_polled_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_polled_at = _parse_last_polled_at(d.pop("lastPolledAt"))

        empty_polls = d.pop("emptyPolls")

        keyword_polling_item = cls(
            platform=platform,
            last_polled_at=last_polled_at,
            empty_polls=empty_polls,
        )

        keyword_polling_item.additional_properties = d
        return keyword_polling_item

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
