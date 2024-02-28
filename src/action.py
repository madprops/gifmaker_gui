# Modules
import state
import widgets

# Libraries
import customtkinter as ctk  # type: ignore

# Standard
from typing import Any

class ActionDialog(ctk.CTkToplevel):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        widgets.prepare_dialog(self, "Choose an Action")

        widgets.make_dialog_buttons(self, [
            {"text": "Browse Input", "command": self.browse_click},
            {"text": "Load State", "command": self.load_click},
            {"text": "Save State", "command": self.save_click},
        ])

        widgets.make_dialog_modal(self)

    def browse_click(self) -> None:
        self.destroy()
        state.browse("input")

    def load_click(self) -> None:
        self.destroy()
        state.load_state()

    def save_click(self) -> None:
        self.destroy()
        state.save_state()


def action_button() -> None:
    ActionDialog()