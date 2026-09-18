from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeywordStatsFeedback")


@_attrs_define
class KeywordStatsFeedback:
    """Your verdicts on this keyword's mentions (PATCH /v1/mentions/{id} relevant).

    Attributes:
        relevant (int): Mentions a person marked relevant.
        not_relevant (int): Mentions a person marked not relevant: the noise the classifier let through.
    """

    relevant: int
    not_relevant: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relevant = self.relevant

        not_relevant = self.not_relevant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relevant": relevant,
                "notRelevant": not_relevant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        relevant = d.pop("relevant")

        not_relevant = d.pop("notRelevant")

        keyword_stats_feedback = cls(
            relevant=relevant,
            not_relevant=not_relevant,
        )

        keyword_stats_feedback.additional_properties = d
        return keyword_stats_feedback

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
