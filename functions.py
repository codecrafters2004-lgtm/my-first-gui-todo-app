import os
from pathlib import Path

from settings import TODO_FILE_PATH


def _ensure_file(path: Path) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text('', encoding='utf-8')
    return str(path)


filepath = _ensure_file(TODO_FILE_PATH)


def get_todos(filepath=filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        todos_local = file.readlines()
        return todos_local


def write_todos(todos, filepath=filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.writelines(todos)

