import requests
from config.environment import Settings
from mail_dashboard_service.core.models.free_email import ActivateEmailPayload, ActivateEmailResponse, CreateEmailPayload, CreateEmailResponse, DeactivateEmaiResponse, DeactivateEmailPayload, DeleteEmailPayload, DeleteEmailResponse, GetEmailPayload, GetEmailResponse, GetEmailsPayload, GetEmailsResponse, GetMoreTimePayload, GetMoreTimeResponse, GetTimeRemainPayload, GetTimeRemainResponse


class FreeEmailApdater:

    def __init__(self, settings: Settings):
        self.settings = settings

    def create(self, payload: CreateEmailPayload) -> CreateEmailResponse:
        response = requests.post(
            self.settings.api.mail_core.create_free_mail,
            data={
                "account_id": payload.account_id
            }
        )
        if not response.ok:
            return CreateEmailResponse(
                message=response.reason,
                status=0
            )
        data = response.json()
        return CreateEmailResponse(
            status=1,
            message=data.get("message"),
            email=data.get("email"),
            expire=data.get("expire")
        )

    def get_remaining(self, payload: GetTimeRemainPayload) -> GetTimeRemainResponse:
        response = requests.get(
            self.settings.api.mail_core.remaining,
            params={
                "account_id": payload.account_id,
                "email": payload.email
            }
        )
        if not response.ok:
            return GetTimeRemainResponse(
                message=response.reason,
                status=0
            )
        data = response.json()
        return GetTimeRemainResponse(
            message=data.get("message"),
            status=1,
            remaining=data.get("remaining")
        )

    def refill(self, payload: GetMoreTimePayload) -> GetMoreTimeResponse:
        response = requests.post(
            self.settings.api.mail_core.refill,
            data={
                "account_id": payload.account_id,
                "email": payload.email
            }
        )
        if not response.ok:
            return GetMoreTimeResponse(
                message=response.reason,
                status=0
            )
        data = response.json()
        return GetMoreTimeResponse(
            status=1,
            message=data.get("message"),
            email=data.get("email"),
            expire=data.get("expire")
        )

    def delete(self, payload: DeleteEmailPayload) -> DeleteEmailResponse:
        response = requests.delete(
            self.settings.api.mail_core.delete,
            data={
                "account_id": payload.account_id,
                "email": payload.email
            }
        )
        if not response.ok:
            return DeleteEmailResponse(
                status=0,
                message=response.reason
            )
        data = response.json()
        return DeleteEmailResponse(
            status=1,
            message=data.get("message"),
            account_id=data.get("account_id"),
            email=data.get("email")
        )

    def get_emails(self, payload: GetEmailsPayload) -> GetEmailsResponse:
        response = requests.get(
            self.settings.api.mail_core.list_email,
            params={
                "account_id": payload.account_id,
            }
        )
        if not response.ok:
            return GetEmailsResponse(
                status=0,
                message=response.reason
            )
        data = response.json()
        return GetEmailsResponse(
            status=1,
            message=data.get("message"),
            emails=data.get("emails"),
        )

    def get_email(self, payload: GetEmailPayload) -> GetEmailResponse:
        response = requests.get(
            self.settings.api.mail_core.get_email,
            params={
                "account_id": payload.account_id,
                "email": payload.email
            }
        )
        if not response.ok:
            return GetEmailResponse(
                status=0,
                message=response.reason
            )
        data = response.json()
        return GetEmailResponse(
            status=1,
            message=data.get("message"),
            email=data.get("emails"),
            expire=data.get("expire"),
            active=data.get("active")
        )

    def activate(self, payload: ActivateEmailPayload) -> ActivateEmailResponse:
        response = requests.post(
            self.settings.api.mail_core.activate,
            data={
                "account_id": payload.account_id,
                "email": payload.email
            }
        )
        if not response.ok:
            return ActivateEmailResponse(
                status=0,
                message=response.reason
            )
        data = response.json()
        return ActivateEmailResponse(
            status=1,
            message=data.get("message"),
            email=data.get("emails"),
            active=data.get("active")
        )

    def deactivate(self, payload: DeactivateEmailPayload) -> DeactivateEmaiResponse:
        response = requests.post(
            self.settings.api.mail_core.activate,
            data={
                "account_id": payload.account_id,
                "email": payload.email
            }
        )
        if not response.ok:
            return DeactivateEmaiResponse(
                status=0,
                message=response.reason
            )
        data = response.json()
        return DeactivateEmaiResponse(
            status=1,
            message=data.get("message"),
            email=data.get("emails"),
            active=data.get("active")
        )
