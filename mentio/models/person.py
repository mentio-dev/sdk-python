from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_platform import PersonPlatform

if TYPE_CHECKING:
    from ..models.person_accounts_item import PersonAccountsItem
    from ..models.person_annotations import PersonAnnotations
    from ..models.person_profile_type_0 import PersonProfileType0
    from ..models.person_reach import PersonReach
    from ..models.person_stats import PersonStats


T = TypeVar("T", bound="Person")


@_attrs_define
class Person:
    """
    Attributes:
        id (str): Person id (aut_...): the canonical account. An account merged into someone resolves to that person.
        platform (PersonPlatform): Platform of the canonical account; `accounts` lists every account.
        name (None | str): Display name as of their newest post; null when the platform has none.
        handle (None | str): Platform handle of the canonical account, formatted as the platform shows it.
        url (None | str): Profile URL of the canonical account.
        avatar_url (None | str):
        accounts (list[PersonAccountsItem]): Every account this workspace treats as this person, the canonical one
            first.
        reach (PersonReach): Platform counts as of their newest post; null where the platform has no such number.
        profile (None | PersonProfileType0): Public profile facts; null until looked up.
        stats (PersonStats): Computed over this workspace's matches.
        annotations (PersonAnnotations): What this workspace wrote about the person.
    """

    id: str
    platform: PersonPlatform
    name: None | str
    handle: None | str
    url: None | str
    avatar_url: None | str
    accounts: list[PersonAccountsItem]
    reach: PersonReach
    profile: None | PersonProfileType0
    stats: PersonStats
    annotations: PersonAnnotations
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.person_profile_type_0 import PersonProfileType0

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
        if isinstance(self.profile, PersonProfileType0):
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
        from ..models.person_accounts_item import PersonAccountsItem
        from ..models.person_annotations import PersonAnnotations
        from ..models.person_profile_type_0 import PersonProfileType0
        from ..models.person_reach import PersonReach
        from ..models.person_stats import PersonStats

        d = dict(src_dict)
        id = d.pop("id")

        platform = PersonPlatform(d.pop("platform"))

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
            accounts_item = PersonAccountsItem.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        reach = PersonReach.from_dict(d.pop("reach"))

        def _parse_profile(data: object) -> None | PersonProfileType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_type_0 = PersonProfileType0.from_dict(data)

                return profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonProfileType0, data)

        profile = _parse_profile(d.pop("profile"))

        stats = PersonStats.from_dict(d.pop("stats"))

        annotations = PersonAnnotations.from_dict(d.pop("annotations"))

        person = cls(
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

        person.additional_properties = d
        return person

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
