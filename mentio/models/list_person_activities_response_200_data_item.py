from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_person_activities_response_200_data_item_channel import (
    ListPersonActivitiesResponse200DataItemChannel,
)

if TYPE_CHECKING:
    from ..models.list_person_activities_response_200_data_item_member_type_0 import (
        ListPersonActivitiesResponse200DataItemMemberType0,
    )


T = TypeVar("T", bound="ListPersonActivitiesResponse200DataItem")


@_attrs_define
class ListPersonActivitiesResponse200DataItem:
    """
    Attributes:
        id (str): Activity id (act_...).
        person_id (str): The person it belongs to (aut_...).
        channel (ListPersonActivitiesResponse200DataItemChannel): How they were reached: email, x, linkedin, bluesky,
            reddit, github, call, meeting or other.
        note (str): What was sent or said, briefly; empty when nothing was written.
        member (ListPersonActivitiesResponse200DataItemMemberType0 | None): Who reached out; null when an API key logged
            it without naming a member, or that member left the workspace.
        occurred_at (str): When the contact happened.
        created_at (str): When it was logged.
    """

    id: str
    person_id: str
    channel: ListPersonActivitiesResponse200DataItemChannel
    note: str
    member: ListPersonActivitiesResponse200DataItemMemberType0 | None
    occurred_at: str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_person_activities_response_200_data_item_member_type_0 import (
            ListPersonActivitiesResponse200DataItemMemberType0,
        )

        id = self.id

        person_id = self.person_id

        channel = self.channel.value

        note = self.note

        member: dict[str, Any] | None
        if isinstance(self.member, ListPersonActivitiesResponse200DataItemMemberType0):
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
        from ..models.list_person_activities_response_200_data_item_member_type_0 import (
            ListPersonActivitiesResponse200DataItemMemberType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        person_id = d.pop("personId")

        channel = ListPersonActivitiesResponse200DataItemChannel(d.pop("channel"))

        note = d.pop("note")

        def _parse_member(
            data: object,
        ) -> ListPersonActivitiesResponse200DataItemMemberType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                member_type_0 = (
                    ListPersonActivitiesResponse200DataItemMemberType0.from_dict(data)
                )

                return member_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListPersonActivitiesResponse200DataItemMemberType0 | None, data)

        member = _parse_member(d.pop("member"))

        occurred_at = d.pop("occurredAt")

        created_at = d.pop("createdAt")

        list_person_activities_response_200_data_item = cls(
            id=id,
            person_id=person_id,
            channel=channel,
            note=note,
            member=member,
            occurred_at=occurred_at,
            created_at=created_at,
        )

        list_person_activities_response_200_data_item.additional_properties = d
        return list_person_activities_response_200_data_item

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
