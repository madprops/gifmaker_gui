# Modules
import config
import widgets

# Libraries
import tkinter as tk
import customtkinter as ctk  # type: ignore
from tkinter import filedialog

# Standard
import json
from pathlib import Path


def action_button() -> None:
    ActionDialog(config.app)


def browse(arg: str) -> None:
    widget = config.args[arg]["widget"]
    file_path = filedialog.askopenfilename()
    widget.delete(0, ctk.END)
    widget.insert(0, file_path)


def save_state():
    file_path = filedialog.asksaveasfilename(
        initialdir=Path(config.root, "states"),
        defaultextension=".json",
        filetypes=[("State Files", "*.json")],
    )

    if file_path:
        state = get_state()

        with open(file_path, "w") as file:
            file.write(state)


def load_state():
    file_path = filedialog.askopenfilename(
        initialdir=Path(config.root, "states"),
    )

    with open(file_path, "r") as file:
        content = file.read()
        state = json.loads(content)
        apply_state(state)


def apply_state(state: dict) -> None:
    for key in state:
        config.args[key]["value"] = state[key]

    widgets.fill_widgets("value")


def get_state() -> str:
    state = {}

    for key in config.args:
        value = config.args[key]["widget"].get()
        state[key] = value

    return json.dumps(state)


class ActionDialog(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
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
