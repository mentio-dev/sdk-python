from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_feed_body_auth_type_0 import CreateFeedBodyAuthType0
    from ..models.create_feed_body_auth_type_1 import CreateFeedBodyAuthType1


T = TypeVar("T", bound="CreateFeedBody")


@_attrs_define
class CreateFeedBody:
    """One feed to connect, with a sign-in when it is members-only.

    Attributes:
        url (str): A feed's address (https://forum.example.com/posts.rss), or a page's (https://forum.example.com): the
            feed the page advertises is used.
        auth (CreateFeedBodyAuthType0 | CreateFeedBodyAuthType1 | Unset): A sign-in for a members-only feed: a cookie,
            or one header. Write-only: stored encrypted, sent to the feed's own site alone, never shown again. A feed with a
            sign-in is read for this workspace alone.
    """

    url: str
    auth: CreateFeedBodyAuthType0 | CreateFeedBodyAuthType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_feed_body_auth_type_0 import CreateFeedBodyAuthType0

        url = self.url

        auth: dict[str, Any] | Unset
        if isinstance(self.auth, Unset):
            auth = UNSET
        elif isinstance(self.auth, CreateFeedBodyAuthType0):
            auth = self.auth.to_dict()
        else:
            auth = self.auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if auth is not UNSET:
            field_dict["auth"] = auth

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_feed_body_auth_type_0 import CreateFeedBodyAuthType0
        from ..models.create_feed_body_auth_type_1 import CreateFeedBodyAuthType1

        d = dict(src_dict)
        url = d.pop("url")

        def _parse_auth(
            data: object,
        ) -> CreateFeedBodyAuthType0 | CreateFeedBodyAuthType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_type_0 = CreateFeedBodyAuthType0.from_dict(data)

                return auth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            auth_type_1 = CreateFeedBodyAuthType1.from_dict(data)

            return auth_type_1

        auth = _parse_auth(d.pop("auth", UNSET))

        create_feed_body = cls(
            url=url,
            auth=auth,
        )

        create_feed_body.additional_properties = d
        return create_feed_body

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
