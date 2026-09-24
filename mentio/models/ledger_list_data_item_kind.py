from enum import StrEnum


class LedgerListDataItemKind(StrEnum):
    ADJUSTMENT = "adjustment"
    DEBIT_KEYWORD_DAYS = "debit_keyword_days"
    DEBIT_MENTIONS = "debit_mentions"
    REFUND = "refund"
    SIGNUP_CREDIT = "signup_credit"
    TOPUP = "topup"

    def __str__(self) -> str:
        return str(self.value)
