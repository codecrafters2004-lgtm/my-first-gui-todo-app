import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def get_path(env_name: str, default: str) -> Path:
    value = os.getenv(env_name)
    if value:
        return Path(value).expanduser()
    return BASE_DIR / default


TODO_FILE_PATH = get_path("TODO_FILE_PATH", "todos.txt")
ADD_ICON_PATH = get_path("ADD_ICON_PATH", "add.png")
COMPLETE_ICON_PATH = get_path("COMPLETE_ICON_PATH", "complete.png")
APP_NAME = os.getenv("APP_NAME", "my_todo_app")
