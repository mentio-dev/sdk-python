from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_subreddit_type_0_keep import KeywordSubredditType0Keep

T = TypeVar("T", bound="KeywordSubredditType0")


@_attrs_define
class KeywordSubredditType0:
    """The subreddit this keyword follows instead of a phrase (its term reads r/<name>); null on a phrase keyword.

    Attributes:
        name (str): The subreddit, without r/.
        keep (KeywordSubredditType0Keep): relevant: the classifier keeps the posts relevant to the keyword's context
            (else your company); the rest are dropped unbilled. all: every new post is a mention, billed like any.
        url (str): The subreddit on reddit.com.
    """

    name: str
    keep: KeywordSubredditType0Keep
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        keep = self.keep.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "keep": keep,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        keep = KeywordSubredditType0Keep(d.pop("keep"))

        url = d.pop("url")

        keyword_subreddit_type_0 = cls(
            name=name,
            keep=keep,
            url=url,
        )

        keyword_subreddit_type_0.additional_properties = d
        return keyword_subreddit_type_0

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
