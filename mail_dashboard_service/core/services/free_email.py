from mail_dashboard_service.core.ports.outbound import FreeEmailPort
from mail_dashboard_service.core.models.free_email import (
    ActivateEmailCommand,
    ActivateEmailPayload,
    ActivateEmailResponse,
    CreateEmailPayload,
    CreateEmailCommand,
    CreateEmailResponse,
    DeactivateEmaiResponse,
    DeactivateEmailCommand,
    DeactivateEmailPayload,
    GetEmailCommand,
    GetEmailPayload,
    GetEmailResponse,
    GetTimeRemainCommand,
    GetTimeRemainPayload,
    GetTimeRemainResponse,
    GetMoreTimeCommand,
    GetMoreTimePayload,
    GetMoreTimeResponse,
    DeleteEmailCommand,
    DeleteEmailPayload,
    DeleteEmailResponse,
    GetEmailsCommand,
    GetEmailsPayload,
    GetEmailsResponse
)


class FreeEmailService:

    def __init__(self, repo: FreeEmailPort) -> None:
        self.repo = repo

    def create_free_email(self, command: CreateEmailCommand) -> CreateEmailResponse:
        payload = CreateEmailPayload(
            account_id=command.account_id
        )
        response = self.repo.create(payload)
        return CreateEmailResponse(
            status=response.status,
            message=response.message,
            email=response.email,
            expire=response.expire
        )

    def get_time_remaining(self, command: GetTimeRemainCommand) -> GetTimeRemainResponse:
        payload = GetTimeRemainPayload(
            account_id=command.account_id,
            email=command.email
        )
        response = self.repo.get_remaining(payload)
        return GetTimeRemainResponse(
            message=response.message,
            remaining=response.remaining,
            status=response.status
        )

    def get_more_time(self, command: GetMoreTimeCommand) -> GetMoreTimeResponse:
        payload = GetMoreTimePayload(
            account_id=command.account_id,
            email=command.email
        )
        response = self.repo.refill(payload)
        return GetMoreTimeResponse(
            message=response.message,
            email=response.email,
            expire=response.expire
        )

    def delete_email(self, command: DeleteEmailCommand) -> DeleteEmailResponse:
        payload = DeleteEmailPayload(
            account_id=command.account_id,
            email=command.email
        )
        response = self.repo.delete(payload)
        return DeleteEmailResponse(
            message=response.message,
            account_id=response.account_id,
            email=response.email
        )

    def get_emails(self, command: GetEmailsCommand) -> GetEmailsResponse:
        payload = GetEmailsPayload(
            account_id=command.account_id
        )
        response = self.repo.get_emails(payload)
        return GetEmailsResponse(
            message=response.message,
            account_id=response.account_id,
            emails=response.emails
        )

    def get_email(self, command: GetEmailCommand) -> GetEmailResponse:
        payload = GetEmailPayload(
            account_id=command.account_id,
            email=command.email
        )
        response = self.repo.get_email(payload)
        return GetEmailResponse(
            status=response.status,
            message=response.message,
            email=response.email,
            expire=response.expire,
            active=response.active
        )

    def activate(self, command: ActivateEmailCommand) -> ActivateEmailResponse:
        payload = ActivateEmailPayload(
            account_id=command.account_id,
            email=command.email
        )
        result = self.repo.activate(payload)
        return ActivateEmailResponse(
            status=result.status,
            message=result.message,
            email=result.email,
            active=result.active
        )

    def deactivate(self, command: DeactivateEmailCommand) -> DeactivateEmaiResponse:
        payload = DeactivateEmailPayload(
            account_id=command.account_id,
            email=command.email
        )
        result = self.repo.activate(payload)
        return DeactivateEmaiResponse(
            status=result.status,
            message=result.message,
            email=result.email,
            active=result.active,
            account_id=result.account_id
        )
