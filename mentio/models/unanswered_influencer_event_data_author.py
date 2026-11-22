from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.unanswered_influencer_event_data_author_platform import (
    UnansweredInfluencerEventDataAuthorPlatform,
)

T = TypeVar("T", bound="UnansweredInfluencerEventDataAuthor")


@_attrs_define
class UnansweredInfluencerEventDataAuthor:
    """Who posted.

    Attributes:
        id (str): The person (aut_...): GET /v1/people/{id}.
        name (None | str): Their name on the platform.
        url (None | str): Their profile.
        platform (UnansweredInfluencerEventDataAuthorPlatform): Where they posted.
        followers (int): Followers when they last posted.
        influence (int): 0 to 100, from followers (100 at 100,000 or more).
    """

    id: str
    name: None | str
    url: None | str
    platform: UnansweredInfluencerEventDataAuthorPlatform
    followers: int
    influence: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        url: None | str
        url = self.url

        platform = self.platform.value

        followers = self.followers

        influence = self.influence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "url": url,
                "platform": platform,
                "followers": followers,
                "influence": influence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

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

        platform = UnansweredInfluencerEventDataAuthorPlatform(d.pop("platform"))

        followers = d.pop("followers")

        influence = d.pop("influence")

        unanswered_influencer_event_data_author = cls(
            id=id,
            name=name,
            url=url,
            platform=platform,
            followers=followers,
            influence=influence,
        )

        unanswered_influencer_event_data_author.additional_properties = d
        return unanswered_influencer_event_data_author

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
