from typing import Protocol
from mail_dashboard_service.core.models.free_email import (
    CreateEmailCommand,
    CreateEmailResponse,
    GetTimeRemainCommand,
    GetTimeRemainResponse,
    GetMoreTimeCommand,
    GetMoreTimeResponse,
    DeleteEmailCommand,
    DeleteEmailResponse,
    GetEmailsCommand,
    GetEmailsResponse
)


class FreeMailUseCase(Protocol):

    def create_free_email(self, command: CreateEmailCommand) -> CreateEmailResponse:
        ...

    def get_time_remaining(self, command: GetTimeRemainCommand) -> GetTimeRemainResponse:
        ...

    def get_more_time(self, command: GetMoreTimeCommand) -> GetMoreTimeResponse:
        ...

    def delete_email(self, command: DeleteEmailCommand) -> DeleteEmailResponse:
        ...

    def get_emails(self, command: GetEmailsCommand) -> GetEmailsResponse:
        ...
