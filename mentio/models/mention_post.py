from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_post_platform import MentionPostPlatform

if TYPE_CHECKING:
    from ..models.mention_post_engagement_type_0 import MentionPostEngagementType0
    from ..models.mention_post_reply_to_type_0 import MentionPostReplyToType0


T = TypeVar("T", bound="MentionPost")


@_attrs_define
class MentionPost:
    """
    Attributes:
        platform (MentionPostPlatform): Platform: bluesky, hackernews, github, stackoverflow, devto, reddit, x, youtube,
            news, linkedin.
        url (str): Permalink of the post.
        text (str): Title and body, truncated to 8 KB at ingest.
        links (list[str]): Links the post carries, in the order written, at most 20. Empty for a post with none, and for
            posts ingested before September 2026.
        published_at (str): When the post was published.
        engagement (MentionPostEngagementType0 | None): Engagement counts as the platform reported them when the post
            was ingested, usually minutes after it was written; a count the platform does not have is null. Null as a whole
            for platforms that report none and for posts ingested before September 2026. X carries all six.
        reply_to (MentionPostReplyToType0 | None): The post this one replies to (X, Bluesky); null for top-level posts.
    """

    platform: MentionPostPlatform
    url: str
    text: str
    links: list[str]
    published_at: str
    engagement: MentionPostEngagementType0 | None
    reply_to: MentionPostReplyToType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mention_post_engagement_type_0 import (
            MentionPostEngagementType0,
        )
        from ..models.mention_post_reply_to_type_0 import (
            MentionPostReplyToType0,
        )

        platform = self.platform.value

        url = self.url

        text = self.text

        links = self.links

        published_at = self.published_at

        engagement: dict[str, Any] | None
        if isinstance(self.engagement, MentionPostEngagementType0):
            engagement = self.engagement.to_dict()
        else:
            engagement = self.engagement

        reply_to: dict[str, Any] | None
        if isinstance(self.reply_to, MentionPostReplyToType0):
            reply_to = self.reply_to.to_dict()
        else:
            reply_to = self.reply_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "url": url,
                "text": text,
                "links": links,
                "publishedAt": published_at,
                "engagement": engagement,
                "replyTo": reply_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mention_post_engagement_type_0 import (
            MentionPostEngagementType0,
        )
        from ..models.mention_post_reply_to_type_0 import (
            MentionPostReplyToType0,
        )

        d = dict(src_dict)
        platform = MentionPostPlatform(d.pop("platform"))

        url = d.pop("url")

        text = d.pop("text")

        links = cast(list[str], d.pop("links"))

        published_at = d.pop("publishedAt")

        def _parse_engagement(data: object) -> MentionPostEngagementType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                engagement_type_0 = MentionPostEngagementType0.from_dict(data)

                return engagement_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionPostEngagementType0 | None, data)

        engagement = _parse_engagement(d.pop("engagement"))

        def _parse_reply_to(data: object) -> MentionPostReplyToType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reply_to_type_0 = MentionPostReplyToType0.from_dict(data)

                return reply_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MentionPostReplyToType0 | None, data)

        reply_to = _parse_reply_to(d.pop("replyTo"))

        mention_post = cls(
            platform=platform,
            url=url,
            text=text,
            links=links,
            published_at=published_at,
            engagement=engagement,
            reply_to=reply_to,
        )

        mention_post.additional_properties = d
        return mention_post

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
