from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_filters_body_subreddits import UpdateFiltersBodySubreddits


T = TypeVar("T", bound="UpdateFiltersBody")


@_attrs_define
class UpdateFiltersBody:
    """Omitted fields are untouched; an empty list clears one.

    Attributes:
        excluded_terms (list[str] | Unset): Replaces the list; [] clears it.
        excluded_authors (list[str] | Unset): Replaces the list; [] clears it.
        excluded_repos (list[str] | Unset): Replaces the list; [] clears it.
        subreddits (UpdateFiltersBodySubreddits | Unset): Reddit only; an omitted list is untouched.
    """

    excluded_terms: list[str] | Unset = UNSET
    excluded_authors: list[str] | Unset = UNSET
    excluded_repos: list[str] | Unset = UNSET
    subreddits: UpdateFiltersBodySubreddits | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        excluded_terms: list[str] | Unset = UNSET
        if not isinstance(self.excluded_terms, Unset):
            excluded_terms = self.excluded_terms

        excluded_authors: list[str] | Unset = UNSET
        if not isinstance(self.excluded_authors, Unset):
            excluded_authors = self.excluded_authors

        excluded_repos: list[str] | Unset = UNSET
        if not isinstance(self.excluded_repos, Unset):
            excluded_repos = self.excluded_repos

        subreddits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subreddits, Unset):
            subreddits = self.subreddits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if excluded_terms is not UNSET:
            field_dict["excludedTerms"] = excluded_terms
        if excluded_authors is not UNSET:
            field_dict["excludedAuthors"] = excluded_authors
        if excluded_repos is not UNSET:
            field_dict["excludedRepos"] = excluded_repos
        if subreddits is not UNSET:
            field_dict["subreddits"] = subreddits

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_filters_body_subreddits import (
            UpdateFiltersBodySubreddits,
        )

        d = dict(src_dict)
        excluded_terms = cast(list[str], d.pop("excludedTerms", UNSET))

        excluded_authors = cast(list[str], d.pop("excludedAuthors", UNSET))

        excluded_repos = cast(list[str], d.pop("excludedRepos", UNSET))

        _subreddits = d.pop("subreddits", UNSET)
        subreddits: UpdateFiltersBodySubreddits | Unset
        if isinstance(_subreddits, Unset):
            subreddits = UNSET
        else:
            subreddits = UpdateFiltersBodySubreddits.from_dict(_subreddits)

        update_filters_body = cls(
            excluded_terms=excluded_terms,
            excluded_authors=excluded_authors,
            excluded_repos=excluded_repos,
            subreddits=subreddits,
        )

        update_filters_body.additional_properties = d
        return update_filters_body

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
