from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_workspace_body_auto_refill_type_0 import (
        CreateWorkspaceBodyAutoRefillType0,
    )


T = TypeVar("T", bound="CreateWorkspaceBody")


@_attrs_define
class CreateWorkspaceBody:
    """
    Attributes:
        name (str): The workspace name, 1 to 100 characters.
        external_id (str | Unset): Your own id for it (a customer id), unique among your workspaces; a second create
            with the same one is a 409.
        monthly_limit_cents (int | None | Unset): The most you move into it in a UTC calendar month, in USD cents; omit
            or null for no limit.
        auto_refill (CreateWorkspaceBodyAutoRefillType0 | None | Unset): Refill it from your balance when it runs low;
            omit or null for off.
    """

    name: str
    external_id: str | Unset = UNSET
    monthly_limit_cents: int | None | Unset = UNSET
    auto_refill: CreateWorkspaceBodyAutoRefillType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_workspace_body_auto_refill_type_0 import (
            CreateWorkspaceBodyAutoRefillType0,
        )

        name = self.name

        external_id = self.external_id

        monthly_limit_cents: int | None | Unset
        if isinstance(self.monthly_limit_cents, Unset):
            monthly_limit_cents = UNSET
        else:
            monthly_limit_cents = self.monthly_limit_cents

        auto_refill: dict[str, Any] | None | Unset
        if isinstance(self.auto_refill, Unset):
            auto_refill = UNSET
        elif isinstance(self.auto_refill, CreateWorkspaceBodyAutoRefillType0):
            auto_refill = self.auto_refill.to_dict()
        else:
            auto_refill = self.auto_refill

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if monthly_limit_cents is not UNSET:
            field_dict["monthlyLimitCents"] = monthly_limit_cents
        if auto_refill is not UNSET:
            field_dict["autoRefill"] = auto_refill

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_workspace_body_auto_refill_type_0 import (
            CreateWorkspaceBodyAutoRefillType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        external_id = d.pop("externalId", UNSET)

        def _parse_monthly_limit_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        monthly_limit_cents = _parse_monthly_limit_cents(
            d.pop("monthlyLimitCents", UNSET)
        )

        def _parse_auto_refill(
            data: object,
        ) -> CreateWorkspaceBodyAutoRefillType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auto_refill_type_0 = CreateWorkspaceBodyAutoRefillType0.from_dict(data)

                return auto_refill_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateWorkspaceBodyAutoRefillType0 | None | Unset, data)

        auto_refill = _parse_auto_refill(d.pop("autoRefill", UNSET))

        create_workspace_body = cls(
            name=name,
            external_id=external_id,
            monthly_limit_cents=monthly_limit_cents,
            auto_refill=auto_refill,
        )

        create_workspace_body.additional_properties = d
        return create_workspace_body

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
