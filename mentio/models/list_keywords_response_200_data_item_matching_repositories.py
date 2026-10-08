from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_keywords_response_200_data_item_matching_repositories_events_item import (
    ListKeywordsResponse200DataItemMatchingRepositoriesEventsItem,
)

T = TypeVar("T", bound="ListKeywordsResponse200DataItemMatchingRepositories")


@_attrs_define
class ListKeywordsResponse200DataItemMatchingRepositories:
    """GitHub only: which repository events naming this keyword become mentions. An event outside the rule is dropped
    before it is stored, so it is never billed.

        Attributes:
            events (list[ListKeywordsResponse200DataItemMatchingRepositoriesEventsItem]): The repository events this keyword
                takes. traction: a repository created in the last 30 days reached 10 stars. stars: one with 100 stars or more
                passed a milestone (100, 250, 500, 1,000, 2,000, 5,000 ...). growth: it gained stars fast in a week. new: every
                repository created, even with no stars (off by default: nearly all of them are noise for a broad keyword).
                Default: traction, stars, growth. Empty: no repository events.
            min_stars (int | None): Only repositories with at least this many stars; null for no minimum.
            min_weekly_stars (int | None): Only repositories that gained at least this many stars in the last 7 days (25 or
                more). It applies to every event, and one whose last week is not known yet does not pass. null: a growth event
                needs 100 stars and 20% of the repository's stars in a week, the other events need no growth.
    """

    events: list[ListKeywordsResponse200DataItemMatchingRepositoriesEventsItem]
    min_stars: int | None
    min_weekly_stars: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        min_stars: int | None
        min_stars = self.min_stars

        min_weekly_stars: int | None
        min_weekly_stars = self.min_weekly_stars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "minStars": min_stars,
                "minWeeklyStars": min_weekly_stars,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = ListKeywordsResponse200DataItemMatchingRepositoriesEventsItem(
                events_item_data
            )

            events.append(events_item)

        def _parse_min_stars(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_stars = _parse_min_stars(d.pop("minStars"))

        def _parse_min_weekly_stars(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        min_weekly_stars = _parse_min_weekly_stars(d.pop("minWeeklyStars"))

        list_keywords_response_200_data_item_matching_repositories = cls(
            events=events,
            min_stars=min_stars,
            min_weekly_stars=min_weekly_stars,
        )

        list_keywords_response_200_data_item_matching_repositories.additional_properties = d
        return list_keywords_response_200_data_item_matching_repositories

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
