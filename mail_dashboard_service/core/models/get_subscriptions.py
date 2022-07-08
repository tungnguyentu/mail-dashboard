from typing import List, Optional
from pydantic import BaseModel


class GetSubsciptionsQuery(BaseModel):
    account_id: str


class GetSubsPayload(BaseModel):
    account_id: str


class ServiceResponse(BaseModel):
    message: str
    status: str


class GetSubsciptionBase(BaseModel):
    created: Optional[str] = None
    deleted: bool = False
    updated: Optional[str] = None


class BillResponse(GetSubsciptionBase):
    _id: Optional[str] = None
    discount: Optional[int] = None
    bill_status: Optional[str] = None
    sub_total: Optional[int] = None
    subscription_id: Optional[str] = None
    total: Optional[int] = None


class GetSubsciptionResponse(GetSubsciptionBase):
    _id: Optional[str] = None
    account_id: Optional[str] = None
    bill: List[BillResponse]
    end_time: Optional[str] = None
    month: Optional[int] = None
    order_id: Optional[str] = None
    plan_id: Optional[str] = None
    price_id: Optional[str] = None
    promotion_id: Optional[str] = None
    start_time: Optional[str] = None
    sub_status: Optional[str] = None


class GetSubsciptionsResponse(ServiceResponse):
    subscriptions: List[GetSubsciptionResponse]
    total: Optional[int] = None
