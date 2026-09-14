from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mention_triage_assignee_type_0 import MentionTriageAssigneeType0


T = TypeVar("T", bound="MentionTriage")


@_attrs_define
class MentionTriage:
    """
    Attributes:
        assignee (MentionTriageAssigneeType0 | None): Workspace member this mention is assigned to; null when
            unassigned.
        snoozed_until (None | str): Until when the mention stays out of the feed; null when not snoozed.
        note (None | str): Internal note; null when none.
    """

    assignee: MentionTriageAssigneeType0 | None
    snoozed_until: None | str
    note: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mention_triage_assignee_type_0 import (
            MentionTriageAssigneeType0,
        )

        assignee: dict[str, Any] | None
        if isinstance(self.assignee, MentionTriageAssigneeType0):
            assignee = self.assignee.to_dict()
        else:
            assignee = self.assignee

        snoozed_until: None | str
        snoozed_until = self.snoozed_until

        note: None | str
        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignee": assignee,
                "snoozedUntil": snoozed_until,
                "note": note,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mention_triage_assignee_type_0 import (
            MentionTriageAssigneeType0,
        )

        d = dict(src_dict)

        def _parse_assignee(data: object) -> MentionTriageAssigneeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                assignee_type_0 = MentionTriageAssigneeType0.from_dict(data)

                return assignee_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionTriageAssigneeType0 | None, data)

        assignee = _parse_assignee(d.pop("assignee"))

        def _parse_snoozed_until(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        snoozed_until = _parse_snoozed_until(d.pop("snoozedUntil"))

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        mention_triage = cls(
            assignee=assignee,
            snoozed_until=snoozed_until,
            note=note,
        )

        mention_triage.additional_properties = d
        return mention_triage

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
