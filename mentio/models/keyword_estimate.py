from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_estimate_platforms_item import KeywordEstimatePlatformsItem
from ..models.keyword_estimate_status import KeywordEstimateStatus

if TYPE_CHECKING:
    from ..models.keyword_estimate_terms_item import KeywordEstimateTermsItem


T = TypeVar("T", bound="KeywordEstimate")


@_attrs_define
class KeywordEstimate:
    """
    Attributes:
        id (str): Estimate id (est_...).
        status (KeywordEstimateStatus): queued: accepted, nothing sampled yet. running: platforms being sampled. done:
            every platform reported. failed: no platform of any term has a number.
        include_paid (bool): Whether paid platforms were sampled.
        platforms (list[KeywordEstimatePlatformsItem]): The platforms asked for.
        terms (list[KeywordEstimateTermsItem]): One entry per term, in the order sent.
        cost_cents (int): What the estimate has cost so far (paid samples read); charged to the wallet when it
            completes.
        max_cost_cents (int): The most it can cost: every paid sample it may read. The wallet had to cover it when it
            started.
        created_at (str): When the estimate was started.
        completed_at (None | str): When it reached done or failed; null while it runs.
    """

    id: str
    status: KeywordEstimateStatus
    include_paid: bool
    platforms: list[KeywordEstimatePlatformsItem]
    terms: list[KeywordEstimateTermsItem]
    cost_cents: int
    max_cost_cents: int
    created_at: str
    completed_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        include_paid = self.include_paid

        platforms = []
        for platforms_item_data in self.platforms:
            platforms_item = platforms_item_data.value
            platforms.append(platforms_item)

        terms = []
        for terms_item_data in self.terms:
            terms_item = terms_item_data.to_dict()
            terms.append(terms_item)

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
                "status": status,
                "includePaid": include_paid,
                "platforms": platforms,
                "terms": terms,
                "costCents": cost_cents,
                "maxCostCents": max_cost_cents,
                "createdAt": created_at,
                "completedAt": completed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_estimate_terms_item import KeywordEstimateTermsItem

        d = dict(src_dict)
        id = d.pop("id")

        status = KeywordEstimateStatus(d.pop("status"))

        include_paid = d.pop("includePaid")

        platforms = []
        _platforms = d.pop("platforms")
        for platforms_item_data in _platforms:
            platforms_item = KeywordEstimatePlatformsItem(platforms_item_data)

            platforms.append(platforms_item)

        terms = []
        _terms = d.pop("terms")
        for terms_item_data in _terms:
            terms_item = KeywordEstimateTermsItem.from_dict(terms_item_data)

            terms.append(terms_item)

        cost_cents = d.pop("costCents")

        max_cost_cents = d.pop("maxCostCents")

        created_at = d.pop("createdAt")

        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completedAt"))

        keyword_estimate = cls(
            id=id,
            status=status,
            include_paid=include_paid,
            platforms=platforms,
            terms=terms,
            cost_cents=cost_cents,
            max_cost_cents=max_cost_cents,
            created_at=created_at,
            completed_at=completed_at,
        )

        keyword_estimate.additional_properties = d
        return keyword_estimate

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
