from fastapi import Depends

from config.environment import Settings

from mail_dashboard_service.adapters.downgrade_account.account import DowngradeAccountAdapter
from mail_dashboard_service.adapters.downgrade_account.mail_core import DowngradeAccountMailCore
from mail_dashboard_service.adapters.downgrade_account.notify import DowngradeAccountNotification
from mail_dashboard_service.core.services.downgrade_account import DowngradeAccountService


def downgrade_account_repository(settings=Depends(Settings)):
    return DowngradeAccountAdapter(settings)


def downgrade_account_mail_core(settings=Depends(Settings)):
    return DowngradeAccountMailCore(settings)


def downgrade_account_notification(settings=Depends(Settings)):
    return DowngradeAccountNotification(settings)


def downgrade_account_service(
    mail_core=Depends(downgrade_account_mail_core),
    notification=Depends(downgrade_account_notification),
    account=Depends(downgrade_account_repository)
):
    return DowngradeAccountService(mail_core, account, notification)
