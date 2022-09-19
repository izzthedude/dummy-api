import logging
import sys
from datetime import datetime
from pathlib import Path

LOGS_DIR = Path(__file__).parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)
LEVEL = logging.DEBUG

FORMATTER = logging.Formatter(
    fmt="[%(asctime)s | %(levelname)s | %(name)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

FILE_HANDLER = logging.FileHandler(
    filename=str(LOGS_DIR / f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"),
    mode="w",
    encoding="utf-8")
FILE_HANDLER.setLevel(LEVEL)
FILE_HANDLER.setFormatter(FORMATTER)

STREAM_HANDLER = logging.StreamHandler(stream=sys.stdout)
STREAM_HANDLER.setLevel(LEVEL)
STREAM_HANDLER.setFormatter(FORMATTER)

logger = logging.getLogger("coronainfo")
logger.setLevel(LEVEL)
logger.addHandler(FILE_HANDLER)
logger.addHandler(STREAM_HANDLER)
logger.info(f"Log file: {LOGS_DIR}")


def get_logger() -> logging.Logger:
    return logger
