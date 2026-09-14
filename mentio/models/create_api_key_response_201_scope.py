from enum import StrEnum


class CreateApiKeyResponse201Scope(StrEnum):
    READ = "read"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
