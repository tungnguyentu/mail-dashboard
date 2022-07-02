from fastapi import APIRouter, Depends

from mail_dashboard_service.api.dto.free_mail import (
    CreateFreeEmailDTO,
    GetTimeExpiredDTO,
    GetMoreTimeDTO,
    GetEmails,
    DeleteEmailDTO
)
from mail_dashboard_service.core.ports.inbound.free_email import FreeMailUseCase
from mail_dashboard_service.api.dependencies.free_mail import (
    create_free_email_service,
    get_time_remaining_service,
    get_more_time_service,
    delete_email_service,
    get_emails_service
)

router = APIRouter()

@router.get("/create",)
def create_free_email(
    payload: CreateFreeEmailDTO,
    service: FreeMailUseCase = Depends(create_free_email_service)
):
    return service.create_free_email(payload)


@router.get("/remaining",)
def get_time_expired(
    payload: GetTimeExpiredDTO,
    service: FreeMailUseCase = Depends(get_time_remaining_service)
):
    return service.get_time_remaining(payload)


@router.get("/more",)
def get_more_time(
    payload: GetMoreTimeDTO,
    service: FreeMailUseCase = Depends(get_more_time_service)
):
    return service.get_more_time(payload)


@router.delete("/delete",)
def delete_email(
    payload: DeleteEmailDTO,
    service: FreeMailUseCase = Depends(delete_email_service)
):
    return service.delete_email(payload)


@router.get("/emails")
def get_emails(
    payload: GetEmails,
    service: FreeMailUseCase = Depends(get_emails_service)
):
    return service.get_emails(payload)
