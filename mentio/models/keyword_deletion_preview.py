from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.keyword_deletion_preview_alerts_item import (
        KeywordDeletionPreviewAlertsItem,
    )
    from ..models.keyword_deletion_preview_automations_item import (
        KeywordDeletionPreviewAutomationsItem,
    )
    from ..models.keyword_deletion_preview_cost import KeywordDeletionPreviewCost
    from ..models.keyword_deletion_preview_keyword import KeywordDeletionPreviewKeyword
    from ..models.keyword_deletion_preview_views_item import (
        KeywordDeletionPreviewViewsItem,
    )


T = TypeVar("T", bound="KeywordDeletionPreview")


@_attrs_define
class KeywordDeletionPreview:
    """
    Attributes:
        keyword (KeywordDeletionPreviewKeyword): The keyword.
        matches (int): Its mentions, every match ever: deleted with it (a post another keyword also matched stays
            there).
        this_month (int): Of those, recorded this calendar month (UTC), plus the thread comments delivered under it.
        cost (KeywordDeletionPreviewCost): What it has cost this month so far. Deleting refunds nothing: charges already
            made stay on the ledger, and from the next daily charge it costs nothing.
        alerts (list[KeywordDeletionPreviewAlertsItem]): Alert rules whose filter names the keyword.
        automations (list[KeywordDeletionPreviewAutomationsItem]): Automations whose filter names the keyword.
        views (list[KeywordDeletionPreviewViewsItem]): Saved views whose filter names the keyword.
    """

    keyword: KeywordDeletionPreviewKeyword
    matches: int
    this_month: int
    cost: KeywordDeletionPreviewCost
    alerts: list[KeywordDeletionPreviewAlertsItem]
    automations: list[KeywordDeletionPreviewAutomationsItem]
    views: list[KeywordDeletionPreviewViewsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword = self.keyword.to_dict()

        matches = self.matches

        this_month = self.this_month

        cost = self.cost.to_dict()

        alerts = []
        for alerts_item_data in self.alerts:
            alerts_item = alerts_item_data.to_dict()
            alerts.append(alerts_item)

        automations = []
        for automations_item_data in self.automations:
            automations_item = automations_item_data.to_dict()
            automations.append(automations_item)

        views = []
        for views_item_data in self.views:
            views_item = views_item_data.to_dict()
            views.append(views_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keyword": keyword,
                "matches": matches,
                "thisMonth": this_month,
                "cost": cost,
                "alerts": alerts,
                "automations": automations,
                "views": views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_deletion_preview_alerts_item import (
            KeywordDeletionPreviewAlertsItem,
        )
        from ..models.keyword_deletion_preview_automations_item import (
            KeywordDeletionPreviewAutomationsItem,
        )
        from ..models.keyword_deletion_preview_cost import KeywordDeletionPreviewCost
        from ..models.keyword_deletion_preview_keyword import (
            KeywordDeletionPreviewKeyword,
        )
        from ..models.keyword_deletion_preview_views_item import (
            KeywordDeletionPreviewViewsItem,
        )

        d = dict(src_dict)
        keyword = KeywordDeletionPreviewKeyword.from_dict(d.pop("keyword"))

        matches = d.pop("matches")

        this_month = d.pop("thisMonth")

        cost = KeywordDeletionPreviewCost.from_dict(d.pop("cost"))

        alerts = []
        _alerts = d.pop("alerts")
        for alerts_item_data in _alerts:
            alerts_item = KeywordDeletionPreviewAlertsItem.from_dict(alerts_item_data)

            alerts.append(alerts_item)

        automations = []
        _automations = d.pop("automations")
        for automations_item_data in _automations:
            automations_item = KeywordDeletionPreviewAutomationsItem.from_dict(
                automations_item_data
            )

            automations.append(automations_item)

        views = []
        _views = d.pop("views")
        for views_item_data in _views:
            views_item = KeywordDeletionPreviewViewsItem.from_dict(views_item_data)

            views.append(views_item)

        keyword_deletion_preview = cls(
            keyword=keyword,
            matches=matches,
            this_month=this_month,
            cost=cost,
            alerts=alerts,
            automations=automations,
            views=views,
        )

        keyword_deletion_preview.additional_properties = d
        return keyword_deletion_preview

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
