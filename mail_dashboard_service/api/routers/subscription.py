from fastapi import APIRouter, Depends, Header
from typing import Union, List

from . import get_account_id

from mail_dashboard_service.api.dto.subscription import GetSubscriptionsDTO
from mail_dashboard_service.core.ports.inbound.upgrade_account import SubscriptionUseCase
from mail_dashboard_service.api.dependencies.subscription import get_subscriptions_service
from mail_dashboard_service.core.models.get_subscriptions import (
    GetSubsciptionsQuery,
    GetSubsciptionsResponse
)


router = APIRouter()


@router.get("/billings/subscriptions",
    response_model=GetSubsciptionsResponse,
    response_model_exclude_unset=True
)
def get_subscriptions(
    account_id: str,
    service: SubscriptionUseCase = Depends(get_subscriptions_service),
    x_token: Union[str, None] = Header(default=None)
):
    account = get_account_id(x_token)
    if not account.get("account_id"):
        return GetSubsciptionsResponse(message="Invalid token", status=404)
    if account_id != account.get("account_id"):
        return GetSubsciptionsResponse(message="Invalid account id", status=404)
    query = GetSubsciptionsQuery(
        account_id=account.get("account_id"),
    )
    result = service.get_subs(query)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result
