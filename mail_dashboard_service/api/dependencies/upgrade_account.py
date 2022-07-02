from fastapi import Depends

from config.environment import Settings

from mail_dashboard_service.adapters.upgrade_account import UpgradeAccountAdapter
from mail_dashboard_service.core.services.upgrade_account import UpgradeAccountService
from mail_dashboard_service.infra.mongo.connection import get_db


def upgrade_account_repository(db=Depends(get_db), settings=Depends(Settings)):
    return UpgradeAccountAdapter(settings, db)


def upgrade_account_service(repo=Depends(upgrade_account_repository)):
    return UpgradeAccountService(repo)
