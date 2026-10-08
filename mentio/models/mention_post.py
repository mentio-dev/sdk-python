from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mention_post_kind import MentionPostKind
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
            news, linkedin, tiktok, instagram, appstore (App Store reviews), googleplay (Google Play reviews), trustpilot
            (Trustpilot reviews), googlemaps (Google reviews of a place), rss (RSS and Atom feeds a keyword reads).
        kind (MentionPostKind): post: a top-level post. comment: an item that answers a post or another comment (a
            Reddit or Hacker News comment, an X or Bluesky reply, a Stack Overflow answer, a YouTube comment).
        url (str): Permalink of the post.
        text (str): Title and body, truncated to 8 KB at ingest.
        title (None | str): The post's own title where the platform has one: a Hacker News story, a Reddit thread, a
            GitHub issue or pull request, a Stack Overflow question, a DEV article, a YouTube video, a news article, a
            titled review. Null for platforms without titles (X, Bluesky, LinkedIn) and for posts ingested before October
            2026.
        image_url (None | str): A preview image of the post, when the platform sent one with it: a YouTube thumbnail, a
            DEV cover, a news article's sharing image, a Bluesky link card or image. Null otherwise.
        subreddit (None | str): The subreddit a Reddit post was written in, without the r/ (SaaS). Null on every other
            platform.
        flair (None | str): A Reddit post's flair, when its subreddit uses them (Question, Show and Tell). Null
            otherwise.
        links (list[str]): Links the post carries, in the order written, at most 20. Empty for a post with none, and for
            posts ingested before September 2026.
        published_at (str): When the post was published.
        engagement (MentionPostEngagementType0 | None): Engagement counts as the platform reported them when the post
            was ingested, usually minutes after it was written; a count the platform does not have is null. Null as a whole
            for platforms that report none and for posts ingested before September 2026. X carries all six.
        reply_to (MentionPostReplyToType0 | None): The post or comment this one answers; null for top-level posts.
    """

    platform: MentionPostPlatform
    kind: MentionPostKind
    url: str
    text: str
    title: None | str
    image_url: None | str
    subreddit: None | str
    flair: None | str
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

        kind = self.kind.value

        url = self.url

        text = self.text

        title: None | str
        title = self.title

        image_url: None | str
        image_url = self.image_url

        subreddit: None | str
        subreddit = self.subreddit

        flair: None | str
        flair = self.flair

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
                "kind": kind,
                "url": url,
                "text": text,
                "title": title,
                "imageUrl": image_url,
                "subreddit": subreddit,
                "flair": flair,
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

        kind = MentionPostKind(d.pop("kind"))

        url = d.pop("url")

        text = d.pop("text")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("imageUrl"))

        def _parse_subreddit(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subreddit = _parse_subreddit(d.pop("subreddit"))

        def _parse_flair(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        flair = _parse_flair(d.pop("flair"))

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
            kind=kind,
            url=url,
            text=text,
            title=title,
            image_url=image_url,
            subreddit=subreddit,
            flair=flair,
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
