from typing import Protocol

from mail_dashboard_service.core.models.downgrade_account import (
    DowngradeAccountCommand,
    DowngradeAccountResponse
)


class DowngradeAccountUseCase(Protocol):

    def downgrade(self, command: DowngradeAccountCommand) -> DowngradeAccountResponse:
        ...