from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_suggestion_source import KeywordSuggestionSource
from ..models.keyword_suggestion_type import KeywordSuggestionType

if TYPE_CHECKING:
    from ..models.keyword_suggestion_effect_type_0 import KeywordSuggestionEffectType0
    from ..models.keyword_suggestion_patch import KeywordSuggestionPatch


T = TypeVar("T", bound="KeywordSuggestion")


@_attrs_define
class KeywordSuggestion:
    """
    Attributes:
        type_ (KeywordSuggestionType): excluded_terms and excluded_authors add to the matching rules; required_terms
            sets them; platforms drops the platforms that are almost all noise; context rewrites the sentence the classifier
            reads.
        values (list[str]): What it adds (terms, authors), drops (platforms) or writes (the context).
        why (str): The reason and the measured effect, in plain words.
        patch (KeywordSuggestionPatch): The body to send to PATCH /v1/keywords/{id} as is to apply it. A list holds the
            whole new list, current entries kept.
        effect (KeywordSuggestionEffectType0 | None): What the change would have done over the window, measured with the
            matcher's own rules. Null for a context, which changes scores, not matches.
        source (KeywordSuggestionSource): rules: computed from the window's posts. ai: written by a language model
            (ai=true).
    """

    type_: KeywordSuggestionType
    values: list[str]
    why: str
    patch: KeywordSuggestionPatch
    effect: KeywordSuggestionEffectType0 | None
    source: KeywordSuggestionSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.keyword_suggestion_effect_type_0 import (
            KeywordSuggestionEffectType0,
        )

        type_ = self.type_.value

        values = self.values

        why = self.why

        patch = self.patch.to_dict()

        effect: dict[str, Any] | None
        if isinstance(self.effect, KeywordSuggestionEffectType0):
            effect = self.effect.to_dict()
        else:
            effect = self.effect

        source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "values": values,
                "why": why,
                "patch": patch,
                "effect": effect,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_suggestion_effect_type_0 import (
            KeywordSuggestionEffectType0,
        )
        from ..models.keyword_suggestion_patch import (
            KeywordSuggestionPatch,
        )

        d = dict(src_dict)
        type_ = KeywordSuggestionType(d.pop("type"))

        values = cast(list[str], d.pop("values"))

        why = d.pop("why")

        patch = KeywordSuggestionPatch.from_dict(d.pop("patch"))

        def _parse_effect(data: object) -> KeywordSuggestionEffectType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                effect_type_0 = KeywordSuggestionEffectType0.from_dict(data)

                return effect_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeywordSuggestionEffectType0 | None, data)

        effect = _parse_effect(d.pop("effect"))

        source = KeywordSuggestionSource(d.pop("source"))

        keyword_suggestion = cls(
            type_=type_,
            values=values,
            why=why,
            patch=patch,
            effect=effect,
            source=source,
        )

        keyword_suggestion.additional_properties = d
        return keyword_suggestion

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
