from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_feeds_response_200_data_item_feed_type_0_health_reason import (
    ImportFeedsResponse200DataItemFeedType0HealthReason,
)
from ..models.import_feeds_response_200_data_item_feed_type_0_health_status import (
    ImportFeedsResponse200DataItemFeedType0HealthStatus,
)

T = TypeVar("T", bound="ImportFeedsResponse200DataItemFeedType0Health")


@_attrs_define
class ImportFeedsResponse200DataItemFeedType0Health:
    """Whether the hourly read works.

    Attributes:
        status (ImportFeedsResponse200DataItemFeedType0HealthStatus): failing: the last 3 hourly reads or more failed (a
            feed.failing event went out); ok otherwise.
        reason (ImportFeedsResponse200DataItemFeedType0HealthReason): Why the last read failed; null when it read well.
        detail (None | str): What the last failed read saw.
        failures (int): Failed hourly reads in a row.
        since (None | str): While failing: since when.
    """

    status: ImportFeedsResponse200DataItemFeedType0HealthStatus
    reason: ImportFeedsResponse200DataItemFeedType0HealthReason
    detail: None | str
    failures: int
    since: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        reason = self.reason.value

        detail: None | str
        detail = self.detail

        failures = self.failures

        since: None | str
        since = self.since

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "reason": reason,
                "detail": detail,
                "failures": failures,
                "since": since,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = ImportFeedsResponse200DataItemFeedType0HealthStatus(d.pop("status"))

        reason = ImportFeedsResponse200DataItemFeedType0HealthReason(d.pop("reason"))

        def _parse_detail(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        detail = _parse_detail(d.pop("detail"))

        failures = d.pop("failures")

        def _parse_since(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        since = _parse_since(d.pop("since"))

        import_feeds_response_200_data_item_feed_type_0_health = cls(
            status=status,
            reason=reason,
            detail=detail,
            failures=failures,
            since=since,
        )

        import_feeds_response_200_data_item_feed_type_0_health.additional_properties = d
        return import_feeds_response_200_data_item_feed_type_0_health

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
