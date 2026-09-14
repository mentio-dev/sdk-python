from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.company_accounts import CompanyAccounts


T = TypeVar("T", bound="Company")


@_attrs_define
class Company:
    """
    Attributes:
        name (str): Brand or company name, as the classifier should call it.
        description (str): What the company does, one paragraph.
        use_cases (list[str]): What people use the product for.
        accounts (CompanyAccounts): Your own accounts, so your own posts are recognized.
        context (str): The text the classifier reads. Composed from the fields above unless you override it.
    """

    name: str
    description: str
    use_cases: list[str]
    accounts: CompanyAccounts
    context: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        use_cases = self.use_cases

        accounts = self.accounts.to_dict()

        context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "useCases": use_cases,
                "accounts": accounts,
                "context": context,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.company_accounts import CompanyAccounts

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        use_cases = cast(list[str], d.pop("useCases"))

        accounts = CompanyAccounts.from_dict(d.pop("accounts"))

        context = d.pop("context")

        company = cls(
            name=name,
            description=description,
            use_cases=use_cases,
            accounts=accounts,
            context=context,
        )

        company.additional_properties = d
        return company

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
