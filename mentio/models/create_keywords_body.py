from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_keywords_body_keywords_item import (
        CreateKeywordsBodyKeywordsItem,
    )


T = TypeVar("T", bound="CreateKeywordsBody")


@_attrs_define
class CreateKeywordsBody:
    """
    Attributes:
        keywords (list[CreateKeywordsBodyKeywordsItem]): The keywords to create, 1 to 100 (10 before the first top-up),
            in order. Each is created or refused on its own.
    """

    keywords: list[CreateKeywordsBodyKeywordsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keywords = []
        for keywords_item_data in self.keywords:
            keywords_item = keywords_item_data.to_dict()
            keywords.append(keywords_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keywords": keywords,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_keywords_body_keywords_item import (
            CreateKeywordsBodyKeywordsItem,
        )

        d = dict(src_dict)
        keywords = []
        _keywords = d.pop("keywords")
        for keywords_item_data in _keywords:
            keywords_item = CreateKeywordsBodyKeywordsItem.from_dict(keywords_item_data)

            keywords.append(keywords_item)

        create_keywords_body = cls(
            keywords=keywords,
        )

        create_keywords_body.additional_properties = d
        return create_keywords_body

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
