from typing import Protocol
from mail_dashboard_service.core.models.upgrade_account import (
    PayOrderPayload,
    CreateQuotaPayload,
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
)


class UpgradeAccountPort(Protocol):

    def upgrade_account(self, payload: UpgradeAccountPayload) -> UpgradeAccountResponse:
        ...


class UpgradeAccountBillingPort(Protocol):

    def refund_order(self, payload: RefundOrderPayload) -> RefundOrderResponse:
        ...

    def pay_order(self, payload: PayOrderPayload) -> PayOrderResponse:
        ...


class UpgradeAccountMailCorePort(Protocol):

    def create_order(self, payload: OrderPayload) -> OrderResponse:
        ...

    def update_order_status(self, payload: OrderUpdateStatusPayload) -> OrderUpdateStatusResponse:
        ...

    def update_order(self, payload: OrderUpdatePayload) -> OrderUpdateResponse:
        ...

    def get_quota_mapping(self, plan_name):
        ...

    def create_quota(self, payload: CreateQuotaPayload) -> CreateQuotaResponse:
        ...
