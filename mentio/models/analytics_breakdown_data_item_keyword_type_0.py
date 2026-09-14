from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analytics_breakdown_data_item_keyword_type_0_kind import (
    AnalyticsBreakdownDataItemKeywordType0Kind,
)

T = TypeVar("T", bound="AnalyticsBreakdownDataItemKeywordType0")


@_attrs_define
class AnalyticsBreakdownDataItemKeywordType0:
    """by=keyword only; null otherwise.

    Attributes:
        id (str): Keyword id (kw_...).
        term (str): The tracked term.
        kind (AnalyticsBreakdownDataItemKeywordType0Kind): brand, competitor or topic.
    """

    id: str
    term: str
    kind: AnalyticsBreakdownDataItemKeywordType0Kind
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        term = self.term

        kind = self.kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "term": term,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        kind = AnalyticsBreakdownDataItemKeywordType0Kind(d.pop("kind"))

        analytics_breakdown_data_item_keyword_type_0 = cls(
            id=id,
            term=term,
            kind=kind,
        )

        analytics_breakdown_data_item_keyword_type_0.additional_properties = d
        return analytics_breakdown_data_item_keyword_type_0

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
