from mail_dashboard_service.core.ports.outbound import FreeEmailPort
from mail_dashboard_service.core.models.free_email import (
    CreateEmailPayload,
    CreateEmailCommand,
    CreateEmailResponse,
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
        account_id = self.repo.get_account_id(command)
        if not account_id:
            return CreateEmailResponse(
                message="Account not found"
            )
        payload = CreateEmailPayload(
            account_id=account_id
        )
        response = self.repo.create(payload)
        return CreateEmailResponse(
            message=response.message,
            email=response.email,
            expire=response.expire
        )

    def get_time_remaining(self, command: GetTimeRemainCommand) -> GetTimeRemainResponse:
        account_id = self.repo.get_account_id(command)
        if not account_id:
            return GetTimeRemainResponse(
                account_id="Account not found"
            )
        payload = GetTimeRemainPayload(
            account_id=account_id,
            email=command.email
        )
        response = self.repo.get_remaining(payload)
        return GetTimeRemainResponse(
            message=response.message,
            remaining=response.remaining
        )

    def get_more_time(self, command: GetMoreTimeCommand) -> GetMoreTimeResponse:
        account_id = self.repo.get_account_id(command)
        if not account_id:
            return GetMoreTimeResponse(
                message="Account not found"
            )
        payload = GetMoreTimePayload(
            account_id=account_id,
            email=command.email
        )
        response = self.repo.refill(payload)
        return GetMoreTimeResponse(
            message=response.message,
            email=response.email,
            expire=response.expire
        )

    def delete_email(self, command: DeleteEmailCommand) -> DeleteEmailResponse:
        account_id = self.repo.get_account_id(command)
        if not account_id:
            return DeleteEmailResponse(
                message="Account not found"
            )
        payload = DeleteEmailPayload(
            account_id=account_id,
            email=command.email
        )
        response = self.repo.delete(payload)
        return DeleteEmailResponse(
            message=response.message,
            account_id=response.account_id,
            email=response.email
        )

    def get_emails(self, command: GetEmailsCommand) -> GetEmailsResponse:
        account_id = self.repo.get_account_id(command)
        if not account_id:
            return GetEmailsResponse(
                message="Account not found"
            )
        payload = GetEmailsPayload(
            account_id=account_id
        )
        response = self.repo.get_emails(payload)
        return GetEmailsResponse(
            message=response.message,
            account_id=response.account_id,
            emails=response.emails
        )
