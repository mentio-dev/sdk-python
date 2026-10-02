from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attention_item_kind import AttentionItemKind
from ..models.attention_item_status import AttentionItemStatus

if TYPE_CHECKING:
    from ..models.attention_item_subject import AttentionItemSubject
    from ..models.channel_failing_event_data import ChannelFailingEventData
    from ..models.keyword_noisy_event_data import KeywordNoisyEventData
    from ..models.mention_spike_event_data import MentionSpikeEventData
    from ..models.negative_spike_event_data import NegativeSpikeEventData


T = TypeVar("T", bound="AttentionItem")


@_attrs_define
class AttentionItem:
    """
    Attributes:
        id (str): Attention item id (att_...).
        kind (AttentionItemKind): mention.spike: far more mentions in the last hour than the keyword usually gets.
            sentiment.negative_spike: the negative share of the last 24 hours jumped. keyword.noisy: most scored matches are
            noise. channel.failing: the channel's last sends all failed.
        status (AttentionItemStatus): open: the condition holds. resolved: it no longer does. dismissed: a person put it
            away; it does not come back for the same episode.
        subject (AttentionItemSubject): What the item is about.
        title (str): One line for a person: what happened.
        opened_at (str): When the condition was first seen.
        resolved_at (None | str): When it no longer held; null while it does.
        dismissed_at (None | str): When a person dismissed it; null if nobody did.
        data (ChannelFailingEventData | KeywordNoisyEventData | MentionSpikeEventData | NegativeSpikeEventData): The
            facts as they stood when it opened: the same object the account event of the same name carries as `data`.
    """

    id: str
    kind: AttentionItemKind
    status: AttentionItemStatus
    subject: AttentionItemSubject
    title: str
    opened_at: str
    resolved_at: None | str
    dismissed_at: None | str
    data: (
        ChannelFailingEventData
        | KeywordNoisyEventData
        | MentionSpikeEventData
        | NegativeSpikeEventData
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.keyword_noisy_event_data import KeywordNoisyEventData
        from ..models.mention_spike_event_data import MentionSpikeEventData
        from ..models.negative_spike_event_data import NegativeSpikeEventData

        id = self.id

        kind = self.kind.value

        status = self.status.value

        subject = self.subject.to_dict()

        title = self.title

        opened_at = self.opened_at

        resolved_at: None | str
        resolved_at = self.resolved_at

        dismissed_at: None | str
        dismissed_at = self.dismissed_at

        data: dict[str, Any]
        if (
            isinstance(self.data, MentionSpikeEventData)
            or isinstance(self.data, NegativeSpikeEventData)
            or isinstance(self.data, KeywordNoisyEventData)
        ):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "status": status,
                "subject": subject,
                "title": title,
                "openedAt": opened_at,
                "resolvedAt": resolved_at,
                "dismissedAt": dismissed_at,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.attention_item_subject import (
            AttentionItemSubject,
        )
        from ..models.channel_failing_event_data import (
            ChannelFailingEventData,
        )
        from ..models.keyword_noisy_event_data import (
            KeywordNoisyEventData,
        )
        from ..models.mention_spike_event_data import (
            MentionSpikeEventData,
        )
        from ..models.negative_spike_event_data import (
            NegativeSpikeEventData,
        )

        d = dict(src_dict)
        id = d.pop("id")

        kind = AttentionItemKind(d.pop("kind"))

        status = AttentionItemStatus(d.pop("status"))

        subject = AttentionItemSubject.from_dict(d.pop("subject"))

        title = d.pop("title")

        opened_at = d.pop("openedAt")

        def _parse_resolved_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_at = _parse_resolved_at(d.pop("resolvedAt"))

        def _parse_dismissed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dismissed_at = _parse_dismissed_at(d.pop("dismissedAt"))

        def _parse_data(
            data: object,
        ) -> (
            ChannelFailingEventData
            | KeywordNoisyEventData
            | MentionSpikeEventData
            | NegativeSpikeEventData
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = MentionSpikeEventData.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = NegativeSpikeEventData.from_dict(data)

                return data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_2 = KeywordNoisyEventData.from_dict(data)

                return data_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_3 = ChannelFailingEventData.from_dict(data)

            return data_type_3

        data = _parse_data(d.pop("data"))

        attention_item = cls(
            id=id,
            kind=kind,
            status=status,
            subject=subject,
            title=title,
            opened_at=opened_at,
            resolved_at=resolved_at,
            dismissed_at=dismissed_at,
            data=data,
        )

        attention_item.additional_properties = d
        return attention_item

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
