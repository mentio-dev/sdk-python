from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_noisy_event_data_keyword_kind import (
    KeywordNoisyEventDataKeywordKind,
)

T = TypeVar("T", bound="KeywordNoisyEventDataKeyword")


@_attrs_define
class KeywordNoisyEventDataKeyword:
    """The keyword the item is about.

    Attributes:
        id (str): Keyword id (kw_...).
        term (str): The tracked term.
        kind (KeywordNoisyEventDataKeywordKind): brand, competitor or topic.
        name (str): The keyword as Mentio names it: the term, or "term (Group)" outside the default group.
        group_id (str): Its group (grp_...).
    """

    id: str
    term: str
    kind: KeywordNoisyEventDataKeywordKind
    name: str
    group_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        term = self.term

        kind = self.kind.value

        name = self.name

        group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "term": term,
                "kind": kind,
                "name": name,
                "groupId": group_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        kind = KeywordNoisyEventDataKeywordKind(d.pop("kind"))

        name = d.pop("name")

        group_id = d.pop("groupId")

        keyword_noisy_event_data_keyword = cls(
            id=id,
            term=term,
            kind=kind,
            name=name,
            group_id=group_id,
        )

        keyword_noisy_event_data_keyword.additional_properties = d
        return keyword_noisy_event_data_keyword

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
