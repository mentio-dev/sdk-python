from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordEstimateTermsItemCost")


@_attrs_define
class KeywordEstimateTermsItemCost:
    """What tracking this term would cost a month at today's prices, with no mention cap.

    Attributes:
        keyword_cents (int): The keyword fee for a month ($5).
        mentions_low_cents (int): Matched mentions a month at $0.008, low end.
        mentions_high_cents (int): Matched mentions a month at $0.008, high end.
        total_low_cents (int): Keyword fee plus mentions, low end.
        total_high_cents (int): Keyword fee plus mentions, high end.
    """

    keyword_cents: int
    mentions_low_cents: int
    mentions_high_cents: int
    total_low_cents: int
    total_high_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword_cents = self.keyword_cents

        mentions_low_cents = self.mentions_low_cents

        mentions_high_cents = self.mentions_high_cents

        total_low_cents = self.total_low_cents

        total_high_cents = self.total_high_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keywordCents": keyword_cents,
                "mentionsLowCents": mentions_low_cents,
                "mentionsHighCents": mentions_high_cents,
                "totalLowCents": total_low_cents,
                "totalHighCents": total_high_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keyword_cents = d.pop("keywordCents")

        mentions_low_cents = d.pop("mentionsLowCents")

        mentions_high_cents = d.pop("mentionsHighCents")

        total_low_cents = d.pop("totalLowCents")

        total_high_cents = d.pop("totalHighCents")

        keyword_estimate_terms_item_cost = cls(
            keyword_cents=keyword_cents,
            mentions_low_cents=mentions_low_cents,
            mentions_high_cents=mentions_high_cents,
            total_low_cents=total_low_cents,
            total_high_cents=total_high_cents,
        )

        keyword_estimate_terms_item_cost.additional_properties = d
        return keyword_estimate_terms_item_cost

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
