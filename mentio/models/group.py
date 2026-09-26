from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.group_stats import GroupStats


T = TypeVar("T", bound="Group")


@_attrs_define
class Group:
    """The group the keyword belongs to.

    Attributes:
        id (str): Group id (grp_...).
        name (str): The group's name.
        external_id (None | str): Your own id for the group, or null.
        is_default (bool): The workspace's default group, where a keyword lands when no group is named.
        context (None | str): The group's own company description for the classifier, or null for the workspace profile.
        stats (GroupStats): Computed over the group's keywords.
        created_at (str): ISO 8601 timestamp, UTC.
        updated_at (str): ISO 8601 timestamp, UTC.
    """

    id: str
    name: str
    external_id: None | str
    is_default: bool
    context: None | str
    stats: GroupStats
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        external_id: None | str
        external_id = self.external_id

        is_default = self.is_default

        context: None | str
        context = self.context

        stats = self.stats.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "externalId": external_id,
                "isDefault": is_default,
                "context": context,
                "stats": stats,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.group_stats import GroupStats

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_id = _parse_external_id(d.pop("externalId"))

        is_default = d.pop("isDefault")

        def _parse_context(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        context = _parse_context(d.pop("context"))

        stats = GroupStats.from_dict(d.pop("stats"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        group = cls(
            id=id,
            name=name,
            external_id=external_id,
            is_default=is_default,
            context=context,
            stats=stats,
            created_at=created_at,
            updated_at=updated_at,
        )

        group.additional_properties = d
        return group

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
