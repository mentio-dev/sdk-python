from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKeywordBodyComments")


@_attrs_define
class CreateKeywordBodyComments:
    """Comments under this keyword's mentions; omitted fields are untouched (on create: off, 20 per post).

    Attributes:
        enabled (bool | Unset): Read the comments under this keyword's relevant mentions, from 30 minutes after each
            post, as long as its platform's conversations last (a day to a month). Each comment delivered costs $0.008
            (comments of fewer than three words are dropped, never billed) (the comments line of the bill). Off by default.
        max_per_post (int | Unset): The newest comments of one thread you receive, 20 by default, 100 at most: the
            ceiling on what one mention's comments can cost. A comment that names the keyword is a mention too, but only
            among these newest ones, so it is never billed past the ceiling.
    """

    enabled: bool | Unset = UNSET
    max_per_post: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        max_per_post = self.max_per_post

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if max_per_post is not UNSET:
            field_dict["maxPerPost"] = max_per_post

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        max_per_post = d.pop("maxPerPost", UNSET)

        create_keyword_body_comments = cls(
            enabled=enabled,
            max_per_post=max_per_post,
        )

        create_keyword_body_comments.additional_properties = d
        return create_keyword_body_comments

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
