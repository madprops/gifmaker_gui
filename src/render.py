# Modules
from config import G
import utils

# Libraries
from tkinter import messagebox

# Standard
import subprocess


def render():
    command = ["gifmaker"]

    def add_arg(item):
        name = item["name"]
        value = item["widget"].get()
        reverse = item.get("reverse")

        if reverse:
            value = not value

        if value and (value != item["default"]):
            command.extend([f"--{name}", value])

    for key in G:
        add_arg(G[key])

    utils.msg("Running Gifmaker")
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        messagebox.showinfo("Alert", f"File was saved at: {result.stdout}")
        print(result.stdout)
    else:
        messagebox.showerror("Error", result.stderr)
        print(result.stderr)
