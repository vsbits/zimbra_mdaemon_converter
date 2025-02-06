from waitress import serve
from app import create_app
from app.utils.logger import logger
from app.config import HOST, PORT


def start_server():
    logger.info(f"Serving on {HOST}:{PORT}")
    try:
        serve(create_app(), listen=f"{HOST}:{PORT}",_quiet=True)
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    start_server()
