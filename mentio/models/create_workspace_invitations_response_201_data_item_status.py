from enum import StrEnum


class CreateWorkspaceInvitationsResponse201DataItemStatus(StrEnum):
    ALREADY_INVITED = "already_invited"
    ALREADY_MEMBER = "already_member"
    INVITED = "invited"

    def __str__(self) -> str:
        return str(self.value)
