from fastapi import APIRouter, Depends

from mail_dashboard_service.api.dto.upgrade_account import UpgradeAccountDTO
from mail_dashboard_service.core.ports.inbound.upgrade_account import UpgradeAccountUseCase
from mail_dashboard_service.api.dependencies.upgrade_account import upgrade_account_service

router = APIRouter()

@router.post("/upgrade")
def upgrade_account(
    payload: UpgradeAccountDTO, 
    service: UpgradeAccountUseCase = Depends(upgrade_account_service)
    ):
    return service.upgrade(payload)
