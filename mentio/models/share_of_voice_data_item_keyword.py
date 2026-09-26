from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.share_of_voice_data_item_keyword_kind import (
    ShareOfVoiceDataItemKeywordKind,
)

if TYPE_CHECKING:
    from ..models.share_of_voice_data_item_keyword_group import (
        ShareOfVoiceDataItemKeywordGroup,
    )


T = TypeVar("T", bound="ShareOfVoiceDataItemKeyword")


@_attrs_define
class ShareOfVoiceDataItemKeyword:
    """The keyword this row is about.

    Attributes:
        id (str): Keyword id (kw_...).
        term (str): The tracked term.
        kind (ShareOfVoiceDataItemKeywordKind): brand, competitor or topic.
        group (ShareOfVoiceDataItemKeywordGroup):
    """

    id: str
    term: str
    kind: ShareOfVoiceDataItemKeywordKind
    group: ShareOfVoiceDataItemKeywordGroup
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        term = self.term

        kind = self.kind.value

        group = self.group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "term": term,
                "kind": kind,
                "group": group,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.share_of_voice_data_item_keyword_group import (
            ShareOfVoiceDataItemKeywordGroup,
        )

        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        kind = ShareOfVoiceDataItemKeywordKind(d.pop("kind"))

        group = ShareOfVoiceDataItemKeywordGroup.from_dict(d.pop("group"))

        share_of_voice_data_item_keyword = cls(
            id=id,
            term=term,
            kind=kind,
            group=group,
        )

        share_of_voice_data_item_keyword.additional_properties = d
        return share_of_voice_data_item_keyword

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
