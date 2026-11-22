from enum import StrEnum


class LedgerListDataItemKind(StrEnum):
    ADJUSTMENT = "adjustment"
    DEBIT_COMMENTS = "debit_comments"
    DEBIT_ESTIMATES = "debit_estimates"
    DEBIT_KEYWORD_DAYS = "debit_keyword_days"
    DEBIT_MENTIONS = "debit_mentions"
    DEBIT_SEARCHES = "debit_searches"
    REFUND = "refund"
    SIGNUP_CREDIT = "signup_credit"
    TOPUP = "topup"
    TRANSFER_IN = "transfer_in"
    TRANSFER_OUT = "transfer_out"

    def __str__(self) -> str:
        return str(self.value)
