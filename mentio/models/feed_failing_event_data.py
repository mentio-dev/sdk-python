from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feed_failing_event_data_reason import FeedFailingEventDataReason

if TYPE_CHECKING:
    from ..models.feed_failing_event_data_feed import FeedFailingEventDataFeed


T = TypeVar("T", bound="FeedFailingEventData")


@_attrs_define
class FeedFailingEventData:
    """
    Attributes:
        attention_id (str): The attention item (att_...): GET /v1/attention lists it, POST /v1/attention/{id}/dismiss
            puts it away.
        url (str): Where to look in the dashboard.
        feed (FeedFailingEventDataFeed): The workspace feed (GET /v1/feeds/{id}).
        reason (FeedFailingEventDataReason): login_required: the feed answers a sign-in or access-denied page (connect
            it with the forum's sign-in, auth). login_expired: the same on a feed that has a sign-in: copy a fresh cookie.
            blocked: a 403, a 429 or a bot check. not_found: the feed is gone. not_a_feed: the address answers a page, not
            RSS or Atom. unreachable: no answer or a server error.
        detail (None | str): What the last failed read saw, in a few words.
        failing_since (str): When it started failing: the third failed read in a row.
        keywords_affected (int): Live keywords of the workspace that read workspace feeds: what misses its posts while
            it fails.
    """

    attention_id: str
    url: str
    feed: FeedFailingEventDataFeed
    reason: FeedFailingEventDataReason
    detail: None | str
    failing_since: str
    keywords_affected: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attention_id = self.attention_id

        url = self.url

        feed = self.feed.to_dict()

        reason = self.reason.value

        detail: None | str
        detail = self.detail

        failing_since = self.failing_since

        keywords_affected = self.keywords_affected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attentionId": attention_id,
                "url": url,
                "feed": feed,
                "reason": reason,
                "detail": detail,
                "failingSince": failing_since,
                "keywordsAffected": keywords_affected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feed_failing_event_data_feed import FeedFailingEventDataFeed

        d = dict(src_dict)
        attention_id = d.pop("attentionId")

        url = d.pop("url")

        feed = FeedFailingEventDataFeed.from_dict(d.pop("feed"))

        reason = FeedFailingEventDataReason(d.pop("reason"))

        def _parse_detail(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        detail = _parse_detail(d.pop("detail"))

        failing_since = d.pop("failingSince")

        keywords_affected = d.pop("keywordsAffected")

        feed_failing_event_data = cls(
            attention_id=attention_id,
            url=url,
            feed=feed,
            reason=reason,
            detail=detail,
            failing_since=failing_since,
            keywords_affected=keywords_affected,
        )

        feed_failing_event_data.additional_properties = d
        return feed_failing_event_data

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
