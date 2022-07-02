import requests
from mail_dashboard_service.core.models.upgrade_account import (
    PayOrderPayload,
    CreateQuotaPayload,
    DisableSubscriptionPayload,
    RefundOrderPayload,
    OrderPayload,
    OrderUpdatePayload,
    OrderUpdateResponse,
    OrderUpdateStatusResponse,
    OrderUpdateStatusPayload,
    CreateQuotaResponse,
    RefundOrderResponse,
    UpgradeAccountPayload,
    UpgradeAccountResponse,
    OrderResponse,
    PayOrderResponse,
    DisableSubscriptionResponse
)


class UpgradeAccountAdapter:

    def __init__(self, settings, mongo):
        self.settings = settings
        self.mongo = mongo

    def get_account_id(self, token) -> str:
        user_response = requests.get(
            self.settings.api.account.check_user,
            params={"token": token}
        )
        if user_response.status_code != 200:
            return user_response.reason
        data = user_response.json()
        user_id = data.get("user_id")
        response = requests.get(
            self.settings.api.account.get_account_id,
            params={"user_id": user_id}
        )
        if response.status_code != 200:
            return response.reason
        data = response.json()
        account_id = response.get("accountId")
        return account_id

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

    def pay_order(self, payload: PayOrderPayload) -> PayOrderResponse:
        response = requests.post(
            self.settings.api.billing.pay_order,
            data={
                "order_id": payload.order_id,
                "plan_id": payload.plan_id,
                "account_id": payload.account_id,
                "months": payload.months
            }
        )
        if not response.ok or response.status_code != 200:
            return PayOrderResponse()
        data = response.json()
        return PayOrderResponse(
            ok=response.ok,
            order_id=data.get("order_id"),
            account_id=data.get("account_id"),
            plan_id=data.get("plan_id"),
            price_id=data.get("price_id"),
            promotion_id=data.get("promotion_id"),
            months=data.get("months"),
            status=data.get("status"),
            start_time=data.get("start_time"),
            end_time=data.get("end_time"),
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

    def refund_order(self, payload: RefundOrderPayload) -> RefundOrderResponse:
        response = requests.post(
            self.settings.api.billing.refund_order,
            data={
                "order_id": payload.order_id
            }
        )
        if not response.ok:
            return RefundOrderResponse()
        data = response.json()
        return RefundOrderResponse(
            sub_id=data.get("sub_id"),
            bill_id=data.get("bill_id"),
        )

    def disable_subcription(self, payload: DisableSubscriptionPayload) -> DisableSubscriptionResponse:
        response = requests.post(
            self.settings.api.billing.disable_subscription,
            data={
                "order_id": payload.order_id
            }
        )
        if not response.ok:
            return DisableSubscriptionResponse()
        data = response.json()
        return DisableSubscriptionResponse(
            sub_id=data.get("sub_id"),
            bill_id=data.get("bill_id"),
        )

    def upgrade_account(self, payload: UpgradeAccountPayload) -> UpgradeAccountResponse:
        response = requests.post(
            self.settings.api.account.upgrade_account,
            data={
                "account_id": payload.account_id,
                "plan_name": payload.plan_name,
            }
        )
        if not response.ok:
            return UpgradeAccountResponse()
        data = response.json()
        data = data.get("data")
        return UpgradeAccountResponse(
            account_id=data.get("accountId"),
            plan_name=data.get("plan"),
            amount=data.get("amount"),
        )
