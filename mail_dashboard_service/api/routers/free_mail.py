from fastapi import APIRouter, Depends

from mail_dashboard_service.core.models.free_email import ActivateEmailCommand, CreateEmailCommand, DeactivateEmailCommand, DeleteEmailCommand, GetEmailCommand, GetEmailsCommand, GetMoreTimeCommand, GetTimeRemainCommand

from . import get_account_id

from mail_dashboard_service.api.dto.free_mail import (
    CreateFreeEmailDTO,
    GetTimeExpiredDTO,
    GetMoreTimeDTO,
    GetEmails,
    GetEmail,
    DeleteEmailDTO,
    ActivateEmailDTO,
    DeactivateEmailDTO
)
from mail_dashboard_service.core.ports.inbound.free_email import FreeMailUseCase
from mail_dashboard_service.api.dependencies.free_mail import (
    create_free_email_service,
    get_time_remaining_service,
    get_more_time_service,
    delete_email_service,
    get_emails_service,
    get_email_service,
    activate_email_service,
    deactivate_email_service
)

router = APIRouter()


@router.post("/create",)
def create_free_email(
    payload: CreateFreeEmailDTO,
    service: FreeMailUseCase = Depends(create_free_email_service)
):
    command = CreateEmailCommand(
        account_id=get_account_id(payload.token)
    )
    result = service.create_free_email(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 201
    return result


@router.get("/remaining",)
def get_time_expired(
    payload: GetTimeExpiredDTO = Depends(GetTimeExpiredDTO),
    service: FreeMailUseCase = Depends(get_time_remaining_service)
):
    command = GetTimeRemainCommand(
        account_id=get_account_id(payload.token),
        email=payload.email
    )
    result = service.get_time_remaining(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result


@router.post("/more",)
def refill(
    payload: GetMoreTimeDTO,
    service: FreeMailUseCase = Depends(get_more_time_service)
):
    command = GetMoreTimeCommand(
        account_id=get_account_id(payload.token),
        email=payload.email
    )
    result = service.get_more_time(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result


@router.delete("/delete",)
def delete_email(
    payload: DeleteEmailDTO,
    service: FreeMailUseCase = Depends(delete_email_service)
):
    command = DeleteEmailCommand(
        account_id=get_account_id(payload.token),
        email=payload.email
    )
    result = service.delete_email(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result


@router.get("/emails")
def get_emails(
    payload: GetEmails = Depends(GetEmails),
    service: FreeMailUseCase = Depends(get_emails_service)
):
    command = GetEmailsCommand(
        account_id=get_account_id(payload.token)
    )
    result = service.get_emails(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result


@router.get("/email")
def get_email(
    payload: GetEmail = Depends(GetEmail),
    service: FreeMailUseCase = Depends(get_email_service)
):
    command = GetEmailCommand(
        account_id=get_account_id(payload.token),
        email=payload.email
    )
    result = service.get_email(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result


@router.post("/activate")
def activate_email(
    payload: ActivateEmailDTO,
    service: FreeMailUseCase = Depends(activate_email_service)
):
    command = ActivateEmailCommand(
        account_id=get_account_id(payload.token),
        email=payload.email
    )
    result = service.activate_email(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result


@router.post("/deactivate")
def deactivate_email(
    payload: DeactivateEmailDTO,
    service: FreeMailUseCase = Depends(deactivate_email_service)
):
    command = DeactivateEmailCommand(
        account_id=get_account_id(payload.token),
        email=payload.email
    )
    result = service.deactivate_email(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result
