from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_keywords_response_200_data_item_kind import (
    ListKeywordsResponse200DataItemKind,
)
from ..models.list_keywords_response_200_data_item_platforms_type_0_item import (
    ListKeywordsResponse200DataItemPlatformsType0Item,
)

if TYPE_CHECKING:
    from ..models.group_ref import GroupRef
    from ..models.list_keywords_response_200_data_item_cap_type_0 import (
        ListKeywordsResponse200DataItemCapType0,
    )
    from ..models.list_keywords_response_200_data_item_matching import (
        ListKeywordsResponse200DataItemMatching,
    )
    from ..models.list_keywords_response_200_data_item_polling_item import (
        ListKeywordsResponse200DataItemPollingItem,
    )
    from ..models.list_keywords_response_200_data_item_stats import (
        ListKeywordsResponse200DataItemStats,
    )


T = TypeVar("T", bound="ListKeywordsResponse200DataItem")


@_attrs_define
class ListKeywordsResponse200DataItem:
    """
    Attributes:
        id (str): Keyword id (kw_...).
        term (str):
        kind (ListKeywordsResponse200DataItemKind):
        muted (bool): Not polled or matched. Either paused by you or by the wallet (see pausedForBalance). A keyword at
            its mention cap is not muted (see pausedForCap).
        paused_for_balance (bool): Muted by the wallet for lack of balance; a top-up resumes it, unmuting by hand needs
            balance too.
        paused_for_cap (bool): At its monthly mention cap: not matched until the first of next month (UTC) or until the
            cap is raised. Not muted: it keeps its place and its daily keyword charge.
        cap (ListKeywordsResponse200DataItemCapType0 | None): The monthly mention cap, or null for none.
        group (GroupRef): The group the keyword belongs to.
        platforms (list[ListKeywordsResponse200DataItemPlatformsType0Item] | None): Platforms this keyword is tracked
            on; null means every platform.
        context (None | str): A sentence the classifier reads for this keyword only, on top of the company profile or
            the group's own description (at most 300 characters): what the term means here, what to ignore. "Arc is our
            browser; ignore the geometry word." Null clears it.
        matching (ListKeywordsResponse200DataItemMatching): Matching rules applied before a mention is stored; a
            rejected post is never billed.
        stats (ListKeywordsResponse200DataItemStats): Computed over this workspace's matches.
        polling (list[ListKeywordsResponse200DataItemPollingItem]): Poll health per platform polled on a schedule. Live
            feeds (Bluesky) have no entry.
        created_at (str): ISO 8601 timestamp, UTC.
    """

    id: str
    term: str
    kind: ListKeywordsResponse200DataItemKind
    muted: bool
    paused_for_balance: bool
    paused_for_cap: bool
    cap: ListKeywordsResponse200DataItemCapType0 | None
    group: GroupRef
    platforms: list[ListKeywordsResponse200DataItemPlatformsType0Item] | None
    context: None | str
    matching: ListKeywordsResponse200DataItemMatching
    stats: ListKeywordsResponse200DataItemStats
    polling: list[ListKeywordsResponse200DataItemPollingItem]
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_keywords_response_200_data_item_cap_type_0 import (
            ListKeywordsResponse200DataItemCapType0,
        )

        id = self.id

        term = self.term

        kind = self.kind.value

        muted = self.muted

        paused_for_balance = self.paused_for_balance

        paused_for_cap = self.paused_for_cap

        cap: dict[str, Any] | None
        if isinstance(self.cap, ListKeywordsResponse200DataItemCapType0):
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
        from ..models.list_keywords_response_200_data_item_cap_type_0 import (
            ListKeywordsResponse200DataItemCapType0,
        )
        from ..models.list_keywords_response_200_data_item_matching import (
            ListKeywordsResponse200DataItemMatching,
        )
        from ..models.list_keywords_response_200_data_item_polling_item import (
            ListKeywordsResponse200DataItemPollingItem,
        )
        from ..models.list_keywords_response_200_data_item_stats import (
            ListKeywordsResponse200DataItemStats,
        )

        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        kind = ListKeywordsResponse200DataItemKind(d.pop("kind"))

        muted = d.pop("muted")

        paused_for_balance = d.pop("pausedForBalance")

        paused_for_cap = d.pop("pausedForCap")

        def _parse_cap(data: object) -> ListKeywordsResponse200DataItemCapType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cap_type_0 = ListKeywordsResponse200DataItemCapType0.from_dict(data)

                return cap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListKeywordsResponse200DataItemCapType0 | None, data)

        cap = _parse_cap(d.pop("cap"))

        group = GroupRef.from_dict(d.pop("group"))

        def _parse_platforms(
            data: object,
        ) -> list[ListKeywordsResponse200DataItemPlatformsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                platforms_type_0 = []
                _platforms_type_0 = data
                for platforms_type_0_item_data in _platforms_type_0:
                    platforms_type_0_item = (
                        ListKeywordsResponse200DataItemPlatformsType0Item(
                            platforms_type_0_item_data
                        )
                    )

                    platforms_type_0.append(platforms_type_0_item)

                return platforms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[ListKeywordsResponse200DataItemPlatformsType0Item] | None, data
            )

        platforms = _parse_platforms(d.pop("platforms"))

        def _parse_context(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        context = _parse_context(d.pop("context"))

        matching = ListKeywordsResponse200DataItemMatching.from_dict(d.pop("matching"))

        stats = ListKeywordsResponse200DataItemStats.from_dict(d.pop("stats"))

        polling = []
        _polling = d.pop("polling")
        for polling_item_data in _polling:
            polling_item = ListKeywordsResponse200DataItemPollingItem.from_dict(
                polling_item_data
            )

            polling.append(polling_item)

        created_at = d.pop("createdAt")

        list_keywords_response_200_data_item = cls(
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

        list_keywords_response_200_data_item.additional_properties = d
        return list_keywords_response_200_data_item

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
