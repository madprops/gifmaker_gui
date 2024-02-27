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
        default = str(item["default"])

        if (value is not None) and (str(value) != default):
            if isinstance(value, str):
                if not value:
                    return

            if isinstance(value, bool):
                cmd = [f"--{name}"]
            else:
                cmd = [f"--{name}", value]

            command.extend(cmd)

    for key in G:
        add_arg(G[key])

    utils.msg(command)

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        messagebox.showinfo("Alert", f"File was saved at: {result.stdout}")
        print(result.stdout)
    else:
        messagebox.showerror("Error", result.stderr)
        print(result.stderr)
