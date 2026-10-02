from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mention_spike_event_data_baseline import MentionSpikeEventDataBaseline
    from ..models.mention_spike_event_data_keyword import MentionSpikeEventDataKeyword
    from ..models.mention_spike_event_data_window import MentionSpikeEventDataWindow


T = TypeVar("T", bound="MentionSpikeEventData")


@_attrs_define
class MentionSpikeEventData:
    """
    Attributes:
        attention_id (str): The attention item (att_...): GET /v1/attention lists it, POST /v1/attention/{id}/dismiss
            puts it away.
        url (str): Where to look in the dashboard.
        keyword (MentionSpikeEventDataKeyword): The keyword the item is about.
        window (MentionSpikeEventDataWindow): The stretch of time the counts cover, by match time.
        matches (int): Fresh matches in the hour: posts published at most 6 hours before they matched. Look-backs and
            free reviews never count.
        relevant (int): Of those, scored relevant so far.
        baseline (MentionSpikeEventDataBaseline): What the keyword usually gets.
    """

    attention_id: str
    url: str
    keyword: MentionSpikeEventDataKeyword
    window: MentionSpikeEventDataWindow
    matches: int
    relevant: int
    baseline: MentionSpikeEventDataBaseline
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attention_id = self.attention_id

        url = self.url

        keyword = self.keyword.to_dict()

        window = self.window.to_dict()

        matches = self.matches

        relevant = self.relevant

        baseline = self.baseline.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attentionId": attention_id,
                "url": url,
                "keyword": keyword,
                "window": window,
                "matches": matches,
                "relevant": relevant,
                "baseline": baseline,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mention_spike_event_data_baseline import (
            MentionSpikeEventDataBaseline,
        )
        from ..models.mention_spike_event_data_keyword import (
            MentionSpikeEventDataKeyword,
        )
        from ..models.mention_spike_event_data_window import (
            MentionSpikeEventDataWindow,
        )

        d = dict(src_dict)
        attention_id = d.pop("attentionId")

        url = d.pop("url")

        keyword = MentionSpikeEventDataKeyword.from_dict(d.pop("keyword"))

        window = MentionSpikeEventDataWindow.from_dict(d.pop("window"))

        matches = d.pop("matches")

        relevant = d.pop("relevant")

        baseline = MentionSpikeEventDataBaseline.from_dict(d.pop("baseline"))

        mention_spike_event_data = cls(
            attention_id=attention_id,
            url=url,
            keyword=keyword,
            window=window,
            matches=matches,
            relevant=relevant,
            baseline=baseline,
        )

        mention_spike_event_data.additional_properties = d
        return mention_spike_event_data

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
