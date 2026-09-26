from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateGroupBody")


@_attrs_define
class CreateGroupBody:
    """
    Attributes:
        name (str): The group's name: a customer, a campaign, a product. Unique per workspace.
        external_id (None | str | Unset): Your own id for the group (a customer id, say). Unique per workspace; find the
            group by it with GET /v1/groups?externalId=.
        context (None | str | Unset): What the classifier reads as "the company" for this group's keywords, in place of
            the WHOLE workspace profile, its relevance guidelines and competitor list included (at most 4000 characters):
            who the business is, what it sells, for whom, what is not it, and any rule that should apply to this group
            ("ignore job posts"). For a group per customer, the customer's description. Null: the workspace profile, as for
            every keyword before groups.
    """

    name: str
    external_id: None | str | Unset = UNSET
    context: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        context: None | str | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        create_group_body = cls(
            name=name,
            external_id=external_id,
            context=context,
        )

        create_group_body.additional_properties = d
        return create_group_body

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
