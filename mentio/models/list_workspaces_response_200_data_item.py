from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_workspaces_response_200_data_item_funding import (
        ListWorkspacesResponse200DataItemFunding,
    )
    from ..models.list_workspaces_response_200_data_item_stats import (
        ListWorkspacesResponse200DataItemStats,
    )
    from ..models.list_workspaces_response_200_data_item_wallet import (
        ListWorkspacesResponse200DataItemWallet,
    )


T = TypeVar("T", bound="ListWorkspacesResponse200DataItem")


@_attrs_define
class ListWorkspacesResponse200DataItem:
    """
    Attributes:
        id (str): Workspace id (org_...); send it as the Mentio-Workspace header to act on this workspace with the
            parent's credential.
        name (str): The workspace name.
        external_id (None | str): Your own id for this workspace (a customer id), unique among your workspaces; null
            when unset.
        parent_id (str): The parent workspace (org_...) that created and funds it.
        created_at (str): When the workspace was created.
        wallet (ListWorkspacesResponse200DataItemWallet): The child's own wallet. A child spends only what it holds;
            nothing is pooled with the parent.
        funding (ListWorkspacesResponse200DataItemFunding): How the parent funds this workspace.
        stats (ListWorkspacesResponse200DataItemStats): Counts.
    """

    id: str
    name: str
    external_id: None | str
    parent_id: str
    created_at: str
    wallet: ListWorkspacesResponse200DataItemWallet
    funding: ListWorkspacesResponse200DataItemFunding
    stats: ListWorkspacesResponse200DataItemStats
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        external_id: None | str
        external_id = self.external_id

        parent_id = self.parent_id

        created_at = self.created_at

        wallet = self.wallet.to_dict()

        funding = self.funding.to_dict()

        stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "externalId": external_id,
                "parentId": parent_id,
                "createdAt": created_at,
                "wallet": wallet,
                "funding": funding,
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_workspaces_response_200_data_item_funding import (
            ListWorkspacesResponse200DataItemFunding,
        )
        from ..models.list_workspaces_response_200_data_item_stats import (
            ListWorkspacesResponse200DataItemStats,
        )
        from ..models.list_workspaces_response_200_data_item_wallet import (
            ListWorkspacesResponse200DataItemWallet,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_id = _parse_external_id(d.pop("externalId"))

        parent_id = d.pop("parentId")

        created_at = d.pop("createdAt")

        wallet = ListWorkspacesResponse200DataItemWallet.from_dict(d.pop("wallet"))

        funding = ListWorkspacesResponse200DataItemFunding.from_dict(d.pop("funding"))

        stats = ListWorkspacesResponse200DataItemStats.from_dict(d.pop("stats"))

        list_workspaces_response_200_data_item = cls(
            id=id,
            name=name,
            external_id=external_id,
            parent_id=parent_id,
            created_at=created_at,
            wallet=wallet,
            funding=funding,
            stats=stats,
        )

        list_workspaces_response_200_data_item.additional_properties = d
        return list_workspaces_response_200_data_item

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
