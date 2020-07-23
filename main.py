"""
Simple Flask app to produce health API
"""
from flask import jsonify

from alex.base import app
from alex.utils import create_logger
from alex.one import run_one
from alex.two import run_two


@app.route("/", methods=["GET"])
def default():
    """
    test
    """
    one = run_one()
    two = run_two()
    output = {"one": one, "two": two}
    status_code = 200
    return jsonify(output), status_code


if __name__ == "__main__":
    app.run()
