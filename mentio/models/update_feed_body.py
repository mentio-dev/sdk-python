from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_feed_body_auth_type_0 import UpdateFeedBodyAuthType0
    from ..models.update_feed_body_auth_type_1 import UpdateFeedBodyAuthType1


T = TypeVar("T", bound="UpdateFeedBody")


@_attrs_define
class UpdateFeedBody:
    """Omitted fields are untouched.

    Attributes:
        title (None | str | Unset): Your name for the feed; null clears it.
        auth (Any | Unset | UpdateFeedBodyAuthType0 | UpdateFeedBodyAuthType1): Replaces the sign-in (checked by reading
            the feed with it first); null removes it and the feed is read signed out again.
    """

    title: None | str | Unset = UNSET
    auth: Any | Unset | UpdateFeedBodyAuthType0 | UpdateFeedBodyAuthType1 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_feed_body_auth_type_0 import UpdateFeedBodyAuthType0
        from ..models.update_feed_body_auth_type_1 import UpdateFeedBodyAuthType1

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        auth: Any | dict[str, Any] | Unset
        if isinstance(self.auth, Unset):
            auth = UNSET
        elif isinstance(self.auth, UpdateFeedBodyAuthType0) or isinstance(
            self.auth, UpdateFeedBodyAuthType1
        ):
            auth = self.auth.to_dict()
        else:
            auth = self.auth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if auth is not UNSET:
            field_dict["auth"] = auth

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_feed_body_auth_type_0 import UpdateFeedBodyAuthType0
        from ..models.update_feed_body_auth_type_1 import UpdateFeedBodyAuthType1

        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_auth(
            data: object,
        ) -> Any | Unset | UpdateFeedBodyAuthType0 | UpdateFeedBodyAuthType1:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_type_0 = UpdateFeedBodyAuthType0.from_dict(data)

                return auth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_type_1 = UpdateFeedBodyAuthType1.from_dict(data)

                return auth_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                Any | Unset | UpdateFeedBodyAuthType0 | UpdateFeedBodyAuthType1, data
            )

        auth = _parse_auth(d.pop("auth", UNSET))

        update_feed_body = cls(
            title=title,
            auth=auth,
        )

        update_feed_body.additional_properties = d
        return update_feed_body

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
