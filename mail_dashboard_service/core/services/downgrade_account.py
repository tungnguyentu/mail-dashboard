from mail_dashboard_service.core.ports.outbound.downgrade_account import (
    DowngradeAccountPort,
    DowngradeMailCorePort,
    DowngradeNotifyPort
)
from mail_dashboard_service.core.models.downgrade_account import (
    DowngradeAccountCommand,
    DowngradeAccountPayload,
    DowngradeAccountResponse,
    UpdateAccountQuotaPayload
)


class DowngradeAccountService:

    def __init__(self,
                 mail_core: DowngradeMailCorePort,
                 account: DowngradeAccountPort,
                 notify: DowngradeNotifyPort
                ):
        self.mail_core = mail_core
        self.account = account
        self.notify = notify

    def downgrade(self, command: DowngradeAccountCommand) -> DowngradeAccountResponse:
        response = self.mail_core.clear_emails(command.account_id)
        plan = self.mail_core.get_default_plan()
        quota_payload = UpdateAccountQuotaPayload(
            account_id=command.account_id,
            email_limit=plan.get("email_limit"),
            custom_email_limit=plan.get("custom_email_limit"),
            alias_limit=plan.get("alias_limit")
        )
        self.mail_core.update_account_quota(quota_payload)
        downgrade_account_payload = DowngradeAccountPayload(
            account_id=command.account_id,
            plan_name=plan.name
        )
        response = self.account.downgrade_account(downgrade_account_payload)
        self.notify.send_downgrade_account_notification(response)
        return DowngradeAccountResponse(
            message=response.message,
            status=response.status,
            account_id=command.account_id,
            plan_name=response.plan_name,
            amount=response.amount
        )
