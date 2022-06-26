from environs import Env

env = Env()
env.read_env()


class Settings:
    API_HOST = env.str("API_HOST", "127.0.0.1")
    API_PORT = env.int("API_PORT", "5050")
    API_DEBUG_MODE = env.bool("API_DEBUG_MODE", True)
    API_AUTO_RELOAD = env.bool("API_AUTO_RELOAD", True)