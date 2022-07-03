import requests
from mail_dashboard_service.core.models.upgrade_account import (
    CreateQuotaPayload,
    OrderPayload,
    OrderUpdatePayload,
    OrderUpdateResponse,
    OrderUpdateStatusResponse,
    OrderUpdateStatusPayload,
    CreateQuotaResponse,
    OrderResponse,

)


class UpgradeAccountMailCoreAdapter:

    def __init__(self, settings, mongo):
        self.settings = settings
        self.mongo = mongo

    def create_order(self, payload: OrderPayload) -> OrderResponse:
        col = self.mongo.orders
        order = {
            "account_id": payload.account_id,
            "status": payload.status
        }
        result = col.insert_one(order)
        return OrderResponse(
            order_id=result.inserted_id
        )

    def update_order_status(self, payload: OrderUpdateStatusPayload) -> OrderUpdateStatusResponse:
        col = self.mongo.orders
        order_query = {
            "_id": payload.order_id
        }
        new_value = {"$set": {"status": payload.status}}
        result = col.update_one(order_query, new_value)
        return OrderUpdateStatusResponse(
            updated=result.raw_result.get("updatedExisting")
        )

    def update_order(self, payload: OrderUpdatePayload) -> OrderUpdateResponse:
        col = self.mongo.orders
        order_query = {
            "_id": payload.order_id
        }
        value = {
            "$set": {
                "plan_id": payload.plan_id,
                "price_id": payload.price_id,
                "promotion_id": payload.promotion_id,
                "months": payload.months,
                "status": payload.status,
                "start_time": payload.start_time,
                "end_time": payload.end_time,
            }
        }
        result = col.update_one(order_query, value)
        return OrderUpdateResponse(
            updated=result.raw_result.get("updatedExisting")
        )

    def get_quota_mapping(self, plan_name):
        quota = {
            "free": self.settings.quota.free,
            "basic": self.settings.quota.basic,
            "premium": self.settings.quota.premium,
        }
        return quota.get(plan_name)

    def create_quota(self, payload: CreateQuotaPayload) -> CreateQuotaResponse:
        response = requests.post(
            self.settings.api.mail_core.create_quota,
            data={
                "account_id": payload.account_id,
                "email_limit": payload.email_limit,
                "custom_email_limit": payload.custom_email_limit,
                "alias_limit": payload.alias_limit
            }
        )
        if not response.ok:
            return CreateQuotaResponse()
        data = response.json()
        return CreateQuotaResponse(
            account_id=data.get("account_id"),
            email_limit=data.get("email_limit"),
            custom_email_limit=data.get("custom_email_limit"),
            alias_limit=data.get("alias_limit")
        )
