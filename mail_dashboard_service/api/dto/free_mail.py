from pydantic import BaseModel, EmailStr


class CreateFreeEmailDTO(BaseModel):
    ...


class GetTimeExpiredDTO(BaseModel):
    email: EmailStr


class GetMoreTimeDTO(BaseModel):
    email: EmailStr


class DeleteEmailDTO(BaseModel):
    email: EmailStr


class GetEmails(BaseModel):
    ...


class GetEmail(BaseModel):
    email: EmailStr


class ActivateEmailDTO(BaseModel):
    email: EmailStr


class DeactivateEmailDTO(BaseModel):
    email: EmailStr
