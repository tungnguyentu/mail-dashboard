from mail_dashboard_service.core.ports.outbound.upgrade_account import UpgradeAccountPort
from mail_dashboard_service.core.models.upgrade_account import (
    UpgradeAccountCommand,
    UpgradeAccountPayload,
    UpgradeAccountResponse,
    PayOrderPayload,
    CreateQuotaPayload,
    DisableSubscriptionPayload,
    RefundOrderPayload,
    OrderPayload
)


class UpgradeAccountService:

    def __init__(self, repo: UpgradeAccountPort) -> None:
        self.repo = repo
    
    def upgrade(self, command: UpgradeAccountCommand) -> UpgradeAccountResponse:
        account_id = self.repo.get_account_id(command.token)
        order_payload = OrderPayload(
            status="OPEN"
        )
        order = self.repo.create_order(order_payload)
        pay_order_payload = PayOrderPayload(
            order_id=order.id,
            plan_id=command.plan_id,
            account_id=account_id,
            months=command.months
        )
        order_result = self.repo.pay_order(pay_order_payload)
        if not order_result.ok:
            return
        order_payload.status = "PAID"
        self.repo.update_order(order_payload)
        quota = self.repo.get_quota_mapping(command.plan_name)
        quota_payload = CreateQuotaPayload(
            account_id=account_id,
            email_limit=quota.email_limit,
            custom_email_limit=quota.custom_email_limit,
            alias_limit=quota.alias_limit
        )
        quota_result = self.repo.create_quota(quota_payload)
        if not quota_result.ok:
            order_payload.status = "FAILED"
            self.repo.update_order(order_payload)
            refund_order_payload = RefundOrderPayload(
                order_id=order.id
            )
            self.repo.refund_order(refund_order_payload)
            disable_subscription_payload = DisableSubscriptionPayload(
                order_id=order.id
            )
            self.repo.disable_subscription(disable_subscription_payload)
            order_payload.status = "REFUNED"
            self.repo.update_order(order_payload)

        upgrade_account_payload = UpgradeAccountPayload(
            account_id=account_id,
            plan_name=command.plan_name
        )
        self.repo.upgrade_account(upgrade_account_payload)
        order_payload.status = "SUCCESS"
        self.repo.update_order(order_payload)