import requests
from mail_dashboard_service.core.models.upgrade_account import (
    UpgradeAccountPayload,
    UpgradeAccountResponse,
)


class UpgradeAccountAdapter:

    def __init__(self, settings):
        self.settings = settings

    def upgrade_account(self, payload: UpgradeAccountPayload) -> UpgradeAccountResponse:
        response = requests.post(
            self.settings.api.account.upgrade_account,
            data={
                "account_id": payload.account_id,
                "plan_name": payload.plan_name,
            }
        )
        if not response.ok:
            return UpgradeAccountResponse(
                status=response.status_code,
                message=response.reason
            )
        data = response.json()
        data = data.get("data")
        return UpgradeAccountResponse(
            status=response.status_code,
            message="Upgrade account successfully",
            account_id=data.get("accountId"),
            plan_name=data.get("plan"),
            amount=data.get("amount"),
        )
