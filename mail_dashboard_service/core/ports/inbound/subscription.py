from typing import Protocol

from mail_dashboard_service.core.models.get_subscriptions import (
    GetSubsciptionsQuery,
    GetSubsciptionsResponse
)


class SubscriptionUseCase(Protocol):

    def get_subs(self, query: GetSubsciptionsQuery) -> GetSubsciptionsResponse:
        ...

