from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MuteAlertAuthorsBody")


@_attrs_define
class MuteAlertAuthorsBody:
    """Authors to add to or remove from the alert's muted list.

    Attributes:
        authors (list[str]): Profile or post links (x.com/name, linkedin.com/in/name, reddit.com/user/name, a post URL),
            handles (@name, u/name), Bluesky DIDs or display names. A link is stored as the author's profile; a plain name
            or handle matches that name on every platform.
    """

    authors: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authors = self.authors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authors": authors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        authors = cast(list[str], d.pop("authors"))

        mute_alert_authors_body = cls(
            authors=authors,
        )

        mute_alert_authors_body.additional_properties = d
        return mute_alert_authors_body

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
