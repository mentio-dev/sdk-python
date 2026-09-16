from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.log_person_activity_body_channel import LogPersonActivityBodyChannel
from ..types import UNSET, Unset

T = TypeVar("T", bound="LogPersonActivityBody")


@_attrs_define
class LogPersonActivityBody:
    """
    Attributes:
        channel (LogPersonActivityBodyChannel): How they were reached: email, x, linkedin, bluesky, reddit, github,
            call, meeting or other.
        note (str | Unset): What was sent or said, briefly. Default: ''.
        occurred_at (datetime.datetime | Unset): When the contact happened (ISO 8601, or epoch ms). Defaults to now.
        member_id (str | Unset): The member who reached out (user id). Defaults to the signed-in member; an API key that
            omits it logs an unattributed activity.
    """

    channel: LogPersonActivityBodyChannel
    note: str | Unset = ""
    occurred_at: datetime.datetime | Unset = UNSET
    member_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.value

        note = self.note

        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        member_id = self.member_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if occurred_at is not UNSET:
            field_dict["occurredAt"] = occurred_at
        if member_id is not UNSET:
            field_dict["memberId"] = member_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel = LogPersonActivityBodyChannel(d.pop("channel"))

        note = d.pop("note", UNSET)

        _occurred_at = d.pop("occurredAt", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at, Unset):
            occurred_at = UNSET
        else:
            occurred_at = datetime.datetime.fromisoformat(_occurred_at)

        member_id = d.pop("memberId", UNSET)

        log_person_activity_body = cls(
            channel=channel,
            note=note,
            occurred_at=occurred_at,
            member_id=member_id,
        )

        log_person_activity_body.additional_properties = d
        return log_person_activity_body

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
