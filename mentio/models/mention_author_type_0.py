from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MentionAuthorType0")


@_attrs_define
class MentionAuthorType0:
    """Who posted it; null when the platform gave no author at all.

    Attributes:
        id (None | str): Person id (aut_...) for GET /v1/people/{id}; null when the account is not in the audience yet.
        name (None | str): Display name as the platform reports it.
        handle (None | str): Platform handle derived from the profile URL, formatted as the platform shows it (@name,
            u/name); null where the platform has none.
        url (None | str): Profile URL.
        avatar_url (None | str): Profile picture; null where the platform has none.
        followers (int | None): Follower count as of their newest post; null where the platform has none.
        tags (list[str]): Your workspace tags on this person.
    """

    id: None | str
    name: None | str
    handle: None | str
    url: None | str
    avatar_url: None | str
    followers: int | None
    tags: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        name: None | str
        name = self.name

        handle: None | str
        handle = self.handle

        url: None | str
        url = self.url

        avatar_url: None | str
        avatar_url = self.avatar_url

        followers: int | None
        followers = self.followers

        tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "handle": handle,
                "url": url,
                "avatarUrl": avatar_url,
                "followers": followers,
                "tags": tags,
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

        def _parse_handle(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        handle = _parse_handle(d.pop("handle"))

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

        tags = cast(list[str], d.pop("tags"))

        mention_author_type_0 = cls(
            id=id,
            name=name,
            handle=handle,
            url=url,
            avatar_url=avatar_url,
            followers=followers,
            tags=tags,
        )

        mention_author_type_0.additional_properties = d
        return mention_author_type_0

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
