import requests
from mail_dashboard_service.core.models.get_subscriptions import (
    GetSubsPayload,
    GetSubsciptionsResponse
)


class GetSubsciptionsAdapter:

    def __init__(self, settings):
        self.settings = settings
    
    def get_subscriptions(self, payload: GetSubsPayload) -> GetSubsciptionsResponse:
        response = requests.get(
            self.settings.api.billing.get_subs,
            params={
                "account_id": payload.account_id
            }
        )
        if not response.ok:
            return GetSubsciptionsResponse(
                message=response.reason,
                status=0
            )
        data = response.json()
        items = data.get("_items", [])
        meta = data.get("_meta", {})
        return GetSubsciptionsResponse(
            subscriptions=items,
            total=meta.get("total")
        )
