from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_deletion_preview_automations_item_effect import (
    KeywordDeletionPreviewAutomationsItemEffect,
)

T = TypeVar("T", bound="KeywordDeletionPreviewAutomationsItem")


@_attrs_define
class KeywordDeletionPreviewAutomationsItem:
    """
    Attributes:
        id (str): Automation id (atm_...).
        name (str): Its name.
        enabled (bool): Whether it is on now.
        effect (KeywordDeletionPreviewAutomationsItemEffect): disabled: it named only this keyword and is switched off
            (never widened to every keyword). narrowed: it stops naming this keyword and keeps working on the rest. empty: a
            view naming only this keyword keeps it and shows nothing.
    """

    id: str
    name: str
    enabled: bool
    effect: KeywordDeletionPreviewAutomationsItemEffect
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        enabled = self.enabled

        effect = self.effect.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "enabled": enabled,
                "effect": effect,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        enabled = d.pop("enabled")

        effect = KeywordDeletionPreviewAutomationsItemEffect(d.pop("effect"))

        keyword_deletion_preview_automations_item = cls(
            id=id,
            name=name,
            enabled=enabled,
            effect=effect,
        )

        keyword_deletion_preview_automations_item.additional_properties = d
        return keyword_deletion_preview_automations_item

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
