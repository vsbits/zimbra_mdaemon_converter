from flask import (
    Blueprint, request, render_template, send_file, flash, url_for, redirect
)
from warnings import catch_warnings
from ..utils import process_request
from ..utils.logger import logger


blp = Blueprint("main", __name__)


@blp.get("/")
def index():
    ip = request.remote_addr
    logger.info(f"GET request from {ip}")
    return render_template("index.html.jinja")


@blp.post("/")
def file():
    file = request.files["file"]
    ip = request.remote_addr

    logger.info(f"POST request from {ip}")

    with catch_warnings(record=True) as w:
        try:
            new_file = process_request(file)
        except Exception as e:
            logger.exception(e)
            flash("Erro ao processar o arquivo", category="error")
            return redirect(url_for("main.index"))

        if len(w) > 0:
            for warning in w:
                logger.warning(warning.message)

    return send_file(
        new_file,
        download_name="contatos_mdaemon.csv",
        mimetype="text/csv"
    )
