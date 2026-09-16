from enum import StrEnum


class UpdateSegmentBodyFilterStagesItem(StrEnum):
    CONTACTED = "contacted"
    CUSTOMER = "customer"
    IN_TALKS = "in_talks"
    NOT_A_FIT = "not_a_fit"
    NOT_CONTACTED = "not_contacted"
    REPLIED = "replied"

    def __str__(self) -> str:
        return str(self.value)
