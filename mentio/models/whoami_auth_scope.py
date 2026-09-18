from enum import StrEnum


class WhoamiAuthScope(StrEnum):
    READ = "read"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
