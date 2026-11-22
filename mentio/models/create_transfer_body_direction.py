from enum import StrEnum


class CreateTransferBodyDirection(StrEnum):
    TO_PARENT = "to_parent"
    TO_WORKSPACE = "to_workspace"

    def __str__(self) -> str:
        return str(self.value)
