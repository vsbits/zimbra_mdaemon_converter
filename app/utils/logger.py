import logging
from ..config import LOG_FILE


logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


logger = logging.getLogger(__name__)
