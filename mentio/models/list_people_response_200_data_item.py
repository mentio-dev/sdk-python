from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_people_response_200_data_item_platform import (
    ListPeopleResponse200DataItemPlatform,
)

if TYPE_CHECKING:
    from ..models.list_people_response_200_data_item_accounts_item import (
        ListPeopleResponse200DataItemAccountsItem,
    )
    from ..models.list_people_response_200_data_item_annotations import (
        ListPeopleResponse200DataItemAnnotations,
    )
    from ..models.list_people_response_200_data_item_profile_type_0 import (
        ListPeopleResponse200DataItemProfileType0,
    )
    from ..models.list_people_response_200_data_item_reach import (
        ListPeopleResponse200DataItemReach,
    )
    from ..models.list_people_response_200_data_item_stats import (
        ListPeopleResponse200DataItemStats,
    )


T = TypeVar("T", bound="ListPeopleResponse200DataItem")


@_attrs_define
class ListPeopleResponse200DataItem:
    """
    Attributes:
        id (str): Person id (aut_...): the canonical account. An account merged into someone resolves to that person.
        platform (ListPeopleResponse200DataItemPlatform): Platform of the canonical account; `accounts` lists every
            account.
        name (None | str): Display name as of their newest post; null when the platform has none.
        handle (None | str): Platform handle of the canonical account, formatted as the platform shows it.
        url (None | str): Profile URL of the canonical account.
        avatar_url (None | str):
        accounts (list[ListPeopleResponse200DataItemAccountsItem]): Every account this workspace treats as this person,
            the canonical one first.
        reach (ListPeopleResponse200DataItemReach): Platform counts as of their newest post; null where the platform has
            no such number.
        profile (ListPeopleResponse200DataItemProfileType0 | None): Public profile facts; null until looked up.
        stats (ListPeopleResponse200DataItemStats): Computed over this workspace's matches.
        annotations (ListPeopleResponse200DataItemAnnotations): What this workspace wrote about the person.
    """

    id: str
    platform: ListPeopleResponse200DataItemPlatform
    name: None | str
    handle: None | str
    url: None | str
    avatar_url: None | str
    accounts: list[ListPeopleResponse200DataItemAccountsItem]
    reach: ListPeopleResponse200DataItemReach
    profile: ListPeopleResponse200DataItemProfileType0 | None
    stats: ListPeopleResponse200DataItemStats
    annotations: ListPeopleResponse200DataItemAnnotations
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_people_response_200_data_item_profile_type_0 import (
            ListPeopleResponse200DataItemProfileType0,
        )

        id = self.id

        platform = self.platform.value

        name: None | str
        name = self.name

        handle: None | str
        handle = self.handle

        url: None | str
        url = self.url

        avatar_url: None | str
        avatar_url = self.avatar_url

        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()
            accounts.append(accounts_item)

        reach = self.reach.to_dict()

        profile: dict[str, Any] | None
        if isinstance(self.profile, ListPeopleResponse200DataItemProfileType0):
            profile = self.profile.to_dict()
        else:
            profile = self.profile

        stats = self.stats.to_dict()

        annotations = self.annotations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "platform": platform,
                "name": name,
                "handle": handle,
                "url": url,
                "avatarUrl": avatar_url,
                "accounts": accounts,
                "reach": reach,
                "profile": profile,
                "stats": stats,
                "annotations": annotations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_people_response_200_data_item_accounts_item import (
            ListPeopleResponse200DataItemAccountsItem,
        )
        from ..models.list_people_response_200_data_item_annotations import (
            ListPeopleResponse200DataItemAnnotations,
        )
        from ..models.list_people_response_200_data_item_profile_type_0 import (
            ListPeopleResponse200DataItemProfileType0,
        )
        from ..models.list_people_response_200_data_item_reach import (
            ListPeopleResponse200DataItemReach,
        )
        from ..models.list_people_response_200_data_item_stats import (
            ListPeopleResponse200DataItemStats,
        )

        d = dict(src_dict)
        id = d.pop("id")

        platform = ListPeopleResponse200DataItemPlatform(d.pop("platform"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_handle(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        handle = _parse_handle(d.pop("handle"))

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        def _parse_avatar_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl"))

        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = ListPeopleResponse200DataItemAccountsItem.from_dict(
                accounts_item_data
            )

            accounts.append(accounts_item)

        reach = ListPeopleResponse200DataItemReach.from_dict(d.pop("reach"))

        def _parse_profile(
            data: object,
        ) -> ListPeopleResponse200DataItemProfileType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_type_0 = ListPeopleResponse200DataItemProfileType0.from_dict(
                    data
                )

                return profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListPeopleResponse200DataItemProfileType0 | None, data)

        profile = _parse_profile(d.pop("profile"))

        stats = ListPeopleResponse200DataItemStats.from_dict(d.pop("stats"))

        annotations = ListPeopleResponse200DataItemAnnotations.from_dict(
            d.pop("annotations")
        )

        list_people_response_200_data_item = cls(
            id=id,
            platform=platform,
            name=name,
            handle=handle,
            url=url,
            avatar_url=avatar_url,
            accounts=accounts,
            reach=reach,
            profile=profile,
            stats=stats,
            annotations=annotations,
        )

        list_people_response_200_data_item.additional_properties = d
        return list_people_response_200_data_item

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
