from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_post_repository_type_0_event import (
    MentionPostRepositoryType0Event,
)

T = TypeVar("T", bound="MentionPostRepositoryType0")


@_attrs_define
class MentionPostRepositoryType0:
    """A GitHub repository event's facts, on a mention whose kind is repository; null on every other mention. The sentence
    is post.title.

        Attributes:
            name (str): The repository, owner/name.
            event (MentionPostRepositoryType0Event): What happened. new: it was created. traction: under 30 days old, it
                reached 10 stars. stars: it passed a star milestone. growth: it gained stars fast in a week. top: one of the
                most starred repositories naming the keyword, brought by a new keyword's look-back.
            stars (int): Its stars when the event was found.
            weekly_stars (int | None): Stars gained in the 7 days before the event; null when that week is not known yet.
    """

    name: str
    event: MentionPostRepositoryType0Event
    stars: int
    weekly_stars: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        event = self.event.value

        stars = self.stars

        weekly_stars: int | None
        weekly_stars = self.weekly_stars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "event": event,
                "stars": stars,
                "weeklyStars": weekly_stars,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        event = MentionPostRepositoryType0Event(d.pop("event"))

        stars = d.pop("stars")

        def _parse_weekly_stars(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        weekly_stars = _parse_weekly_stars(d.pop("weeklyStars"))

        mention_post_repository_type_0 = cls(
            name=name,
            event=event,
            stars=stars,
            weekly_stars=weekly_stars,
        )

        mention_post_repository_type_0.additional_properties = d
        return mention_post_repository_type_0

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
