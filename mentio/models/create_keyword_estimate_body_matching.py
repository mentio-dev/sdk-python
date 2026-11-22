from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_keyword_estimate_body_matching_required_mode import (
    CreateKeywordEstimateBodyMatchingRequiredMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKeywordEstimateBodyMatching")


@_attrs_define
class CreateKeywordEstimateBodyMatching:
    """The rules the keyword would carry, as on a keyword: a sampled post must pass them to count. Omitted fields take the
    keyword defaults.

        Attributes:
            required_terms (list[str] | Unset): The post must ALSO contain these terms, any one of them or all of them per
                requiredMode. A `*` at the start or the end of an entry is a wildcard (alert* matches alerts and alerting).
                Empty: no requirement.
            required_mode (CreateKeywordEstimateBodyMatchingRequiredMode | Unset): any: at least one required term must
                appear. all: every one must.
            required_groups (list[list[str]] | Unset): Combinations: the post must ALSO contain every term of at least one
                group (an OR of ANDs), on top of requiredTerms, with the same phrase and wildcard rules. See
                [Keywords](/guides/keywords#several-searches-in-one-keyword).
            excluded_terms (list[str] | Unset): A post containing any of these is dropped. A `*` at the start or the end of
                an entry is a wildcard (beta.* matches beta.0.1; *bot matches nightlybot).
            exact_phrase (bool | Unset): true: only the exact phrase matches (a term sent in double quotes sets it). false:
                a multi-word keyword also matches its words close together, kept and billed only when scored relevant. See
                [Keywords](/guides/keywords#the-exact-phrase-only).
    """

    required_terms: list[str] | Unset = UNSET
    required_mode: CreateKeywordEstimateBodyMatchingRequiredMode | Unset = UNSET
    required_groups: list[list[str]] | Unset = UNSET
    excluded_terms: list[str] | Unset = UNSET
    exact_phrase: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        required_terms: list[str] | Unset = UNSET
        if not isinstance(self.required_terms, Unset):
            required_terms = self.required_terms

        required_mode: str | Unset = UNSET
        if not isinstance(self.required_mode, Unset):
            required_mode = self.required_mode.value

        required_groups: list[list[str]] | Unset = UNSET
        if not isinstance(self.required_groups, Unset):
            required_groups = []
            for required_groups_item_data in self.required_groups:
                required_groups_item = required_groups_item_data

                required_groups.append(required_groups_item)

        excluded_terms: list[str] | Unset = UNSET
        if not isinstance(self.excluded_terms, Unset):
            excluded_terms = self.excluded_terms

        exact_phrase = self.exact_phrase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if required_terms is not UNSET:
            field_dict["requiredTerms"] = required_terms
        if required_mode is not UNSET:
            field_dict["requiredMode"] = required_mode
        if required_groups is not UNSET:
            field_dict["requiredGroups"] = required_groups
        if excluded_terms is not UNSET:
            field_dict["excludedTerms"] = excluded_terms
        if exact_phrase is not UNSET:
            field_dict["exactPhrase"] = exact_phrase

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        required_terms = cast(list[str], d.pop("requiredTerms", UNSET))

        _required_mode = d.pop("requiredMode", UNSET)
        required_mode: CreateKeywordEstimateBodyMatchingRequiredMode | Unset
        if isinstance(_required_mode, Unset):
            required_mode = UNSET
        else:
            required_mode = CreateKeywordEstimateBodyMatchingRequiredMode(
                _required_mode
            )

        _required_groups = d.pop("requiredGroups", UNSET)
        required_groups: list[list[str]] | Unset = UNSET
        if _required_groups is not UNSET:
            required_groups = []
            for required_groups_item_data in _required_groups:
                required_groups_item = cast(list[str], required_groups_item_data)

                required_groups.append(required_groups_item)

        excluded_terms = cast(list[str], d.pop("excludedTerms", UNSET))

        exact_phrase = d.pop("exactPhrase", UNSET)

        create_keyword_estimate_body_matching = cls(
            required_terms=required_terms,
            required_mode=required_mode,
            required_groups=required_groups,
            excluded_terms=excluded_terms,
            exact_phrase=exact_phrase,
        )

        create_keyword_estimate_body_matching.additional_properties = d
        return create_keyword_estimate_body_matching

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
