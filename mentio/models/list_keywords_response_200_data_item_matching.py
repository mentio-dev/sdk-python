from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_keywords_response_200_data_item_matching_required_mode import (
    ListKeywordsResponse200DataItemMatchingRequiredMode,
)

if TYPE_CHECKING:
    from ..models.list_keywords_response_200_data_item_matching_repositories import (
        ListKeywordsResponse200DataItemMatchingRepositories,
    )
    from ..models.list_keywords_response_200_data_item_matching_subreddits import (
        ListKeywordsResponse200DataItemMatchingSubreddits,
    )


T = TypeVar("T", bound="ListKeywordsResponse200DataItemMatching")


@_attrs_define
class ListKeywordsResponse200DataItemMatching:
    """Matching rules applied before a mention is stored; a rejected post is never billed.

    Attributes:
        required_terms (list[str]): The post must ALSO contain these terms, any one of them or all of them per
            requiredMode. A `*` at the start or the end of an entry is a wildcard (alert* matches alerts and alerting).
            Empty: no requirement.
        required_mode (ListKeywordsResponse200DataItemMatchingRequiredMode): any: at least one required term must
            appear. all: every one must.
        required_groups (list[list[str]]): Combinations of terms, at most 50 of 10 terms each: the post must ALSO
            contain every term of at least one group (an OR of ANDs). For the keyword inreach, [["weather", "alert*"],
            ["tsunami"], ["flash flood"]] keeps a post about inReach weather alerts, tsunamis or flash floods, one keyword
            instead of three. Same phrase and wildcard rules as requiredTerms; when both are set a post must pass both.
            Empty: no combinations.
        excluded_terms (list[str]): A post containing any of these is dropped. A `*` at the start or the end of an entry
            is a wildcard (beta.* matches beta.0.1; *bot matches nightlybot).
        excluded_authors (list[str]): Posts by these authors are dropped: profile or post links, @handles, u/names,
            Bluesky DIDs or display names, stored in canonical form like an alert's muted list.
        case_sensitive (bool): true: the term must appear in the case it was typed (RAG, never rag). Default false.
        exact_phrase (bool): true: only the exact phrase matches. false (default): a multi-word keyword also matches a
            post holding its words close together, in any order, plurals and spellings (non-profit, nonprofit) included;
            such a match is kept and billed only when the classifier scores it relevant. A term sent in double quotes sets
            this to true.
        subreddits (ListKeywordsResponse200DataItemMatchingSubreddits): Reddit only, for this keyword alone; the
            workspace filters' own subreddit lists (GET /v1/filters) still apply to every keyword, and a post must pass
            both.
        repositories (ListKeywordsResponse200DataItemMatchingRepositories): GitHub only: which repository events naming
            this keyword become mentions. An event outside the rule is dropped before it is stored, so it is never billed.
    """

    required_terms: list[str]
    required_mode: ListKeywordsResponse200DataItemMatchingRequiredMode
    required_groups: list[list[str]]
    excluded_terms: list[str]
    excluded_authors: list[str]
    case_sensitive: bool
    exact_phrase: bool
    subreddits: ListKeywordsResponse200DataItemMatchingSubreddits
    repositories: ListKeywordsResponse200DataItemMatchingRepositories
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        required_terms = self.required_terms

        required_mode = self.required_mode.value

        required_groups = []
        for required_groups_item_data in self.required_groups:
            required_groups_item = required_groups_item_data

            required_groups.append(required_groups_item)

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
                "requiredGroups": required_groups,
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
        from ..models.list_keywords_response_200_data_item_matching_repositories import (
            ListKeywordsResponse200DataItemMatchingRepositories,
        )
        from ..models.list_keywords_response_200_data_item_matching_subreddits import (
            ListKeywordsResponse200DataItemMatchingSubreddits,
        )

        d = dict(src_dict)
        required_terms = cast(list[str], d.pop("requiredTerms"))

        required_mode = ListKeywordsResponse200DataItemMatchingRequiredMode(
            d.pop("requiredMode")
        )

        required_groups = []
        _required_groups = d.pop("requiredGroups")
        for required_groups_item_data in _required_groups:
            required_groups_item = cast(list[str], required_groups_item_data)

            required_groups.append(required_groups_item)

        excluded_terms = cast(list[str], d.pop("excludedTerms"))

        excluded_authors = cast(list[str], d.pop("excludedAuthors"))

        case_sensitive = d.pop("caseSensitive")

        exact_phrase = d.pop("exactPhrase")

        subreddits = ListKeywordsResponse200DataItemMatchingSubreddits.from_dict(
            d.pop("subreddits")
        )

        repositories = ListKeywordsResponse200DataItemMatchingRepositories.from_dict(
            d.pop("repositories")
        )

        list_keywords_response_200_data_item_matching = cls(
            required_terms=required_terms,
            required_mode=required_mode,
            required_groups=required_groups,
            excluded_terms=excluded_terms,
            excluded_authors=excluded_authors,
            case_sensitive=case_sensitive,
            exact_phrase=exact_phrase,
            subreddits=subreddits,
            repositories=repositories,
        )

        list_keywords_response_200_data_item_matching.additional_properties = d
        return list_keywords_response_200_data_item_matching

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
