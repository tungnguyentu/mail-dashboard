import requests
from mail_dashboard_service.core.models.downgrade_account import (
    DowngradeAccountPayload,
    DowngradeAccountResponse
)

class DowngradeAccountAdapter:

    def __init__(self, settings):
        self.settings = settings

    def downgrade_account(self, payload: DowngradeAccountPayload) -> DowngradeAccountResponse:
        response = requests.post(
            self.settings.api.account.downgrade_account,
            data={
                "account_id": payload.account_id,
                "plan": payload.plan_name,
            }
        )
        if not response.ok:
            return DowngradeAccountResponse(
                status=response.status_code,
                message=response.reason
            )
        data = response.json()
        status_code = data.get('code')
        message = data.get("message")
        data = data.get('data')
        return DowngradeAccountResponse(
            status=status_code,
            message=message,
            account_id=data.get("accountId"),
            plan_name=data.get("plan"),
            amount=data.get("amount"),
        )
