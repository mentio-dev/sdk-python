from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_status import MentionStatus

if TYPE_CHECKING:
    from ..models.mention_author_type_0 import MentionAuthorType0
    from ..models.mention_classification_type_0 import MentionClassificationType0
    from ..models.mention_keyword import MentionKeyword
    from ..models.mention_post import MentionPost
    from ..models.mention_triage import MentionTriage


T = TypeVar("T", bound="Mention")


@_attrs_define
class Mention:
    """
    Attributes:
        id (str): Mention id (mm_...): one post matched to one of your keywords. A post matching two keywords has two
            ids.
        status (MentionStatus): open: nobody handled it yet. ignored: hidden from the feed and channels by you. done:
            handled.
        relevant (bool): The classifier scored it at or above the delivery threshold (40).
        delivered (bool): Reached at least one of your channels.
        priority (float): Attention score, one decimal, computed at read time: relevance halved, author reach on a
            follower ladder (unknown reach counts 8), the strongest intent (buy intent 20 down to praise 5), minus 2 per day
            of age floored at 20.
        keyword (MentionKeyword): The keyword this post matched.
        post (MentionPost):
        author (MentionAuthorType0 | None): Who posted it; null when the platform gave no author at all.
        classification (MentionClassificationType0 | None): The classifier verdict, as corrected by your feedback; null
            while the post is still queued for classification.
        triage (MentionTriage):
        created_at (str): When the match was recorded; the default feed order.
    """

    id: str
    status: MentionStatus
    relevant: bool
    delivered: bool
    priority: float
    keyword: MentionKeyword
    post: MentionPost
    author: MentionAuthorType0 | None
    classification: MentionClassificationType0 | None
    triage: MentionTriage
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mention_author_type_0 import MentionAuthorType0
        from ..models.mention_classification_type_0 import (
            MentionClassificationType0,
        )

        id = self.id

        status = self.status.value

        relevant = self.relevant

        delivered = self.delivered

        priority = self.priority

        keyword = self.keyword.to_dict()

        post = self.post.to_dict()

        author: dict[str, Any] | None
        if isinstance(self.author, MentionAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

        classification: dict[str, Any] | None
        if isinstance(self.classification, MentionClassificationType0):
            classification = self.classification.to_dict()
        else:
            classification = self.classification

        triage = self.triage.to_dict()

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "relevant": relevant,
                "delivered": delivered,
                "priority": priority,
                "keyword": keyword,
                "post": post,
                "author": author,
                "classification": classification,
                "triage": triage,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mention_author_type_0 import MentionAuthorType0
        from ..models.mention_classification_type_0 import (
            MentionClassificationType0,
        )
        from ..models.mention_keyword import MentionKeyword
        from ..models.mention_post import MentionPost
        from ..models.mention_triage import MentionTriage

        d = dict(src_dict)
        id = d.pop("id")

        status = MentionStatus(d.pop("status"))

        relevant = d.pop("relevant")

        delivered = d.pop("delivered")

        priority = d.pop("priority")

        keyword = MentionKeyword.from_dict(d.pop("keyword"))

        post = MentionPost.from_dict(d.pop("post"))

        def _parse_author(data: object) -> MentionAuthorType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = MentionAuthorType0.from_dict(data)

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionAuthorType0 | None, data)

        author = _parse_author(d.pop("author"))

        def _parse_classification(data: object) -> MentionClassificationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                classification_type_0 = MentionClassificationType0.from_dict(data)

                return classification_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionClassificationType0 | None, data)

        classification = _parse_classification(d.pop("classification"))

        triage = MentionTriage.from_dict(d.pop("triage"))

        created_at = d.pop("createdAt")

        mention = cls(
            id=id,
            status=status,
            relevant=relevant,
            delivered=delivered,
            priority=priority,
            keyword=keyword,
            post=post,
            author=author,
            classification=classification,
            triage=triage,
            created_at=created_at,
        )

        mention.additional_properties = d
        return mention

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
