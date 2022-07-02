from environs import Env

env = Env()
env.read_env()


class MailCoreApiSettings:
    create_free_mail = env.str("CREATE_FREE_MAIL")
    remaining = env.str("REMAINING")
    refill = env.str("REFILL")
    delete = env.str("DELETE")
    list_email = env.str("LIST_EMAIL")


class AccountApiSettings:
    check_user = env.str("CHECK_USER", )


class APISetting:
    account = AccountApiSettings
    mail_core = MailCoreApiSettings


class MongodbSetting:
    uri = env.str("MONGO_URI", "mongodb://localhost:27017")
    db = env.str("MONGO_DB", "")
    collection = env.str("MONGO_COLLECTION", "")

class QuotaSetting:
    free = env.dict("QUOTA_FREE", subcast_values=int, default={})
    custom = env.str("QUOTA_BASIC", subcast_values=int, default={})
    premium = env.str("QUOTA_PREMIUM", subcast_values=int, default={})


class Settings:
    api = APISetting
    mongo = MongodbSetting
    quota = QuotaSetting
    API_HOST = env.str("API_HOST", "127.0.0.1")
    API_PORT = env.int("API_PORT", "5050")
    API_DEBUG_MODE = env.bool("API_DEBUG_MODE", True)
    API_AUTO_RELOAD = env.bool("API_AUTO_RELOAD", True)
