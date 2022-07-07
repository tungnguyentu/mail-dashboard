import requests
from mail_dashboard_service.core.models.downgrade_account import (
    UpdateAccountQuotaPayload,
    UpdateAccountQuotaResponse,
    ClearEmailsResponse
)

class DowngradeAccountMailCore:

    def __init__(self, settings) -> None:
        self.settings = settings
    
    def clear_emails(self, account_id) -> None:
        response = requests.delete(
            self.settings.api.mail_core.clear_emails,
            data={
                "account_id": account_id
            }
        )   
        if not response.ok:
            return ClearEmailsResponse(
                status=response.status_code,
                message=response.reason
            )
        data = response.json()
        return ClearEmailsResponse(
            status=response.status_code,
            message=data.get("message"),
            account_id=data.get("account_id"),
        )
    
    def get_default_plan(self) -> dict:
        return self.settings.quota.default
    
    def update_account_quota(self, payload: UpdateAccountQuotaPayload) -> UpdateAccountQuotaResponse:
        response = requests.patch(
            self.settings.api.mail_core.update_account_quota,
            data={
                "account_id": payload.account_id,
                "email_limit": payload.email_limit,
                "custom_email_limit": payload.custom_email_limit,
                "alias_limit": payload.alias_limit
            }
        )
        if not response.ok:
            return UpdateAccountQuotaResponse(
                status=response.status_code,
                message=response.reason
            )
        data = response.json()
        return UpdateAccountQuotaResponse(
            status=response.status_code,
            message=data.get("message"),
            account_id=data.get("account_id"),
            email_limit=data.get("email_limit"),
            custom_email_limit=data.get("custom_email_limit"),
            alias_limit=data.get("alias_limit"),
        )