from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.keyword_estimate_terms_item_cost import KeywordEstimateTermsItemCost
    from ..models.keyword_estimate_terms_item_monthly import (
        KeywordEstimateTermsItemMonthly,
    )
    from ..models.keyword_estimate_terms_item_platforms_item import (
        KeywordEstimateTermsItemPlatformsItem,
    )


T = TypeVar("T", bound="KeywordEstimateTermsItem")


@_attrs_define
class KeywordEstimateTermsItem:
    """
    Attributes:
        term (str): The candidate keyword, normalized as a keyword stores it.
        monthly (KeywordEstimateTermsItemMonthly): Sum over the platforms that have a number.
        complete (bool): true when every platform asked for has a number; false when some were skipped or failed (their
            volume is not in the sum).
        cost (KeywordEstimateTermsItemCost): What tracking this term would cost a month at today's prices, with no
            mention cap.
        platforms (list[KeywordEstimateTermsItemPlatformsItem]): One entry per platform asked for.
    """

    term: str
    monthly: KeywordEstimateTermsItemMonthly
    complete: bool
    cost: KeywordEstimateTermsItemCost
    platforms: list[KeywordEstimateTermsItemPlatformsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        monthly = self.monthly.to_dict()

        complete = self.complete

        cost = self.cost.to_dict()

        platforms = []
        for platforms_item_data in self.platforms:
            platforms_item = platforms_item_data.to_dict()
            platforms.append(platforms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "term": term,
                "monthly": monthly,
                "complete": complete,
                "cost": cost,
                "platforms": platforms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_estimate_terms_item_cost import (
            KeywordEstimateTermsItemCost,
        )
        from ..models.keyword_estimate_terms_item_monthly import (
            KeywordEstimateTermsItemMonthly,
        )
        from ..models.keyword_estimate_terms_item_platforms_item import (
            KeywordEstimateTermsItemPlatformsItem,
        )

        d = dict(src_dict)
        term = d.pop("term")

        monthly = KeywordEstimateTermsItemMonthly.from_dict(d.pop("monthly"))

        complete = d.pop("complete")

        cost = KeywordEstimateTermsItemCost.from_dict(d.pop("cost"))

        platforms = []
        _platforms = d.pop("platforms")
        for platforms_item_data in _platforms:
            platforms_item = KeywordEstimateTermsItemPlatformsItem.from_dict(
                platforms_item_data
            )

            platforms.append(platforms_item)

        keyword_estimate_terms_item = cls(
            term=term,
            monthly=monthly,
            complete=complete,
            cost=cost,
            platforms=platforms,
        )

        keyword_estimate_terms_item.additional_properties = d
        return keyword_estimate_terms_item

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
