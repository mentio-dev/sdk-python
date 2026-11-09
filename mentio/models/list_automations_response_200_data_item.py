from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_automations_response_200_data_item_actions import (
        ListAutomationsResponse200DataItemActions,
    )
    from ..models.list_automations_response_200_data_item_filter import (
        ListAutomationsResponse200DataItemFilter,
    )


T = TypeVar("T", bound="ListAutomationsResponse200DataItem")


@_attrs_define
class ListAutomationsResponse200DataItem:
    """
    Attributes:
        id (str): Automation id (atm_...).
        name (str): Automation name, unique in the workspace.
        enabled (bool): false: kept but not run.
        filter_ (ListAutomationsResponse200DataItemFilter): Which mentions it acts on: the fields of GET /v1/mentions,
            like a view.
        actions (ListAutomationsResponse200DataItemActions): What it does to each mention the filter selects.
        created_at (str): ISO 8601 timestamp, UTC.
        updated_at (str): ISO 8601 timestamp, UTC.
    """

    id: str
    name: str
    enabled: bool
    filter_: ListAutomationsResponse200DataItemFilter
    actions: ListAutomationsResponse200DataItemActions
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        enabled = self.enabled

        filter_ = self.filter_.to_dict()

        actions = self.actions.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "enabled": enabled,
                "filter": filter_,
                "actions": actions,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_automations_response_200_data_item_actions import (
            ListAutomationsResponse200DataItemActions,
        )
        from ..models.list_automations_response_200_data_item_filter import (
            ListAutomationsResponse200DataItemFilter,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        enabled = d.pop("enabled")

        filter_ = ListAutomationsResponse200DataItemFilter.from_dict(d.pop("filter"))

        actions = ListAutomationsResponse200DataItemActions.from_dict(d.pop("actions"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        list_automations_response_200_data_item = cls(
            id=id,
            name=name,
            enabled=enabled,
            filter_=filter_,
            actions=actions,
            created_at=created_at,
            updated_at=updated_at,
        )

        list_automations_response_200_data_item.additional_properties = d
        return list_automations_response_200_data_item

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
