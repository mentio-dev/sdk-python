from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.negative_spike_event_data_baseline import (
        NegativeSpikeEventDataBaseline,
    )
    from ..models.negative_spike_event_data_keyword import NegativeSpikeEventDataKeyword
    from ..models.negative_spike_event_data_window import NegativeSpikeEventDataWindow


T = TypeVar("T", bound="NegativeSpikeEventData")


@_attrs_define
class NegativeSpikeEventData:
    """
    Attributes:
        attention_id (str): The attention item (att_...): GET /v1/attention lists it, POST /v1/attention/{id}/dismiss
            puts it away.
        url (str): Where to look in the dashboard.
        keyword (NegativeSpikeEventDataKeyword): The keyword the item is about.
        window (NegativeSpikeEventDataWindow): The stretch of time the counts cover, by match time.
        negative (int): Relevant matches scored negative in the window.
        relevant (int): Relevant matches in the window.
        share (float): negative / relevant.
        baseline (NegativeSpikeEventDataBaseline): What the keyword usually reads.
    """

    attention_id: str
    url: str
    keyword: NegativeSpikeEventDataKeyword
    window: NegativeSpikeEventDataWindow
    negative: int
    relevant: int
    share: float
    baseline: NegativeSpikeEventDataBaseline
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attention_id = self.attention_id

        url = self.url

        keyword = self.keyword.to_dict()

        window = self.window.to_dict()

        negative = self.negative

        relevant = self.relevant

        share = self.share

        baseline = self.baseline.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attentionId": attention_id,
                "url": url,
                "keyword": keyword,
                "window": window,
                "negative": negative,
                "relevant": relevant,
                "share": share,
                "baseline": baseline,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.negative_spike_event_data_baseline import (
            NegativeSpikeEventDataBaseline,
        )
        from ..models.negative_spike_event_data_keyword import (
            NegativeSpikeEventDataKeyword,
        )
        from ..models.negative_spike_event_data_window import (
            NegativeSpikeEventDataWindow,
        )

        d = dict(src_dict)
        attention_id = d.pop("attentionId")

        url = d.pop("url")

        keyword = NegativeSpikeEventDataKeyword.from_dict(d.pop("keyword"))

        window = NegativeSpikeEventDataWindow.from_dict(d.pop("window"))

        negative = d.pop("negative")

        relevant = d.pop("relevant")

        share = d.pop("share")

        baseline = NegativeSpikeEventDataBaseline.from_dict(d.pop("baseline"))

        negative_spike_event_data = cls(
            attention_id=attention_id,
            url=url,
            keyword=keyword,
            window=window,
            negative=negative,
            relevant=relevant,
            share=share,
            baseline=baseline,
        )

        negative_spike_event_data.additional_properties = d
        return negative_spike_event_data

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
