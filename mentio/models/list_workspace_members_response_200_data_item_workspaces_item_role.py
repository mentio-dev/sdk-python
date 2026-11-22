from enum import StrEnum


class ListWorkspaceMembersResponse200DataItemWorkspacesItemRole(StrEnum):
    ADMIN = "admin"
    MEMBER = "member"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
