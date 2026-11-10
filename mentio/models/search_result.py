from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_result_author_type_0 import SearchResultAuthorType0
    from ..models.search_result_classification_type_0 import (
        SearchResultClassificationType0,
    )
    from ..models.search_result_post import SearchResultPost


T = TypeVar("T", bound="SearchResult")


@_attrs_define
class SearchResult:
    """
    Attributes:
        id (str): Result id (sres_...).
        search_id (str): The search it belongs to (srch_...).
        post (SearchResultPost): The post: platform, text, link, publish time and engagement.
        author (None | SearchResultAuthorType0): Who posted it; null when the platform gave no author at all.
        classification (None | SearchResultClassificationType0): The verdict, judged against your company profile; null
            while the result waits for the classifier.
        relevant (bool): Scored at or above the relevance line (40).
        already_in_workspace (bool): The same post is already one of your mentions (a keyword of yours matched it).
        created_at (str): When the search stored it.
    """

    id: str
    search_id: str
    post: SearchResultPost
    author: None | SearchResultAuthorType0
    classification: None | SearchResultClassificationType0
    relevant: bool
    already_in_workspace: bool
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.search_result_author_type_0 import SearchResultAuthorType0
        from ..models.search_result_classification_type_0 import (
            SearchResultClassificationType0,
        )

        id = self.id

        search_id = self.search_id

        post = self.post.to_dict()

        author: dict[str, Any] | None
        if isinstance(self.author, SearchResultAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

        classification: dict[str, Any] | None
        if isinstance(self.classification, SearchResultClassificationType0):
            classification = self.classification.to_dict()
        else:
            classification = self.classification

        relevant = self.relevant

        already_in_workspace = self.already_in_workspace

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "searchId": search_id,
                "post": post,
                "author": author,
                "classification": classification,
                "relevant": relevant,
                "alreadyInWorkspace": already_in_workspace,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.search_result_author_type_0 import SearchResultAuthorType0
        from ..models.search_result_classification_type_0 import (
            SearchResultClassificationType0,
        )
        from ..models.search_result_post import SearchResultPost

        d = dict(src_dict)
        id = d.pop("id")

        search_id = d.pop("searchId")

        post = SearchResultPost.from_dict(d.pop("post"))

        def _parse_author(data: object) -> None | SearchResultAuthorType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = SearchResultAuthorType0.from_dict(data)

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchResultAuthorType0, data)

        author = _parse_author(d.pop("author"))

        def _parse_classification(
            data: object,
        ) -> None | SearchResultClassificationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                classification_type_0 = SearchResultClassificationType0.from_dict(data)

                return classification_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchResultClassificationType0, data)

        classification = _parse_classification(d.pop("classification"))

        relevant = d.pop("relevant")

        already_in_workspace = d.pop("alreadyInWorkspace")

        created_at = d.pop("createdAt")

        search_result = cls(
            id=id,
            search_id=search_id,
            post=post,
            author=author,
            classification=classification,
            relevant=relevant,
            already_in_workspace=already_in_workspace,
            created_at=created_at,
        )

        search_result.additional_properties = d
        return search_result

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
