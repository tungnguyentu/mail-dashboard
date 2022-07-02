import requests
from config.environment import Settings


class FreeEmailApdater:

    def __init__(self, settings: Settings):
        self.settings = settings
    
    def get_account_id(self, payload):
        user_response = requests.get(
            self.settings.api.account.check_user,
            params={"token": payload.token}
        )
        if user_response.status_code != 200:
            return user_response.reason
        data = user_response.json()
        user_id = data.get("user_id")
        response = requests.get(
            self.settings.api.account.get_account_id,
            params={"user_id": user_id}
        )
        if response.status_code != 200:
            return response.reason
        data = response.json()
        account_id = response.get("accountId")
        return account_id

    def create(self, payload):
        response = requests.post(
            self.settings.api.mail_core.create_free_mail,
            data={
                "account_id": payload.account_id
            }
        )
        if response.status_code != 201:
            return response.reason
        return response.json()


    def get_remaining(self, payload):
        response = requests.get(
            self.settings.api.mail_core.remaining,
            params={
                "account_id": payload.account_id,
                "email": payload.email
            }
        )
        if response.status_code != 200:
            return response.reason
        return response.json()

    def refill(self, payload):
        response = requests.post(
            self.settings.api.mail_core.refill,
            data={
                "account_id": payload.account_id,
                "email": payload.email
            }
        )
        if response.status_code != 200:
            return response.reason
        return response.json()

    def delete(self, payload):
        response = requests.delete(
            self.settings.api.mail_core.delete,
            data={
                "account_id": payload.account_id,
                "email": payload.email
            }
        )
        if response.status_code != 200:
            return response.reason
        return response.json()

    def get_emails(self, payload):
        response = requests.get(
            self.settings.api.mail_core.list_email,
            params={
                "account_id": payload.account_id,
            }
        )
        if response.status_code != 200:
            return response.reason
        return response.json()
