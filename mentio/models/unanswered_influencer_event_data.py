from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.unanswered_influencer_event_data_author import (
        UnansweredInfluencerEventDataAuthor,
    )
    from ..models.unanswered_influencer_event_data_keyword import (
        UnansweredInfluencerEventDataKeyword,
    )
    from ..models.unanswered_influencer_event_data_mention import (
        UnansweredInfluencerEventDataMention,
    )


T = TypeVar("T", bound="UnansweredInfluencerEventData")


@_attrs_define
class UnansweredInfluencerEventData:
    """
    Attributes:
        attention_id (str): The attention item (att_...): GET /v1/attention lists it, POST /v1/attention/{id}/dismiss
            puts it away.
        url (str): Where to look in the dashboard.
        author (UnansweredInfluencerEventDataAuthor): Who posted.
        keyword (UnansweredInfluencerEventDataKeyword): The keyword the item is about.
        mentions (int): Their relevant mentions of the last 48 hours still open (not done or ignored) 3 hours or more
            after they matched.
        mention (UnansweredInfluencerEventDataMention): The newest open mention, the one to answer first.
    """

    attention_id: str
    url: str
    author: UnansweredInfluencerEventDataAuthor
    keyword: UnansweredInfluencerEventDataKeyword
    mentions: int
    mention: UnansweredInfluencerEventDataMention
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attention_id = self.attention_id

        url = self.url

        author = self.author.to_dict()

        keyword = self.keyword.to_dict()

        mentions = self.mentions

        mention = self.mention.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attentionId": attention_id,
                "url": url,
                "author": author,
                "keyword": keyword,
                "mentions": mentions,
                "mention": mention,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.unanswered_influencer_event_data_author import (
            UnansweredInfluencerEventDataAuthor,
        )
        from ..models.unanswered_influencer_event_data_keyword import (
            UnansweredInfluencerEventDataKeyword,
        )
        from ..models.unanswered_influencer_event_data_mention import (
            UnansweredInfluencerEventDataMention,
        )

        d = dict(src_dict)
        attention_id = d.pop("attentionId")

        url = d.pop("url")

        author = UnansweredInfluencerEventDataAuthor.from_dict(d.pop("author"))

        keyword = UnansweredInfluencerEventDataKeyword.from_dict(d.pop("keyword"))

        mentions = d.pop("mentions")

        mention = UnansweredInfluencerEventDataMention.from_dict(d.pop("mention"))

        unanswered_influencer_event_data = cls(
            attention_id=attention_id,
            url=url,
            author=author,
            keyword=keyword,
            mentions=mentions,
            mention=mention,
        )

        unanswered_influencer_event_data.additional_properties = d
        return unanswered_influencer_event_data

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
