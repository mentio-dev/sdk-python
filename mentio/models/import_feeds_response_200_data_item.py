from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_feeds_response_200_data_item_status import (
    ImportFeedsResponse200DataItemStatus,
)

if TYPE_CHECKING:
    from ..models.import_feeds_response_200_data_item_error_type_0 import (
        ImportFeedsResponse200DataItemErrorType0,
    )
    from ..models.import_feeds_response_200_data_item_feed_type_0 import (
        ImportFeedsResponse200DataItemFeedType0,
    )


T = TypeVar("T", bound="ImportFeedsResponse200DataItem")


@_attrs_define
class ImportFeedsResponse200DataItem:
    """
    Attributes:
        url (str): The address as it was sent.
        status (ImportFeedsResponse200DataItemStatus): added: connected now. already: the workspace reads this feed
            already. failed: not connected, see error.
        feed (ImportFeedsResponse200DataItemFeedType0 | None): The feed, when added or already there; null when failed.
        error (ImportFeedsResponse200DataItemErrorType0 | None): Why it was not connected; null unless failed.
    """

    url: str
    status: ImportFeedsResponse200DataItemStatus
    feed: ImportFeedsResponse200DataItemFeedType0 | None
    error: ImportFeedsResponse200DataItemErrorType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.import_feeds_response_200_data_item_error_type_0 import (
            ImportFeedsResponse200DataItemErrorType0,
        )
        from ..models.import_feeds_response_200_data_item_feed_type_0 import (
            ImportFeedsResponse200DataItemFeedType0,
        )

        url = self.url

        status = self.status.value

        feed: dict[str, Any] | None
        if isinstance(self.feed, ImportFeedsResponse200DataItemFeedType0):
            feed = self.feed.to_dict()
        else:
            feed = self.feed

        error: dict[str, Any] | None
        if isinstance(self.error, ImportFeedsResponse200DataItemErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "status": status,
                "feed": feed,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.import_feeds_response_200_data_item_error_type_0 import (
            ImportFeedsResponse200DataItemErrorType0,
        )
        from ..models.import_feeds_response_200_data_item_feed_type_0 import (
            ImportFeedsResponse200DataItemFeedType0,
        )

        d = dict(src_dict)
        url = d.pop("url")

        status = ImportFeedsResponse200DataItemStatus(d.pop("status"))

        def _parse_feed(data: object) -> ImportFeedsResponse200DataItemFeedType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feed_type_0 = ImportFeedsResponse200DataItemFeedType0.from_dict(data)

                return feed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImportFeedsResponse200DataItemFeedType0 | None, data)

        feed = _parse_feed(d.pop("feed"))

        def _parse_error(
            data: object,
        ) -> ImportFeedsResponse200DataItemErrorType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = ImportFeedsResponse200DataItemErrorType0.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImportFeedsResponse200DataItemErrorType0 | None, data)

        error = _parse_error(d.pop("error"))

        import_feeds_response_200_data_item = cls(
            url=url,
            status=status,
            feed=feed,
            error=error,
        )

        import_feeds_response_200_data_item.additional_properties = d
        return import_feeds_response_200_data_item

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
