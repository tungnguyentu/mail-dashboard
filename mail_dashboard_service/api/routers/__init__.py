import requests

def get_account_id(self, token) -> str:
    user_response = requests.get(
        self.settings.api.account.check_user,
        params={"token": token}
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