from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListAutomationsResponse200DataItemActions")


@_attrs_define
class ListAutomationsResponse200DataItemActions:
    """What it does to each mention the filter selects.

    Attributes:
        add_labels (list[str]): Labels it adds.
        assignee_id (None | str): The member it assigns, or null.
    """

    add_labels: list[str]
    assignee_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_labels = self.add_labels

        assignee_id: None | str
        assignee_id = self.assignee_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addLabels": add_labels,
                "assigneeId": assignee_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        add_labels = cast(list[str], d.pop("addLabels"))

        def _parse_assignee_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        assignee_id = _parse_assignee_id(d.pop("assigneeId"))

        list_automations_response_200_data_item_actions = cls(
            add_labels=add_labels,
            assignee_id=assignee_id,
        )

        list_automations_response_200_data_item_actions.additional_properties = d
        return list_automations_response_200_data_item_actions

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
