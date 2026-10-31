import os
import subprocess
import sys
from pathlib import Path

from settings import ADD_ICON_PATH, APP_NAME, BASE_DIR, COMPLETE_ICON_PATH, TODO_FILE_PATH


def build_app() -> None:
    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--name",
        os.getenv("APP_NAME", APP_NAME),
        "--onefile",
        "--windowed",
        "--add-data",
        f"{ADD_ICON_PATH}{os.pathsep}.",
        "--add-data",
        f"{COMPLETE_ICON_PATH}{os.pathsep}.",
        "--add-data",
        f"{TODO_FILE_PATH}{os.pathsep}.",
        str(BASE_DIR / "gui.py"),
    ]
    subprocess.run(command, check=True)


if __name__ == "__main__":
    build_app()
