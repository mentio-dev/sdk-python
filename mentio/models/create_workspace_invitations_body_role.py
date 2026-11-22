from enum import StrEnum


class CreateWorkspaceInvitationsBodyRole(StrEnum):
    ADMIN = "admin"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
