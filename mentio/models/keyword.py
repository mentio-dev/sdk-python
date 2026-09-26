from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_kind import KeywordKind
from ..models.keyword_platforms_type_0_item import KeywordPlatformsType0Item

if TYPE_CHECKING:
    from ..models.group_ref import GroupRef
    from ..models.keyword_cap_type_0 import KeywordCapType0
    from ..models.keyword_matching import KeywordMatching
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
        muted (bool): Not polled or matched. Either paused by you or by the wallet (see pausedForBalance). A keyword at
            its mention cap is not muted (see pausedForCap).
        paused_for_balance (bool): Muted by the wallet for lack of balance; a top-up resumes it, unmuting by hand needs
            balance too.
        paused_for_cap (bool): At its monthly mention cap: not matched until the first of next month (UTC) or until the
            cap is raised. Not muted: it keeps its place and its daily keyword charge.
        cap (KeywordCapType0 | None): The monthly mention cap, or null for none.
        group (GroupRef): The group the keyword belongs to.
        platforms (list[KeywordPlatformsType0Item] | None): Platforms this keyword is tracked on; null means every
            platform.
        context (None | str): A sentence the classifier reads for this keyword only, on top of the company profile (at
            most 300 characters): what the term means here, what to ignore. "Arc is our browser; ignore the geometry word."
            Null clears it.
        matching (KeywordMatching): Matching rules applied before a mention is stored; a rejected post is never billed.
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
    paused_for_cap: bool
    cap: KeywordCapType0 | None
    group: GroupRef
    platforms: list[KeywordPlatformsType0Item] | None
    context: None | str
    matching: KeywordMatching
    stats: KeywordStats
    polling: list[KeywordPollingItem]
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.keyword_cap_type_0 import KeywordCapType0

        id = self.id

        term = self.term

        kind = self.kind.value

        muted = self.muted

        paused_for_balance = self.paused_for_balance

        paused_for_cap = self.paused_for_cap

        cap: dict[str, Any] | None
        if isinstance(self.cap, KeywordCapType0):
            cap = self.cap.to_dict()
        else:
            cap = self.cap

        group = self.group.to_dict()

        platforms: list[str] | None
        if isinstance(self.platforms, list):
            platforms = []
            for platforms_type_0_item_data in self.platforms:
                platforms_type_0_item = platforms_type_0_item_data.value
                platforms.append(platforms_type_0_item)

        else:
            platforms = self.platforms

        context: None | str
        context = self.context

        matching = self.matching.to_dict()

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
                "pausedForCap": paused_for_cap,
                "cap": cap,
                "group": group,
                "platforms": platforms,
                "context": context,
                "matching": matching,
                "stats": stats,
                "polling": polling,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.group_ref import GroupRef
        from ..models.keyword_cap_type_0 import KeywordCapType0
        from ..models.keyword_matching import KeywordMatching
        from ..models.keyword_polling_item import KeywordPollingItem
        from ..models.keyword_stats import KeywordStats

        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        kind = KeywordKind(d.pop("kind"))

        muted = d.pop("muted")

        paused_for_balance = d.pop("pausedForBalance")

        paused_for_cap = d.pop("pausedForCap")

        def _parse_cap(data: object) -> KeywordCapType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cap_type_0 = KeywordCapType0.from_dict(data)

                return cap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeywordCapType0 | None, data)

        cap = _parse_cap(d.pop("cap"))

        group = GroupRef.from_dict(d.pop("group"))

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

        def _parse_context(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        context = _parse_context(d.pop("context"))

        matching = KeywordMatching.from_dict(d.pop("matching"))

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
            paused_for_cap=paused_for_cap,
            cap=cap,
            group=group,
            platforms=platforms,
            context=context,
            matching=matching,
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
