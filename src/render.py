# Modules
import config
from config import G
import utils

# Libraries
import tkinter as tk
from tkinter import messagebox, simpledialog

# Standard
import subprocess
from pathlib import Path


def render():
    command = ["gifmaker"]

    def add_arg(item):
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

    for key in G:
        add_arg(G[key])

    utils.msg(" ".join(command))

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        ResultDialog(config.app, path=result.stdout)
    else:
        messagebox.showerror("Error", result.stderr)
        utils.msg(result.stderr)


class ResultDialog(simpledialog.Dialog):
    def __init__(self, parent, path):
        self.path = path
        super().__init__(parent)

    def body(self, parent):
        tk.Label(parent, text=f"File saved at: {self.path}").pack()

        self.button1 = tk.Button(parent, text="Open File", command=self.open_file_click)
        self.button1.pack(side=tk.LEFT, padx=5)

        self.button1 = tk.Button(parent, text="Open Directory", command=self.open_dir_click)
        self.button1.pack(side=tk.LEFT, padx=5)

        self.button2 = tk.Button(parent, text="Dismiss", command=self.dismiss_click)
        self.button2.pack(side=tk.LEFT, padx=5)

    def buttonbox(self):
        pass

    def open_file_click(self):
        try:
            subprocess.run(["xdg-open", self.path], check=True)
        except subprocess.CalledProcessError as e:
            utils.msg(f"Error opening file: {e}")

    def open_dir_click(self):
        try:
            subprocess.run(["xdg-open", Path(self.path).parent], check=True)
        except subprocess.CalledProcessError as e:
            utils.msg(f"Error opening file: {e}")

    def dismiss_click(self):
        self.ok()
