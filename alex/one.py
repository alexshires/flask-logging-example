from alex.utils import create_logger

logger = create_logger(__name__)


def run_one():
    logger.debug("test from one")
    return 1
