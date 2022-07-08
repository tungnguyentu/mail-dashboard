from typing import Protocol
from mail_dashboard_service.core.models.downgrade_account import (
    DowngradeAccountPayload,
    DowngradeAccountResponse
)

class DowngradeAccountPort(Protocol):

    def downgrade_account(self, payload):
        ...


class DowngradeMailCorePort(Protocol):
    ...


class DowngradeNotifyPort(Protocol):
    ...
