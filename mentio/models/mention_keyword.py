from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_keyword_matched_as import MentionKeywordMatchedAs
from ..models.mention_keyword_matched_in import MentionKeywordMatchedIn

if TYPE_CHECKING:
    from ..models.group_ref import GroupRef


T = TypeVar("T", bound="MentionKeyword")


@_attrs_define
class MentionKeyword:
    """The keyword this post matched, the group it is in, and how it matched.

    Attributes:
        id (str): Keyword id (kw_...).
        term (str): The tracked term.
        group (GroupRef): The group the keyword belongs to.
        matched_as (MentionKeywordMatchedAs): phrase: the post holds the term as written. close_words: it holds the
            term's words close together, in another order or form (kept and billed only because the classifier scored it
            relevant).
        matched_in (MentionKeywordMatchedIn): text: the term is in the post itself (its text, caption, hashtags or
            review). speech: it is only in what is said in the video (TikTok), whose transcript follows the 🎙 mark in
            post.text.
    """

    id: str
    term: str
    group: GroupRef
    matched_as: MentionKeywordMatchedAs
    matched_in: MentionKeywordMatchedIn
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        term = self.term

        group = self.group.to_dict()

        matched_as = self.matched_as.value

        matched_in = self.matched_in.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "term": term,
                "group": group,
                "matchedAs": matched_as,
                "matchedIn": matched_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.group_ref import GroupRef

        d = dict(src_dict)
        id = d.pop("id")

        term = d.pop("term")

        group = GroupRef.from_dict(d.pop("group"))

        matched_as = MentionKeywordMatchedAs(d.pop("matchedAs"))

        matched_in = MentionKeywordMatchedIn(d.pop("matchedIn"))

        mention_keyword = cls(
            id=id,
            term=term,
            group=group,
            matched_as=matched_as,
            matched_in=matched_in,
        )

        mention_keyword.additional_properties = d
        return mention_keyword

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
