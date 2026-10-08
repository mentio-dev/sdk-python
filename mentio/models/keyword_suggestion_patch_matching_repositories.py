from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_suggestion_patch_matching_repositories_events_item import (
    KeywordSuggestionPatchMatchingRepositoriesEventsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordSuggestionPatchMatchingRepositories")


@_attrs_define
class KeywordSuggestionPatchMatchingRepositories:
    """GitHub only: each field is replaced when sent, kept when omitted; null clears a minimum.

    Attributes:
        events (list[KeywordSuggestionPatchMatchingRepositoriesEventsItem] | Unset): The repository events this keyword
            takes. traction: a repository created in the last 30 days reached 10 stars. stars: one with 100 stars or more
            passed a milestone (100, 250, 500, 1,000, 2,000, 5,000 ...). growth: it gained stars fast in a week. new: every
            repository created, even with no stars (off by default: nearly all of them are noise for a broad keyword).
            Default: traction, stars, growth. Empty: no repository events.
        min_stars (int | None | Unset): Only repositories with at least this many stars; null for no minimum.
        min_weekly_stars (int | None | Unset): Only repositories that gained at least this many stars in the last 7 days
            (25 or more). It applies to every event, and one whose last week is not known yet does not pass. null: a growth
            event needs 100 stars and 20% of the repository's stars in a week, the other events need no growth.
    """

    events: list[KeywordSuggestionPatchMatchingRepositoriesEventsItem] | Unset = UNSET
    min_stars: int | None | Unset = UNSET
    min_weekly_stars: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        min_stars: int | None | Unset
        if isinstance(self.min_stars, Unset):
            min_stars = UNSET
        else:
            min_stars = self.min_stars

        min_weekly_stars: int | None | Unset
        if isinstance(self.min_weekly_stars, Unset):
            min_weekly_stars = UNSET
        else:
            min_weekly_stars = self.min_weekly_stars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if min_stars is not UNSET:
            field_dict["minStars"] = min_stars
        if min_weekly_stars is not UNSET:
            field_dict["minWeeklyStars"] = min_weekly_stars

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _events = d.pop("events", UNSET)
        events: list[KeywordSuggestionPatchMatchingRepositoriesEventsItem] | Unset = (
            UNSET
        )
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = KeywordSuggestionPatchMatchingRepositoriesEventsItem(
                    events_item_data
                )

                events.append(events_item)

        def _parse_min_stars(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_stars = _parse_min_stars(d.pop("minStars", UNSET))

        def _parse_min_weekly_stars(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_weekly_stars = _parse_min_weekly_stars(d.pop("minWeeklyStars", UNSET))

        keyword_suggestion_patch_matching_repositories = cls(
            events=events,
            min_stars=min_stars,
            min_weekly_stars=min_weekly_stars,
        )

        keyword_suggestion_patch_matching_repositories.additional_properties = d
        return keyword_suggestion_patch_matching_repositories

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
