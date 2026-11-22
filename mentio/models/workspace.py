from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workspace_funding import WorkspaceFunding
    from ..models.workspace_stats import WorkspaceStats
    from ..models.workspace_wallet import WorkspaceWallet


T = TypeVar("T", bound="Workspace")


@_attrs_define
class Workspace:
    """
    Attributes:
        id (str): Workspace id (org_...); send it as the Mentio-Workspace header to act on this workspace with the
            parent's credential.
        name (str): The workspace name.
        external_id (None | str): Your own id for this workspace (a customer id), unique among your workspaces; null
            when unset.
        parent_id (str): The parent workspace (org_...) that created and funds it.
        created_at (str): When the workspace was created.
        wallet (WorkspaceWallet): The child's own wallet. A child spends only what it holds; nothing is pooled with the
            parent.
        funding (WorkspaceFunding): How the parent funds this workspace.
        stats (WorkspaceStats): Counts.
    """

    id: str
    name: str
    external_id: None | str
    parent_id: str
    created_at: str
    wallet: WorkspaceWallet
    funding: WorkspaceFunding
    stats: WorkspaceStats
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
        from ..models.workspace_funding import WorkspaceFunding
        from ..models.workspace_stats import WorkspaceStats
        from ..models.workspace_wallet import WorkspaceWallet

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

        wallet = WorkspaceWallet.from_dict(d.pop("wallet"))

        funding = WorkspaceFunding.from_dict(d.pop("funding"))

        stats = WorkspaceStats.from_dict(d.pop("stats"))

        workspace = cls(
            id=id,
            name=name,
            external_id=external_id,
            parent_id=parent_id,
            created_at=created_at,
            wallet=wallet,
            funding=funding,
            stats=stats,
        )

        workspace.additional_properties = d
        return workspace

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
