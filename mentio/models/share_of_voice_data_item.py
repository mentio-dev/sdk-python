from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.share_of_voice_data_item_keyword import ShareOfVoiceDataItemKeyword
    from ..models.share_of_voice_data_item_previous_type_0 import (
        ShareOfVoiceDataItemPreviousType0,
    )


T = TypeVar("T", bound="ShareOfVoiceDataItem")


@_attrs_define
class ShareOfVoiceDataItem:
    """
    Attributes:
        keyword (ShareOfVoiceDataItemKeyword): The keyword this row is about.
        matched (int): Matches of this keyword in the window.
        relevant (int): Of those, scored at or above the relevance threshold.
        negative (int): Of those, classified negative.
        buy_intent (int): Of those, carrying the buy_intent intent.
        share (float | None): Percent of brand plus competitor matches, one decimal; null for topics, which stay out of
            the split.
        previous (None | ShareOfVoiceDataItemPreviousType0): The same keyword over the period right before the window;
            null unless compare=true.
    """

    keyword: ShareOfVoiceDataItemKeyword
    matched: int
    relevant: int
    negative: int
    buy_intent: int
    share: float | None
    previous: None | ShareOfVoiceDataItemPreviousType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.share_of_voice_data_item_previous_type_0 import (
            ShareOfVoiceDataItemPreviousType0,
        )

        keyword = self.keyword.to_dict()

        matched = self.matched

        relevant = self.relevant

        negative = self.negative

        buy_intent = self.buy_intent

        share: float | None
        share = self.share

        previous: dict[str, Any] | None
        if isinstance(self.previous, ShareOfVoiceDataItemPreviousType0):
            previous = self.previous.to_dict()
        else:
            previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keyword": keyword,
                "matched": matched,
                "relevant": relevant,
                "negative": negative,
                "buyIntent": buy_intent,
                "share": share,
                "previous": previous,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.share_of_voice_data_item_keyword import (
            ShareOfVoiceDataItemKeyword,
        )
        from ..models.share_of_voice_data_item_previous_type_0 import (
            ShareOfVoiceDataItemPreviousType0,
        )

        d = dict(src_dict)
        keyword = ShareOfVoiceDataItemKeyword.from_dict(d.pop("keyword"))

        matched = d.pop("matched")

        relevant = d.pop("relevant")

        negative = d.pop("negative")

        buy_intent = d.pop("buyIntent")

        def _parse_share(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        share = _parse_share(d.pop("share"))

        def _parse_previous(data: object) -> None | ShareOfVoiceDataItemPreviousType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                previous_type_0 = ShareOfVoiceDataItemPreviousType0.from_dict(data)

                return previous_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ShareOfVoiceDataItemPreviousType0, data)

        previous = _parse_previous(d.pop("previous"))

        share_of_voice_data_item = cls(
            keyword=keyword,
            matched=matched,
            relevant=relevant,
            negative=negative,
            buy_intent=buy_intent,
            share=share,
            previous=previous,
        )

        share_of_voice_data_item.additional_properties = d
        return share_of_voice_data_item

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
