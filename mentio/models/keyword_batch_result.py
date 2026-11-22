from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.keyword_batch_result_data_item import KeywordBatchResultDataItem


T = TypeVar("T", bound="KeywordBatchResult")


@_attrs_define
class KeywordBatchResult:
    """
    Attributes:
        data (list[KeywordBatchResultDataItem]): One result per keyword sent, in the same order.
        created (int): Keywords created.
        failed (int): Keywords refused.
    """

    data: list[KeywordBatchResultDataItem]
    created: int
    failed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        created = self.created

        failed = self.failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "created": created,
                "failed": failed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_batch_result_data_item import KeywordBatchResultDataItem

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = KeywordBatchResultDataItem.from_dict(data_item_data)

            data.append(data_item)

        created = d.pop("created")

        failed = d.pop("failed")

        keyword_batch_result = cls(
            data=data,
            created=created,
            failed=failed,
        )

        keyword_batch_result.additional_properties = d
        return keyword_batch_result

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
