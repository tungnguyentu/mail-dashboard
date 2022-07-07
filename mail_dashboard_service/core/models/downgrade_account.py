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

    