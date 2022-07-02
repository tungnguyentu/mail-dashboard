from pydantic import BaseModel


class UpgradeAccountDTO(BaseModel):
    token: str
    plan_id: str
    plan_name: str
    months: int
