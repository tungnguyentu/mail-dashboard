from typing import Protocol


class FreeEmailPort(Protocol):

    def get_account_id(self, payload):
        ...

    def create(self, payload):
        ...

    def get_remaining(self, payload):
        ...

    def refill(self, payload):
        ...

    def delete(self, payload):
        ...

    def get_emails(self, payload):
        ...
