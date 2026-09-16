from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_activity_channel import PersonActivityChannel

if TYPE_CHECKING:
    from ..models.person_activity_member_type_0 import PersonActivityMemberType0


T = TypeVar("T", bound="PersonActivity")


@_attrs_define
class PersonActivity:
    """
    Attributes:
        id (str): Activity id (act_...).
        person_id (str): The person it belongs to (aut_...).
        channel (PersonActivityChannel): How they were reached: email, x, linkedin, bluesky, reddit, github, call,
            meeting or other.
        note (str): What was sent or said, briefly; empty when nothing was written.
        member (None | PersonActivityMemberType0): Who reached out; null when an API key logged it without naming a
            member, or that member left the workspace.
        occurred_at (str): When the contact happened.
        created_at (str): When it was logged.
    """

    id: str
    person_id: str
    channel: PersonActivityChannel
    note: str
    member: None | PersonActivityMemberType0
    occurred_at: str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.person_activity_member_type_0 import (
            PersonActivityMemberType0,
        )

        id = self.id

        person_id = self.person_id

        channel = self.channel.value

        note = self.note

        member: dict[str, Any] | None
        if isinstance(self.member, PersonActivityMemberType0):
            member = self.member.to_dict()
        else:
            member = self.member

        occurred_at = self.occurred_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "personId": person_id,
                "channel": channel,
                "note": note,
                "member": member,
                "occurredAt": occurred_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.person_activity_member_type_0 import (
            PersonActivityMemberType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        person_id = d.pop("personId")

        channel = PersonActivityChannel(d.pop("channel"))

        note = d.pop("note")

        def _parse_member(data: object) -> None | PersonActivityMemberType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                member_type_0 = PersonActivityMemberType0.from_dict(data)

                return member_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonActivityMemberType0, data)

        member = _parse_member(d.pop("member"))

        occurred_at = d.pop("occurredAt")

        created_at = d.pop("createdAt")

        person_activity = cls(
            id=id,
            person_id=person_id,
            channel=channel,
            note=note,
            member=member,
            occurred_at=occurred_at,
            created_at=created_at,
        )

        person_activity.additional_properties = d
        return person_activity

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
