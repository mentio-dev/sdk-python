from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_account_body_platform import CreateAccountBodyPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_account_body_cap_type_0 import CreateAccountBodyCapType0


T = TypeVar("T", bound="CreateAccountBody")


@_attrs_define
class CreateAccountBody:
    """
    Attributes:
        platform (CreateAccountBodyPlatform): x, bluesky or github. instagram is refused for now (a 400): its follower
            list is not readable newest first.
        handle (str): The handle on the platform, with or without the @; a profile link works too (https://x.com/acme,
            https://bsky.app/profile/acme.bsky.social).
        group_id (str | Unset): The keyword group it belongs to (grp_...); omit for the default group.
        cap (CreateAccountBodyCapType0 | None | Unset): A monthly cap on billed new followers; omit or null for none.
    """

    platform: CreateAccountBodyPlatform
    handle: str
    group_id: str | Unset = UNSET
    cap: CreateAccountBodyCapType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_account_body_cap_type_0 import CreateAccountBodyCapType0

        platform = self.platform.value

        handle = self.handle

        group_id = self.group_id

        cap: dict[str, Any] | None | Unset
        if isinstance(self.cap, Unset):
            cap = UNSET
        elif isinstance(self.cap, CreateAccountBodyCapType0):
            cap = self.cap.to_dict()
        else:
            cap = self.cap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "handle": handle,
            }
        )
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if cap is not UNSET:
            field_dict["cap"] = cap

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_account_body_cap_type_0 import CreateAccountBodyCapType0

        d = dict(src_dict)
        platform = CreateAccountBodyPlatform(d.pop("platform"))

        handle = d.pop("handle")

        group_id = d.pop("groupId", UNSET)

        def _parse_cap(data: object) -> CreateAccountBodyCapType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cap_type_0 = CreateAccountBodyCapType0.from_dict(data)

                return cap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateAccountBodyCapType0 | None | Unset, data)

        cap = _parse_cap(d.pop("cap", UNSET))

        create_account_body = cls(
            platform=platform,
            handle=handle,
            group_id=group_id,
            cap=cap,
        )

        create_account_body.additional_properties = d
        return create_account_body

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
