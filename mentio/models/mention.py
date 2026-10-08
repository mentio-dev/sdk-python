from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_status import MentionStatus

if TYPE_CHECKING:
    from ..models.mention_author_type_0 import MentionAuthorType0
    from ..models.mention_classification_type_0 import MentionClassificationType0
    from ..models.mention_duplicates_item import MentionDuplicatesItem
    from ..models.mention_keyword import MentionKeyword
    from ..models.mention_post import MentionPost
    from ..models.mention_review_type_0 import MentionReviewType0
    from ..models.mention_stats import MentionStats
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
        keyword (MentionKeyword): The keyword this post matched, the group it is in, and how it matched.
        post (MentionPost):
        parent_mention_id (None | str): For a comment whose parent post or comment is itself one of your mentions: that
            mention's id (mm_...). Null otherwise.
        author (MentionAuthorType0 | None): Who posted it; null when the platform gave no author at all.
        review (MentionReviewType0 | None): An app store review's facts; null for every other post. Its sentiment comes
            from the stars (4 and 5 positive, 3 neutral, 1 and 2 negative) and it always counts as relevant, since you chose
            the app.
        classification (MentionClassificationType0 | None): The classifier verdict, as corrected by your feedback; null
            while the post is still queued for classification.
        triage (MentionTriage):
        duplicate_of (None | str): Set on a cross-post: the id of the mention this one copies (the same author posting
            the same text again for the same keyword within three days, like one announcement pasted into five subreddits).
            A copy is billed like any mention but is listed only under its original and never alerted on its own. null for
            an original.
        duplicates (list[MentionDuplicatesItem]): The cross-posts filed under this mention, oldest first: where else its
            author posted it. Empty when there are none, and on a copy.
        stats (MentionStats): Computed counts.
        created_at (str): When the match was recorded; the default feed order.
    """

    id: str
    status: MentionStatus
    relevant: bool
    delivered: bool
    priority: float
    keyword: MentionKeyword
    post: MentionPost
    parent_mention_id: None | str
    author: MentionAuthorType0 | None
    review: MentionReviewType0 | None
    classification: MentionClassificationType0 | None
    triage: MentionTriage
    duplicate_of: None | str
    duplicates: list[MentionDuplicatesItem]
    stats: MentionStats
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mention_author_type_0 import MentionAuthorType0
        from ..models.mention_classification_type_0 import (
            MentionClassificationType0,
        )
        from ..models.mention_review_type_0 import MentionReviewType0

        id = self.id

        status = self.status.value

        relevant = self.relevant

        delivered = self.delivered

        priority = self.priority

        keyword = self.keyword.to_dict()

        post = self.post.to_dict()

        parent_mention_id: None | str
        parent_mention_id = self.parent_mention_id

        author: dict[str, Any] | None
        if isinstance(self.author, MentionAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

        review: dict[str, Any] | None
        if isinstance(self.review, MentionReviewType0):
            review = self.review.to_dict()
        else:
            review = self.review

        classification: dict[str, Any] | None
        if isinstance(self.classification, MentionClassificationType0):
            classification = self.classification.to_dict()
        else:
            classification = self.classification

        triage = self.triage.to_dict()

        duplicate_of: None | str
        duplicate_of = self.duplicate_of

        duplicates = []
        for duplicates_item_data in self.duplicates:
            duplicates_item = duplicates_item_data.to_dict()
            duplicates.append(duplicates_item)

        stats = self.stats.to_dict()

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
                "parentMentionId": parent_mention_id,
                "author": author,
                "review": review,
                "classification": classification,
                "triage": triage,
                "duplicateOf": duplicate_of,
                "duplicates": duplicates,
                "stats": stats,
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
        from ..models.mention_duplicates_item import (
            MentionDuplicatesItem,
        )
        from ..models.mention_keyword import MentionKeyword
        from ..models.mention_post import MentionPost
        from ..models.mention_review_type_0 import MentionReviewType0
        from ..models.mention_stats import MentionStats
        from ..models.mention_triage import MentionTriage

        d = dict(src_dict)
        id = d.pop("id")

        status = MentionStatus(d.pop("status"))

        relevant = d.pop("relevant")

        delivered = d.pop("delivered")

        priority = d.pop("priority")

        keyword = MentionKeyword.from_dict(d.pop("keyword"))

        post = MentionPost.from_dict(d.pop("post"))

        def _parse_parent_mention_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_mention_id = _parse_parent_mention_id(d.pop("parentMentionId"))

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

        def _parse_review(data: object) -> MentionReviewType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                review_type_0 = MentionReviewType0.from_dict(data)

                return review_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionReviewType0 | None, data)

        review = _parse_review(d.pop("review"))

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

        def _parse_duplicate_of(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        duplicate_of = _parse_duplicate_of(d.pop("duplicateOf"))

        duplicates = []
        _duplicates = d.pop("duplicates")
        for duplicates_item_data in _duplicates:
            duplicates_item = MentionDuplicatesItem.from_dict(duplicates_item_data)

            duplicates.append(duplicates_item)

        stats = MentionStats.from_dict(d.pop("stats"))

        created_at = d.pop("createdAt")

        mention = cls(
            id=id,
            status=status,
            relevant=relevant,
            delivered=delivered,
            priority=priority,
            keyword=keyword,
            post=post,
            parent_mention_id=parent_mention_id,
            author=author,
            review=review,
            classification=classification,
            triage=triage,
            duplicate_of=duplicate_of,
            duplicates=duplicates,
            stats=stats,
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
