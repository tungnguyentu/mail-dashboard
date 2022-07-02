from pydantic import BaseModel, EmailStr


#Create
class CreateEmailPayload(BaseModel):
    account_id: str


class CreateEmailCommand(BaseModel):
    token: str


class CreateEmailResponse(BaseModel):
    message: str
    email: EmailStr = None
    expire: int = None


#Get Time Remain
class GetTimeRemainPayload(BaseModel):
    account_id: str
    email: EmailStr


class GetTimeRemainCommand(BaseModel):
    token: str
    email: EmailStr


class GetTimeRemainResponse(BaseModel):
    message: str
    remaining: int = None


# Refill
class GetMoreTimeCommand(BaseModel):
    token: str
    email: EmailStr


class GetMoreTimePayload(BaseModel):
    account_id: str
    email: EmailStr


class GetMoreTimeResponse(BaseModel):
    message: str
    email: EmailStr = None
    expire: int = None


#delete email

class DeleteEmailCommand(BaseModel):
    token: str
    email: EmailStr


class DeleteEmailPayload(BaseModel):
    account_id: str
    email: EmailStr


class DeleteEmailResponse(BaseModel):
    message: str
    account_id: str = None
    email: EmailStr = None

# list email
class GetEmailsCommand(BaseModel):
    token: str


class GetEmailsPayload(BaseModel):
    account_id: str


class GetEmailsResponse(BaseModel):
    message: str
    account_id: str = None
    emails: dict = None
