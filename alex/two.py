from alex.utils import create_logger

logger = create_logger(__name__)


def run_two():
    logger.debug("test from two")
    return 2
