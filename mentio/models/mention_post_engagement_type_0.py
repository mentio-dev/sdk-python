from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MentionPostEngagementType0")


@_attrs_define
class MentionPostEngagementType0:
    """Engagement counts as the platform reported them when the post was ingested, usually minutes after it was written; a
    count the platform does not have is null. Null as a whole for platforms that report none and for posts ingested
    before September 2026. X carries all six.

        Attributes:
            likes (int | None):
            reposts (int | None):
            replies (int | None):
            quotes (int | None):
            views (int | None):
            bookmarks (int | None):
    """

    likes: int | None
    reposts: int | None
    replies: int | None
    quotes: int | None
    views: int | None
    bookmarks: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        likes: int | None
        likes = self.likes

        reposts: int | None
        reposts = self.reposts

        replies: int | None
        replies = self.replies

        quotes: int | None
        quotes = self.quotes

        views: int | None
        views = self.views

        bookmarks: int | None
        bookmarks = self.bookmarks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "likes": likes,
                "reposts": reposts,
                "replies": replies,
                "quotes": quotes,
                "views": views,
                "bookmarks": bookmarks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_likes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        likes = _parse_likes(d.pop("likes"))

        def _parse_reposts(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        reposts = _parse_reposts(d.pop("reposts"))

        def _parse_replies(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        replies = _parse_replies(d.pop("replies"))

        def _parse_quotes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        quotes = _parse_quotes(d.pop("quotes"))

        def _parse_views(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        views = _parse_views(d.pop("views"))

        def _parse_bookmarks(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        bookmarks = _parse_bookmarks(d.pop("bookmarks"))

        mention_post_engagement_type_0 = cls(
            likes=likes,
            reposts=reposts,
            replies=replies,
            quotes=quotes,
            views=views,
            bookmarks=bookmarks,
        )

        mention_post_engagement_type_0.additional_properties = d
        return mention_post_engagement_type_0

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
