from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_matching_required_mode import KeywordMatchingRequiredMode

if TYPE_CHECKING:
    from ..models.keyword_matching_repositories import KeywordMatchingRepositories
    from ..models.keyword_matching_subreddits import KeywordMatchingSubreddits


T = TypeVar("T", bound="KeywordMatching")


@_attrs_define
class KeywordMatching:
    """Matching rules applied before a mention is stored; a rejected post is never billed.

    Attributes:
        required_terms (list[str]): The post must ALSO contain these terms, any one of them or all of them per
            requiredMode. Empty: no requirement.
        required_mode (KeywordMatchingRequiredMode): any: at least one required term must appear. all: every one must.
        excluded_terms (list[str]): A post containing any of these is dropped. A `*` at the start or the end of an entry
            is a wildcard (beta.* matches beta.0.1; *bot matches nightlybot).
        excluded_authors (list[str]): Posts by these authors are dropped: profile or post links, @handles, u/names,
            Bluesky DIDs or display names, stored in canonical form like an alert's muted list.
        case_sensitive (bool): true: the term must appear in the case it was typed (RAG, never rag). Default false.
        exact_phrase (bool): true: only the exact phrase matches. false (default): a multi-word keyword also matches a
            post holding its words close together, in any order, plurals and spellings (non-profit, nonprofit) included;
            such a match is kept and billed only when the classifier scores it relevant. A term sent in double quotes sets
            this to true.
        subreddits (KeywordMatchingSubreddits): Reddit only, for this keyword alone; the workspace filters' own
            subreddit lists (GET /v1/filters) still apply to every keyword, and a post must pass both.
        repositories (KeywordMatchingRepositories): GitHub only: which repository events naming this keyword become
            mentions. An event outside the rule is dropped before it is stored, so it is never billed.
    """

    required_terms: list[str]
    required_mode: KeywordMatchingRequiredMode
    excluded_terms: list[str]
    excluded_authors: list[str]
    case_sensitive: bool
    exact_phrase: bool
    subreddits: KeywordMatchingSubreddits
    repositories: KeywordMatchingRepositories
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        required_terms = self.required_terms

        required_mode = self.required_mode.value

        excluded_terms = self.excluded_terms

        excluded_authors = self.excluded_authors

        case_sensitive = self.case_sensitive

        exact_phrase = self.exact_phrase

        subreddits = self.subreddits.to_dict()

        repositories = self.repositories.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requiredTerms": required_terms,
                "requiredMode": required_mode,
                "excludedTerms": excluded_terms,
                "excludedAuthors": excluded_authors,
                "caseSensitive": case_sensitive,
                "exactPhrase": exact_phrase,
                "subreddits": subreddits,
                "repositories": repositories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_matching_repositories import (
            KeywordMatchingRepositories,
        )
        from ..models.keyword_matching_subreddits import (
            KeywordMatchingSubreddits,
        )

        d = dict(src_dict)
        required_terms = cast(list[str], d.pop("requiredTerms"))

        required_mode = KeywordMatchingRequiredMode(d.pop("requiredMode"))

        excluded_terms = cast(list[str], d.pop("excludedTerms"))

        excluded_authors = cast(list[str], d.pop("excludedAuthors"))

        case_sensitive = d.pop("caseSensitive")

        exact_phrase = d.pop("exactPhrase")

        subreddits = KeywordMatchingSubreddits.from_dict(d.pop("subreddits"))

        repositories = KeywordMatchingRepositories.from_dict(d.pop("repositories"))

        keyword_matching = cls(
            required_terms=required_terms,
            required_mode=required_mode,
            excluded_terms=excluded_terms,
            excluded_authors=excluded_authors,
            case_sensitive=case_sensitive,
            exact_phrase=exact_phrase,
            subreddits=subreddits,
            repositories=repositories,
        )

        keyword_matching.additional_properties = d
        return keyword_matching

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
