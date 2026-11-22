from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracked_account_platform import TrackedAccountPlatform

if TYPE_CHECKING:
    from ..models.group_ref import GroupRef
    from ..models.tracked_account_cap_type_0 import TrackedAccountCapType0
    from ..models.tracked_account_polling import TrackedAccountPolling
    from ..models.tracked_account_stats import TrackedAccountStats


T = TypeVar("T", bound="TrackedAccount")


@_attrs_define
class TrackedAccount:
    """
    Attributes:
        id (str): Tracked account id (acc_...).
        platform (TrackedAccountPlatform): x, instagram, bluesky or github.
        handle (str): The account's handle on the platform, without the @.
        name (None | str): Display name, as the last poll read it.
        avatar_url (None | str): Profile picture, as the last poll read it.
        url (str): The account's profile.
        group (GroupRef): The group the keyword belongs to.
        muted (bool): Not read and not charged: paused by a person or by the wallet.
        paused_for_balance (bool): The wallet paused it; a top-up resumes it.
        paused_for_cap (bool): It reached its monthly follower cap; it resumes on the 1st (UTC) or when the cap is
            raised.
        cap (None | TrackedAccountCapType0): A monthly cap on billed new followers.
        stats (TrackedAccountStats): Counts about the account.
        polling (TrackedAccountPolling): The poller's state.
        created_at (str): When tracking started.
    """

    id: str
    platform: TrackedAccountPlatform
    handle: str
    name: None | str
    avatar_url: None | str
    url: str
    group: GroupRef
    muted: bool
    paused_for_balance: bool
    paused_for_cap: bool
    cap: None | TrackedAccountCapType0
    stats: TrackedAccountStats
    polling: TrackedAccountPolling
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tracked_account_cap_type_0 import TrackedAccountCapType0

        id = self.id

        platform = self.platform.value

        handle = self.handle

        name: None | str
        name = self.name

        avatar_url: None | str
        avatar_url = self.avatar_url

        url = self.url

        group = self.group.to_dict()

        muted = self.muted

        paused_for_balance = self.paused_for_balance

        paused_for_cap = self.paused_for_cap

        cap: dict[str, Any] | None
        if isinstance(self.cap, TrackedAccountCapType0):
            cap = self.cap.to_dict()
        else:
            cap = self.cap

        stats = self.stats.to_dict()

        polling = self.polling.to_dict()

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "platform": platform,
                "handle": handle,
                "name": name,
                "avatarUrl": avatar_url,
                "url": url,
                "group": group,
                "muted": muted,
                "pausedForBalance": paused_for_balance,
                "pausedForCap": paused_for_cap,
                "cap": cap,
                "stats": stats,
                "polling": polling,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.group_ref import GroupRef
        from ..models.tracked_account_cap_type_0 import TrackedAccountCapType0
        from ..models.tracked_account_polling import TrackedAccountPolling
        from ..models.tracked_account_stats import TrackedAccountStats

        d = dict(src_dict)
        id = d.pop("id")

        platform = TrackedAccountPlatform(d.pop("platform"))

        handle = d.pop("handle")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_avatar_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl"))

        url = d.pop("url")

        group = GroupRef.from_dict(d.pop("group"))

        muted = d.pop("muted")

        paused_for_balance = d.pop("pausedForBalance")

        paused_for_cap = d.pop("pausedForCap")

        def _parse_cap(data: object) -> None | TrackedAccountCapType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cap_type_0 = TrackedAccountCapType0.from_dict(data)

                return cap_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TrackedAccountCapType0, data)

        cap = _parse_cap(d.pop("cap"))

        stats = TrackedAccountStats.from_dict(d.pop("stats"))

        polling = TrackedAccountPolling.from_dict(d.pop("polling"))

        created_at = d.pop("createdAt")

        tracked_account = cls(
            id=id,
            platform=platform,
            handle=handle,
            name=name,
            avatar_url=avatar_url,
            url=url,
            group=group,
            muted=muted,
            paused_for_balance=paused_for_balance,
            paused_for_cap=paused_for_cap,
            cap=cap,
            stats=stats,
            polling=polling,
            created_at=created_at,
        )

        tracked_account.additional_properties = d
        return tracked_account

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
