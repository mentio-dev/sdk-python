from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.import_feeds_response_200_data_item_feed_type_0_auth_type_0 import (
        ImportFeedsResponse200DataItemFeedType0AuthType0,
    )
    from ..models.import_feeds_response_200_data_item_feed_type_0_health import (
        ImportFeedsResponse200DataItemFeedType0Health,
    )
    from ..models.import_feeds_response_200_data_item_feed_type_0_stats import (
        ImportFeedsResponse200DataItemFeedType0Stats,
    )


T = TypeVar("T", bound="ImportFeedsResponse200DataItemFeedType0")


@_attrs_define
class ImportFeedsResponse200DataItemFeedType0:
    """The feed, when added or already there; null when failed.

    Attributes:
        id (str): Feed id (fd_...).
        url (str): The feed itself (after redirects, or the one the page advertised): what is polled.
        title (None | str): The feed's own title, when it has one.
        connected_at (str): When the workspace connected it.
        reading_since (str): Nothing published before this is a live mention: the connection, or the last time its sign-
            in was added or removed (signed in and signed out, a post is read as two different posts, so the switch starts
            over rather than bill one twice).
        auth (ImportFeedsResponse200DataItemFeedType0AuthType0 | None): The sign-in the feed is read with, or null for a
            public feed. PATCH { auth } replaces it, { auth: null } removes it.
        health (ImportFeedsResponse200DataItemFeedType0Health): Whether the hourly read works.
        stats (ImportFeedsResponse200DataItemFeedType0Stats): How the hourly poll of this feed is going.
    """

    id: str
    url: str
    title: None | str
    connected_at: str
    reading_since: str
    auth: ImportFeedsResponse200DataItemFeedType0AuthType0 | None
    health: ImportFeedsResponse200DataItemFeedType0Health
    stats: ImportFeedsResponse200DataItemFeedType0Stats
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.import_feeds_response_200_data_item_feed_type_0_auth_type_0 import (
            ImportFeedsResponse200DataItemFeedType0AuthType0,
        )

        id = self.id

        url = self.url

        title: None | str
        title = self.title

        connected_at = self.connected_at

        reading_since = self.reading_since

        auth: dict[str, Any] | None
        if isinstance(self.auth, ImportFeedsResponse200DataItemFeedType0AuthType0):
            auth = self.auth.to_dict()
        else:
            auth = self.auth

        health = self.health.to_dict()

        stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "title": title,
                "connectedAt": connected_at,
                "readingSince": reading_since,
                "auth": auth,
                "health": health,
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.import_feeds_response_200_data_item_feed_type_0_auth_type_0 import (
            ImportFeedsResponse200DataItemFeedType0AuthType0,
        )
        from ..models.import_feeds_response_200_data_item_feed_type_0_health import (
            ImportFeedsResponse200DataItemFeedType0Health,
        )
        from ..models.import_feeds_response_200_data_item_feed_type_0_stats import (
            ImportFeedsResponse200DataItemFeedType0Stats,
        )

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        connected_at = d.pop("connectedAt")

        reading_since = d.pop("readingSince")

        def _parse_auth(
            data: object,
        ) -> ImportFeedsResponse200DataItemFeedType0AuthType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_type_0 = (
                    ImportFeedsResponse200DataItemFeedType0AuthType0.from_dict(data)
                )

                return auth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImportFeedsResponse200DataItemFeedType0AuthType0 | None, data)

        auth = _parse_auth(d.pop("auth"))

        health = ImportFeedsResponse200DataItemFeedType0Health.from_dict(
            d.pop("health")
        )

        stats = ImportFeedsResponse200DataItemFeedType0Stats.from_dict(d.pop("stats"))

        import_feeds_response_200_data_item_feed_type_0 = cls(
            id=id,
            url=url,
            title=title,
            connected_at=connected_at,
            reading_since=reading_since,
            auth=auth,
            health=health,
            stats=stats,
        )

        import_feeds_response_200_data_item_feed_type_0.additional_properties = d
        return import_feeds_response_200_data_item_feed_type_0

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
