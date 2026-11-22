from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.topic_cluster_event_data_baseline import TopicClusterEventDataBaseline
    from ..models.topic_cluster_event_data_keyword import TopicClusterEventDataKeyword
    from ..models.topic_cluster_event_data_tag import TopicClusterEventDataTag
    from ..models.topic_cluster_event_data_window import TopicClusterEventDataWindow


T = TypeVar("T", bound="TopicClusterEventData")


@_attrs_define
class TopicClusterEventData:
    """
    Attributes:
        attention_id (str): The attention item (att_...): GET /v1/attention lists it, POST /v1/attention/{id}/dismiss
            puts it away.
        url (str): Where to look in the dashboard.
        keyword (TopicClusterEventDataKeyword): The keyword the item is about.
        window (TopicClusterEventDataWindow): The stretch of time the counts cover, by match time.
        tag (TopicClusterEventDataTag): What the posts share.
        count (int): Relevant posts of the window carrying it (posts at most 3 days old when matched).
        authors (int): Different authors among them.
        baseline (TopicClusterEventDataBaseline): What the keyword usually gets.
    """

    attention_id: str
    url: str
    keyword: TopicClusterEventDataKeyword
    window: TopicClusterEventDataWindow
    tag: TopicClusterEventDataTag
    count: int
    authors: int
    baseline: TopicClusterEventDataBaseline
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attention_id = self.attention_id

        url = self.url

        keyword = self.keyword.to_dict()

        window = self.window.to_dict()

        tag = self.tag.to_dict()

        count = self.count

        authors = self.authors

        baseline = self.baseline.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attentionId": attention_id,
                "url": url,
                "keyword": keyword,
                "window": window,
                "tag": tag,
                "count": count,
                "authors": authors,
                "baseline": baseline,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.topic_cluster_event_data_baseline import (
            TopicClusterEventDataBaseline,
        )
        from ..models.topic_cluster_event_data_keyword import (
            TopicClusterEventDataKeyword,
        )
        from ..models.topic_cluster_event_data_tag import TopicClusterEventDataTag
        from ..models.topic_cluster_event_data_window import TopicClusterEventDataWindow

        d = dict(src_dict)
        attention_id = d.pop("attentionId")

        url = d.pop("url")

        keyword = TopicClusterEventDataKeyword.from_dict(d.pop("keyword"))

        window = TopicClusterEventDataWindow.from_dict(d.pop("window"))

        tag = TopicClusterEventDataTag.from_dict(d.pop("tag"))

        count = d.pop("count")

        authors = d.pop("authors")

        baseline = TopicClusterEventDataBaseline.from_dict(d.pop("baseline"))

        topic_cluster_event_data = cls(
            attention_id=attention_id,
            url=url,
            keyword=keyword,
            window=window,
            tag=tag,
            count=count,
            authors=authors,
            baseline=baseline,
        )

        topic_cluster_event_data.additional_properties = d
        return topic_cluster_event_data

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
