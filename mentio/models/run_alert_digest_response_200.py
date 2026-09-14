from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.run_alert_digest_response_200_skipped import (
    RunAlertDigestResponse200Skipped,
)

if TYPE_CHECKING:
    from ..models.run_alert_digest_response_200_outcomes_item import (
        RunAlertDigestResponse200OutcomesItem,
    )


T = TypeVar("T", bound="RunAlertDigestResponse200")


@_attrs_define
class RunAlertDigestResponse200:
    """
    Attributes:
        skipped (RunAlertDigestResponse200Skipped): Why nothing was sent, if nothing was.
        matched (int):
        relevant (int):
        outcomes (list[RunAlertDigestResponse200OutcomesItem]):
    """

    skipped: RunAlertDigestResponse200Skipped
    matched: int
    relevant: int
    outcomes: list[RunAlertDigestResponse200OutcomesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skipped = self.skipped.value

        matched = self.matched

        relevant = self.relevant

        outcomes = []
        for outcomes_item_data in self.outcomes:
            outcomes_item = outcomes_item_data.to_dict()
            outcomes.append(outcomes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "skipped": skipped,
                "matched": matched,
                "relevant": relevant,
                "outcomes": outcomes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.run_alert_digest_response_200_outcomes_item import (
            RunAlertDigestResponse200OutcomesItem,
        )

        d = dict(src_dict)
        skipped = RunAlertDigestResponse200Skipped(d.pop("skipped"))

        matched = d.pop("matched")

        relevant = d.pop("relevant")

        outcomes = []
        _outcomes = d.pop("outcomes")
        for outcomes_item_data in _outcomes:
            outcomes_item = RunAlertDigestResponse200OutcomesItem.from_dict(
                outcomes_item_data
            )

            outcomes.append(outcomes_item)

        run_alert_digest_response_200 = cls(
            skipped=skipped,
            matched=matched,
            relevant=relevant,
            outcomes=outcomes,
        )

        run_alert_digest_response_200.additional_properties = d
        return run_alert_digest_response_200

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
