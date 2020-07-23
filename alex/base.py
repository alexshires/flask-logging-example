import os
import logging
from flask import Flask, jsonify

from alex.utils import create_logger

app = Flask(__name__)
app.logger.setLevel(logging.ERROR)
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)


logger = create_logger(__name__)
logger.debug("test from base")
