from pathlib import Path


def setup(app):
    @app.get("/worldometer")
    async def worldometer():
        content = ""
        path = Path(__file__).parent / "static" / "worldometer.html"
        with open(path, "r") as file:
            content = file.read()
            content = " ".join(content.split())

        return {"html": content}
