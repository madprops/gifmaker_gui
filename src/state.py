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

    widgets.fill_widgets()


def get_state() -> str:
    state = {}

    for key in config.args:
        value = config.args[key]["widget"].get()
        state[key] = value

    return json.dumps(state)


class ActionDialog(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color="#252933")
        self.label = ctk.CTkLabel(self, text="Choose an Action", font=config.font)
        self.label.pack(pady=(10, 0))

        self.buttons = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons.pack(padx=20, pady=(10, 20))

        self.button1 = ctk.CTkButton(self.buttons, text="Browse Input", command=self.browse_click)
        self.button1.pack(side=tk.LEFT, padx=5)

        self.button2 = ctk.CTkButton(self.buttons, text="Load State", command=self.load_click)
        self.button2.pack(side=tk.LEFT, padx=5)

        self.button3 = ctk.CTkButton(self.buttons, text="Save State", command=self.save_click)
        self.button3.pack(side=tk.LEFT, padx=5)

    def browse_click(self) -> None:
        browse("input")

    def load_click(self) -> None:
        load_state()

    def save_click(self) -> None:
        save_state()
