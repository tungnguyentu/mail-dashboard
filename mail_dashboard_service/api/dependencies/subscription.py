from fastapi import Depends

from config.environment import Settings

from mail_dashboard_service.adapters.get_subscriptions import GetSubsciptionsAdapter
from mail_dashboard_service.core.services.subscriptions import SubsciptionsService


def subscription_repository(settings=Depends(Settings)):
    return GetSubsciptionsAdapter(settings)


def get_subscriptions_service(repo=Depends(subscription_repository)):
    return SubsciptionsService(repo)
