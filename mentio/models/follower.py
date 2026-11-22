from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Follower")


@_attrs_define
class Follower:
    """
    Attributes:
        key (str): The follower's id on the platform.
        handle (None | str): Their handle, without the @.
        name (None | str): Display name.
        url (None | str): Their profile.
        avatar_url (None | str): Their profile picture, or null.
        bio (None | str): Their bio, when the platform gave it.
        followers (int | None): Their own follower count, when the platform gave it.
        verified (bool | None): Verified on the platform, when it said; null when unknown.
        followed_at (str): When Mentio first saw them follow (the poll time, not the platform's).
    """

    key: str
    handle: None | str
    name: None | str
    url: None | str
    avatar_url: None | str
    bio: None | str
    followers: int | None
    verified: bool | None
    followed_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        handle: None | str
        handle = self.handle

        name: None | str
        name = self.name

        url: None | str
        url = self.url

        avatar_url: None | str
        avatar_url = self.avatar_url

        bio: None | str
        bio = self.bio

        followers: int | None
        followers = self.followers

        verified: bool | None
        verified = self.verified

        followed_at = self.followed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "handle": handle,
                "name": name,
                "url": url,
                "avatarUrl": avatar_url,
                "bio": bio,
                "followers": followers,
                "verified": verified,
                "followedAt": followed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        def _parse_handle(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        handle = _parse_handle(d.pop("handle"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

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

        def _parse_bio(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bio = _parse_bio(d.pop("bio"))

        def _parse_followers(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        followers = _parse_followers(d.pop("followers"))

        def _parse_verified(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        verified = _parse_verified(d.pop("verified"))

        followed_at = d.pop("followedAt")

        follower = cls(
            key=key,
            handle=handle,
            name=name,
            url=url,
            avatar_url=avatar_url,
            bio=bio,
            followers=followers,
            verified=verified,
            followed_at=followed_at,
        )

        follower.additional_properties = d
        return follower

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
