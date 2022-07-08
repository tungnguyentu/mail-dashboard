from typing import Optional
from pydantic import BaseModel


class ServiceResponse(BaseModel):
    status: int
    message: str


class DowngradeAccountCommand(BaseModel):
    account_id: str


class DowngradeAccountPayload(BaseModel):
    account_id: str


class DowngradeAccountResponse(ServiceResponse):
    account_id: Optional[str] = None
    plan_name: Optional[str] = None
    amount: Optional[int] = None


class UpdateAccountQuotaPayload(BaseModel):
    account_id: str
    email_limit: Optional[int] = None
    custom_email_limit: Optional[int] = None
    alias_limit: Optional[int] = None


class ClearEmailsResponse(ServiceResponse):
    account_id: str


class UpdateAccountQuotaResponse(ServiceResponse):
    account_id: Optional[str] = None
    email_limit: Optional[int] = None
    custom_email_limit: Optional[int] = None
    alias_limit: Optional[int] = None


class DowngradeAccountNotificationResponse(ServiceResponse):
    ...