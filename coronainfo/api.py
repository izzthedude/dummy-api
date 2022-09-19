from pathlib import Path

MODULE_DIR = Path(__file__).parent
STATIC_DIR = MODULE_DIR / "static"


def setup(app, path: str = "coronainfo"):
    path = "/" + path

    @app.get(path)
    async def worldometer():
        content = ""
        worldometer_path = STATIC_DIR / "worldometer.html"
        with open(worldometer_path, "r") as file:
            content = file.read()
            content = " ".join(content.split())

        return {"html": content}
