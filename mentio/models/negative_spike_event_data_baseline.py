from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NegativeSpikeEventDataBaseline")


@_attrs_define
class NegativeSpikeEventDataBaseline:
    """What the keyword usually reads.

    Attributes:
        negative (int): Negative relevant matches in the 7 days before the window.
        relevant (int): Relevant matches in those 7 days.
        share (float): The usual negative share, smoothed so a quiet week still has one.
    """

    negative: int
    relevant: int
    share: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        negative = self.negative

        relevant = self.relevant

        share = self.share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "negative": negative,
                "relevant": relevant,
                "share": share,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        negative = d.pop("negative")

        relevant = d.pop("relevant")

        share = d.pop("share")

        negative_spike_event_data_baseline = cls(
            negative=negative,
            relevant=relevant,
            share=share,
        )

        negative_spike_event_data_baseline.additional_properties = d
        return negative_spike_event_data_baseline

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
