from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_kind import KeywordKind
from ..models.keyword_platforms_type_0_item import KeywordPlatformsType0Item

if TYPE_CHECKING:
    from ..models.keyword_polling_item import KeywordPollingItem
    from ..models.keyword_stats import KeywordStats


T = TypeVar("T", bound="Keyword")


@_attrs_define
class Keyword:
    """
    Attributes:
        id (str): Keyword id (kw_...).
        term (str):
        kind (KeywordKind):
        muted (bool): Not polled or matched. Either paused by you or by the wallet (see pausedForBalance).
        paused_for_balance (bool): Muted by the wallet for lack of balance; a top-up resumes it, unmuting by hand needs
            balance too.
        platforms (list[KeywordPlatformsType0Item] | None): Platforms this keyword is tracked on; null means every
            platform.
        stats (KeywordStats): Computed over this workspace's matches.
        polling (list[KeywordPollingItem]): Poll health per platform polled on a schedule. Live feeds (Bluesky) have no
            entry.
        created_at (str): ISO 8601 timestamp, UTC.
    """

    id: str
    term: str
    kind: KeywordKind
    muted: bool
    paused_for_balance: bool
    platforms: list[KeywordPlatformsType0Item] | None
    stats: KeywordStats
    polling: list[KeywordPollingItem]
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        term = self.term

        kind = self.kind.value

        muted = self.muted

        paused_for_balance = self.paused_for_balance

        platforms: list[str] | None
        if isinstance(self.platforms, list):
            platforms = []
            for platforms_type_0_item_data in self.platforms:
                platforms_type_0_item = platforms_type_0_item_data.value
                platforms.append(platforms_type_0_item)

        else:
            platforms = self.platforms

        stats = self.stats.to_dict()

        polling = []
        for polling_item_data in self.polling:
            polling_item = polling_item_data.to_dict()
            polling.append(polling_item)

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "term": term,
                "kind": kind,
                "muted": muted,
                "pausedForBalance": paused_for_balance,
                "platforms": platforms,
                "stats": stats,
                "polling": polling,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_polling_item import KeywordPollingItem
        from ..models.keyword_stats import KeywordStats

        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        kind = KeywordKind(d.pop("kind"))

        muted = d.pop("muted")

        paused_for_balance = d.pop("pausedForBalance")

        def _parse_platforms(data: object) -> list[KeywordPlatformsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                platforms_type_0 = []
                _platforms_type_0 = data
                for platforms_type_0_item_data in _platforms_type_0:
                    platforms_type_0_item = KeywordPlatformsType0Item(
                        platforms_type_0_item_data
                    )

                    platforms_type_0.append(platforms_type_0_item)

                return platforms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[KeywordPlatformsType0Item] | None, data)

        platforms = _parse_platforms(d.pop("platforms"))

        stats = KeywordStats.from_dict(d.pop("stats"))

        polling = []
        _polling = d.pop("polling")
        for polling_item_data in _polling:
            polling_item = KeywordPollingItem.from_dict(polling_item_data)

            polling.append(polling_item)

        created_at = d.pop("createdAt")

        keyword = cls(
            id=id,
            term=term,
            kind=kind,
            muted=muted,
            paused_for_balance=paused_for_balance,
            platforms=platforms,
            stats=stats,
            polling=polling,
            created_at=created_at,
        )

        keyword.additional_properties = d
        return keyword

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
