from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.usage_breakdown_data_item_group_type_0 import (
        UsageBreakdownDataItemGroupType0,
    )
    from ..models.usage_breakdown_data_item_keyword_type_0 import (
        UsageBreakdownDataItemKeywordType0,
    )
    from ..models.usage_breakdown_data_item_workspace_type_0 import (
        UsageBreakdownDataItemWorkspaceType0,
    )


T = TypeVar("T", bound="UsageBreakdownDataItem")


@_attrs_define
class UsageBreakdownDataItem:
    """
    Attributes:
        key (str): The row's key: the UTC day (YYYY-MM-DD) for by=day, the platform for by=platform, the keyword id for
            by=keyword, the group id for by=group, the workspace id for by=workspace.
        label (str): Readable name: the keyword term or the group name, otherwise the key.
        keyword (None | UsageBreakdownDataItemKeywordType0): by=keyword only; null otherwise.
        group (None | UsageBreakdownDataItemGroupType0): by=group only; null otherwise.
        workspace (None | UsageBreakdownDataItemWorkspaceType0): by=workspace only; null otherwise.
        keyword_days (int | None): Keyword-days the daily tick charged in this row. Null for by=platform and for days
            before the first recorded tick (unknown, not zero); before window.keywordDaysFrom a keyword row is a floor.
        keyword_cents (int): The keyword-days at the keyword rate ($5 a month, 500/30 cents a day), rounded once on the
            total.
        matched_mentions (int): Matches recorded in the window, relevant or not.
        billable_mentions (int): Of the matches billed in the window (every scored match, relevant or not), the ones in
            this group.
        unclassified_mentions (int): Matches in the window that are never charged: not scored yet, classification
            failed, or a free review from a new app's look-back. Every other match is charged, on the mentions or comments
            line.
        mention_cents (int): The billed mentions at $0.008 each, rounded once on the total.
        billable_comments (int): Comments billed in the window (the comments line): comments delivered under your
            mentions and comments that matched a keyword, each once per workspace.
        comment_cents (int): The billed comments at $0.008 each, rounded once on the total.
        total_cents (int): keywordCents plus mentionCents plus commentCents.
        account_days (int): Tracked-account days metered: the days the daily tick charged an account for. 0 on
            by=keyword rows (an account is not a keyword).
        account_cents (int): The account-days at the account rate ($2 a month, 200/30 cents a day), rounded once on the
            total.
        billable_followers (int): New followers of tracked accounts billed in the window, under the platform and group
            the account had when they were billed (a moved or deleted account keeps them there).
        follower_cents (int): The new followers at $0.008 each, rounded once on the total.
    """

    key: str
    label: str
    keyword: None | UsageBreakdownDataItemKeywordType0
    group: None | UsageBreakdownDataItemGroupType0
    workspace: None | UsageBreakdownDataItemWorkspaceType0
    keyword_days: int | None
    keyword_cents: int
    matched_mentions: int
    billable_mentions: int
    unclassified_mentions: int
    mention_cents: int
    billable_comments: int
    comment_cents: int
    total_cents: int
    account_days: int
    account_cents: int
    billable_followers: int
    follower_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.usage_breakdown_data_item_group_type_0 import (
            UsageBreakdownDataItemGroupType0,
        )
        from ..models.usage_breakdown_data_item_keyword_type_0 import (
            UsageBreakdownDataItemKeywordType0,
        )
        from ..models.usage_breakdown_data_item_workspace_type_0 import (
            UsageBreakdownDataItemWorkspaceType0,
        )

        key = self.key

        label = self.label

        keyword: dict[str, Any] | None
        if isinstance(self.keyword, UsageBreakdownDataItemKeywordType0):
            keyword = self.keyword.to_dict()
        else:
            keyword = self.keyword

        group: dict[str, Any] | None
        if isinstance(self.group, UsageBreakdownDataItemGroupType0):
            group = self.group.to_dict()
        else:
            group = self.group

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, UsageBreakdownDataItemWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        keyword_days: int | None
        keyword_days = self.keyword_days

        keyword_cents = self.keyword_cents

        matched_mentions = self.matched_mentions

        billable_mentions = self.billable_mentions

        unclassified_mentions = self.unclassified_mentions

        mention_cents = self.mention_cents

        billable_comments = self.billable_comments

        comment_cents = self.comment_cents

        total_cents = self.total_cents

        account_days = self.account_days

        account_cents = self.account_cents

        billable_followers = self.billable_followers

        follower_cents = self.follower_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "keyword": keyword,
                "group": group,
                "workspace": workspace,
                "keywordDays": keyword_days,
                "keywordCents": keyword_cents,
                "matchedMentions": matched_mentions,
                "billableMentions": billable_mentions,
                "unclassifiedMentions": unclassified_mentions,
                "mentionCents": mention_cents,
                "billableComments": billable_comments,
                "commentCents": comment_cents,
                "totalCents": total_cents,
                "accountDays": account_days,
                "accountCents": account_cents,
                "billableFollowers": billable_followers,
                "followerCents": follower_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_breakdown_data_item_group_type_0 import (
            UsageBreakdownDataItemGroupType0,
        )
        from ..models.usage_breakdown_data_item_keyword_type_0 import (
            UsageBreakdownDataItemKeywordType0,
        )
        from ..models.usage_breakdown_data_item_workspace_type_0 import (
            UsageBreakdownDataItemWorkspaceType0,
        )

        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        def _parse_keyword(data: object) -> None | UsageBreakdownDataItemKeywordType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keyword_type_0 = UsageBreakdownDataItemKeywordType0.from_dict(data)

                return keyword_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UsageBreakdownDataItemKeywordType0, data)

        keyword = _parse_keyword(d.pop("keyword"))

        def _parse_group(data: object) -> None | UsageBreakdownDataItemGroupType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_0 = UsageBreakdownDataItemGroupType0.from_dict(data)

                return group_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UsageBreakdownDataItemGroupType0, data)

        group = _parse_group(d.pop("group"))

        def _parse_workspace(
            data: object,
        ) -> None | UsageBreakdownDataItemWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = UsageBreakdownDataItemWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UsageBreakdownDataItemWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        def _parse_keyword_days(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        keyword_days = _parse_keyword_days(d.pop("keywordDays"))

        keyword_cents = d.pop("keywordCents")

        matched_mentions = d.pop("matchedMentions")

        billable_mentions = d.pop("billableMentions")

        unclassified_mentions = d.pop("unclassifiedMentions")

        mention_cents = d.pop("mentionCents")

        billable_comments = d.pop("billableComments")

        comment_cents = d.pop("commentCents")

        total_cents = d.pop("totalCents")

        account_days = d.pop("accountDays")

        account_cents = d.pop("accountCents")

        billable_followers = d.pop("billableFollowers")

        follower_cents = d.pop("followerCents")

        usage_breakdown_data_item = cls(
            key=key,
            label=label,
            keyword=keyword,
            group=group,
            workspace=workspace,
            keyword_days=keyword_days,
            keyword_cents=keyword_cents,
            matched_mentions=matched_mentions,
            billable_mentions=billable_mentions,
            unclassified_mentions=unclassified_mentions,
            mention_cents=mention_cents,
            billable_comments=billable_comments,
            comment_cents=comment_cents,
            total_cents=total_cents,
            account_days=account_days,
            account_cents=account_cents,
            billable_followers=billable_followers,
            follower_cents=follower_cents,
        )

        usage_breakdown_data_item.additional_properties = d
        return usage_breakdown_data_item

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
