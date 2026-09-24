from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_channel_deliveries_response_200_data_item_kind import (
    ListChannelDeliveriesResponse200DataItemKind,
)
from ..models.list_channel_deliveries_response_200_data_item_status import (
    ListChannelDeliveriesResponse200DataItemStatus,
)

if TYPE_CHECKING:
    from ..models.list_channel_deliveries_response_200_data_item_alert import (
        ListChannelDeliveriesResponse200DataItemAlert,
    )
    from ..models.list_channel_deliveries_response_200_data_item_mention_type_0 import (
        ListChannelDeliveriesResponse200DataItemMentionType0,
    )


T = TypeVar("T", bound="ListChannelDeliveriesResponse200DataItem")


@_attrs_define
class ListChannelDeliveriesResponse200DataItem:
    """
    Attributes:
        id (str): Delivery id (dlv_...), also the webhook payload id.
        kind (ListChannelDeliveriesResponse200DataItemKind): mention: an instant rule's delivery. digest: a daily or
            weekly summary. event: an account event the channel subscribed to.
        event (str): The event name the payload carried: the rule's (mention.matched unless it set one, digest for a
            summary) or the account event's.
        status (ListChannelDeliveriesResponse200DataItemStatus):
        attempts (int):
        error (None | str): The last failure, when there was one.
        sent_at (None | str): ISO 8601 timestamp, UTC.
        created_at (str): ISO 8601 timestamp, UTC.
        alert (ListChannelDeliveriesResponse200DataItemAlert): The alert that produced it; name only, since alerts can
            be deleted. name is null for an account event, which no rule produces.
        mention (ListChannelDeliveriesResponse200DataItemMentionType0 | None): For mention deliveries: the post, text
            cut to 160 characters.
    """

    id: str
    kind: ListChannelDeliveriesResponse200DataItemKind
    event: str
    status: ListChannelDeliveriesResponse200DataItemStatus
    attempts: int
    error: None | str
    sent_at: None | str
    created_at: str
    alert: ListChannelDeliveriesResponse200DataItemAlert
    mention: ListChannelDeliveriesResponse200DataItemMentionType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_channel_deliveries_response_200_data_item_mention_type_0 import (
            ListChannelDeliveriesResponse200DataItemMentionType0,
        )

        id = self.id

        kind = self.kind.value

        event = self.event

        status = self.status.value

        attempts = self.attempts

        error: None | str
        error = self.error

        sent_at: None | str
        sent_at = self.sent_at

        created_at = self.created_at

        alert = self.alert.to_dict()

        mention: dict[str, Any] | None
        if isinstance(
            self.mention, ListChannelDeliveriesResponse200DataItemMentionType0
        ):
            mention = self.mention.to_dict()
        else:
            mention = self.mention

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "event": event,
                "status": status,
                "attempts": attempts,
                "error": error,
                "sentAt": sent_at,
                "createdAt": created_at,
                "alert": alert,
                "mention": mention,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_channel_deliveries_response_200_data_item_alert import (
            ListChannelDeliveriesResponse200DataItemAlert,
        )
        from ..models.list_channel_deliveries_response_200_data_item_mention_type_0 import (
            ListChannelDeliveriesResponse200DataItemMentionType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        kind = ListChannelDeliveriesResponse200DataItemKind(d.pop("kind"))

        event = d.pop("event")

        status = ListChannelDeliveriesResponse200DataItemStatus(d.pop("status"))

        attempts = d.pop("attempts")

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        def _parse_sent_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sent_at = _parse_sent_at(d.pop("sentAt"))

        created_at = d.pop("createdAt")

        alert = ListChannelDeliveriesResponse200DataItemAlert.from_dict(d.pop("alert"))

        def _parse_mention(
            data: object,
        ) -> ListChannelDeliveriesResponse200DataItemMentionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mention_type_0 = (
                    ListChannelDeliveriesResponse200DataItemMentionType0.from_dict(data)
                )

                return mention_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListChannelDeliveriesResponse200DataItemMentionType0 | None, data
            )

        mention = _parse_mention(d.pop("mention"))

        list_channel_deliveries_response_200_data_item = cls(
            id=id,
            kind=kind,
            event=event,
            status=status,
            attempts=attempts,
            error=error,
            sent_at=sent_at,
            created_at=created_at,
            alert=alert,
            mention=mention,
        )

        list_channel_deliveries_response_200_data_item.additional_properties = d
        return list_channel_deliveries_response_200_data_item

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
