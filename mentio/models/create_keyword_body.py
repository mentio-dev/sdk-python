from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_keyword_body_kind import CreateKeywordBodyKind
from ..models.create_keyword_body_platforms_type_0_item import (
    CreateKeywordBodyPlatformsType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_keyword_body_cap_type_0 import CreateKeywordBodyCapType0
    from ..models.create_keyword_body_matching import CreateKeywordBodyMatching


T = TypeVar("T", bound="CreateKeywordBody")


@_attrs_define
class CreateKeywordBody:
    """
    Attributes:
        term (str): The word or phrase to track, matched case-insensitively as a phrase.
        kind (CreateKeywordBodyKind | Unset): brand: your own names. competitor: theirs. topic: the space. Drives share
            of voice and segments. Default: CreateKeywordBodyKind.BRAND.
        platforms (list[CreateKeywordBodyPlatformsType0Item] | None | Unset): Platforms to track it on; omit or null for
            every platform.
        context (None | str | Unset): A sentence the classifier reads for this keyword only, on top of the company
            profile or the group's own description (at most 300 characters): what the term means here, what to ignore. "Arc
            is our browser; ignore the geometry word." Null clears it.
        matching (CreateKeywordBodyMatching | Unset): Omitted fields are untouched; an empty list clears one.
        cap (CreateKeywordBodyCapType0 | None | Unset): A monthly mention cap; omit or null for none.
        group_id (str | Unset): The group to track it in (grp_...); omit for the workspace's default group. A term may
            be tracked once per group.
    """

    term: str
    kind: CreateKeywordBodyKind | Unset = CreateKeywordBodyKind.BRAND
    platforms: list[CreateKeywordBodyPlatformsType0Item] | None | Unset = UNSET
    context: None | str | Unset = UNSET
    matching: CreateKeywordBodyMatching | Unset = UNSET
    cap: CreateKeywordBodyCapType0 | None | Unset = UNSET
    group_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_keyword_body_cap_type_0 import (
            CreateKeywordBodyCapType0,
        )

        term = self.term

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        platforms: list[str] | None | Unset
        if isinstance(self.platforms, Unset):
            platforms = UNSET
        elif isinstance(self.platforms, list):
            platforms = []
            for platforms_type_0_item_data in self.platforms:
                platforms_type_0_item = platforms_type_0_item_data.value
                platforms.append(platforms_type_0_item)

        else:
            platforms = self.platforms

        context: None | str | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        matching: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matching, Unset):
            matching = self.matching.to_dict()

        cap: dict[str, Any] | None | Unset
        if isinstance(self.cap, Unset):
            cap = UNSET
        elif isinstance(self.cap, CreateKeywordBodyCapType0):
            cap = self.cap.to_dict()
        else:
            cap = self.cap

        group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "term": term,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if context is not UNSET:
            field_dict["context"] = context
        if matching is not UNSET:
            field_dict["matching"] = matching
        if cap is not UNSET:
            field_dict["cap"] = cap
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_keyword_body_cap_type_0 import (
            CreateKeywordBodyCapType0,
        )
        from ..models.create_keyword_body_matching import (
            CreateKeywordBodyMatching,
        )

        d = dict(src_dict)
        term = d.pop("term")

        _kind = d.pop("kind", UNSET)
        kind: CreateKeywordBodyKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = CreateKeywordBodyKind(_kind)

        def _parse_platforms(
            data: object,
        ) -> list[CreateKeywordBodyPlatformsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                platforms_type_0 = []
                _platforms_type_0 = data
                for platforms_type_0_item_data in _platforms_type_0:
                    platforms_type_0_item = CreateKeywordBodyPlatformsType0Item(
                        platforms_type_0_item_data
                    )

                    platforms_type_0.append(platforms_type_0_item)

                return platforms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CreateKeywordBodyPlatformsType0Item] | None | Unset, data)

        platforms = _parse_platforms(d.pop("platforms", UNSET))

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        _matching = d.pop("matching", UNSET)
        matching: CreateKeywordBodyMatching | Unset
        if isinstance(_matching, Unset):
            matching = UNSET
        else:
            matching = CreateKeywordBodyMatching.from_dict(_matching)

        def _parse_cap(data: object) -> CreateKeywordBodyCapType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cap_type_0 = CreateKeywordBodyCapType0.from_dict(data)

                return cap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateKeywordBodyCapType0 | None | Unset, data)

        cap = _parse_cap(d.pop("cap", UNSET))

        group_id = d.pop("groupId", UNSET)

        create_keyword_body = cls(
            term=term,
            kind=kind,
            platforms=platforms,
            context=context,
            matching=matching,
            cap=cap,
            group_id=group_id,
        )

        create_keyword_body.additional_properties = d
        return create_keyword_body

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
