from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_workspace_body_auto_refill_type_0 import (
        UpdateWorkspaceBodyAutoRefillType0,
    )


T = TypeVar("T", bound="UpdateWorkspaceBody")


@_attrs_define
class UpdateWorkspaceBody:
    """
    Attributes:
        name (str | Unset): New name, 1 to 100 characters.
        external_id (None | str | Unset): Your own id for it; null clears it.
        monthly_limit_cents (int | None | Unset): The monthly ceiling on transfers in, in USD cents; null removes it.
        auto_refill (None | Unset | UpdateWorkspaceBodyAutoRefillType0): The automatic refill; null turns it off.
    """

    name: str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    monthly_limit_cents: int | None | Unset = UNSET
    auto_refill: None | Unset | UpdateWorkspaceBodyAutoRefillType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_workspace_body_auto_refill_type_0 import (
            UpdateWorkspaceBodyAutoRefillType0,
        )

        name = self.name

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        monthly_limit_cents: int | None | Unset
        if isinstance(self.monthly_limit_cents, Unset):
            monthly_limit_cents = UNSET
        else:
            monthly_limit_cents = self.monthly_limit_cents

        auto_refill: dict[str, Any] | None | Unset
        if isinstance(self.auto_refill, Unset):
            auto_refill = UNSET
        elif isinstance(self.auto_refill, UpdateWorkspaceBodyAutoRefillType0):
            auto_refill = self.auto_refill.to_dict()
        else:
            auto_refill = self.auto_refill

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if monthly_limit_cents is not UNSET:
            field_dict["monthlyLimitCents"] = monthly_limit_cents
        if auto_refill is not UNSET:
            field_dict["autoRefill"] = auto_refill

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_workspace_body_auto_refill_type_0 import (
            UpdateWorkspaceBodyAutoRefillType0,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

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
        ) -> None | Unset | UpdateWorkspaceBodyAutoRefillType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auto_refill_type_0 = UpdateWorkspaceBodyAutoRefillType0.from_dict(data)

                return auto_refill_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateWorkspaceBodyAutoRefillType0, data)

        auto_refill = _parse_auto_refill(d.pop("autoRefill", UNSET))

        update_workspace_body = cls(
            name=name,
            external_id=external_id,
            monthly_limit_cents=monthly_limit_cents,
            auto_refill=auto_refill,
        )

        update_workspace_body.additional_properties = d
        return update_workspace_body

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
