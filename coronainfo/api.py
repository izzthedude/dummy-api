from pathlib import Path

from coronainfo import _logger

MODULE_DIR = Path(__file__).parent
STATIC_DIR = MODULE_DIR / "static"
logger = _logger.get_logger()


def setup(app, route: str = "coronainfo"):
    route = "/" + route

    @app.get(route)
    async def worldometer():
        content = ""
        worldometer_path = STATIC_DIR / "worldometer.html"

        try:
            with open(worldometer_path, "r") as file:
                content = file.read()
                content = " ".join(content.split())

        except Exception as err:
            logger.error(f"An eror has occurred while trying to get worldometer HTML content:", exc_info=True)
            logger.info(f"Returning an empty string")

        return {"html": content}
