from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_email_channel_kind import CreateEmailChannelKind

T = TypeVar("T", bound="CreateEmailChannel")


@_attrs_define
class CreateEmailChannel:
    """
    Attributes:
        kind (CreateEmailChannelKind):
        emails (list[str]): Each address gets a confirmation link; workspace members are confirmed on sight.
    """

    kind: CreateEmailChannelKind
    emails: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        emails = self.emails

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "emails": emails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = CreateEmailChannelKind(d.pop("kind"))

        emails = cast(list[str], d.pop("emails"))

        create_email_channel = cls(
            kind=kind,
            emails=emails,
        )

        create_email_channel.additional_properties = d
        return create_email_channel

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
