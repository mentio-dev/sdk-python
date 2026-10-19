from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FeedStats")


@_attrs_define
class FeedStats:
    """How the hourly poll of this feed is going.

    Attributes:
        last_polled_at (None | str): When the feed was last read; null until its first poll (within the hour).
        empty_polls (int): Polls in a row that brought nothing new; a feed that keeps reading empty may have moved.
    """

    last_polled_at: None | str
    empty_polls: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_polled_at: None | str
        last_polled_at = self.last_polled_at

        empty_polls = self.empty_polls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastPolledAt": last_polled_at,
                "emptyPolls": empty_polls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_last_polled_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_polled_at = _parse_last_polled_at(d.pop("lastPolledAt"))

        empty_polls = d.pop("emptyPolls")

        feed_stats = cls(
            last_polled_at=last_polled_at,
            empty_polls=empty_polls,
        )

        feed_stats.additional_properties = d
        return feed_stats

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
