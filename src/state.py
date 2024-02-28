# Modules
import config
import widgets

# Libraries
import customtkinter as ctk  # type: ignore
from tkinter import filedialog

# Standard
import json
from pathlib import Path
from typing import Any, Dict


def browse(arg: str) -> None:
    widget = config.args[arg]["widget"]
    file_path = filedialog.askopenfilename()
    widget.delete(0, ctk.END)
    widget.insert(0, file_path)


def save_state() -> None:
    assert isinstance(config.root, Path)

    file_path = filedialog.asksaveasfilename(
        initialdir=Path(config.root, "states"),
        defaultextension=".json",
        filetypes=[("State Files", "*.json")],
    )

    if not file_path:
        return

    state = get_state()

    with open(file_path, "w") as file:
        file.write(state)


def load_state() -> None:
    assert isinstance(config.root, Path)

    file_path = filedialog.askopenfilename(
        initialdir=Path(config.root, "states"),
    )

    if not file_path:
        return

    path = Path(file_path)

    if not path.exists() or not path.is_file():
        return

    with open(path, "r") as file:
        content = file.read()
        state = json.loads(content)
        apply_state(state)


def apply_state(state: Dict[str, Any]) -> None:
    for key in state:
        arg = config.args.get(key)

        if arg:
            arg["value"] = state[key]

    widgets.fill_widgets("value")


def get_state() -> str:
    state = {}

    for key in config.args:
        value = config.args[key]["widget"].get()
        state[key] = value

    return json.dumps(state)


class ActionDialog:
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        widgets.prepare_dialog(self, "Choose an Action")

        widgets.make_dialog_buttons(self, [
            {"text": "Browse Input", "command": self.browse_click},
            {"text": "Load State", "command": self.load_click},
            {"text": "Save State", "command": self.save_click},
        ])

    def browse_click(self) -> None:
        browse("input")

    def load_click(self) -> None:
        load_state()

    def save_click(self) -> None:
        save_state()


def action_button() -> None:
    ActionDialog(config.app)
