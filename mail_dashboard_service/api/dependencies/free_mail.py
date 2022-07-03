from fastapi import Depends

from config.environment import Settings

from mail_dashboard_service.adapters.free_email import FreeEmailApdater
from mail_dashboard_service.core.services.free_email import FreeEmailService


def free_mail_repository(settings=Depends(Settings)):
    return FreeEmailApdater(settings)


def create_free_email_service(repo=Depends(free_mail_repository)):
    return FreeEmailService(repo)


def get_time_remaining_service(repo=Depends(free_mail_repository)):
    return FreeEmailService(repo)


def get_more_time_service(repo=Depends(free_mail_repository)):
    return FreeEmailService(repo)


def delete_email_service(repo=Depends(free_mail_repository)):
    return FreeEmailService(repo)


def get_emails_service(repo=Depends(free_mail_repository)):
    return FreeEmailService(repo)


def get_email_service(repo=Depends(free_mail_repository)):
    return FreeEmailService(repo)


def activate_email_service(repo=Depends(free_mail_repository)):
    return FreeEmailService(repo)


def deactivate_email_service(repo=Depends(free_mail_repository)):
    return FreeEmailService(repo)
