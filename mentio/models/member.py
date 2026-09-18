from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.member_role import MemberRole

T = TypeVar("T", bound="Member")


@_attrs_define
class Member:
    """
    Attributes:
        id (str): Membership id (mem_...), what DELETE /v1/members/{id} takes.
        user_id (str): The person's user id, what assigneeId and ownerId take.
        email (str): The account's email address.
        name (None | str): The name on the account; null when they never set one.
        role (MemberRole): owner: everything, billing included. admin: manages the team. member: works the feed.
        joined_at (str): When the membership was created.
    """

    id: str
    user_id: str
    email: str
    name: None | str
    role: MemberRole
    joined_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        email = self.email

        name: None | str
        name = self.name

        role = self.role.value

        joined_at = self.joined_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "userId": user_id,
                "email": email,
                "name": name,
                "role": role,
                "joinedAt": joined_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("userId")

        email = d.pop("email")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        role = MemberRole(d.pop("role"))

        joined_at = d.pop("joinedAt")

        member = cls(
            id=id,
            user_id=user_id,
            email=email,
            name=name,
            role=role,
            joined_at=joined_at,
        )

        member.additional_properties = d
        return member

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
