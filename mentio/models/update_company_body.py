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
        website (None | str | Unset): The company website; null clears it.
        competitors (list[str] | Unset): Replaces the whole list; [] clears it.
        guidelines (None | str | Unset): Free-text rules for the classifier; null clears them.
        context (str | Unset): Overrides the composed context until the next profile edit.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    use_cases: list[str] | Unset = UNSET
    accounts: UpdateCompanyBodyAccounts | Unset = UNSET
    website: None | str | Unset = UNSET
    competitors: list[str] | Unset = UNSET
    guidelines: None | str | Unset = UNSET
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

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        competitors: list[str] | Unset = UNSET
        if not isinstance(self.competitors, Unset):
            competitors = self.competitors

        guidelines: None | str | Unset
        if isinstance(self.guidelines, Unset):
            guidelines = UNSET
        else:
            guidelines = self.guidelines

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
        if website is not UNSET:
            field_dict["website"] = website
        if competitors is not UNSET:
            field_dict["competitors"] = competitors
        if guidelines is not UNSET:
            field_dict["guidelines"] = guidelines
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

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        competitors = cast(list[str], d.pop("competitors", UNSET))

        def _parse_guidelines(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guidelines = _parse_guidelines(d.pop("guidelines", UNSET))

        context = d.pop("context", UNSET)

        update_company_body = cls(
            name=name,
            description=description,
            use_cases=use_cases,
            accounts=accounts,
            website=website,
            competitors=competitors,
            guidelines=guidelines,
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
