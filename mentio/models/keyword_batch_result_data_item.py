from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_batch_result_data_item_status import (
    KeywordBatchResultDataItemStatus,
)

if TYPE_CHECKING:
    from ..models.keyword_batch_result_data_item_error_type_0 import (
        KeywordBatchResultDataItemErrorType0,
    )
    from ..models.keyword_batch_result_data_item_keyword_type_0 import (
        KeywordBatchResultDataItemKeywordType0,
    )


T = TypeVar("T", bound="KeywordBatchResultDataItem")


@_attrs_define
class KeywordBatchResultDataItem:
    """
    Attributes:
        index (int): Position of the keyword in the request, from 0.
        status (KeywordBatchResultDataItemStatus): created: the keyword exists now. failed: nothing was created for it;
            error says why.
        keyword (KeywordBatchResultDataItemKeywordType0 | None): The created keyword; null when it failed.
        error (KeywordBatchResultDataItemErrorType0 | None): Why it failed; null when created.
    """

    index: int
    status: KeywordBatchResultDataItemStatus
    keyword: KeywordBatchResultDataItemKeywordType0 | None
    error: KeywordBatchResultDataItemErrorType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.keyword_batch_result_data_item_error_type_0 import (
            KeywordBatchResultDataItemErrorType0,
        )
        from ..models.keyword_batch_result_data_item_keyword_type_0 import (
            KeywordBatchResultDataItemKeywordType0,
        )

        index = self.index

        status = self.status.value

        keyword: dict[str, Any] | None
        if isinstance(self.keyword, KeywordBatchResultDataItemKeywordType0):
            keyword = self.keyword.to_dict()
        else:
            keyword = self.keyword

        error: dict[str, Any] | None
        if isinstance(self.error, KeywordBatchResultDataItemErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "status": status,
                "keyword": keyword,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_batch_result_data_item_error_type_0 import (
            KeywordBatchResultDataItemErrorType0,
        )
        from ..models.keyword_batch_result_data_item_keyword_type_0 import (
            KeywordBatchResultDataItemKeywordType0,
        )

        d = dict(src_dict)
        index = d.pop("index")

        status = KeywordBatchResultDataItemStatus(d.pop("status"))

        def _parse_keyword(
            data: object,
        ) -> KeywordBatchResultDataItemKeywordType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_type_0 = KeywordBatchResultDataItemKeywordType0.from_dict(data)

                return keyword_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeywordBatchResultDataItemKeywordType0 | None, data)

        keyword = _parse_keyword(d.pop("keyword"))

        def _parse_error(data: object) -> KeywordBatchResultDataItemErrorType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = KeywordBatchResultDataItemErrorType0.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeywordBatchResultDataItemErrorType0 | None, data)

        error = _parse_error(d.pop("error"))

        keyword_batch_result_data_item = cls(
            index=index,
            status=status,
            keyword=keyword,
            error=error,
        )

        keyword_batch_result_data_item.additional_properties = d
        return keyword_batch_result_data_item

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
