# Modules
import config
from config import G

# Libraries
import customtkinter as tk
from tkinter import filedialog


def browse(text_widget):
    file_path = filedialog.askopenfilename()
    text_widget.delete(0, tk.END)
    text_widget.insert(0, file_path)


def make_frame():
    frame = tk.CTkFrame(config.app, fg_color="transparent")
    frame.grid(row=config.frame_number, column=0, padx=0, pady=0, sticky="ew")
    config.frame_number += 1
    return frame


def make_label(frame, col, text, sticky="w"):
    label = tk.CTkLabel(frame, text=f"{text}:", font=config.font)
    label.grid(row=0, column=col, padx=config.padx, pady=config.pady, sticky=sticky)
    return label


def make_text(frame, col, value="", width=None, sticky="w", placeholder=""):
    w = width if width else config.text_width
    widget = tk.CTkEntry(frame, placeholder_text=placeholder, font=config.font, width=w)
    widget.grid(row=0, column=col, padx=config.padx, pady=config.pady, sticky=sticky)

    if value:
        widget.insert(0, value)

    return widget


def make_button(frame, col, text, command, color="grey", text_color=None, hover_color=None, sticky="w"):
    widget = tk.CTkButton(frame, text=text, command=command, font=config.font,
                          fg_color=color, text_color=text_color, hover_color=hover_color, )

    widget.grid(row=0, column=col, padx=config.padx, pady=config.pady, sticky=sticky)
    return widget


def make_select(frame, col, values=None, sticky="w"):
    v = values if values else ["empty"]
    widget = tk.CTkComboBox(frame, values=v, state="readonly", width=config.select_width, font=config.font)
    widget.grid(row=0, column=col, padx=config.padx, pady=config.pady, sticky=sticky)
    return widget


def make_checkbox(frame, col, sticky="w"):
    widget = tk.CTkCheckBox(frame, font=config.font, text="", onvalue=True, offvalue=False, width=1)
    widget.grid(row=0, column=col, padx=config.padx, pady=config.pady, sticky=sticky)
    return widget


def fill_widgets():
    for key in G:
        value = G[key]["default"]
        set_widget(G[key]["widget"], value, G[key]["type"], G[key].get("choices"))


def set_widget(widget, value, wtype, extra):
    if wtype == "text":
        set_text(widget, value)
    elif wtype == "checkbox":
        set_checkbox(widget, value)
    elif wtype == "select":
        set_select(widget, value, extra)


def set_text(widget, value):
    if not value:
        return

    if isinstance(value, list):
        value = ",".join(map(str, value))
    else:
        value = str(value)

    widget.delete(0, "end")
    widget.insert(0, value)


def set_checkbox(widget, value):
    if value:
        widget.select()
    else:
        widget.deselect()


def set_select(widget, value, extra):
    if extra:
        widget.configure(values=extra)

    widget.set(value)
