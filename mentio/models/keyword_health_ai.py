from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_health_ai_status import KeywordHealthAiStatus

T = TypeVar("T", bound="KeywordHealthAi")


@_attrs_define
class KeywordHealthAi:
    """The optional language model half of the report.

    Attributes:
        requested (bool): ai=true was asked.
        status (KeywordHealthAiStatus): off: not asked. generated: written now. cached: written earlier today for the
            same keyword, window and settings. unavailable: the model failed, answered nothing usable or is not configured.
            rate_limited: the workspace's 20 model calls this hour are spent.
    """

    requested: bool
    status: KeywordHealthAiStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested = self.requested

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requested": requested,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        requested = d.pop("requested")

        status = KeywordHealthAiStatus(d.pop("status"))

        keyword_health_ai = cls(
            requested=requested,
            status=status,
        )

        keyword_health_ai.additional_properties = d
        return keyword_health_ai

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
