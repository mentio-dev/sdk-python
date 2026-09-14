from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_mention_body_status import UpdateMentionBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateMentionBody")


@_attrs_define
class UpdateMentionBody:
    """Every field is optional; omitted fields are untouched.

    Attributes:
        status (UpdateMentionBodyStatus | Unset): ignored or done to handle it; open to put it back.
        assignee_id (None | str | Unset): A workspace member (user id), or null to unassign.
        snoozed_until (datetime.datetime | Unset): ISO 8601 (or epoch ms) until which the mention leaves the feed; null
            wakes it.
        note (None | str | Unset): Internal note; null or empty clears it.
    """

    status: UpdateMentionBodyStatus | Unset = UNSET
    assignee_id: None | str | Unset = UNSET
    snoozed_until: datetime.datetime | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        else:
            assignee_id = self.assignee_id

        snoozed_until: str | Unset = UNSET
        if not isinstance(self.snoozed_until, Unset):
            snoozed_until = self.snoozed_until.isoformat()

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if snoozed_until is not UNSET:
            field_dict["snoozedUntil"] = snoozed_until
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: UpdateMentionBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateMentionBodyStatus(_status)

        def _parse_assignee_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_id = _parse_assignee_id(d.pop("assigneeId", UNSET))

        _snoozed_until = d.pop("snoozedUntil", UNSET)
        snoozed_until: datetime.datetime | Unset
        if isinstance(_snoozed_until, Unset):
            snoozed_until = UNSET
        else:
            snoozed_until = datetime.datetime.fromisoformat(_snoozed_until)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        update_mention_body = cls(
            status=status,
            assignee_id=assignee_id,
            snoozed_until=snoozed_until,
            note=note,
        )

        update_mention_body.additional_properties = d
        return update_mention_body

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
