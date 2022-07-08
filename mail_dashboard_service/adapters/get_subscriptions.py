import requests
from mail_dashboard_service.core.models.get_subscriptions import (
    GetSubsPayload,
    GetSubsciptionsResponse,
    GetSubsciptionResponse,
    BillResponse
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
        subs = []
        for item in items:
            bills = item.get("bill", [])
            bill_responses = []
            for bill in bills:
                bill_responses.append(BillResponse(
                    _id=bill.get("id"),
                    discount=bill.get("discount"),
                    bill_status=bill.get("status"),
                    sub_total=bill.get("sub_total"),
                    subscription_id=bill.get("subscription_id"),
                    total=bill.get("total")
                ))
            subs.append(GetSubsciptionResponse(
                created=item.get("_created"),
                deleted=item.get("_deleted"),
                updated=item.get("_updated"),
                account_id=item.get("account_id"),
                end_time=item.get("end_time"),
                _id=item.get("id"),
                month=item.get("month"),
                order_id=item.get("order_id"),
                plan_id=item.get("plan_id"),
                price_id=item.get("price_id"),
                promotion_id=item.get("promotion_id"),
                start_time=item.get("start_time"),
                sub_status=item.get("status"),
                bill=bill_responses
            ))
        return GetSubsciptionsResponse(
            subscriptions=subs,
            total=meta.get("total")
        )
