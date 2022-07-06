from typing import List
from pydantic import BaseModel


class GetSubsciptionsQuery(BaseModel):
    account_id: str


class GetSubsPayload(BaseModel):
    account_id: str


class ServiceResponse(BaseModel):
    message: str
    status: str


class GetSubsciptionBase(ServiceResponse):
    created: str
    deleted: bool
    updated: str


class BillResponse(GetSubsciptionBase):
    _id: str
    discount: int
    bill_status: str
    sub_total: int
    subscription_id: str
    total: int


class GetSubsciptionResponse(GetSubsciptionBase):
    _id: str
    account_id: str
    bill: List[BillResponse]
    end_time: str
    month: int
    order_id: str
    plan_id: str
    price_id: str
    promotion_id: str
    start_time: str
    sub_status: str


class GetSubsciptionsResponse(ServiceResponse):
    subscriptions: list
    total: int
