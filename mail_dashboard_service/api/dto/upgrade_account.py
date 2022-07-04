from pydantic import BaseModel


class UpgradeAccountDTO(BaseModel):
    plan_id: str
    plan_name: str
    months: int
