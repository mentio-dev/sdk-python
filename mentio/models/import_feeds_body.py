from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.import_feeds_body_feeds_item import ImportFeedsBodyFeedsItem


T = TypeVar("T", bound="ImportFeedsBody")


@_attrs_define
class ImportFeedsBody:
    """
    Attributes:
        feeds (list[ImportFeedsBodyFeedsItem]): Up to 100 feeds, each { url } or { url, auth } for a members-only one.
            Each is checked on its own: one that fails never stops the others.
    """

    feeds: list[ImportFeedsBodyFeedsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feeds = []
        for feeds_item_data in self.feeds:
            feeds_item = feeds_item_data.to_dict()
            feeds.append(feeds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feeds": feeds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.import_feeds_body_feeds_item import ImportFeedsBodyFeedsItem

        d = dict(src_dict)
        feeds = []
        _feeds = d.pop("feeds")
        for feeds_item_data in _feeds:
            feeds_item = ImportFeedsBodyFeedsItem.from_dict(feeds_item_data)

            feeds.append(feeds_item)

        import_feeds_body = cls(
            feeds=feeds,
        )

        import_feeds_body.additional_properties = d
        return import_feeds_body

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
