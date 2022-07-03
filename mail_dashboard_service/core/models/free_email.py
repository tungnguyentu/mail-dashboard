from pydantic import BaseModel, EmailStr


class ServiceResponse(BaseModel):
    status: int
    message: str


# Create
class CreateEmailPayload(BaseModel):
    account_id: str


class CreateEmailCommand(BaseModel):
    account_id: str


class CreateEmailResponse(ServiceResponse):
    email: EmailStr = None
    expire: int = None


# Get Time Remain
class GetTimeRemainPayload(BaseModel):
    account_id: str
    email: EmailStr


class GetTimeRemainCommand(BaseModel):
    account_id: str
    email: EmailStr


class GetTimeRemainResponse(ServiceResponse):
    remaining: int = None


# Refill
class GetMoreTimeCommand(BaseModel):
    account_id: str
    email: EmailStr


class GetMoreTimePayload(BaseModel):
    account_id: str
    email: EmailStr


class GetMoreTimeResponse(ServiceResponse):
    message: str
    email: EmailStr = None
    expire: int = None


# delete email

class DeleteEmailCommand(BaseModel):
    account_id: str
    email: EmailStr


class DeleteEmailPayload(BaseModel):
    account_id: str
    email: EmailStr


class DeleteEmailResponse(ServiceResponse):
    account_id: str = None
    email: EmailStr = None

# list email


class GetEmailsCommand(BaseModel):
    account_id: str


class GetEmailsPayload(BaseModel):
    account_id: str


class GetEmailsResponse(ServiceResponse):
    message: str
    account_id: str = None
    emails: dict = None


class GetEmailCommand(BaseModel):
    account_id: str
    email: EmailStr


class GetEmailPayload(BaseModel):
    account_id: str
    email: EmailStr


class GetEmailResponse(ServiceResponse):
    email: EmailStr
    expire: int
    active: int


class ActivateEmailCommand(BaseModel):
    account_id: str
    email: EmailStr


class ActivateEmailPayload(BaseModel):
    account_id: str
    email: EmailStr


class ActivateEmailResponse(ServiceResponse):
    email: EmailStr
    active: int


class DeactivateEmailCommand(BaseModel):
    account_id: str
    email: EmailStr


class DeactivateEmailPayload(BaseModel):
    account_id: str
    email: EmailStr


class DeactivateEmaiResponse(ServiceResponse):
    email: EmailStr
    active: int
    account_id: str
