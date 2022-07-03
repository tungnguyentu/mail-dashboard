import requests
from mail_dashboard_service.core.models.upgrade_account import (
    PayOrderPayload,
    RefundOrderPayload,
    RefundOrderResponse,
    PayOrderResponse,
)


class UpgradeAccountBillingAdapter:

    def __init__(self, settings):
        self.settings = settings

    def refund_order(self, payload: RefundOrderPayload) -> RefundOrderResponse:
        response = requests.post(
            self.settings.api.billing.refund_order,
            data={
                "order_id": payload.order_id
            }
        )
        if not response.ok:
            return RefundOrderResponse()
        data = response.json()
        return RefundOrderResponse(
            sub_id=data.get("sub_id"),
            bill_id=data.get("bill_id"),
        )

    def pay_order(self, payload: PayOrderPayload) -> PayOrderResponse:
        response = requests.post(
            self.settings.api.billing.pay_order,
            data={
                "order_id": payload.order_id,
                "plan_id": payload.plan_id,
                "account_id": payload.account_id,
                "months": payload.months
            }
        )
        if not response.ok or response.status_code != 200:
            return PayOrderResponse()
        data = response.json()
        return PayOrderResponse(
            ok=response.ok,
            order_id=data.get("order_id"),
            account_id=data.get("account_id"),
            plan_id=data.get("plan_id"),
            price_id=data.get("price_id"),
            promotion_id=data.get("promotion_id"),
            months=data.get("months"),
            status=data.get("status"),
            start_time=data.get("start_time"),
            end_time=data.get("end_time"),
        )
