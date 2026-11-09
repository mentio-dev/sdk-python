from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_mentions_body_update import UpdateMentionsBodyUpdate


T = TypeVar("T", bound="UpdateMentionsBody")


@_attrs_define
class UpdateMentionsBody:
    """
    Attributes:
        ids (list[str]): Mention ids (mm_...), 1 to 100: a page of GET /v1/mentions.
        update (UpdateMentionsBodyUpdate): Every field is optional, at least one is required; omitted fields are
            untouched.
    """

    ids: list[str]
    update: UpdateMentionsBodyUpdate
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        update = self.update.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
                "update": update,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_mentions_body_update import UpdateMentionsBodyUpdate

        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        update = UpdateMentionsBodyUpdate.from_dict(d.pop("update"))

        update_mentions_body = cls(
            ids=ids,
            update=update,
        )

        update_mentions_body.additional_properties = d
        return update_mentions_body

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
