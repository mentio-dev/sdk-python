from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsSeriesDataItemKeywordType0Group")


@_attrs_define
class AnalyticsSeriesDataItemKeywordType0Group:
    """
    Attributes:
        id (str): Group id (grp_...).
        name (str): The group's name.
        external_id (None | str): Your own id for the group, or null.
        is_default (bool): The workspace's default group, where a keyword lands when no group is named.
    """

    id: str
    name: str
    external_id: None | str
    is_default: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        external_id: None | str
        external_id = self.external_id

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "externalId": external_id,
                "isDefault": is_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_id = _parse_external_id(d.pop("externalId"))

        is_default = d.pop("isDefault")

        analytics_series_data_item_keyword_type_0_group = cls(
            id=id,
            name=name,
            external_id=external_id,
            is_default=is_default,
        )

        analytics_series_data_item_keyword_type_0_group.additional_properties = d
        return analytics_series_data_item_keyword_type_0_group

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
