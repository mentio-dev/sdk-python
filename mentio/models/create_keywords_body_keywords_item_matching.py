from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_keywords_body_keywords_item_matching_required_mode import (
    CreateKeywordsBodyKeywordsItemMatchingRequiredMode,
)
from ..models.create_keywords_body_keywords_item_matching_term_in_item import (
    CreateKeywordsBodyKeywordsItemMatchingTermInItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_keywords_body_keywords_item_matching_repositories import (
        CreateKeywordsBodyKeywordsItemMatchingRepositories,
    )
    from ..models.create_keywords_body_keywords_item_matching_subreddits import (
        CreateKeywordsBodyKeywordsItemMatchingSubreddits,
    )


T = TypeVar("T", bound="CreateKeywordsBodyKeywordsItemMatching")


@_attrs_define
class CreateKeywordsBodyKeywordsItemMatching:
    """Omitted fields are untouched; an empty list clears one.

    Attributes:
        required_terms (list[str] | Unset): The post must ALSO contain these terms, any one of them or all of them per
            requiredMode. A `*` at the start or the end of an entry is a wildcard (alert* matches alerts and alerting).
            Empty: no requirement.
        required_mode (CreateKeywordsBodyKeywordsItemMatchingRequiredMode | Unset): any: at least one required term must
            appear. all: every one must.
        required_groups (list[list[str]] | Unset): Combinations: the post must ALSO contain every term of at least one
            group (an OR of ANDs), on top of requiredTerms, with the same phrase and wildcard rules. See
            [Keywords](/guides/keywords#several-searches-in-one-keyword).
        excluded_terms (list[str] | Unset): A post containing any of these is dropped. A `*` at the start or the end of
            an entry is a wildcard (beta.* matches beta.0.1; *bot matches nightlybot).
        excluded_authors (list[str] | Unset): Posts by these authors are dropped: profile or post links, @handles,
            u/names, Bluesky DIDs or display names, stored in canonical form like an alert's muted list.
        case_sensitive (bool | Unset): true: the term must appear in the case it was typed (RAG, never rag). Default
            false.
        exact_phrase (bool | Unset): true: only the exact phrase matches (a term sent in double quotes sets it). false:
            a multi-word keyword also matches its words close together, kept and billed only when scored relevant. See
            [Keywords](/guides/keywords#the-exact-phrase-only).
        only_authors (list[str] | Unset): When non-empty, only posts BY these accounts match, in the forms
            excludedAuthors takes; a Bluesky handle is stored with its DID. Reviews and comments read under a mention are
            exempt.
        term_in (list[CreateKeywordsBodyKeywordsItemMatchingTermInItem] | Unset): Where the term must appear, any part
            listed; empty: anywhere; reviews are exempt. See [Keywords](/guides/keywords#where-the-term-must-appear).

            - title: the post's title (none on X, Bluesky or LinkedIn).
            - body: the text after the title.
            - url: the post's link.
            - author: the author's name or handle.
        repositories (CreateKeywordsBodyKeywordsItemMatchingRepositories | Unset): GitHub only: each field is replaced
            when sent, kept when omitted; null clears a minimum.
        subreddits (CreateKeywordsBodyKeywordsItemMatchingSubreddits | Unset): Reddit only, for this keyword alone: each
            list is replaced when sent, kept when omitted.
    """

    required_terms: list[str] | Unset = UNSET
    required_mode: CreateKeywordsBodyKeywordsItemMatchingRequiredMode | Unset = UNSET
    required_groups: list[list[str]] | Unset = UNSET
    excluded_terms: list[str] | Unset = UNSET
    excluded_authors: list[str] | Unset = UNSET
    case_sensitive: bool | Unset = UNSET
    exact_phrase: bool | Unset = UNSET
    only_authors: list[str] | Unset = UNSET
    term_in: list[CreateKeywordsBodyKeywordsItemMatchingTermInItem] | Unset = UNSET
    repositories: CreateKeywordsBodyKeywordsItemMatchingRepositories | Unset = UNSET
    subreddits: CreateKeywordsBodyKeywordsItemMatchingSubreddits | Unset = UNSET
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

        excluded_authors: list[str] | Unset = UNSET
        if not isinstance(self.excluded_authors, Unset):
            excluded_authors = self.excluded_authors

        case_sensitive = self.case_sensitive

        exact_phrase = self.exact_phrase

        only_authors: list[str] | Unset = UNSET
        if not isinstance(self.only_authors, Unset):
            only_authors = self.only_authors

        term_in: list[str] | Unset = UNSET
        if not isinstance(self.term_in, Unset):
            term_in = []
            for term_in_item_data in self.term_in:
                term_in_item = term_in_item_data.value
                term_in.append(term_in_item)

        repositories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = self.repositories.to_dict()

        subreddits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subreddits, Unset):
            subreddits = self.subreddits.to_dict()

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
        if excluded_authors is not UNSET:
            field_dict["excludedAuthors"] = excluded_authors
        if case_sensitive is not UNSET:
            field_dict["caseSensitive"] = case_sensitive
        if exact_phrase is not UNSET:
            field_dict["exactPhrase"] = exact_phrase
        if only_authors is not UNSET:
            field_dict["onlyAuthors"] = only_authors
        if term_in is not UNSET:
            field_dict["termIn"] = term_in
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if subreddits is not UNSET:
            field_dict["subreddits"] = subreddits

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_keywords_body_keywords_item_matching_repositories import (
            CreateKeywordsBodyKeywordsItemMatchingRepositories,
        )
        from ..models.create_keywords_body_keywords_item_matching_subreddits import (
            CreateKeywordsBodyKeywordsItemMatchingSubreddits,
        )

        d = dict(src_dict)
        required_terms = cast(list[str], d.pop("requiredTerms", UNSET))

        _required_mode = d.pop("requiredMode", UNSET)
        required_mode: CreateKeywordsBodyKeywordsItemMatchingRequiredMode | Unset
        if isinstance(_required_mode, Unset):
            required_mode = UNSET
        else:
            required_mode = CreateKeywordsBodyKeywordsItemMatchingRequiredMode(
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

        excluded_authors = cast(list[str], d.pop("excludedAuthors", UNSET))

        case_sensitive = d.pop("caseSensitive", UNSET)

        exact_phrase = d.pop("exactPhrase", UNSET)

        only_authors = cast(list[str], d.pop("onlyAuthors", UNSET))

        _term_in = d.pop("termIn", UNSET)
        term_in: list[CreateKeywordsBodyKeywordsItemMatchingTermInItem] | Unset = UNSET
        if _term_in is not UNSET:
            term_in = []
            for term_in_item_data in _term_in:
                term_in_item = CreateKeywordsBodyKeywordsItemMatchingTermInItem(
                    term_in_item_data
                )

                term_in.append(term_in_item)

        _repositories = d.pop("repositories", UNSET)
        repositories: CreateKeywordsBodyKeywordsItemMatchingRepositories | Unset
        if isinstance(_repositories, Unset):
            repositories = UNSET
        else:
            repositories = CreateKeywordsBodyKeywordsItemMatchingRepositories.from_dict(
                _repositories
            )

        _subreddits = d.pop("subreddits", UNSET)
        subreddits: CreateKeywordsBodyKeywordsItemMatchingSubreddits | Unset
        if isinstance(_subreddits, Unset):
            subreddits = UNSET
        else:
            subreddits = CreateKeywordsBodyKeywordsItemMatchingSubreddits.from_dict(
                _subreddits
            )

        create_keywords_body_keywords_item_matching = cls(
            required_terms=required_terms,
            required_mode=required_mode,
            required_groups=required_groups,
            excluded_terms=excluded_terms,
            excluded_authors=excluded_authors,
            case_sensitive=case_sensitive,
            exact_phrase=exact_phrase,
            only_authors=only_authors,
            term_in=term_in,
            repositories=repositories,
            subreddits=subreddits,
        )

        create_keywords_body_keywords_item_matching.additional_properties = d
        return create_keywords_body_keywords_item_matching

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
