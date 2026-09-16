from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_segment_body_filter_keyword_kinds_item import (
    CreateSegmentBodyFilterKeywordKindsItem,
)
from ..models.create_segment_body_filter_never_keyword_kinds_item import (
    CreateSegmentBodyFilterNeverKeywordKindsItem,
)
from ..models.create_segment_body_filter_not_platforms_item import (
    CreateSegmentBodyFilterNotPlatformsItem,
)
from ..models.create_segment_body_filter_platforms_item import (
    CreateSegmentBodyFilterPlatformsItem,
)
from ..models.create_segment_body_filter_stages_item import (
    CreateSegmentBodyFilterStagesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSegmentBodyFilter")


@_attrs_define
class CreateSegmentBodyFilter:
    """
    Attributes:
        platforms (list[CreateSegmentBodyFilterPlatformsItem] | Unset): People with an account on any of these
            platforms.
        tags (list[str] | Unset): People carrying any of these tags.
        min_followers (int | Unset): At least this many followers. Unknown reach never matches.
        max_followers (int | Unset): At most this many followers. Unknown reach never matches.
        min_mentions (int | Unset): At least this many matched mentions.
        min_negative (int | Unset): At least this many negative mentions.
        intents (list[str] | Unset): At least one mention carrying any of these intents.
        keyword_kinds (list[CreateSegmentBodyFilterKeywordKindsItem] | Unset): Mentioned a keyword of any of these
            kinds.
        never_keyword_kinds (list[CreateSegmentBodyFilterNeverKeywordKindsItem] | Unset): Never mentioned a keyword of
            these kinds.
        not_platforms (list[CreateSegmentBodyFilterNotPlatformsItem] | Unset): Nobody with an account on these
            platforms.
        not_tags (list[str] | Unset): Nobody carrying any of these tags.
        not_intents (list[str] | Unset): Nobody whose mentions carry any of these intents.
        new_since_days (int | Unset): First seen within this many days.
        link_hosts (list[str] | Unset): At least one mention linking to any of these hosts, the host itself or a
            subdomain of it.
        muted (bool | Unset): true: only muted people; false: only unmuted.
        stages (list[CreateSegmentBodyFilterStagesItem] | Unset): People at any of these outreach stages.
        automated (bool | Unset): true: only people whose matched posts are mostly machine-made (bot accounts); false:
            only the rest.
        owner_ids (list[str] | Unset): People owned by any of these members (user ids); "none" matches people nobody
            owns.
    """

    platforms: list[CreateSegmentBodyFilterPlatformsItem] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    min_followers: int | Unset = UNSET
    max_followers: int | Unset = UNSET
    min_mentions: int | Unset = UNSET
    min_negative: int | Unset = UNSET
    intents: list[str] | Unset = UNSET
    keyword_kinds: list[CreateSegmentBodyFilterKeywordKindsItem] | Unset = UNSET
    never_keyword_kinds: list[CreateSegmentBodyFilterNeverKeywordKindsItem] | Unset = (
        UNSET
    )
    not_platforms: list[CreateSegmentBodyFilterNotPlatformsItem] | Unset = UNSET
    not_tags: list[str] | Unset = UNSET
    not_intents: list[str] | Unset = UNSET
    new_since_days: int | Unset = UNSET
    link_hosts: list[str] | Unset = UNSET
    muted: bool | Unset = UNSET
    stages: list[CreateSegmentBodyFilterStagesItem] | Unset = UNSET
    automated: bool | Unset = UNSET
    owner_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platforms: list[str] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.value
                platforms.append(platforms_item)

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        min_followers = self.min_followers

        max_followers = self.max_followers

        min_mentions = self.min_mentions

        min_negative = self.min_negative

        intents: list[str] | Unset = UNSET
        if not isinstance(self.intents, Unset):
            intents = self.intents

        keyword_kinds: list[str] | Unset = UNSET
        if not isinstance(self.keyword_kinds, Unset):
            keyword_kinds = []
            for keyword_kinds_item_data in self.keyword_kinds:
                keyword_kinds_item = keyword_kinds_item_data.value
                keyword_kinds.append(keyword_kinds_item)

        never_keyword_kinds: list[str] | Unset = UNSET
        if not isinstance(self.never_keyword_kinds, Unset):
            never_keyword_kinds = []
            for never_keyword_kinds_item_data in self.never_keyword_kinds:
                never_keyword_kinds_item = never_keyword_kinds_item_data.value
                never_keyword_kinds.append(never_keyword_kinds_item)

        not_platforms: list[str] | Unset = UNSET
        if not isinstance(self.not_platforms, Unset):
            not_platforms = []
            for not_platforms_item_data in self.not_platforms:
                not_platforms_item = not_platforms_item_data.value
                not_platforms.append(not_platforms_item)

        not_tags: list[str] | Unset = UNSET
        if not isinstance(self.not_tags, Unset):
            not_tags = self.not_tags

        not_intents: list[str] | Unset = UNSET
        if not isinstance(self.not_intents, Unset):
            not_intents = self.not_intents

        new_since_days = self.new_since_days

        link_hosts: list[str] | Unset = UNSET
        if not isinstance(self.link_hosts, Unset):
            link_hosts = self.link_hosts

        muted = self.muted

        stages: list[str] | Unset = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.value
                stages.append(stages_item)

        automated = self.automated

        owner_ids: list[str] | Unset = UNSET
        if not isinstance(self.owner_ids, Unset):
            owner_ids = self.owner_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if tags is not UNSET:
            field_dict["tags"] = tags
        if min_followers is not UNSET:
            field_dict["minFollowers"] = min_followers
        if max_followers is not UNSET:
            field_dict["maxFollowers"] = max_followers
        if min_mentions is not UNSET:
            field_dict["minMentions"] = min_mentions
        if min_negative is not UNSET:
            field_dict["minNegative"] = min_negative
        if intents is not UNSET:
            field_dict["intents"] = intents
        if keyword_kinds is not UNSET:
            field_dict["keywordKinds"] = keyword_kinds
        if never_keyword_kinds is not UNSET:
            field_dict["neverKeywordKinds"] = never_keyword_kinds
        if not_platforms is not UNSET:
            field_dict["notPlatforms"] = not_platforms
        if not_tags is not UNSET:
            field_dict["notTags"] = not_tags
        if not_intents is not UNSET:
            field_dict["notIntents"] = not_intents
        if new_since_days is not UNSET:
            field_dict["newSinceDays"] = new_since_days
        if link_hosts is not UNSET:
            field_dict["linkHosts"] = link_hosts
        if muted is not UNSET:
            field_dict["muted"] = muted
        if stages is not UNSET:
            field_dict["stages"] = stages
        if automated is not UNSET:
            field_dict["automated"] = automated
        if owner_ids is not UNSET:
            field_dict["ownerIds"] = owner_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _platforms = d.pop("platforms", UNSET)
        platforms: list[CreateSegmentBodyFilterPlatformsItem] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = CreateSegmentBodyFilterPlatformsItem(
                    platforms_item_data
                )

                platforms.append(platforms_item)

        tags = cast(list[str], d.pop("tags", UNSET))

        min_followers = d.pop("minFollowers", UNSET)

        max_followers = d.pop("maxFollowers", UNSET)

        min_mentions = d.pop("minMentions", UNSET)

        min_negative = d.pop("minNegative", UNSET)

        intents = cast(list[str], d.pop("intents", UNSET))

        _keyword_kinds = d.pop("keywordKinds", UNSET)
        keyword_kinds: list[CreateSegmentBodyFilterKeywordKindsItem] | Unset = UNSET
        if _keyword_kinds is not UNSET:
            keyword_kinds = []
            for keyword_kinds_item_data in _keyword_kinds:
                keyword_kinds_item = CreateSegmentBodyFilterKeywordKindsItem(
                    keyword_kinds_item_data
                )

                keyword_kinds.append(keyword_kinds_item)

        _never_keyword_kinds = d.pop("neverKeywordKinds", UNSET)
        never_keyword_kinds: (
            list[CreateSegmentBodyFilterNeverKeywordKindsItem] | Unset
        ) = UNSET
        if _never_keyword_kinds is not UNSET:
            never_keyword_kinds = []
            for never_keyword_kinds_item_data in _never_keyword_kinds:
                never_keyword_kinds_item = CreateSegmentBodyFilterNeverKeywordKindsItem(
                    never_keyword_kinds_item_data
                )

                never_keyword_kinds.append(never_keyword_kinds_item)

        _not_platforms = d.pop("notPlatforms", UNSET)
        not_platforms: list[CreateSegmentBodyFilterNotPlatformsItem] | Unset = UNSET
        if _not_platforms is not UNSET:
            not_platforms = []
            for not_platforms_item_data in _not_platforms:
                not_platforms_item = CreateSegmentBodyFilterNotPlatformsItem(
                    not_platforms_item_data
                )

                not_platforms.append(not_platforms_item)

        not_tags = cast(list[str], d.pop("notTags", UNSET))

        not_intents = cast(list[str], d.pop("notIntents", UNSET))

        new_since_days = d.pop("newSinceDays", UNSET)

        link_hosts = cast(list[str], d.pop("linkHosts", UNSET))

        muted = d.pop("muted", UNSET)

        _stages = d.pop("stages", UNSET)
        stages: list[CreateSegmentBodyFilterStagesItem] | Unset = UNSET
        if _stages is not UNSET:
            stages = []
            for stages_item_data in _stages:
                stages_item = CreateSegmentBodyFilterStagesItem(stages_item_data)

                stages.append(stages_item)

        automated = d.pop("automated", UNSET)

        owner_ids = cast(list[str], d.pop("ownerIds", UNSET))

        create_segment_body_filter = cls(
            platforms=platforms,
            tags=tags,
            min_followers=min_followers,
            max_followers=max_followers,
            min_mentions=min_mentions,
            min_negative=min_negative,
            intents=intents,
            keyword_kinds=keyword_kinds,
            never_keyword_kinds=never_keyword_kinds,
            not_platforms=not_platforms,
            not_tags=not_tags,
            not_intents=not_intents,
            new_since_days=new_since_days,
            link_hosts=link_hosts,
            muted=muted,
            stages=stages,
            automated=automated,
            owner_ids=owner_ids,
        )

        create_segment_body_filter.additional_properties = d
        return create_segment_body_filter

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
