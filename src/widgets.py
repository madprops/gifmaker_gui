# Modules
import config
from config import args
from framedata import FrameData

# Libraries
import tkinter as tk
import customtkinter as ctk  # type: ignore

# Standard
from typing import Any, Union, List, Tuple, Callable, Dict


def make_frame() -> ctk.CTkFrame:
    frame = ctk.CTkFrame(config.app, fg_color="transparent")
    frame.grid(row=config.frame_number, column=0, padx=config.frame_padx,
               pady=config.frame_pady, sticky="ew")
    config.frame_number += 1
    return frame


def make_label(d: FrameData, text: str, sticky: str = "w") -> ctk.CTkLabel:
    label = ctk.CTkLabel(d.frame, text=f"{text}:", font=config.font)
    label.grid(row=0, column=d.col, padx=config.padx, pady=config.pady, sticky=sticky)
    d.col += 1
    return label


def make_text(d: FrameData, value: str = "", width: Union[int, None] = None, sticky: str = "w",
              placeholder: str = "") -> ctk.CTkEntry:
    w = width if width else config.text_width
    widget = ctk.CTkEntry(d.frame, placeholder_text=placeholder, font=config.font, width=w)
    widget.grid(row=0, column=d.col, padx=config.padx, pady=config.pady, sticky=sticky)

    if value:
        widget.insert(0, value)

    d.col += 1
    return widget


def make_button(d: FrameData, text: str, command: Callable[..., Any], color: str = "grey",
                text_color: Union[str, None] = None, hover_color: Union[Tuple[str, str], None] = None,
                sticky: str = "w") -> ctk.CTkButton:
    widget = ctk.CTkButton(d.frame, text=text, command=command, font=config.font,
                           fg_color=color, text_color=text_color, hover_color=hover_color, )

    widget.grid(row=0, column=d.col, padx=config.padx, pady=config.pady, sticky=sticky)
    d.col += 1
    return widget


def make_select(d: FrameData, values: Union[List[Any], None] = None, sticky: str = "w") -> ctk.CTkComboBox:
    v = values if values else ["empty"]
    widget = ctk.CTkComboBox(d.frame, values=v, state="readonly", width=config.select_width, font=config.font)
    widget.grid(row=0, column=d.col, padx=config.padx, pady=config.pady, sticky=sticky)
    d.col += 1
    return widget


def make_checkbox(d: FrameData, sticky: str = "w") -> ctk.CTkCheckBox:
    widget = ctk.CTkCheckBox(d.frame, font=config.font, text="", onvalue=True, offvalue=False, width=1)
    widget.grid(row=0, column=d.col, padx=config.padx, pady=config.pady, sticky=sticky)
    d.col += 1
    return widget


def fill_widgets(mode: str = "default") -> None:
    for key in args:
        value = args[key][mode]
        set_widget(args[key]["widget"], value, args[key]["type"], args[key].get("choices"))


def set_widget(widget: ctk.CTkBaseClass, value: Any, wtype: str, extra: Any) -> None:
    if wtype == "text":
        set_text(widget, value)
    elif wtype == "checkbox":
        set_checkbox(widget, value)
    elif wtype == "select":
        set_select(widget, value, extra)


def set_text(widget: ctk.CTkEntry, value: Any) -> None:
    if not value:
        return

    if isinstance(value, list):
        value = ",".join(map(str, value))
    else:
        value = str(value)

    widget.delete(0, "end")
    widget.insert(0, value)


def set_checkbox(widget: ctk.CTkCheckBox, value: Any) -> None:
    if value:
        widget.select()
    else:
        widget.deselect()


def set_select(widget: ctk.CTkBaseClass, value: Any, extra: Any) -> None:
    if extra:
        widget.configure(values=extra)

    widget.set(value)


def add(name: str, d: FrameData) -> None:
    item = args[name]
    make_label(d, item["label"])

    if item["type"] == "text":
        item["widget"] = make_text(d,
                                   sticky=item.get("sticky"), placeholder=item.get("placeholder", ""),
                                   width=item.get("width"))
    elif item["type"] == "checkbox":
        item["widget"] = make_checkbox(d)
    elif item["type"] == "select":
        item["widget"] = make_select(d)


def prepare_dialog(parent: ctk.CTkToplevel, text: str) -> None:
    parent.configure(fg_color=config.dialog_color)
    parent.label = ctk.CTkLabel(parent, text=text, font=config.font)
    parent.label.pack(pady=(10, 0))


def make_dialog_buttons(parent: ctk.CTkToplevel, items: List[Dict[str, Any]]) -> None:
    buttons = ctk.CTkFrame(parent, fg_color="transparent")
    buttons.pack(padx=20, pady=(10, 20))
    bpack = {"side": tk.LEFT, "padx": 5}

    items.append({"text": "Dismiss", "command": lambda: parent.destroy()})

    for item in items:
        ctk.CTkButton(buttons, text=item["text"],
                      command=item["command"], font=config.font).pack(**bpack)


def make_dialog_modal(parent: ctk.CTkToplevel) -> None:
    parent.wait_visibility()
    parent.grab_set_global()
    parent.lift()
    parent.bind("<Escape>", lambda e: parent.destroy())
