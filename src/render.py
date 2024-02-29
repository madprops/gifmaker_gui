# Modules
import config
from config import args
import utils
import widgets

# Libraries
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
        default = str(item["value"])

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


class ResultDialog(ctk.CTkToplevel): #type: ignore
    def __init__(self, *args: Any, path: str, **kwargs: Any):
        super().__init__(*args, **kwargs)
        widgets.prepare_dialog(self, path)
        self.path = path

        widgets.make_dialog_buttons(self, [
            {"text": "Open File", "command": self.open_file_click},
            {"text": "Open Directory", "command": self.open_dir_click},
            {"text": "Dismiss", "command": self.dismiss_click},
        ])

        widgets.make_dialog_modal(self)

    def open_file_click(self) -> None:
        utils.open_path(Path(self.path))

    def open_dir_click(self) -> None:
        utils.open_path(Path(self.path).parent)
