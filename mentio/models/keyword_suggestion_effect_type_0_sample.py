from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordSuggestionEffectType0Sample")


@_attrs_define
class KeywordSuggestionEffectType0Sample:
    """The measurement behind the estimate: the matcher's own rules run over the sampled posts.

    Attributes:
        noise_removed (int): Sampled noise posts the change rejects.
        noise (int): Noise posts sampled.
        relevant_removed (int): Sampled relevant posts the change rejects.
        relevant (int): Relevant posts sampled.
    """

    noise_removed: int
    noise: int
    relevant_removed: int
    relevant: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        noise_removed = self.noise_removed

        noise = self.noise

        relevant_removed = self.relevant_removed

        relevant = self.relevant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "noiseRemoved": noise_removed,
                "noise": noise,
                "relevantRemoved": relevant_removed,
                "relevant": relevant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        noise_removed = d.pop("noiseRemoved")

        noise = d.pop("noise")

        relevant_removed = d.pop("relevantRemoved")

        relevant = d.pop("relevant")

        keyword_suggestion_effect_type_0_sample = cls(
            noise_removed=noise_removed,
            noise=noise,
            relevant_removed=relevant_removed,
            relevant=relevant,
        )

        keyword_suggestion_effect_type_0_sample.additional_properties = d
        return keyword_suggestion_effect_type_0_sample

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
