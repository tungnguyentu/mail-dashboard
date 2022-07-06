from mail_dashboard_service.core.models.get_subscriptions import (
    GetSubsciptionsQuery,
    GetSubsciptionsResponse
)
from mail_dashboard_service.core.ports.outbound.subscription import GetSubsciptionsPort


class SubsciptionsService:
    
    def __init__(self, sub: GetSubsciptionsPort):
        self.sub = query
    
    def get_subs(self, query: GetSubsciptionsQuery) -> GetSubsciptionsResponse:
        payload = GetSubsPayload(
            account_id=query.account_id
        )
        response = self.sub.get_subscriptions(payload)

        return GetSubsciptionsResponse(
            message="Get Subscription Success",
            status=1,
            subscriptions=response.subscriptions,
            total=response.total
        )