from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_company_body_accounts import UpdateCompanyBodyAccounts


T = TypeVar("T", bound="UpdateCompanyBody")


@_attrs_define
class UpdateCompanyBody:
    """Omitted fields are untouched.

    Attributes:
        name (str | Unset):
        description (str | Unset):
        use_cases (list[str] | Unset): Replaces the whole list.
        accounts (UpdateCompanyBodyAccounts | Unset):
        context (str | Unset): Overrides the composed context until the next profile edit.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    use_cases: list[str] | Unset = UNSET
    accounts: UpdateCompanyBodyAccounts | Unset = UNSET
    context: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        use_cases: list[str] | Unset = UNSET
        if not isinstance(self.use_cases, Unset):
            use_cases = self.use_cases

        accounts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = self.accounts.to_dict()

        context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if use_cases is not UNSET:
            field_dict["useCases"] = use_cases
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_company_body_accounts import (
            UpdateCompanyBodyAccounts,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        use_cases = cast(list[str], d.pop("useCases", UNSET))

        _accounts = d.pop("accounts", UNSET)
        accounts: UpdateCompanyBodyAccounts | Unset
        if isinstance(_accounts, Unset):
            accounts = UNSET
        else:
            accounts = UpdateCompanyBodyAccounts.from_dict(_accounts)

        context = d.pop("context", UNSET)

        update_company_body = cls(
            name=name,
            description=description,
            use_cases=use_cases,
            accounts=accounts,
            context=context,
        )

        update_company_body.additional_properties = d
        return update_company_body

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
