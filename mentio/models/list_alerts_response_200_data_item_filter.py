from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_alerts_response_200_data_item_filter_platforms_item import (
    ListAlertsResponse200DataItemFilterPlatformsItem,
)
from ..models.list_alerts_response_200_data_item_filter_sentiments_item import (
    ListAlertsResponse200DataItemFilterSentimentsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAlertsResponse200DataItemFilter")


@_attrs_define
class ListAlertsResponse200DataItemFilter:
    """
    Attributes:
        keyword_ids (list[str] | Unset): Only these keywords.
        platforms (list[ListAlertsResponse200DataItemFilterPlatformsItem] | Unset): Only posts from these platforms.
        min_relevance (int | Unset): Only mentions scored at least this; unclassified ones never pass.
        sentiments (list[ListAlertsResponse200DataItemFilterSentimentsItem] | Unset): Only these sentiments.
        intents (list[str] | Unset): At least one of these intents.
        exclude_authors (list[str] | Unset): Never these authors: display names, handles or profile URLs.
        min_followers (int | Unset): Only authors with at least this many followers. Unknown reach never passes.
        tags (list[str] | Unset): Only authors your workspace tagged with any of these.
        link_hosts (list[str] | Unset): Only posts linking to any of these hosts, the host itself or a subdomain of it
            (octolens.com also matches blog.octolens.com). A post with no links never passes.
    """

    keyword_ids: list[str] | Unset = UNSET
    platforms: list[ListAlertsResponse200DataItemFilterPlatformsItem] | Unset = UNSET
    min_relevance: int | Unset = UNSET
    sentiments: list[ListAlertsResponse200DataItemFilterSentimentsItem] | Unset = UNSET
    intents: list[str] | Unset = UNSET
    exclude_authors: list[str] | Unset = UNSET
    min_followers: int | Unset = UNSET
    tags: list[str] | Unset = UNSET
    link_hosts: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword_ids: list[str] | Unset = UNSET
        if not isinstance(self.keyword_ids, Unset):
            keyword_ids = self.keyword_ids

        platforms: list[str] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.value
                platforms.append(platforms_item)

        min_relevance = self.min_relevance

        sentiments: list[str] | Unset = UNSET
        if not isinstance(self.sentiments, Unset):
            sentiments = []
            for sentiments_item_data in self.sentiments:
                sentiments_item = sentiments_item_data.value
                sentiments.append(sentiments_item)

        intents: list[str] | Unset = UNSET
        if not isinstance(self.intents, Unset):
            intents = self.intents

        exclude_authors: list[str] | Unset = UNSET
        if not isinstance(self.exclude_authors, Unset):
            exclude_authors = self.exclude_authors

        min_followers = self.min_followers

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        link_hosts: list[str] | Unset = UNSET
        if not isinstance(self.link_hosts, Unset):
            link_hosts = self.link_hosts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyword_ids is not UNSET:
            field_dict["keywordIds"] = keyword_ids
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if min_relevance is not UNSET:
            field_dict["minRelevance"] = min_relevance
        if sentiments is not UNSET:
            field_dict["sentiments"] = sentiments
        if intents is not UNSET:
            field_dict["intents"] = intents
        if exclude_authors is not UNSET:
            field_dict["excludeAuthors"] = exclude_authors
        if min_followers is not UNSET:
            field_dict["minFollowers"] = min_followers
        if tags is not UNSET:
            field_dict["tags"] = tags
        if link_hosts is not UNSET:
            field_dict["linkHosts"] = link_hosts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keyword_ids = cast(list[str], d.pop("keywordIds", UNSET))

        _platforms = d.pop("platforms", UNSET)
        platforms: list[ListAlertsResponse200DataItemFilterPlatformsItem] | Unset = (
            UNSET
        )
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = ListAlertsResponse200DataItemFilterPlatformsItem(
                    platforms_item_data
                )

                platforms.append(platforms_item)

        min_relevance = d.pop("minRelevance", UNSET)

        _sentiments = d.pop("sentiments", UNSET)
        sentiments: list[ListAlertsResponse200DataItemFilterSentimentsItem] | Unset = (
            UNSET
        )
        if _sentiments is not UNSET:
            sentiments = []
            for sentiments_item_data in _sentiments:
                sentiments_item = ListAlertsResponse200DataItemFilterSentimentsItem(
                    sentiments_item_data
                )

                sentiments.append(sentiments_item)

        intents = cast(list[str], d.pop("intents", UNSET))

        exclude_authors = cast(list[str], d.pop("excludeAuthors", UNSET))

        min_followers = d.pop("minFollowers", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        link_hosts = cast(list[str], d.pop("linkHosts", UNSET))

        list_alerts_response_200_data_item_filter = cls(
            keyword_ids=keyword_ids,
            platforms=platforms,
            min_relevance=min_relevance,
            sentiments=sentiments,
            intents=intents,
            exclude_authors=exclude_authors,
            min_followers=min_followers,
            tags=tags,
            link_hosts=link_hosts,
        )

        list_alerts_response_200_data_item_filter.additional_properties = d
        return list_alerts_response_200_data_item_filter

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
