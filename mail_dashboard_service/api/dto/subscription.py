from pydantic import BaseModel


class GetSubscriptionsDTO(BaseModel):
    account_id: str
