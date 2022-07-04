from fastapi import APIRouter, Depends

from . import get_account_id

from mail_dashboard_service.api.dto.upgrade_account import UpgradeAccountDTO
from mail_dashboard_service.core.ports.inbound.upgrade_account import UpgradeAccountUseCase
from mail_dashboard_service.api.dependencies.upgrade_account import upgrade_account_service
from mail_dashboard_service.core.models.upgrade_account import UpgradeAccountCommand, UpgradeAccountResponse

router = APIRouter()


@router.post(
    "/upgrade",
    response_model=UpgradeAccountResponse,
    response_model_exclude_unset=True
)
def upgrade_account(
    payload: UpgradeAccountDTO,
    service: UpgradeAccountUseCase = Depends(upgrade_account_service)
):
    account = get_account_id(payload.token)
    if not account.get("account_id"):
        return UpgradeAccountResponse(message="Invalid token", status=404)
    command = UpgradeAccountCommand(
        account_id=account.get("account_id"),
        plan_name=payload.plan_name,
        plan_id=payload.plan_id,
        months=payload.months,
    )
    result = service.upgrade(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result
