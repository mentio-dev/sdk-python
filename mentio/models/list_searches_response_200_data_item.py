from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_searches_response_200_data_item_kind import (
    ListSearchesResponse200DataItemKind,
)
from ..models.list_searches_response_200_data_item_range import (
    ListSearchesResponse200DataItemRange,
)
from ..models.list_searches_response_200_data_item_status import (
    ListSearchesResponse200DataItemStatus,
)

if TYPE_CHECKING:
    from ..models.list_searches_response_200_data_item_platforms_item import (
        ListSearchesResponse200DataItemPlatformsItem,
    )
    from ..models.list_searches_response_200_data_item_stats import (
        ListSearchesResponse200DataItemStats,
    )


T = TypeVar("T", bound="ListSearchesResponse200DataItem")


@_attrs_define
class ListSearchesResponse200DataItem:
    """
    Attributes:
        id (str): Search id (srch_...).
        term (str): The term searched, as typed.
        range_ (ListSearchesResponse200DataItemRange): How far back the search reads, ending now: 24h, 7d or 30d.
            Instagram reads at most its last 7 days whatever the range.
        kind (ListSearchesResponse200DataItemKind): brand, competitor or topic: what the classifier was told the term
            is.
        context (None | str): The hint the classifier read, or null.
        status (ListSearchesResponse200DataItemStatus): queued: accepted, nothing read yet. running: platforms being
            read or results scored. done: every platform reported and every result scored. failed: no platform could be
            read.
        from_ (str): The start of the window read (the end is createdAt).
        platforms (list[ListSearchesResponse200DataItemPlatformsItem]): One entry per platform asked for, in the order
            asked.
        stats (ListSearchesResponse200DataItemStats): Counts across platforms.
        cost_cents (int): What the search has cost so far: $0.008 per scored result, rounded to the cent. A result the
            classifier could not score costs nothing.
        max_cost_cents (int): The most it can cost: 25 results for each platform read, at $0.008 each. The wallet had to
            cover it when the search started.
        created_at (str): When the search was started.
        completed_at (None | str): When it reached done or failed; null while it runs.
    """

    id: str
    term: str
    range_: ListSearchesResponse200DataItemRange
    kind: ListSearchesResponse200DataItemKind
    context: None | str
    status: ListSearchesResponse200DataItemStatus
    from_: str
    platforms: list[ListSearchesResponse200DataItemPlatformsItem]
    stats: ListSearchesResponse200DataItemStats
    cost_cents: int
    max_cost_cents: int
    created_at: str
    completed_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        term = self.term

        range_ = self.range_.value

        kind = self.kind.value

        context: None | str
        context = self.context

        status = self.status.value

        from_ = self.from_

        platforms = []
        for platforms_item_data in self.platforms:
            platforms_item = platforms_item_data.to_dict()
            platforms.append(platforms_item)

        stats = self.stats.to_dict()

        cost_cents = self.cost_cents

        max_cost_cents = self.max_cost_cents

        created_at = self.created_at

        completed_at: None | str
        completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "term": term,
                "range": range_,
                "kind": kind,
                "context": context,
                "status": status,
                "from": from_,
                "platforms": platforms,
                "stats": stats,
                "costCents": cost_cents,
                "maxCostCents": max_cost_cents,
                "createdAt": created_at,
                "completedAt": completed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_searches_response_200_data_item_platforms_item import (
            ListSearchesResponse200DataItemPlatformsItem,
        )
        from ..models.list_searches_response_200_data_item_stats import (
            ListSearchesResponse200DataItemStats,
        )

        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        range_ = ListSearchesResponse200DataItemRange(d.pop("range"))

        kind = ListSearchesResponse200DataItemKind(d.pop("kind"))

        def _parse_context(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        context = _parse_context(d.pop("context"))

        status = ListSearchesResponse200DataItemStatus(d.pop("status"))

        from_ = d.pop("from")

        platforms = []
        _platforms = d.pop("platforms")
        for platforms_item_data in _platforms:
            platforms_item = ListSearchesResponse200DataItemPlatformsItem.from_dict(
                platforms_item_data
            )

            platforms.append(platforms_item)

        stats = ListSearchesResponse200DataItemStats.from_dict(d.pop("stats"))

        cost_cents = d.pop("costCents")

        max_cost_cents = d.pop("maxCostCents")

        created_at = d.pop("createdAt")

        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completedAt"))

        list_searches_response_200_data_item = cls(
            id=id,
            term=term,
            range_=range_,
            kind=kind,
            context=context,
            status=status,
            from_=from_,
            platforms=platforms,
            stats=stats,
            cost_cents=cost_cents,
            max_cost_cents=max_cost_cents,
            created_at=created_at,
            completed_at=completed_at,
        )

        list_searches_response_200_data_item.additional_properties = d
        return list_searches_response_200_data_item

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
