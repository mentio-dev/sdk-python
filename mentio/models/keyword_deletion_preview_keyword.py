from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordDeletionPreviewKeyword")


@_attrs_define
class KeywordDeletionPreviewKeyword:
    """The keyword.

    Attributes:
        id (str): Keyword id (kw_...).
        term (str): The tracked term.
        name (str): The keyword as Mentio names it: the term, or "term (Group)" outside the default group.
    """

    id: str
    term: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        term = self.term

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "term": term,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        name = d.pop("name")

        keyword_deletion_preview_keyword = cls(
            id=id,
            term=term,
            name=name,
        )

        keyword_deletion_preview_keyword.additional_properties = d
        return keyword_deletion_preview_keyword

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
