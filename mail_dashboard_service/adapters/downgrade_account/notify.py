import requests
from mail_dashboard_service.core.models.downgrade_account import DowngradeAccountNotificationResponse


class DowngradeAccountNotification:

    def __init__(self, settings):
        self.settings = settings

    def send_downgrade_account_notification(self, payload):
        response = requests.post(
            self.settings.api.notification.downgrade_account,
            data={
                "type": payload.account_id,
                "send_to": payload.account_id,
                "template_name": self.settings.notification.downgrade_account_template_name,
            }
        )
        if not response.ok:
            return DowngradeAccountNotificationResponse(
                status=response.status_code,
                message=response.reason
            )
        data = response.json()
        return DowngradeAccountNotificationResponse(
            status=response.status_code,
            message=data.get("message")
        )
