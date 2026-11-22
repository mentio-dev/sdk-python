from enum import StrEnum


class CreateWorkspaceInvitationsResponse201DataItemInvitationType0Role(StrEnum):
    ADMIN = "admin"
    MEMBER = "member"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
