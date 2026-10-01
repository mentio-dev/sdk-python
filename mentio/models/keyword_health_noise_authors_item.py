from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordHealthNoiseAuthorsItem")


@_attrs_define
class KeywordHealthNoiseAuthorsItem:
    """
    Attributes:
        name (str): The author as the platform shows them.
        entry (str): What matching.excludedAuthors would store for them.
        noise_posts (int): Sampled noise posts by them.
    """

    name: str
    entry: str
    noise_posts: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        entry = self.entry

        noise_posts = self.noise_posts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "entry": entry,
                "noisePosts": noise_posts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        entry = d.pop("entry")

        noise_posts = d.pop("noisePosts")

        keyword_health_noise_authors_item = cls(
            name=name,
            entry=entry,
            noise_posts=noise_posts,
        )

        keyword_health_noise_authors_item.additional_properties = d
        return keyword_health_noise_authors_item

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
