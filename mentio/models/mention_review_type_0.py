from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mention_review_type_0_app import MentionReviewType0App


T = TypeVar("T", bound="MentionReviewType0")


@_attrs_define
class MentionReviewType0:
    """An app store review's facts; null for every other post. Its sentiment comes from the stars (4 and 5 positive, 3
    neutral, 1 and 2 negative) and it always counts as relevant, since you chose the app.

        Attributes:
            rating (int): Stars the reviewer gave.
            rating_max (int): The top of the scale: 5 on both stores.
            title (None | str): The review's headline; null where the store has none (Google Play).
            version (None | str): The app version the reviewer ran, when the store says.
            country (None | str): The storefront it was read in, a lowercase two-letter code.
            response (None | str): The developer's reply as it stood when the review was collected; null for none.
            response_at (None | str): When the developer replied.
            app (MentionReviewType0App): The app reviewed.
    """

    rating: int
    rating_max: int
    title: None | str
    version: None | str
    country: None | str
    response: None | str
    response_at: None | str
    app: MentionReviewType0App
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rating = self.rating

        rating_max = self.rating_max

        title: None | str
        title = self.title

        version: None | str
        version = self.version

        country: None | str
        country = self.country

        response: None | str
        response = self.response

        response_at: None | str
        response_at = self.response_at

        app = self.app.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rating": rating,
                "ratingMax": rating_max,
                "title": title,
                "version": version,
                "country": country,
                "response": response,
                "responseAt": response_at,
                "app": app,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mention_review_type_0_app import (
            MentionReviewType0App,
        )

        d = dict(src_dict)
        rating = d.pop("rating")

        rating_max = d.pop("ratingMax")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_response(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        response = _parse_response(d.pop("response"))

        def _parse_response_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        response_at = _parse_response_at(d.pop("responseAt"))

        app = MentionReviewType0App.from_dict(d.pop("app"))

        mention_review_type_0 = cls(
            rating=rating,
            rating_max=rating_max,
            title=title,
            version=version,
            country=country,
            response=response,
            response_at=response_at,
            app=app,
        )

        mention_review_type_0.additional_properties = d
        return mention_review_type_0

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
