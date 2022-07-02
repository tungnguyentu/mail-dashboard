from typing import Protocol
from mail_dashboard_service.core.models.upgrade_account import (
    PayOrderPayload,
    CreateQuotaPayload,
    DisableSubscriptionPayload,
    RefundOrderPayload,
    OrderPayload,
    OrderUpdatePayload,
    OrderUpdateResponse,
    OrderUpdateStatusResponse,
    OrderUpdateStatusPayload,
    CreateQuotaResponse,
    RefundOrderResponse,
    UpgradeAccountPayload,
    UpgradeAccountResponse,
    OrderResponse,
    PayOrderResponse,
    DisableSubscriptionResponse
)


class UpgradeAccountPort(Protocol):

    def get_account_id(self, token) -> str:
        ...

    def create_order(self, payload: OrderPayload) -> OrderResponse:
        ...

    def update_order_status(self, payload: OrderUpdateStatusPayload) -> OrderUpdateStatusResponse:
        ...

    def update_order(self, payload: OrderUpdatePayload) -> OrderUpdateResponse:
        ...

    def pay_order(self, payload: PayOrderPayload) -> PayOrderResponse:
        ...

    def get_quota_mapping(self, plan_name):
        ...

    def create_quota(self, payload: CreateQuotaPayload) -> CreateQuotaResponse:
        ...

    def refund_order(self, payload: RefundOrderPayload) -> RefundOrderResponse:
        ...

    def disable_subcription(self, payload: DisableSubscriptionPayload) -> DisableSubscriptionResponse:
        ...

    def upgrade_account(self, payload: UpgradeAccountPayload) -> UpgradeAccountResponse:
        ...
