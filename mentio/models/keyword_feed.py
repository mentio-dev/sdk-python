from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordFeed")


@_attrs_define
class KeywordFeed:
    """
    Attributes:
        url (str): The feed itself (after redirects): what is polled.
        title (None | str): The feed's own title, when it has one.
        connected_at (str): When this keyword started reading the feed: nothing published before it is a live mention.
    """

    url: str
    title: None | str
    connected_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        title: None | str
        title = self.title

        connected_at = self.connected_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "title": title,
                "connectedAt": connected_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        connected_at = d.pop("connectedAt")

        keyword_feed = cls(
            url=url,
            title=title,
            connected_at=connected_at,
        )

        keyword_feed.additional_properties = d
        return keyword_feed

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
