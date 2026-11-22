from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_keyword_body_subreddit_keep import UpdateKeywordBodySubredditKeep

T = TypeVar("T", bound="UpdateKeywordBodySubreddit")


@_attrs_define
class UpdateKeywordBodySubreddit:
    """A keyword that follows a subreddit: what it keeps from now on. The subreddit itself cannot change (create another
    keyword), and a phrase keyword cannot become one (400).

        Attributes:
            keep (UpdateKeywordBodySubredditKeep): relevant: the classifier keeps the posts relevant to the keyword's
                context (else your company); the rest are dropped unbilled. all: every new post is a mention, billed like any.
    """

    keep: UpdateKeywordBodySubredditKeep
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keep = self.keep.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keep": keep,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keep = UpdateKeywordBodySubredditKeep(d.pop("keep"))

        update_keyword_body_subreddit = cls(
            keep=keep,
        )

        update_keyword_body_subreddit.additional_properties = d
        return update_keyword_body_subreddit

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
