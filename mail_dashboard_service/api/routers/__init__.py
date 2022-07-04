import requests

def get_account_id(self, token) -> str:
    user_response = requests.get(
        self.settings.api.account.check_user,
        params={"token": token}
    )
    if not user_response.ok:
        return {
            "reason": user_response.reason,
            "account_id": None
        }
    data = user_response.json()
    account_id = data.get("accountId")
    return {
        "account_id": account_id
    }
