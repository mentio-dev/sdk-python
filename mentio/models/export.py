from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_format import ExportFormat
from ..models.export_resource import ExportResource
from ..models.export_status import ExportStatus

if TYPE_CHECKING:
    from ..models.export_delivery_type_0 import ExportDeliveryType0
    from ..models.export_download_type_0 import ExportDownloadType0
    from ..models.export_error_type_0 import ExportErrorType0
    from ..models.export_filter import ExportFilter
    from ..models.export_stats import ExportStats
    from ..models.export_window_type_0 import ExportWindowType0


T = TypeVar("T", bound="Export")


@_attrs_define
class Export:
    """
    Attributes:
        id (str): Export id (exp_...).
        resource (ExportResource): What is exported: mentions.
        format_ (ExportFormat): csv: the spreadsheet columns of GET /v1/mentions/export.csv, text cut at 1,000
            characters. jsonl: one whole Mention object per line (newline-delimited JSON), as GET /v1/mentions returns it.
        status (ExportStatus): queued: waiting to start. running: rows are being written. succeeded: the file is ready.
            failed: it stopped (error says why). expired: it succeeded and the file has been deleted since.
        filter_ (ExportFilter): Which mentions: every filter of GET /v1/mentions, in the same vocabulary (a list as an
            array or comma-separated), viewId and alertId included. {} is every mention the list shows.
        schedule_id (None | str): The schedule that ran it (exs_...), or null for one created by hand.
        window (ExportWindowType0 | None): A scheduled run: the stretch of match time it covers. null for a one-off
            export, which reads the filter as given.
        max_rows (int): The most rows it writes.
        stats (ExportStats): Progress, and the size of the file once it succeeded.
        truncated (bool): true when more mentions matched than it holds (maxRows or the 2 GiB file bound): narrow the
            filter and export again.
        error (ExportErrorType0 | None): Why it failed; null otherwise.
        download (ExportDownloadType0 | None): Once it succeeded: a signed download link, valid for an hour. null
            before, after the file expired, or when this deployment cannot sign links.
        file_expires_at (None | str): When the file is deleted: 7 days after it succeeded.
        delivery (ExportDeliveryType0 | None): A scheduled run: where the file goes and how that went. null for a one-
            off export.
        created_at (str): ISO 8601 timestamp, UTC.
        started_at (None | str): When the first rows were written.
        completed_at (None | str): When it succeeded or failed.
    """

    id: str
    resource: ExportResource
    format_: ExportFormat
    status: ExportStatus
    filter_: ExportFilter
    schedule_id: None | str
    window: ExportWindowType0 | None
    max_rows: int
    stats: ExportStats
    truncated: bool
    error: ExportErrorType0 | None
    download: ExportDownloadType0 | None
    file_expires_at: None | str
    delivery: ExportDeliveryType0 | None
    created_at: str
    started_at: None | str
    completed_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.export_delivery_type_0 import ExportDeliveryType0
        from ..models.export_download_type_0 import ExportDownloadType0
        from ..models.export_error_type_0 import ExportErrorType0
        from ..models.export_window_type_0 import ExportWindowType0

        id = self.id

        resource = self.resource.value

        format_ = self.format_.value

        status = self.status.value

        filter_ = self.filter_.to_dict()

        schedule_id: None | str
        schedule_id = self.schedule_id

        window: dict[str, Any] | None
        if isinstance(self.window, ExportWindowType0):
            window = self.window.to_dict()
        else:
            window = self.window

        max_rows = self.max_rows

        stats = self.stats.to_dict()

        truncated = self.truncated

        error: dict[str, Any] | None
        if isinstance(self.error, ExportErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        download: dict[str, Any] | None
        if isinstance(self.download, ExportDownloadType0):
            download = self.download.to_dict()
        else:
            download = self.download

        file_expires_at: None | str
        file_expires_at = self.file_expires_at

        delivery: dict[str, Any] | None
        if isinstance(self.delivery, ExportDeliveryType0):
            delivery = self.delivery.to_dict()
        else:
            delivery = self.delivery

        created_at = self.created_at

        started_at: None | str
        started_at = self.started_at

        completed_at: None | str
        completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "resource": resource,
                "format": format_,
                "status": status,
                "filter": filter_,
                "scheduleId": schedule_id,
                "window": window,
                "maxRows": max_rows,
                "stats": stats,
                "truncated": truncated,
                "error": error,
                "download": download,
                "fileExpiresAt": file_expires_at,
                "delivery": delivery,
                "createdAt": created_at,
                "startedAt": started_at,
                "completedAt": completed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.export_delivery_type_0 import ExportDeliveryType0
        from ..models.export_download_type_0 import ExportDownloadType0
        from ..models.export_error_type_0 import ExportErrorType0
        from ..models.export_filter import ExportFilter
        from ..models.export_stats import ExportStats
        from ..models.export_window_type_0 import ExportWindowType0

        d = dict(src_dict)
        id = d.pop("id")

        resource = ExportResource(d.pop("resource"))

        format_ = ExportFormat(d.pop("format"))

        status = ExportStatus(d.pop("status"))

        filter_ = ExportFilter.from_dict(d.pop("filter"))

        def _parse_schedule_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        schedule_id = _parse_schedule_id(d.pop("scheduleId"))

        def _parse_window(data: object) -> ExportWindowType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_0 = ExportWindowType0.from_dict(data)

                return window_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportWindowType0 | None, data)

        window = _parse_window(d.pop("window"))

        max_rows = d.pop("maxRows")

        stats = ExportStats.from_dict(d.pop("stats"))

        truncated = d.pop("truncated")

        def _parse_error(data: object) -> ExportErrorType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = ExportErrorType0.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportErrorType0 | None, data)

        error = _parse_error(d.pop("error"))

        def _parse_download(data: object) -> ExportDownloadType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                download_type_0 = ExportDownloadType0.from_dict(data)

                return download_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportDownloadType0 | None, data)

        download = _parse_download(d.pop("download"))

        def _parse_file_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_expires_at = _parse_file_expires_at(d.pop("fileExpiresAt"))

        def _parse_delivery(data: object) -> ExportDeliveryType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                delivery_type_0 = ExportDeliveryType0.from_dict(data)

                return delivery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportDeliveryType0 | None, data)

        delivery = _parse_delivery(d.pop("delivery"))

        created_at = d.pop("createdAt")

        def _parse_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        started_at = _parse_started_at(d.pop("startedAt"))

        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completedAt"))

        export = cls(
            id=id,
            resource=resource,
            format_=format_,
            status=status,
            filter_=filter_,
            schedule_id=schedule_id,
            window=window,
            max_rows=max_rows,
            stats=stats,
            truncated=truncated,
            error=error,
            download=download,
            file_expires_at=file_expires_at,
            delivery=delivery,
            created_at=created_at,
            started_at=started_at,
            completed_at=completed_at,
        )

        export.additional_properties = d
        return export

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
