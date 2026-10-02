from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.keyword_noisy_event_data_keyword import KeywordNoisyEventDataKeyword


T = TypeVar("T", bound="KeywordNoisyEventData")


@_attrs_define
class KeywordNoisyEventData:
    """
    Attributes:
        attention_id (str): The attention item (att_...): GET /v1/attention lists it, POST /v1/attention/{id}/dismiss
            puts it away.
        url (str): Where to look in the dashboard.
        keyword (KeywordNoisyEventDataKeyword): The keyword the item is about.
        window_days (int): The window the noise is measured over, in days (since the keyword's last change when that is
            inside it).
        scored (int): Matches the classifier scored in that window.
        relevant (int): Of those, relevant.
        noise_share (float): The share scored under the relevance line. Every match bills, relevant or not.
    """

    attention_id: str
    url: str
    keyword: KeywordNoisyEventDataKeyword
    window_days: int
    scored: int
    relevant: int
    noise_share: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attention_id = self.attention_id

        url = self.url

        keyword = self.keyword.to_dict()

        window_days = self.window_days

        scored = self.scored

        relevant = self.relevant

        noise_share = self.noise_share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attentionId": attention_id,
                "url": url,
                "keyword": keyword,
                "windowDays": window_days,
                "scored": scored,
                "relevant": relevant,
                "noiseShare": noise_share,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_noisy_event_data_keyword import (
            KeywordNoisyEventDataKeyword,
        )

        d = dict(src_dict)
        attention_id = d.pop("attentionId")

        url = d.pop("url")

        keyword = KeywordNoisyEventDataKeyword.from_dict(d.pop("keyword"))

        window_days = d.pop("windowDays")

        scored = d.pop("scored")

        relevant = d.pop("relevant")

        noise_share = d.pop("noiseShare")

        keyword_noisy_event_data = cls(
            attention_id=attention_id,
            url=url,
            keyword=keyword,
            window_days=window_days,
            scored=scored,
            relevant=relevant,
            noise_share=noise_share,
        )

        keyword_noisy_event_data.additional_properties = d
        return keyword_noisy_event_data

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
