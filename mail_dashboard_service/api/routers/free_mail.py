from fastapi import APIRouter, Depends, Header
from typing import Union

from pydantic import EmailStr

from mail_dashboard_service.core.models.free_email import ActivateEmailCommand, ActivateEmailResponse, CreateEmailCommand, CreateEmailResponse, DeactivateEmaiResponse, DeactivateEmailCommand, DeleteEmailCommand, DeleteEmailResponse, GetEmailCommand, GetEmailResponse, GetEmailsCommand, GetEmailsResponse, GetMoreTimeCommand, GetMoreTimeResponse, GetTimeRemainCommand, GetTimeRemainResponse

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


@router.post("/emails",
    response_model=CreateEmailResponse,
    response_model_exclude_unset=True
)
def create_free_email(
    service: FreeMailUseCase = Depends(create_free_email_service),
    x_token: Union[str, None] = Header(default=None)
):
    account = get_account_id(x_token)
    if not account.get("account_id"):
        return CreateEmailResponse(message="Invalid token", status=404)
    command = CreateEmailCommand(
        account_id=account.get("account_id")
    )
    result = service.create_free_email(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 201
    return result


@router.get("/emails/{email}/remaining",
    response_model=GetTimeRemainResponse,
    response_model_exclude_unset=True
)
def get_time_expired(
    email: EmailStr,
    service: FreeMailUseCase = Depends(get_time_remaining_service),
    x_token: Union[str, None] = Header(default=None)
):
    account = get_account_id(x_token)
    if not account.get("account_id"):
        return GetTimeRemainResponse(message="Invalid token", status=404)
    command = GetTimeRemainCommand(
        account_id=account.get("account_id"),
        email=email
    )
    result = service.get_time_remaining(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result


@router.post("/emails/refill",
    response_model=GetMoreTimeResponse,
    response_model_exclude_unset=True
)
def refill(
    payload: GetMoreTimeDTO,
    service: FreeMailUseCase = Depends(get_more_time_service),
    x_token: Union[str, None] = Header(default=None)
):
    account = get_account_id(x_token)
    if not account.get("account_id"):
        return GetMoreTimeResponse(message="Invalid token", status=404)
    command = GetMoreTimeCommand(
        account_id=account.get("account_id"),
        email=payload.email
    )
    result = service.get_more_time(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result


@router.delete("/emails",
    response_model=DeleteEmailResponse,
    response_model_exclude_unset=True
)
def delete_email(
    payload: DeleteEmailDTO,
    service: FreeMailUseCase = Depends(delete_email_service),
    x_token: Union[str, None] = Header(default=None)
):
    account = get_account_id(x_token)
    if not account.get("account_id"):
        return DeleteEmailResponse(message="Invalid token", status=404)
    command = DeleteEmailCommand(
        account_id=account.get("account_id"),
        email=payload.email
    )
    result = service.delete_email(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result


@router.get("/emails",
    response_model=GetEmailsResponse,
    response_model_exclude_unset=True
)
def get_emails(
    service: FreeMailUseCase = Depends(get_emails_service),
    x_token: Union[str, None] = Header(default=None)
):
    account = get_account_id(x_token)
    if not account.get("account_id"):
        return GetEmailsResponse(message="Invalid token", status=404)
    command = GetEmailsCommand(
        account_id=account.get("account_id")
    )
    result = service.get_emails(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result


@router.get("/emails/{email}",
    response_model=GetEmailResponse,
    response_model_exclude_unset=True
)
def get_email(
    email: EmailStr,
    service: FreeMailUseCase = Depends(get_email_service),
    x_token: Union[str, None] = Header(default=None)
):
    account = get_account_id(x_token)
    if not account.get("account_id"):
        return GetEmailResponse(message="Invalid token", status=404)
    command = GetEmailCommand(
        account_id=account.get("account_id"),
        email=email
    )
    result = service.get_email(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result


@router.post("/emails/activate",
    response_model=ActivateEmailResponse,
    response_model_exclude_unset=True
)
def activate_email(
    payload: ActivateEmailDTO,
    service: FreeMailUseCase = Depends(activate_email_service),
    x_token: Union[str, None] = Header(default=None)
):
    account = get_account_id(x_token)
    if not account.get("account_id"):
        return ActivateEmailResponse(message="Invalid token", status=404)
    command = ActivateEmailCommand(
        account_id=account.get("account_id"),
        email=payload.email
    )
    result = service.activate_email(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result


@router.post("/emails/deactivate",
    response_model=DeactivateEmaiResponse,
    response_model_exclude_unset=True
)
def deactivate_email(
    payload: DeactivateEmailDTO,
    service: FreeMailUseCase = Depends(deactivate_email_service),
    x_token: Union[str, None] = Header(default=None)
):
    account = get_account_id(x_token)
    if not account.get("account_id"):
        return DeactivateEmaiResponse(message="Invalid token", status=404)
    command = DeactivateEmailCommand(
        account_id=account.get("account_id"),
        email=payload.email
    )
    result = service.deactivate_email(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result
