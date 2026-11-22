from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyword_estimate_terms_item_platforms_item_method import (
    KeywordEstimateTermsItemPlatformsItemMethod,
)
from ..models.keyword_estimate_terms_item_platforms_item_platform import (
    KeywordEstimateTermsItemPlatformsItemPlatform,
)
from ..models.keyword_estimate_terms_item_platforms_item_reason import (
    KeywordEstimateTermsItemPlatformsItemReason,
)
from ..models.keyword_estimate_terms_item_platforms_item_status import (
    KeywordEstimateTermsItemPlatformsItemStatus,
)

if TYPE_CHECKING:
    from ..models.keyword_estimate_terms_item_platforms_item_monthly_type_0 import (
        KeywordEstimateTermsItemPlatformsItemMonthlyType0,
    )
    from ..models.keyword_estimate_terms_item_platforms_item_sample_type_0 import (
        KeywordEstimateTermsItemPlatformsItemSampleType0,
    )


T = TypeVar("T", bound="KeywordEstimateTermsItemPlatformsItem")


@_attrs_define
class KeywordEstimateTermsItemPlatformsItem:
    """
    Attributes:
        platform (KeywordEstimateTermsItemPlatformsItemPlatform): Platform, one of:
            - Social: bluesky, x, reddit, linkedin, facebook, instagram, tiktok, threads, mastodon
            - Developer: hackernews, github, stackoverflow, devto
            - Media: news, youtube, podcasts (with transcripts), rss (keyword feeds)
            - Web: web (blogs), substack, producthunt
            - Reviews: appstore, googleplay, trustpilot, googlemaps (Google reviews)
        status (KeywordEstimateTermsItemPlatformsItemStatus): queued: not sampled yet. running: being sampled. done: it
            has a number. skipped: no number (see reason). failed: the sample failed (see reason).
        reason (KeywordEstimateTermsItemPlatformsItemReason): Why a platform has no number; null otherwise.

            - unsupported: no term search, and no index for the term.
            - paid: a paid platform, includePaid was false.
            - quota: youtube, its quota is kept for live tracking.
            - credentials, budget: not connected, or its monthly budget is spent.
            - rate_limited, error, timeout: the sample failed.
        method (KeywordEstimateTermsItemPlatformsItemMethod): index: counted from the posts Mentio already reads for
            this term (the closest to what a keyword gets). sample: one page of the platform's own search, extrapolated to a
            month. null without a number.
        monthly (KeywordEstimateTermsItemPlatformsItemMonthlyType0 | None): Expected matched mentions a month on this
            platform; null without a number.
        sample (KeywordEstimateTermsItemPlatformsItemSampleType0 | None): What the number rests on; null without a
            number.
        cost_cents (int): What sampling this platform cost: 0 for index numbers and free platforms.
    """

    platform: KeywordEstimateTermsItemPlatformsItemPlatform
    status: KeywordEstimateTermsItemPlatformsItemStatus
    reason: KeywordEstimateTermsItemPlatformsItemReason
    method: KeywordEstimateTermsItemPlatformsItemMethod
    monthly: KeywordEstimateTermsItemPlatformsItemMonthlyType0 | None
    sample: KeywordEstimateTermsItemPlatformsItemSampleType0 | None
    cost_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.keyword_estimate_terms_item_platforms_item_monthly_type_0 import (
            KeywordEstimateTermsItemPlatformsItemMonthlyType0,
        )
        from ..models.keyword_estimate_terms_item_platforms_item_sample_type_0 import (
            KeywordEstimateTermsItemPlatformsItemSampleType0,
        )

        platform = self.platform.value

        status = self.status.value

        reason = self.reason.value

        method = self.method.value

        monthly: dict[str, Any] | None
        if isinstance(self.monthly, KeywordEstimateTermsItemPlatformsItemMonthlyType0):
            monthly = self.monthly.to_dict()
        else:
            monthly = self.monthly

        sample: dict[str, Any] | None
        if isinstance(self.sample, KeywordEstimateTermsItemPlatformsItemSampleType0):
            sample = self.sample.to_dict()
        else:
            sample = self.sample

        cost_cents = self.cost_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "status": status,
                "reason": reason,
                "method": method,
                "monthly": monthly,
                "sample": sample,
                "costCents": cost_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.keyword_estimate_terms_item_platforms_item_monthly_type_0 import (
            KeywordEstimateTermsItemPlatformsItemMonthlyType0,
        )
        from ..models.keyword_estimate_terms_item_platforms_item_sample_type_0 import (
            KeywordEstimateTermsItemPlatformsItemSampleType0,
        )

        d = dict(src_dict)
        platform = KeywordEstimateTermsItemPlatformsItemPlatform(d.pop("platform"))

        status = KeywordEstimateTermsItemPlatformsItemStatus(d.pop("status"))

        reason = KeywordEstimateTermsItemPlatformsItemReason(d.pop("reason"))

        method = KeywordEstimateTermsItemPlatformsItemMethod(d.pop("method"))

        def _parse_monthly(
            data: object,
        ) -> KeywordEstimateTermsItemPlatformsItemMonthlyType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                monthly_type_0 = (
                    KeywordEstimateTermsItemPlatformsItemMonthlyType0.from_dict(data)
                )

                return monthly_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeywordEstimateTermsItemPlatformsItemMonthlyType0 | None, data)

        monthly = _parse_monthly(d.pop("monthly"))

        def _parse_sample(
            data: object,
        ) -> KeywordEstimateTermsItemPlatformsItemSampleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sample_type_0 = (
                    KeywordEstimateTermsItemPlatformsItemSampleType0.from_dict(data)
                )

                return sample_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeywordEstimateTermsItemPlatformsItemSampleType0 | None, data)

        sample = _parse_sample(d.pop("sample"))

        cost_cents = d.pop("costCents")

        keyword_estimate_terms_item_platforms_item = cls(
            platform=platform,
            status=status,
            reason=reason,
            method=method,
            monthly=monthly,
            sample=sample,
            cost_cents=cost_cents,
        )

        keyword_estimate_terms_item_platforms_item.additional_properties = d
        return keyword_estimate_terms_item_platforms_item

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
