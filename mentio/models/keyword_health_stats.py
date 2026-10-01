from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.keyword_health_stats_by_platform_item import (
        KeywordHealthStatsByPlatformItem,
    )
    from ..models.keyword_health_stats_cost import KeywordHealthStatsCost
    from ..models.keyword_health_stats_weekly_item import KeywordHealthStatsWeeklyItem


T = TypeVar("T", bound="KeywordHealthStats")


@_attrs_define
class KeywordHealthStats:
    """Computed over the keyword's matches in the window.

    Attributes:
        matches (int): Matches recorded in the window, relevant or not.
        relevant (int): Scored at or above the relevance line (40).
        filtered (int): Scored under the line: the noise. Billed like any match.
        unscored (int): Not scored yet, or failed to score (never billed).
        noise_share (float | None): filtered / (relevant + filtered); null with nothing scored.
        workspace_share (float | None): This keyword's share of the workspace's matches in the window; null when the
            workspace matched nothing.
        judged_since (None | str): When the keyword last changed its matching rules, platforms or context (or was
            unmuted), when that is inside the window: the status, the reasons, noiseTerms, noiseAuthors and suggestions read
            only the matches since then, while these numbers keep the whole window. Null: everything reads the whole window.
        by_platform (list[KeywordHealthStatsByPlatformItem]): One row per platform it matched on, most matches first.
        weekly (list[KeywordHealthStatsWeeklyItem]): The trend, one row per 7 days of the window, oldest first; the last
            row may be shorter.
        cost (KeywordHealthStatsCost): What the keyword cost over the window at list price.
    """

    matches: int
    relevant: int
    filtered: int
    unscored: int
    noise_share: float | None
    workspace_share: float | None
    judged_since: None | str
    by_platform: list[KeywordHealthStatsByPlatformItem]
    weekly: list[KeywordHealthStatsWeeklyItem]
    cost: KeywordHealthStatsCost
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matches = self.matches

        relevant = self.relevant

        filtered = self.filtered

        unscored = self.unscored

        noise_share: float | None
        noise_share = self.noise_share

        workspace_share: float | None
        workspace_share = self.workspace_share

        judged_since: None | str
        judged_since = self.judged_since

        by_platform = []
        for by_platform_item_data in self.by_platform:
            by_platform_item = by_platform_item_data.to_dict()
            by_platform.append(by_platform_item)

        weekly = []
        for weekly_item_data in self.weekly:
            weekly_item = weekly_item_data.to_dict()
            weekly.append(weekly_item)

        cost = self.cost.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matches": matches,
                "relevant": relevant,
                "filtered": filtered,
                "unscored": unscored,
                "noiseShare": noise_share,
                "workspaceShare": workspace_share,
                "judgedSince": judged_since,
                "byPlatform": by_platform,
                "weekly": weekly,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_health_stats_by_platform_item import (
            KeywordHealthStatsByPlatformItem,
        )
        from ..models.keyword_health_stats_cost import (
            KeywordHealthStatsCost,
        )
        from ..models.keyword_health_stats_weekly_item import (
            KeywordHealthStatsWeeklyItem,
        )

        d = dict(src_dict)
        matches = d.pop("matches")

        relevant = d.pop("relevant")

        filtered = d.pop("filtered")

        unscored = d.pop("unscored")

        def _parse_noise_share(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        noise_share = _parse_noise_share(d.pop("noiseShare"))

        def _parse_workspace_share(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        workspace_share = _parse_workspace_share(d.pop("workspaceShare"))

        def _parse_judged_since(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        judged_since = _parse_judged_since(d.pop("judgedSince"))

        by_platform = []
        _by_platform = d.pop("byPlatform")
        for by_platform_item_data in _by_platform:
            by_platform_item = KeywordHealthStatsByPlatformItem.from_dict(
                by_platform_item_data
            )

            by_platform.append(by_platform_item)

        weekly = []
        _weekly = d.pop("weekly")
        for weekly_item_data in _weekly:
            weekly_item = KeywordHealthStatsWeeklyItem.from_dict(weekly_item_data)

            weekly.append(weekly_item)

        cost = KeywordHealthStatsCost.from_dict(d.pop("cost"))

        keyword_health_stats = cls(
            matches=matches,
            relevant=relevant,
            filtered=filtered,
            unscored=unscored,
            noise_share=noise_share,
            workspace_share=workspace_share,
            judged_since=judged_since,
            by_platform=by_platform,
            weekly=weekly,
            cost=cost,
        )

        keyword_health_stats.additional_properties = d
        return keyword_health_stats

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
