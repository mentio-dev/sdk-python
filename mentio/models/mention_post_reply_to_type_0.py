from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MentionPostReplyToType0")


@_attrs_define
class MentionPostReplyToType0:
    """The post this one replies to (X, Bluesky); null for top-level posts.

    Attributes:
        author (None | str): Parent post author as the platform names them.
        url (None | str): Parent post URL.
        text (None | str): Parent post text, when the platform gave it.
    """

    author: None | str
    url: None | str
    text: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author: None | str
        author = self.author

        url: None | str
        url = self.url

        text: None | str
        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author": author,
                "url": url,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_author(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        author = _parse_author(d.pop("author"))

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        def _parse_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text = _parse_text(d.pop("text"))

        mention_post_reply_to_type_0 = cls(
            author=author,
            url=url,
            text=text,
        )

        mention_post_reply_to_type_0.additional_properties = d
        return mention_post_reply_to_type_0

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
