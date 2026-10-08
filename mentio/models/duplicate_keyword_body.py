from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.duplicate_keyword_body_include_item import DuplicateKeywordBodyIncludeItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateKeywordBody")


@_attrs_define
class DuplicateKeywordBody:
    """
    Attributes:
        term (str): The term of the copy. The same term as the original only in another group (groupId): a term is
            tracked once per group. Wrap it in double quotes for the exact phrase only.
        group_id (str | Unset): The group of the copy (grp_...); omit for the original's group.
        include (list[DuplicateKeywordBodyIncludeItem] | Unset): Also copy these: reviewSources (its review apps) and
            feeds (its RSS or Atom feeds). Off by default, since two keywords on one app or feed collect, and bill, every
            review or item twice.
    """

    term: str
    group_id: str | Unset = UNSET
    include: list[DuplicateKeywordBodyIncludeItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        group_id = self.group_id

        include: list[str] | Unset = UNSET
        if not isinstance(self.include, Unset):
            include = []
            for include_item_data in self.include:
                include_item = include_item_data.value
                include.append(include_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "term": term,
            }
        )
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if include is not UNSET:
            field_dict["include"] = include

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        term = d.pop("term")

        group_id = d.pop("groupId", UNSET)

        _include = d.pop("include", UNSET)
        include: list[DuplicateKeywordBodyIncludeItem] | Unset = UNSET
        if _include is not UNSET:
            include = []
            for include_item_data in _include:
                include_item = DuplicateKeywordBodyIncludeItem(include_item_data)

                include.append(include_item)

        duplicate_keyword_body = cls(
            term=term,
            group_id=group_id,
            include=include,
        )

        duplicate_keyword_body.additional_properties = d
        return duplicate_keyword_body

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
