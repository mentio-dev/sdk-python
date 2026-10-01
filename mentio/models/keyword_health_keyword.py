from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.group_ref import GroupRef


T = TypeVar("T", bound="KeywordHealthKeyword")


@_attrs_define
class KeywordHealthKeyword:
    """The keyword the report is about.

    Attributes:
        id (str): Keyword id (kw_...).
        term (str): The term as typed.
        group (GroupRef): The group the keyword belongs to.
    """

    id: str
    term: str
    group: GroupRef
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        term = self.term

        group = self.group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "term": term,
                "group": group,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.group_ref import GroupRef

        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        group = GroupRef.from_dict(d.pop("group"))

        keyword_health_keyword = cls(
            id=id,
            term=term,
            group=group,
        )

        keyword_health_keyword.additional_properties = d
        return keyword_health_keyword

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
