from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LedgerListDataItemTransferType0")


@_attrs_define
class LedgerListDataItemTransferType0:
    """transfer_in and transfer_out rows: the transfer and the other workspace; null on every other row.

    Attributes:
        id (str): Transfer id (trf_...); the other workspace's row carries the same id.
        workspace_id (str): The other workspace of the transfer (org_...): the child it funded, or the parent it came
            from.
    """

    id: str
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspaceId": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspaceId")

        ledger_list_data_item_transfer_type_0 = cls(
            id=id,
            workspace_id=workspace_id,
        )

        ledger_list_data_item_transfer_type_0.additional_properties = d
        return ledger_list_data_item_transfer_type_0

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
