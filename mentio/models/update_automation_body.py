from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_automation_body_actions import UpdateAutomationBodyActions
    from ..models.update_automation_body_filter import UpdateAutomationBodyFilter


T = TypeVar("T", bound="UpdateAutomationBody")


@_attrs_define
class UpdateAutomationBody:
    """
    Attributes:
        name (str | Unset): Automation name, unique in the workspace.
        enabled (bool | Unset): false stops it; true runs it again on new mentions.
        filter_ (UpdateAutomationBodyFilter | Unset): Replaces the whole filter.
        actions (UpdateAutomationBodyActions | Unset): Replaces every action.
    """

    name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    filter_: UpdateAutomationBodyFilter | Unset = UNSET
    actions: UpdateAutomationBodyActions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enabled = self.enabled

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_automation_body_actions import UpdateAutomationBodyActions
        from ..models.update_automation_body_filter import UpdateAutomationBodyFilter

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: UpdateAutomationBodyFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = UpdateAutomationBodyFilter.from_dict(_filter_)

        _actions = d.pop("actions", UNSET)
        actions: UpdateAutomationBodyActions | Unset
        if isinstance(_actions, Unset):
            actions = UNSET
        else:
            actions = UpdateAutomationBodyActions.from_dict(_actions)

        update_automation_body = cls(
            name=name,
            enabled=enabled,
            filter_=filter_,
            actions=actions,
        )

        update_automation_body.additional_properties = d
        return update_automation_body

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
