from typing import Protocol
from mail_dashboard_service.core.models.free_email import (
    ActivateEmailCommand,
    ActivateEmailResponse,
    CreateEmailCommand,
    CreateEmailResponse,
    DeactivateEmaiResponse,
    DeactivateEmailCommand,
    GetEmailCommand,
    GetEmailResponse,
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

    def get_email(self, command: GetEmailCommand) -> GetEmailResponse:
        ...

    def activate(self, command: ActivateEmailCommand) -> ActivateEmailResponse:
        ...

    def deactivate(self, command: DeactivateEmailCommand) -> DeactivateEmaiResponse:
        ...
