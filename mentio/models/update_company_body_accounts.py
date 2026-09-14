from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCompanyBodyAccounts")


@_attrs_define
class UpdateCompanyBodyAccounts:
    """
    Attributes:
        x (None | str | Unset):
        linkedin (None | str | Unset):
    """

    x: None | str | Unset = UNSET
    linkedin: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x: None | str | Unset
        if isinstance(self.x, Unset):
            x = UNSET
        else:
            x = self.x

        linkedin: None | str | Unset
        if isinstance(self.linkedin, Unset):
            linkedin = UNSET
        else:
            linkedin = self.linkedin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if linkedin is not UNSET:
            field_dict["linkedin"] = linkedin

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_x(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        x = _parse_x(d.pop("x", UNSET))

        def _parse_linkedin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin = _parse_linkedin(d.pop("linkedin", UNSET))

        update_company_body_accounts = cls(
            x=x,
            linkedin=linkedin,
        )

        update_company_body_accounts.additional_properties = d
        return update_company_body_accounts

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
