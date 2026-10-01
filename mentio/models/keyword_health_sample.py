from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordHealthSample")


@_attrs_define
class KeywordHealthSample:
    """The posts behind noiseTerms, noiseAuthors and the effects, after the keyword's current rules (a post an older rule
    let in is not counted). Review platforms are matched by app, not by text, and are left out.

        Attributes:
            noise (int): Noise posts read (the newest of the window, or since stats.judgedSince, at most 200), on platforms
                matched by text. None under 20 scored matches since a change.
            relevant (int): Relevant posts read, likewise.
    """

    noise: int
    relevant: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        noise = self.noise

        relevant = self.relevant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "noise": noise,
                "relevant": relevant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        noise = d.pop("noise")

        relevant = d.pop("relevant")

        keyword_health_sample = cls(
            noise=noise,
            relevant=relevant,
        )

        keyword_health_sample.additional_properties = d
        return keyword_health_sample

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
