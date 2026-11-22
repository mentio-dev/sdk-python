from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_keyword_estimate_body_platforms_item import (
    CreateKeywordEstimateBodyPlatformsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_keyword_estimate_body_matching import (
        CreateKeywordEstimateBodyMatching,
    )


T = TypeVar("T", bound="CreateKeywordEstimateBody")


@_attrs_define
class CreateKeywordEstimateBody:
    """
    Attributes:
        terms (list[str]): Up to 10 candidate keywords, each estimated on its own.
        platforms (list[CreateKeywordEstimateBodyPlatformsItem] | Unset): The platforms the keyword would track; omit
            for every platform (what a new keyword tracks).
        matching (CreateKeywordEstimateBodyMatching | Unset): The rules the keyword would carry, as on a keyword: a
            sampled post must pass them to count. Omitted fields take the keyword defaults.
        include_paid (bool | Unset): Also sample the paid platforms. See [Keyword estimates](/guides/keyword-
            estimates#cost).

            - false (default): index numbers and free samples only; costs nothing.
            - true: also the paid platforms, 2 to 20 cents per term and platform read; funded only. Default: False.
    """

    terms: list[str]
    platforms: list[CreateKeywordEstimateBodyPlatformsItem] | Unset = UNSET
    matching: CreateKeywordEstimateBodyMatching | Unset = UNSET
    include_paid: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        terms = self.terms

        platforms: list[str] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.value
                platforms.append(platforms_item)

        matching: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matching, Unset):
            matching = self.matching.to_dict()

        include_paid = self.include_paid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "terms": terms,
            }
        )
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if matching is not UNSET:
            field_dict["matching"] = matching
        if include_paid is not UNSET:
            field_dict["includePaid"] = include_paid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_keyword_estimate_body_matching import (
            CreateKeywordEstimateBodyMatching,
        )

        d = dict(src_dict)
        terms = cast(list[str], d.pop("terms"))

        _platforms = d.pop("platforms", UNSET)
        platforms: list[CreateKeywordEstimateBodyPlatformsItem] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = CreateKeywordEstimateBodyPlatformsItem(
                    platforms_item_data
                )

                platforms.append(platforms_item)

        _matching = d.pop("matching", UNSET)
        matching: CreateKeywordEstimateBodyMatching | Unset
        if isinstance(_matching, Unset):
            matching = UNSET
        else:
            matching = CreateKeywordEstimateBodyMatching.from_dict(_matching)

        include_paid = d.pop("includePaid", UNSET)

        create_keyword_estimate_body = cls(
            terms=terms,
            platforms=platforms,
            matching=matching,
            include_paid=include_paid,
        )

        create_keyword_estimate_body.additional_properties = d
        return create_keyword_estimate_body

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
