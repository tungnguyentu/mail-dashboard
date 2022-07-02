import logging

logging.basicConfig(
    format="[%(levelname)s] - [%(asctime)s] - %(message)s", datefmt="%d-%b-%y %H:%M:%S"
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
