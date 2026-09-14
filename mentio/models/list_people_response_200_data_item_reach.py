from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListPeopleResponse200DataItemReach")


@_attrs_define
class ListPeopleResponse200DataItemReach:
    """Platform counts as of their newest post; null where the platform has no such number.

    Attributes:
        followers (int | None):
        following (int | None):
        posts (int | None):
    """

    followers: int | None
    following: int | None
    posts: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        followers: int | None
        followers = self.followers

        following: int | None
        following = self.following

        posts: int | None
        posts = self.posts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "followers": followers,
                "following": following,
                "posts": posts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_followers(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        followers = _parse_followers(d.pop("followers"))

        def _parse_following(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        following = _parse_following(d.pop("following"))

        def _parse_posts(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        posts = _parse_posts(d.pop("posts"))

        list_people_response_200_data_item_reach = cls(
            followers=followers,
            following=following,
            posts=posts,
        )

        list_people_response_200_data_item_reach.additional_properties = d
        return list_people_response_200_data_item_reach

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
