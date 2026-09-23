from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListKeywordsResponse200DataItemStatsNoise")


@_attrs_define
class ListKeywordsResponse200DataItemStatsNoise:
    """Relevance over the last 14 days of scored matches, so a keyword tightened today stops being flagged within two
    weeks.

        Attributes:
            scored (int): Matches of the last 14 days (by match time) the classifier has scored.
            relevant (int): Of those, the ones scored relevant.
            noisy (bool): At least 20 scored matches in the last 14 days and under 30% of them relevant: tighten the keyword
                with required terms, excluded terms or context. Every match bills, relevant or not.
    """

    scored: int
    relevant: int
    noisy: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scored = self.scored

        relevant = self.relevant

        noisy = self.noisy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scored": scored,
                "relevant": relevant,
                "noisy": noisy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        scored = d.pop("scored")

        relevant = d.pop("relevant")

        noisy = d.pop("noisy")

        list_keywords_response_200_data_item_stats_noise = cls(
            scored=scored,
            relevant=relevant,
            noisy=noisy,
        )

        list_keywords_response_200_data_item_stats_noise.additional_properties = d
        return list_keywords_response_200_data_item_stats_noise

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
