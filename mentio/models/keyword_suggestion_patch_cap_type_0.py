from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_suggestion_patch_cap_type_0_per import (
    KeywordSuggestionPatchCapType0Per,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordSuggestionPatchCapType0")


@_attrs_define
class KeywordSuggestionPatchCapType0:
    """Replaces the mention cap and its period (per, default month); null removes it. A cap above the current period's
    count resumes a capped keyword at once, one at or under it pauses it.

        Attributes:
            mentions (int): Charged items allowed per period (see per): matched mentions plus the thread comments delivered
                under them. Every match counts, relevant or not, the look-back a new keyword gets included, because every match
                bills.
            per (KeywordSuggestionPatchCapType0Per | Unset): The period the cap counts in, in UTC: day (from 00:00), week
                (from Monday 00:00) or month (the calendar month, the default). At the cap the keyword stops until the next
                period starts, so a daily cap keeps mentions coming every day with a fixed ceiling on spend. Default:
                KeywordSuggestionPatchCapType0Per.MONTH.
    """

    mentions: int
    per: KeywordSuggestionPatchCapType0Per | Unset = (
        KeywordSuggestionPatchCapType0Per.MONTH
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mentions = self.mentions

        per: str | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mentions": mentions,
            }
        )
        if per is not UNSET:
            field_dict["per"] = per

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mentions = d.pop("mentions")

        _per = d.pop("per", UNSET)
        per: KeywordSuggestionPatchCapType0Per | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = KeywordSuggestionPatchCapType0Per(_per)

        keyword_suggestion_patch_cap_type_0 = cls(
            mentions=mentions,
            per=per,
        )

        keyword_suggestion_patch_cap_type_0.additional_properties = d
        return keyword_suggestion_patch_cap_type_0

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
