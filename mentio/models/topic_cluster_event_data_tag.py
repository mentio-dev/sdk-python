from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.topic_cluster_event_data_tag_type import TopicClusterEventDataTagType

T = TypeVar("T", bound="TopicClusterEventDataTag")


@_attrs_define
class TopicClusterEventDataTag:
    """What the posts share.

    Attributes:
        type_ (TopicClusterEventDataTagType): intent: a tag the classifier gave (question, complaint, comparison...).
            hashtag: a hashtag the posts carry, lowercase, without the #.
        value (str): The tag.
    """

    type_: TopicClusterEventDataTagType
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = TopicClusterEventDataTagType(d.pop("type"))

        value = d.pop("value")

        topic_cluster_event_data_tag = cls(
            type_=type_,
            value=value,
        )

        topic_cluster_event_data_tag.additional_properties = d
        return topic_cluster_event_data_tag

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
