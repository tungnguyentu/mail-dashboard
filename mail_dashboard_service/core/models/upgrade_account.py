from typing import Optional
from pydantic import BaseModel


class ServiceResponse(BaseModel):
    status: int
    message: str


class UpgradeAccountCommand(BaseModel):
    account_id: str
    plan_id: str
    plan_name: str
    months: int


class UpgradeAccountPayload(BaseModel):
    account_id: str
    plan_name: str


class UpgradeAccountResponse(ServiceResponse):
    account_id: Optional[str] = None
    plan_name: Optional[str] = None
    amount: Optional[float] = None


class PayOrderPayload(BaseModel):
    order_id: str
    plan_id: str
    account_id: str
    months: int


class PayOrderResponse(ServiceResponse):
    order_id: Optional[str] = None
    account_id: Optional[str] = None
    plan_id: Optional[str] = None
    price_id: Optional[str] = None
    promotion_id: Optional[str] = None
    months: Optional[int] = None
    status: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None


class GetQuotaPayload(BaseModel):
    account_id: str


class CreateQuotaPayload(BaseModel):
    account_id: str
    email_limit: int
    custom_email_limit: int
    alias_limit: int


class UpdateQuotaPayload(BaseModel):
    account_id: str
    email_limit: int
    custom_email_limit: int
    alias_limit: int


class CreateQuotaResponse(ServiceResponse):
    account_id: Optional[str] = None
    email_limit: Optional[int] = None
    custom_email_limit: Optional[int] = None
    alias_limit: Optional[int] = None


class RefundOrderPayload(BaseModel):
    order_id: str


class RefundOrderResponse(ServiceResponse):
    sub_id: Optional[str]
    bill_id: Optional[str]


class OrderPayload(BaseModel):
    account_id: str
    status: str


class OrderUpdateStatusPayload(BaseModel):
    order_id: str
    status: str


class OrderUpdateStatusResponse(ServiceResponse):
    updated: bool


class OrderResponse(ServiceResponse):
    order_id: str


class OrderUpdatePayload(BaseModel):
    plan_id: str
    price_id: str
    promotion_id: str
    months: int
    status: str
    start_time: str
    end_time: str


class OrderUpdateResponse(ServiceResponse):
    updated: bool


class UpdateQuotaResponse(ServiceResponse):
    account_id: Optional[str] = None
    email_limit: Optional[int] = None
    custom_email_limit: Optional[int] = None
    alias_limit: Optional[int] = None


class GetQuotaResponse(ServiceResponse):
    account_id: Optional[str] = None
    email_limit: Optional[int] = None
    custom_email_limit: Optional[int] = None
    alias_limit: Optional[int] = None