# Standard
import sys
from typing import Any


def msg(message: str) -> None:
    print(message, file=sys.stderr)


def respond(message: str) -> None:
    print(message, file=sys.stdout)


def colortext(color: str, text: str) -> str:
    codes = {
        "red": "\x1b[31m",
        "green": "\x1b[32m",
        "yellow": "\x1b[33m",
        "blue": "\x1b[34m",
        "magenta": "\x1b[35m",
        "cyan": "\x1b[36m",
    }

    if color in codes:
        code = codes[color]
        text = f"{code}{text}\x1b[0m"

    return text


def show_parents(obj: Any) -> None:
    child_class = obj.__class__
    parent_classes = child_class.__bases__
    parents = ", ".join([parent.__name__ for parent in parent_classes])
    msg("Parent classes of " + child_class.__name__ + " are: " + parents)
