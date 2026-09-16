from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_people_response_200_data_item_outreach_stage import (
    ListPeopleResponse200DataItemOutreachStage,
)

if TYPE_CHECKING:
    from ..models.list_people_response_200_data_item_outreach_owner_type_0 import (
        ListPeopleResponse200DataItemOutreachOwnerType0,
    )


T = TypeVar("T", bound="ListPeopleResponse200DataItemOutreach")


@_attrs_define
class ListPeopleResponse200DataItemOutreach:
    """Where your workspace stands with the person. The first logged activity claims an unowned person for whoever reached
    out and moves not_contacted to contacted.

        Attributes:
            owner (ListPeopleResponse200DataItemOutreachOwnerType0 | None): The teammate who owns the contact; null when
                nobody does, or the owner left the workspace.
            stage (ListPeopleResponse200DataItemOutreachStage): Where your workspace stands with the person: not_contacted,
                contacted, replied, in_talks, customer or not_a_fit.
            last_contacted_at (None | str): The newest logged activity; null when nobody logged a contact.
    """

    owner: ListPeopleResponse200DataItemOutreachOwnerType0 | None
    stage: ListPeopleResponse200DataItemOutreachStage
    last_contacted_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_people_response_200_data_item_outreach_owner_type_0 import (
            ListPeopleResponse200DataItemOutreachOwnerType0,
        )

        owner: dict[str, Any] | None
        if isinstance(self.owner, ListPeopleResponse200DataItemOutreachOwnerType0):
            owner = self.owner.to_dict()
        else:
            owner = self.owner

        stage = self.stage.value

        last_contacted_at: None | str
        last_contacted_at = self.last_contacted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "stage": stage,
                "lastContactedAt": last_contacted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.list_people_response_200_data_item_outreach_owner_type_0 import (
            ListPeopleResponse200DataItemOutreachOwnerType0,
        )

        d = dict(src_dict)

        def _parse_owner(
            data: object,
        ) -> ListPeopleResponse200DataItemOutreachOwnerType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                owner_type_0 = (
                    ListPeopleResponse200DataItemOutreachOwnerType0.from_dict(data)
                )

                return owner_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListPeopleResponse200DataItemOutreachOwnerType0 | None, data)

        owner = _parse_owner(d.pop("owner"))

        stage = ListPeopleResponse200DataItemOutreachStage(d.pop("stage"))

        def _parse_last_contacted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_contacted_at = _parse_last_contacted_at(d.pop("lastContactedAt"))

        list_people_response_200_data_item_outreach = cls(
            owner=owner,
            stage=stage,
            last_contacted_at=last_contacted_at,
        )

        list_people_response_200_data_item_outreach.additional_properties = d
        return list_people_response_200_data_item_outreach

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
