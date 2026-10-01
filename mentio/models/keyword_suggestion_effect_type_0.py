from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.keyword_suggestion_effect_type_0_sample import (
        KeywordSuggestionEffectType0Sample,
    )


T = TypeVar("T", bound="KeywordSuggestionEffectType0")


@_attrs_define
class KeywordSuggestionEffectType0:
    """What the change would have done over the window, measured with the matcher's own rules. Null for a context, which
    changes scores, not matches.

        Attributes:
            noise_removed (int): Noise matches of the window (since stats.judgedSince when set) the change would have
                removed (estimated from the sample unless exact).
            relevant_removed (int): Relevant matches of the window it would have removed.
            cents_saved (int): What the removed matches cost at the mention rate: what the change would have saved over the
                window.
            sample (KeywordSuggestionEffectType0Sample): The measurement behind the estimate: the matcher's own rules run
                over the sampled posts.
            exact (bool): The sample was the whole window, so the counts are measured, not estimated.
    """

    noise_removed: int
    relevant_removed: int
    cents_saved: int
    sample: KeywordSuggestionEffectType0Sample
    exact: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        noise_removed = self.noise_removed

        relevant_removed = self.relevant_removed

        cents_saved = self.cents_saved

        sample = self.sample.to_dict()

        exact = self.exact

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "noiseRemoved": noise_removed,
                "relevantRemoved": relevant_removed,
                "centsSaved": cents_saved,
                "sample": sample,
                "exact": exact,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_suggestion_effect_type_0_sample import (
            KeywordSuggestionEffectType0Sample,
        )

        d = dict(src_dict)
        noise_removed = d.pop("noiseRemoved")

        relevant_removed = d.pop("relevantRemoved")

        cents_saved = d.pop("centsSaved")

        sample = KeywordSuggestionEffectType0Sample.from_dict(d.pop("sample"))

        exact = d.pop("exact")

        keyword_suggestion_effect_type_0 = cls(
            noise_removed=noise_removed,
            relevant_removed=relevant_removed,
            cents_saved=cents_saved,
            sample=sample,
            exact=exact,
        )

        keyword_suggestion_effect_type_0.additional_properties = d
        return keyword_suggestion_effect_type_0

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
