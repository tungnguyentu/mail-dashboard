from fastapi import Depends

from config.environment import Settings
from mail_dashboard_service.adapters.upgrade_account.mail_core import UpgradeAccountMailCoreAdapter
from mail_dashboard_service.adapters.upgrade_account.billing import UpgradeAccountBillingAdapter
from mail_dashboard_service.adapters.upgrade_account.account import UpgradeAccountAdapter
from mail_dashboard_service.core.services.upgrade_account import UpgradeAccountService
from mail_dashboard_service.infra.mongo.connection import get_db


def upgrade_account_repository(settings=Depends(Settings)):
    return UpgradeAccountAdapter(settings)


def upgrade_account_mail_core(db=Depends(get_db), settings=Depends(Settings)):
    return UpgradeAccountMailCoreAdapter(settings, db)


def upgrade_account_billing(settings=Depends(Settings)):
    return UpgradeAccountBillingAdapter(settings)


def upgrade_account_service(
    mail_core=Depends(upgrade_account_mail_core),
    billing=Depends(upgrade_account_billing),
    account=Depends(upgrade_account_repository)
):
    return UpgradeAccountService(mail_core, billing, account)
