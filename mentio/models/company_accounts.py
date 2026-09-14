from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompanyAccounts")


@_attrs_define
class CompanyAccounts:
    """Your own accounts, so your own posts are recognized.

    Attributes:
        x (None | str): X handle without the @.
        linkedin (None | str): LinkedIn page slug or URL.
    """

    x: None | str
    linkedin: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x: None | str
        x = self.x

        linkedin: None | str
        linkedin = self.linkedin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "x": x,
                "linkedin": linkedin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_x(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        x = _parse_x(d.pop("x"))

        def _parse_linkedin(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin = _parse_linkedin(d.pop("linkedin"))

        company_accounts = cls(
            x=x,
            linkedin=linkedin,
        )

        company_accounts.additional_properties = d
        return company_accounts

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
