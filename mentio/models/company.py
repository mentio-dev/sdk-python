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
        website (None | str): The company website, as set up during onboarding.
        competitors (list[str]): Competitors by name, so the classifier reads a rival's mention as such; usually the
            same names as your competitor keywords.
        guidelines (None | str): Free-text rules for the classifier: what counts as relevant for you and what never does
            ("posts about our API, never job listings"). The second biggest lever after the description.
        context (str): The text the classifier reads. Composed from the fields above unless you override it.
    """

    name: str
    description: str
    use_cases: list[str]
    accounts: CompanyAccounts
    website: None | str
    competitors: list[str]
    guidelines: None | str
    context: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        use_cases = self.use_cases

        accounts = self.accounts.to_dict()

        website: None | str
        website = self.website

        competitors = self.competitors

        guidelines: None | str
        guidelines = self.guidelines

        context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "useCases": use_cases,
                "accounts": accounts,
                "website": website,
                "competitors": competitors,
                "guidelines": guidelines,
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

        def _parse_website(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website = _parse_website(d.pop("website"))

        competitors = cast(list[str], d.pop("competitors"))

        def _parse_guidelines(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        guidelines = _parse_guidelines(d.pop("guidelines"))

        context = d.pop("context")

        company = cls(
            name=name,
            description=description,
            use_cases=use_cases,
            accounts=accounts,
            website=website,
            competitors=competitors,
            guidelines=guidelines,
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
