from pydantic import BaseModel


class DowngradeAccountDTO(BaseModel):
    account_id: str

