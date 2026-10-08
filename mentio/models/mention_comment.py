from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mention_comment_author_type_0 import MentionCommentAuthorType0
    from ..models.mention_comment_classification_type_0 import (
        MentionCommentClassificationType0,
    )
    from ..models.mention_comment_engagement_type_0 import MentionCommentEngagementType0


T = TypeVar("T", bound="MentionComment")


@_attrs_define
class MentionComment:
    """
    Attributes:
        id (str): Comment id (men_...): the item itself, the same for every workspace it reaches.
        url (str): Permalink of the comment.
        text (str): The comment, truncated to 8 KB at ingest.
        published_at (str): When the comment was written.
        author (MentionCommentAuthorType0 | None): Who wrote it; null when the platform gave no author (a deleted
            account).
        parent_comment_id (None | str): The comment this one answers, when it is a reply inside the thread; null for a
            comment on the post itself.
        engagement (MentionCommentEngagementType0 | None): Engagement counts as the platform reported them when the post
            was ingested, usually minutes after it was written; a count the platform does not have is null. Null as a whole
            for platforms that report none and for posts ingested before September 2026. X carries all six.
        classification (MentionCommentClassificationType0 | None): A light read of the comment (sentiment and intent
            tags); null until it is scored, usually minutes after the thread arrives.
        mention_id (None | str): When this comment itself names one of your keywords, its mention (mm_...), with the
            full verdict. Null otherwise.
    """

    id: str
    url: str
    text: str
    published_at: str
    author: MentionCommentAuthorType0 | None
    parent_comment_id: None | str
    engagement: MentionCommentEngagementType0 | None
    classification: MentionCommentClassificationType0 | None
    mention_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mention_comment_author_type_0 import (
            MentionCommentAuthorType0,
        )
        from ..models.mention_comment_classification_type_0 import (
            MentionCommentClassificationType0,
        )
        from ..models.mention_comment_engagement_type_0 import (
            MentionCommentEngagementType0,
        )

        id = self.id

        url = self.url

        text = self.text

        published_at = self.published_at

        author: dict[str, Any] | None
        if isinstance(self.author, MentionCommentAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

        parent_comment_id: None | str
        parent_comment_id = self.parent_comment_id

        engagement: dict[str, Any] | None
        if isinstance(self.engagement, MentionCommentEngagementType0):
            engagement = self.engagement.to_dict()
        else:
            engagement = self.engagement

        classification: dict[str, Any] | None
        if isinstance(self.classification, MentionCommentClassificationType0):
            classification = self.classification.to_dict()
        else:
            classification = self.classification

        mention_id: None | str
        mention_id = self.mention_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "text": text,
                "publishedAt": published_at,
                "author": author,
                "parentCommentId": parent_comment_id,
                "engagement": engagement,
                "classification": classification,
                "mentionId": mention_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mention_comment_author_type_0 import (
            MentionCommentAuthorType0,
        )
        from ..models.mention_comment_classification_type_0 import (
            MentionCommentClassificationType0,
        )
        from ..models.mention_comment_engagement_type_0 import (
            MentionCommentEngagementType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        text = d.pop("text")

        published_at = d.pop("publishedAt")

        def _parse_author(data: object) -> MentionCommentAuthorType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = MentionCommentAuthorType0.from_dict(data)

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionCommentAuthorType0 | None, data)

        author = _parse_author(d.pop("author"))

        def _parse_parent_comment_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_comment_id = _parse_parent_comment_id(d.pop("parentCommentId"))

        def _parse_engagement(data: object) -> MentionCommentEngagementType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                engagement_type_0 = MentionCommentEngagementType0.from_dict(data)

                return engagement_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionCommentEngagementType0 | None, data)

        engagement = _parse_engagement(d.pop("engagement"))

        def _parse_classification(
            data: object,
        ) -> MentionCommentClassificationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                classification_type_0 = MentionCommentClassificationType0.from_dict(
                    data
                )

                return classification_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionCommentClassificationType0 | None, data)

        classification = _parse_classification(d.pop("classification"))

        def _parse_mention_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mention_id = _parse_mention_id(d.pop("mentionId"))

        mention_comment = cls(
            id=id,
            url=url,
            text=text,
            published_at=published_at,
            author=author,
            parent_comment_id=parent_comment_id,
            engagement=engagement,
            classification=classification,
            mention_id=mention_id,
        )

        mention_comment.additional_properties = d
        return mention_comment

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
