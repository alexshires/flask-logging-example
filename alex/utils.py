import logging, sys


def create_logger(name = __name__, log_level: int = logging.DEBUG) -> logging.Logger:
    """ Create a logger object to be used throughout the script

    Args:
        log_level (int): The level of the logs (see https://docs.python.org/3/library/logging.html)

    Returns:
        logging.Logger: Our logging object
    """
    # Instantiate a logging object
    logger = logging.getLogger(name)
    # Set the level of the logs
    logger.setLevel(log_level)

    # create a logging format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%dT%H:%M:%S"
    )

    # create a file and stream handler handler
    stream_handler = logging.StreamHandler(sys.stdout)
    # Set the formatting
    stream_handler.setFormatter(formatter)
    # Add the handler to the logger object
    logger.addHandler(stream_handler)

    return logger
