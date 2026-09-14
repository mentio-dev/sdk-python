from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_people_response_200_data_item_stats_sentiment import (
        ListPeopleResponse200DataItemStatsSentiment,
    )


T = TypeVar("T", bound="ListPeopleResponse200DataItemStats")


@_attrs_define
class ListPeopleResponse200DataItemStats:
    """Computed over this workspace's matches.

    Attributes:
        mentions (int): Every match of theirs for this workspace, relevant or not.
        relevant (int): Of those, scored relevant.
        sentiment (ListPeopleResponse200DataItemStatsSentiment):
        first_seen_at (str): Their oldest matched post.
        last_seen_at (str): Their newest matched post.
    """

    mentions: int
    relevant: int
    sentiment: ListPeopleResponse200DataItemStatsSentiment
    first_seen_at: str
    last_seen_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mentions = self.mentions

        relevant = self.relevant

        sentiment = self.sentiment.to_dict()

        first_seen_at = self.first_seen_at

        last_seen_at = self.last_seen_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mentions": mentions,
                "relevant": relevant,
                "sentiment": sentiment,
                "firstSeenAt": first_seen_at,
                "lastSeenAt": last_seen_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_people_response_200_data_item_stats_sentiment import (
            ListPeopleResponse200DataItemStatsSentiment,
        )

        d = dict(src_dict)
        mentions = d.pop("mentions")

        relevant = d.pop("relevant")

        sentiment = ListPeopleResponse200DataItemStatsSentiment.from_dict(
            d.pop("sentiment")
        )

        first_seen_at = d.pop("firstSeenAt")

        last_seen_at = d.pop("lastSeenAt")

        list_people_response_200_data_item_stats = cls(
            mentions=mentions,
            relevant=relevant,
            sentiment=sentiment,
            first_seen_at=first_seen_at,
            last_seen_at=last_seen_at,
        )

        list_people_response_200_data_item_stats.additional_properties = d
        return list_people_response_200_data_item_stats

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
