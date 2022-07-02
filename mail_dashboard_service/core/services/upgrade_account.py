from mail_dashboard_service.core.ports.outbound.upgrade_account import UpgradeAccountPort
from mail_dashboard_service.core.models.upgrade_account import (
    OrderUpdatePayload,
    UpgradeAccountCommand,
    UpgradeAccountPayload,
    UpgradeAccountResponse,
    PayOrderPayload,
    CreateQuotaPayload,
    DisableSubscriptionPayload,
    RefundOrderPayload,
    OrderPayload,
    OrderUpdateStatusPayload
)


class UpgradeAccountService:

    def __init__(self, repo: UpgradeAccountPort) -> None:
        self.repo = repo

    def upgrade(self, command: UpgradeAccountCommand) -> UpgradeAccountResponse:
        account_id = self.repo.get_account_id(command.token)
        if not account_id:
            return UpgradeAccountResponse()
        order_payload = OrderPayload(
            account_id=account_id,
            status="OPEN"
        )
        order = self.repo.create_order(order_payload)
        pay_order_payload = PayOrderPayload(
            order_id=str(order.order_id),
            plan_id=command.plan_id,
            account_id=account_id,
            months=command.months
        )
        order_result = self.repo.pay_order(pay_order_payload)
        if not order_result.ok:
            return
        order_update_status_payload = OrderUpdateStatusPayload(
            order_id=order.order_id
        )
        order_update_status_payload.status = "PAID"
        self.repo.update_order_status(order_update_status_payload)
        quota = self.repo.get_quota_mapping(command.plan_name)

        quota_payload = CreateQuotaPayload(
            account_id=account_id,
            email_limit=quota.get("email_limit"),
            custom_email_limit=quota.get("custom_email_limit"),
            alias_limit=quota.get("alias_limit")
        )
        quota_result = self.repo.create_quota(quota_payload)
        if not quota_result.ok:
            order_update_status_payload.status = "FAILED"
            self.repo.update_order_status(order_update_status_payload)
            refund_order_payload = RefundOrderPayload(
                order_id=order.order_id
            )
            self.repo.refund_order(refund_order_payload)
            disable_subscription_payload = DisableSubscriptionPayload(
                order_id=order.order_id
            )
            self.repo.disable_subscription(disable_subscription_payload)
            order_update_status_payload.status = "REFUNED"
            self.repo.update_order_status(order_update_status_payload)

        upgrade_account_payload = UpgradeAccountPayload(
            account_id=account_id,
            plan_name=command.plan_name
        )
        upgrade_account_result = self.repo.upgrade_account(
            upgrade_account_payload)
        order_update_payload = OrderUpdatePayload(
            plan_id=order_result.plan_id,
            price_id=order_result.price_id,
            promotion_id=order_result.promotion_id,
            months=order_result.months,
            status="SUCCESS",
            start_time=order_result.start_time,
            end_time=order_result.end_time
        )
        self.repo.update_order(order_update_payload)
        return upgrade_account_result
