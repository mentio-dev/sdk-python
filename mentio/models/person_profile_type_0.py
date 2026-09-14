from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.person_profile_type_0_links_item import PersonProfileType0LinksItem


T = TypeVar("T", bound="PersonProfileType0")


@_attrs_define
class PersonProfileType0:
    """Public profile facts; null until looked up.

    Attributes:
        bio (None | str):
        company (None | str):
        location (None | str):
        website (None | str):
        email (None | str): Only when the person made it public on the platform.
        links (list[PersonProfileType0LinksItem]): Other accounts the person lists on their profile.
        fetched_at (str): When the profile was read.
    """

    bio: None | str
    company: None | str
    location: None | str
    website: None | str
    email: None | str
    links: list[PersonProfileType0LinksItem]
    fetched_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bio: None | str
        bio = self.bio

        company: None | str
        company = self.company

        location: None | str
        location = self.location

        website: None | str
        website = self.website

        email: None | str
        email = self.email

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        fetched_at = self.fetched_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bio": bio,
                "company": company,
                "location": location,
                "website": website,
                "email": email,
                "links": links,
                "fetchedAt": fetched_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.person_profile_type_0_links_item import (
            PersonProfileType0LinksItem,
        )

        d = dict(src_dict)

        def _parse_bio(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bio = _parse_bio(d.pop("bio"))

        def _parse_company(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company = _parse_company(d.pop("company"))

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_website(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website = _parse_website(d.pop("website"))

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = PersonProfileType0LinksItem.from_dict(links_item_data)

            links.append(links_item)

        fetched_at = d.pop("fetchedAt")

        person_profile_type_0 = cls(
            bio=bio,
            company=company,
            location=location,
            website=website,
            email=email,
            links=links,
            fetched_at=fetched_at,
        )

        person_profile_type_0.additional_properties = d
        return person_profile_type_0

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
