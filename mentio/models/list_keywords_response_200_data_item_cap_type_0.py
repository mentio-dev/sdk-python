from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_keywords_response_200_data_item_cap_type_0_own_per import (
    ListKeywordsResponse200DataItemCapType0OwnPer,
)
from ..models.list_keywords_response_200_data_item_cap_type_0_per import (
    ListKeywordsResponse200DataItemCapType0Per,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListKeywordsResponse200DataItemCapType0")


@_attrs_define
class ListKeywordsResponse200DataItemCapType0:
    """The mention cap and its period, or null for none.

    Attributes:
        mentions (int): Charged items allowed per period (see per): matched mentions plus the thread comments delivered
            under them. Every match counts, relevant or not, the look-back a new keyword gets included, because every match
            bills.
        used (int): Charged items (matches plus thread comments) counted in the current period: today, this week from
            Monday or this month, UTC. The keyword pauses when it reaches mentions.
        welcome (bool): Set by Mentio, not you: a workspace on its welcome credit collects at most 200 mentions a
            keyword a month. The first top-up removes it.
        own (int | None): Your own cap. With welcome true, the cap the keyword gets back at the first top-up (null for
            none); otherwise the same as mentions. Sending mentions: 200 back while welcome is true changes nothing.
        own_per (ListKeywordsResponse200DataItemCapType0OwnPer): The period of your own cap (null when own is null);
            with welcome false, the same as per.
        resumes_at (None | str): While paused for its cap (pausedForCap): when its next period starts and it matches
            again. Null otherwise.
        per (ListKeywordsResponse200DataItemCapType0Per | Unset): The period the cap counts in, in UTC: day (from
            00:00), week (from Monday 00:00) or month (the calendar month, the default). At the cap the keyword stops until
            the next period starts, so a daily cap keeps mentions coming every day with a fixed ceiling on spend. Default:
            ListKeywordsResponse200DataItemCapType0Per.MONTH.
    """

    mentions: int
    used: int
    welcome: bool
    own: int | None
    own_per: ListKeywordsResponse200DataItemCapType0OwnPer
    resumes_at: None | str
    per: ListKeywordsResponse200DataItemCapType0Per | Unset = (
        ListKeywordsResponse200DataItemCapType0Per.MONTH
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mentions = self.mentions

        used = self.used

        welcome = self.welcome

        own: int | None
        own = self.own

        own_per = self.own_per.value

        resumes_at: None | str
        resumes_at = self.resumes_at

        per: str | Unset = UNSET
        if not isinstance(self.per, Unset):
            per = self.per.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mentions": mentions,
                "used": used,
                "welcome": welcome,
                "own": own,
                "ownPer": own_per,
                "resumesAt": resumes_at,
            }
        )
        if per is not UNSET:
            field_dict["per"] = per

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mentions = d.pop("mentions")

        used = d.pop("used")

        welcome = d.pop("welcome")

        def _parse_own(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        own = _parse_own(d.pop("own"))

        own_per = ListKeywordsResponse200DataItemCapType0OwnPer(d.pop("ownPer"))

        def _parse_resumes_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resumes_at = _parse_resumes_at(d.pop("resumesAt"))

        _per = d.pop("per", UNSET)
        per: ListKeywordsResponse200DataItemCapType0Per | Unset
        if isinstance(_per, Unset):
            per = UNSET
        else:
            per = ListKeywordsResponse200DataItemCapType0Per(_per)

        list_keywords_response_200_data_item_cap_type_0 = cls(
            mentions=mentions,
            used=used,
            welcome=welcome,
            own=own,
            own_per=own_per,
            resumes_at=resumes_at,
            per=per,
        )

        list_keywords_response_200_data_item_cap_type_0.additional_properties = d
        return list_keywords_response_200_data_item_cap_type_0

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
