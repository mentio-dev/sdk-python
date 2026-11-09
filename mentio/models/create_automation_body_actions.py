from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAutomationBodyActions")


@_attrs_define
class CreateAutomationBodyActions:
    """What to do to each mention the filter selects; at least one action.

    Attributes:
        add_labels (list[str] | Unset): Labels to add, at most 10. A mention keeps at most 20 labels.
        assignee_id (None | str | Unset): A workspace member (user id) to assign when the mention has nobody yet;
            someone already assigned is kept.
    """

    add_labels: list[str] | Unset = UNSET
    assignee_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        add_labels: list[str] | Unset = UNSET
        if not isinstance(self.add_labels, Unset):
            add_labels = self.add_labels

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        else:
            assignee_id = self.assignee_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if add_labels is not UNSET:
            field_dict["addLabels"] = add_labels
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        add_labels = cast(list[str], d.pop("addLabels", UNSET))

        def _parse_assignee_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_id = _parse_assignee_id(d.pop("assigneeId", UNSET))

        create_automation_body_actions = cls(
            add_labels=add_labels,
            assignee_id=assignee_id,
        )

        return create_automation_body_actions
