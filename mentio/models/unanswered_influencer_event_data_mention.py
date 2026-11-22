from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UnansweredInfluencerEventDataMention")


@_attrs_define
class UnansweredInfluencerEventDataMention:
    """The newest open mention, the one to answer first.

    Attributes:
        id (str): The newest of them (mm_...): GET /v1/mentions/{id}.
        url (str): The post.
        relevance (int): Its relevance score.
        published_at (str): When it was posted.
        matched_at (str): When Mentio matched it.
    """

    id: str
    url: str
    relevance: int
    published_at: str
    matched_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        relevance = self.relevance

        published_at = self.published_at

        matched_at = self.matched_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "relevance": relevance,
                "publishedAt": published_at,
                "matchedAt": matched_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        relevance = d.pop("relevance")

        published_at = d.pop("publishedAt")

        matched_at = d.pop("matchedAt")

        unanswered_influencer_event_data_mention = cls(
            id=id,
            url=url,
            relevance=relevance,
            published_at=published_at,
            matched_at=matched_at,
        )

        unanswered_influencer_event_data_mention.additional_properties = d
        return unanswered_influencer_event_data_mention

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
