from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_automation_body_actions import CreateAutomationBodyActions
    from ..models.create_automation_body_filter import CreateAutomationBodyFilter


T = TypeVar("T", bound="CreateAutomationBody")


@_attrs_define
class CreateAutomationBody:
    """
    Attributes:
        name (str): Unique per workspace, case-insensitive.
        actions (CreateAutomationBodyActions): What to do to each mention the filter selects; at least one action.
        enabled (bool | Unset): false saves it without running it. Default: True.
        filter_ (CreateAutomationBodyFilter | Unset): Which new mentions it acts on; empty acts on every one.
    """

    name: str
    actions: CreateAutomationBodyActions
    enabled: bool | Unset = True
    filter_: CreateAutomationBodyFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        actions = self.actions.to_dict()

        enabled = self.enabled

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "actions": actions,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_automation_body_actions import CreateAutomationBodyActions
        from ..models.create_automation_body_filter import CreateAutomationBodyFilter

        d = dict(src_dict)
        name = d.pop("name")

        actions = CreateAutomationBodyActions.from_dict(d.pop("actions"))

        enabled = d.pop("enabled", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: CreateAutomationBodyFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = CreateAutomationBodyFilter.from_dict(_filter_)

        create_automation_body = cls(
            name=name,
            actions=actions,
            enabled=enabled,
            filter_=filter_,
        )

        create_automation_body.additional_properties = d
        return create_automation_body

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
