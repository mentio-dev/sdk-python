from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_keyword_body_subreddit_keep import CreateKeywordBodySubredditKeep
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKeywordBodySubreddit")


@_attrs_define
class CreateKeywordBodySubreddit:
    """Follow a whole subreddit in place of `term`: its new posts are read every 3 hours, named or not. Send no
    `platforms`; `context` says what to keep. See [Follow a whole subreddit](/platforms/reddit#follow-a-whole-
    subreddit).

        Attributes:
            name (str): The subreddit: SaaS, r/SaaS or a reddit.com link to it. A name Reddit would not allow is a 400.
            keep (CreateKeywordBodySubredditKeep | Unset): relevant: the classifier keeps the posts relevant to the
                keyword's context (else your company); the rest are dropped unbilled. all: every new post is a mention, billed
                like any. Default: CreateKeywordBodySubredditKeep.RELEVANT.
    """

    name: str
    keep: CreateKeywordBodySubredditKeep | Unset = (
        CreateKeywordBodySubredditKeep.RELEVANT
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        keep: str | Unset = UNSET
        if not isinstance(self.keep, Unset):
            keep = self.keep.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if keep is not UNSET:
            field_dict["keep"] = keep

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        _keep = d.pop("keep", UNSET)
        keep: CreateKeywordBodySubredditKeep | Unset
        if isinstance(_keep, Unset):
            keep = UNSET
        else:
            keep = CreateKeywordBodySubredditKeep(_keep)

        create_keyword_body_subreddit = cls(
            name=name,
            keep=keep,
        )

        create_keyword_body_subreddit.additional_properties = d
        return create_keyword_body_subreddit

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
