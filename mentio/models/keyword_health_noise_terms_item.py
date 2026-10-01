from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordHealthNoiseTermsItem")


@_attrs_define
class KeywordHealthNoiseTermsItem:
    """
    Attributes:
        term (str): A word or two-word phrase.
        noise_posts (int): Sampled noise posts that carry it.
        relevant_posts (int): Sampled relevant posts that carry it.
        lift (float | None): How many times more common it is in noise than in relevant posts (smoothed); null with no
            relevant post to compare.
    """

    term: str
    noise_posts: int
    relevant_posts: int
    lift: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        noise_posts = self.noise_posts

        relevant_posts = self.relevant_posts

        lift: float | None
        lift = self.lift

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "term": term,
                "noisePosts": noise_posts,
                "relevantPosts": relevant_posts,
                "lift": lift,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        term = d.pop("term")

        noise_posts = d.pop("noisePosts")

        relevant_posts = d.pop("relevantPosts")

        def _parse_lift(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        lift = _parse_lift(d.pop("lift"))

        keyword_health_noise_terms_item = cls(
            term=term,
            noise_posts=noise_posts,
            relevant_posts=relevant_posts,
            lift=lift,
        )

        keyword_health_noise_terms_item.additional_properties = d
        return keyword_health_noise_terms_item

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
