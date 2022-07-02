from pydantic import UUID4, BaseModel


class UpgradeAccountCommand(BaseModel):
    token: str
    plan_id: str
    plan_name: str
    months: int

class UpgradeAccountPayload(BaseModel):
    account_id: str
    plan_name: str


class UpgradeAccountResponse(BaseModel):
    ...


class PayOrderPayload(BaseModel):
    order_id: UUID4
    plan_id: str
    account_id: str
    months: int


class CreateQuotaPayload(BaseModel):
    account_id: str
    email_limit: int
    custom_email_limit: int
    alias_limit: int

class DisableSubscriptionPayload(BaseModel):
    order_id: str


class RefundOrderPayload(BaseModel):
    order_id: str


class OrderPayload(BaseModel):
    status: str