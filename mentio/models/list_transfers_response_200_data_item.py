from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_transfers_response_200_data_item_direction import (
    ListTransfersResponse200DataItemDirection,
)

T = TypeVar("T", bound="ListTransfersResponse200DataItem")


@_attrs_define
class ListTransfersResponse200DataItem:
    """
    Attributes:
        id (str): Transfer id (trf_...).
        workspace_id (str): The child workspace (org_...).
        direction (ListTransfersResponse200DataItemDirection): to_workspace: from the parent into the child workspace.
            to_parent: from the child back to the parent.
        amount_cents (int): How much moved, in USD cents, always positive; `direction` says which way.
        note (None | str): Free text written with it; automatic refills read "Automatic refill".
        created_at (str): When the money moved.
    """

    id: str
    workspace_id: str
    direction: ListTransfersResponse200DataItemDirection
    amount_cents: int
    note: None | str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        direction = self.direction.value

        amount_cents = self.amount_cents

        note: None | str
        note = self.note

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspaceId": workspace_id,
                "direction": direction,
                "amountCents": amount_cents,
                "note": note,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspaceId")

        direction = ListTransfersResponse200DataItemDirection(d.pop("direction"))

        amount_cents = d.pop("amountCents")

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        created_at = d.pop("createdAt")

        list_transfers_response_200_data_item = cls(
            id=id,
            workspace_id=workspace_id,
            direction=direction,
            amount_cents=amount_cents,
            note=note,
            created_at=created_at,
        )

        list_transfers_response_200_data_item.additional_properties = d
        return list_transfers_response_200_data_item

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
