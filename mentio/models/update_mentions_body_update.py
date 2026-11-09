from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_mentions_body_update_status import UpdateMentionsBodyUpdateStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateMentionsBodyUpdate")


@_attrs_define
class UpdateMentionsBodyUpdate:
    """Every field is optional, at least one is required; omitted fields are untouched.

    Attributes:
        status (UpdateMentionsBodyUpdateStatus | Unset): ignored or done to handle them; open to put them back.
        assignee_id (None | str | Unset): A workspace member (user id), or null to unassign.
        add_labels (list[str] | Unset): Labels to add; a mention keeps at most 20, and labels past that are not added.
        remove_labels (list[str] | Unset): Labels to remove; a label a mention does not carry is ignored.
    """

    status: UpdateMentionsBodyUpdateStatus | Unset = UNSET
    assignee_id: None | str | Unset = UNSET
    add_labels: list[str] | Unset = UNSET
    remove_labels: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        else:
            assignee_id = self.assignee_id

        add_labels: list[str] | Unset = UNSET
        if not isinstance(self.add_labels, Unset):
            add_labels = self.add_labels

        remove_labels: list[str] | Unset = UNSET
        if not isinstance(self.remove_labels, Unset):
            remove_labels = self.remove_labels

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if add_labels is not UNSET:
            field_dict["addLabels"] = add_labels
        if remove_labels is not UNSET:
            field_dict["removeLabels"] = remove_labels

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: UpdateMentionsBodyUpdateStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateMentionsBodyUpdateStatus(_status)

        def _parse_assignee_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_id = _parse_assignee_id(d.pop("assigneeId", UNSET))

        add_labels = cast(list[str], d.pop("addLabels", UNSET))

        remove_labels = cast(list[str], d.pop("removeLabels", UNSET))

        update_mentions_body_update = cls(
            status=status,
            assignee_id=assignee_id,
            add_labels=add_labels,
            remove_labels=remove_labels,
        )

        return update_mentions_body_update
