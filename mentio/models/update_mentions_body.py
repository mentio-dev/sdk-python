from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_mentions_body_filter import UpdateMentionsBodyFilter
    from ..models.update_mentions_body_update import UpdateMentionsBodyUpdate


T = TypeVar("T", bound="UpdateMentionsBody")


@_attrs_define
class UpdateMentionsBody:
    """
    Attributes:
        update (UpdateMentionsBodyUpdate): Every field is optional, at least one is required; omitted fields are
            untouched.
        ids (list[str] | Unset): Mention ids (mm_...), 1 to 100: a page of GET /v1/mentions. Send ids or filter, never
            both.
        filter_ (UpdateMentionsBodyFilter | Unset): Instead of ids: act on every mention these filters select, up to
            1000 a call, newest first. While nextCursor comes back, call again with the same filter and that cursor; the set
            is fixed when the first call runs, so mentions arriving meanwhile are left alone.
        cursor (str | Unset): With filter only: nextCursor from the previous call, to carry on where it stopped.
    """

    update: UpdateMentionsBodyUpdate
    ids: list[str] | Unset = UNSET
    filter_: UpdateMentionsBodyFilter | Unset = UNSET
    cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        update = self.update.to_dict()

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "update": update,
            }
        )
        if ids is not UNSET:
            field_dict["ids"] = ids
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_mentions_body_filter import UpdateMentionsBodyFilter
        from ..models.update_mentions_body_update import UpdateMentionsBodyUpdate

        d = dict(src_dict)
        update = UpdateMentionsBodyUpdate.from_dict(d.pop("update"))

        ids = cast(list[str], d.pop("ids", UNSET))

        _filter_ = d.pop("filter", UNSET)
        filter_: UpdateMentionsBodyFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = UpdateMentionsBodyFilter.from_dict(_filter_)

        cursor = d.pop("cursor", UNSET)

        update_mentions_body = cls(
            update=update,
            ids=ids,
            filter_=filter_,
            cursor=cursor,
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
