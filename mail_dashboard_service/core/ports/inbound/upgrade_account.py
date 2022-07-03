from typing import Protocol

from mail_dashboard_service.core.models.upgrade_account import UpgradeAccountCommand, UpgradeAccountResponse


class UpgradeAccountUseCase(Protocol):

    def upgrade(self, command: UpgradeAccountCommand) -> UpgradeAccountResponse:
        ...
