from enum import StrEnum


class ListApiKeysResponse200DataItemScope(StrEnum):
    READ = "read"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
