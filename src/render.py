# Modules
import config
from config import args
import utils

# Libraries
import tkinter as tk
import customtkinter as ctk  # type: ignore
from tkinter import messagebox

# Standard
import subprocess
from pathlib import Path
from typing import Dict, Any


def render() -> None:
    command = ["gifmaker"]

    def add_arg(item: Dict[str, Any]) -> None:
        value = item["widget"].get()
        default = str(item["default"])

        if (value is not None) and (str(value) != default):
            if isinstance(value, str):
                if not value:
                    return

            if isinstance(value, bool):
                cmd = [f"--{key}"]
            else:
                cmd = [f"--{key}", value]

            command.extend(cmd)

    for key in args:
        add_arg(args[key])

    utils.msg(" ".join(command))

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        ResultDialog(config.app, path=result.stdout.strip())
    else:
        messagebox.showerror("Error", result.stderr)
        utils.msg(result.stderr)


class ResultDialog(ctk.CTkToplevel):
    def __init__(self, *args, path: str, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color="#252933")
        self.label = ctk.CTkLabel(self, text=path, font=config.font)
        self.label.pack(pady=(10, 0))

        self.buttons = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons.pack(padx=20, pady=(10, 20))

        self.button1 = ctk.CTkButton(self.buttons, text="Open File", command=self.open_file_click)
        self.button1.pack(side=tk.LEFT, padx=5)

        self.button1 = ctk.CTkButton(self.buttons, text="Open Directory", command=self.open_dir_click)
        self.button1.pack(side=tk.LEFT, padx=5)

        self.button2 = ctk.CTkButton(self.buttons, text="Dismiss", command=self.dismiss_click)
        self.button2.pack(side=tk.LEFT, padx=5)

    def open_file_click(self) -> None:
        self.ok()
        utils.open_path(self.path)

    def open_dir_click(self) -> None:
        self.ok()
        utils.open_path(Path(self.path).parent)

    def dismiss_click(self) -> None:
        self.ok()
