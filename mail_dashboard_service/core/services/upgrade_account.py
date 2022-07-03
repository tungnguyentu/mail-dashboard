from mail_dashboard_service.core.ports.outbound.upgrade_account import (
    UpgradeAccountBillingPort,
    UpgradeAccountMailCorePort,
    UpgradeAccountPort
)
from mail_dashboard_service.core.models.upgrade_account import (
    OrderUpdatePayload,
    UpgradeAccountCommand,
    UpgradeAccountPayload,
    UpgradeAccountResponse,
    PayOrderPayload,
    CreateQuotaPayload,
    RefundOrderPayload,
    OrderPayload,
    OrderUpdateStatusPayload
)


class UpgradeAccountService:

    def __init__(self,
                 mail_core: UpgradeAccountMailCorePort,
                 billing: UpgradeAccountBillingPort,
                 account: UpgradeAccountPort
                 ) -> None:
        self.mail_core = mail_core
        self.billing = billing
        self.account = account

    def upgrade(self, command: UpgradeAccountCommand) -> UpgradeAccountResponse:
        order_payload = OrderPayload(
            account_id=command.account_id,
            status="OPEN"
        )
        order = self.mail_core.create_order(order_payload)
        pay_order_payload = PayOrderPayload(
            order_id=str(order.order_id),
            plan_id=command.plan_id,
            account_id=command.account_id,
            months=command.months
        )
        order_result = self.billing.pay_order(pay_order_payload)
        if not order_result.ok:
            return UpgradeAccountResponse(
                status=0,
                message="Error while paying order, upgrade account failed"
            )
        order_update_status_payload = OrderUpdateStatusPayload(
            order_id=order.order_id
        )
        order_update_status_payload.status = "PAID"
        self.mail_core.update_order_status(order_update_status_payload)
        quota = self.mail.get_quota_mapping(command.plan_name)

        quota_payload = CreateQuotaPayload(
            account_id=command.account_id,
            email_limit=quota.get("email_limit"),
            custom_email_limit=quota.get("custom_email_limit"),
            alias_limit=quota.get("alias_limit")
        )
        quota_result = self.mail_core.create_quota(quota_payload)
        if not quota_result.ok:
            order_update_status_payload.status = "FAILED"
            self.mail_core.update_order_status(order_update_status_payload)
            refund_order_payload = RefundOrderPayload(
                order_id=order.order_id
            )
            self.billing.refund_order(refund_order_payload)
            order_update_status_payload.status = "REFUNED"
            self.mail_core.update_order_status(order_update_status_payload)
            return UpgradeAccountResponse(
                status=0,
                message="Upgrade Account Failed, Refunded Order"
            )

        upgrade_account_payload = UpgradeAccountPayload(
            account_id=command.account_id,
            plan_name=command.plan_name
        )
        upgrade_account_result = self.account.upgrade_account(
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
        self.mail_core.update_order(order_update_payload)
        return UpgradeAccountResponse(
            status=upgrade_account_result.status,
            message=upgrade_account_result.message,
            account_id=upgrade_account_result.account_id,
            plan_name=upgrade_account_result.plan_name,
            amount=upgrade_account_result.amount
        )
