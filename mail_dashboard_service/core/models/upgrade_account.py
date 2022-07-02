from typing import Optional
from pydantic import BaseModel


class UpgradeAccountCommand(BaseModel):
    token: str
    plan_id: str
    plan_name: str
    months: int


class UpgradeAccountPayload(BaseModel):
    account_id: str
    plan_name: str


class UpgradeAccountResponse(BaseModel):
    account_id: Optional[str] = None
    plan_name: Optional[str] = None
    amount: Optional[float] = None


class PayOrderPayload(BaseModel):
    order_id: str
    plan_id: str
    account_id: str
    months: int


class PayOrderResponse(BaseModel):
    order_id: Optional[str] = None
    account_id: Optional[str] = None
    plan_id: Optional[str] = None
    price_id: Optional[str] = None
    promotion_id: Optional[str] = None
    months: Optional[int] = None
    status: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None


class CreateQuotaPayload(BaseModel):
    account_id: str
    email_limit: int
    custom_email_limit: int
    alias_limit: int


class CreateQuotaResponse(BaseModel):
    account_id: Optional[str] = None
    email_limit: Optional[int] = None
    custom_email_limit: Optional[int] = None
    alias_limit: Optional[int] = None


class DisableSubscriptionPayload(BaseModel):
    order_id: str


class DisableSubscriptionResponse(BaseModel):
    sub_id: str
    bill_id: str


class RefundOrderPayload(BaseModel):
    order_id: str


class RefundOrderResponse(BaseModel):
    sub_id: Optional[str]
    bill_id: Optional[str]


class OrderPayload(BaseModel):
    account_id: str
    status: str


class OrderUpdateStatusPayload(BaseModel):
    order_id: str
    status: str


class OrderUpdateStatusResponse(BaseModel):
    updated: bool


class OrderResponse(BaseModel):
    order_id: str


class OrderUpdatePayload(BaseModel):
    plan_id: str
    price_id: str
    promotion_id: str
    months: int
    status: str
    start_time: str
    end_time: str


class OrderUpdateResponse(BaseModel):
    updated: bool
