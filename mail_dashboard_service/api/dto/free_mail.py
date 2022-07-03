from pydantic import BaseModel, EmailStr


class CreateFreeEmailDTO(BaseModel):
    token: str


class GetTimeExpiredDTO(BaseModel):
    token: str
    email: EmailStr


class GetMoreTimeDTO(BaseModel):
    token: str
    email: EmailStr


class DeleteEmailDTO(BaseModel):
    token: str
    email: EmailStr


class GetEmails(BaseModel):
    token: str


class GetEmail(BaseModel):
    token: str
    email: EmailStr


class ActivateEmailDTO(BaseModel):
    token: str
    email: EmailStr


class DeactivateEmailDTO(BaseModel):
    token: str
    email: EmailStr
