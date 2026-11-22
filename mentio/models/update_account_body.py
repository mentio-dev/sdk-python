from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_account_body_cap_type_0 import UpdateAccountBodyCapType0


T = TypeVar("T", bound="UpdateAccountBody")


@_attrs_define
class UpdateAccountBody:
    """
    Attributes:
        muted (bool | Unset): Pause (true) or resume (false) reading and charging it.
        group_id (str | Unset): Move it to this keyword group (grp_...).
        cap (None | Unset | UpdateAccountBodyCapType0): Set the monthly follower cap; null removes it.
    """

    muted: bool | Unset = UNSET
    group_id: str | Unset = UNSET
    cap: None | Unset | UpdateAccountBodyCapType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_account_body_cap_type_0 import UpdateAccountBodyCapType0

        muted = self.muted

        group_id = self.group_id

        cap: dict[str, Any] | None | Unset
        if isinstance(self.cap, Unset):
            cap = UNSET
        elif isinstance(self.cap, UpdateAccountBodyCapType0):
            cap = self.cap.to_dict()
        else:
            cap = self.cap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if muted is not UNSET:
            field_dict["muted"] = muted
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if cap is not UNSET:
            field_dict["cap"] = cap

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_account_body_cap_type_0 import UpdateAccountBodyCapType0

        d = dict(src_dict)
        muted = d.pop("muted", UNSET)

        group_id = d.pop("groupId", UNSET)

        def _parse_cap(data: object) -> None | Unset | UpdateAccountBodyCapType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cap_type_0 = UpdateAccountBodyCapType0.from_dict(data)

                return cap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAccountBodyCapType0, data)

        cap = _parse_cap(d.pop("cap", UNSET))

        update_account_body = cls(
            muted=muted,
            group_id=group_id,
            cap=cap,
        )

        update_account_body.additional_properties = d
        return update_account_body

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
