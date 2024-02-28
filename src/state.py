# Modules
import config
import widgets

# Libraries
import tkinter as tk
import customtkinter as ctk  # type: ignore
from tkinter import filedialog, simpledialog

state = "test"


def action_button() -> None:
    dialog = ActionDialog(config.app)


def save_state():
    file_path = filedialog.asksaveasfilename(defaultextension=".toml", filetypes=[("TOML Files", "*.toml")])

    if file_path:
        with open(file_path, "w") as file:
            file.write(state)


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
        widgets.browse("input")

    def load_click(self) -> None:
        print("Load State")

    def save_click(self) -> None:
        print("Save State")
