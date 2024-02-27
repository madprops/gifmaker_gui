# Modules
import config
from config import args
import utils

# Libraries
import tkinter as tk
import customtkinter as ctk  # type: ignore
from tkinter import messagebox, simpledialog

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
        ResultDialog(config.app, path=result.stdout)
    else:
        messagebox.showerror("Error", result.stderr)
        utils.msg(result.stderr)


class ResultDialog(simpledialog.Dialog):
    def __init__(self, parent: ctk.CTkFrame, path: str):
        self.path = path
        super().__init__(parent)

    def body(self, parent: ctk.CTkFrame) -> None:
        tk.Label(parent, text=f"File saved at: {self.path}").pack()

        self.button1 = ctk.CTkButton(parent, text="Open File", command=self.open_file_click)
        self.button1.pack(side=tk.LEFT, padx=5)

        self.button1 = ctk.CTkButton(parent, text="Open Directory", command=self.open_dir_click)
        self.button1.pack(side=tk.LEFT, padx=5)

        self.button2 = ctk.CTkButton(parent, text="Dismiss", command=self.dismiss_click)
        self.button2.pack(side=tk.LEFT, padx=5)

    def buttonbox(self) -> None:
        pass

    def open_file_click(self) -> None:
        self.ok()

        try:
            subprocess.run(["xdg-open", self.path], check=True)
        except subprocess.CalledProcessError as e:
            utils.msg(f"Error opening file: {e}")

    def open_dir_click(self) -> None:
        self.ok()

        try:
            subprocess.run(["xdg-open", Path(self.path).parent], check=True)
        except subprocess.CalledProcessError as e:
            utils.msg(f"Error opening file: {e}")

    def dismiss_click(self) -> None:
        self.ok()
