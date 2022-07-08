from fastapi import APIRouter, Depends

from mail_dashboard_service.api.dto.downgrade_account import DowngradeAccountDTO
from mail_dashboard_service.core.ports.inbound.downgrade_account import DowngradeAccountUseCase
from mail_dashboard_service.api.dependencies.downgrade_account import downgrade_account_service
from mail_dashboard_service.core.models.downgrade_account import DowngradeAccountCommand, DowngradeAccountResponse

router = APIRouter()


@router.post(
    "/account/downgrade",
    response_model=DowngradeAccountResponse,
    response_model_exclude_unset=True
)
def upgrade_account(
    payload: DowngradeAccountDTO,
    service: DowngradeAccountUseCase = Depends(downgrade_account_service),
):
    command = DowngradeAccountCommand(
        account_id=payload.account_id
    )
    result = service.downgrade(command)
    if not result.status:
        result.status = 404
    else:
        result.status = 200
    return result
