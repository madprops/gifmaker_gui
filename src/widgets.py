# Modules
import config
from config import G

# Libraries
import customtkinter as tk
from tkinter import filedialog


def browse(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)


def make_frame():
    frame = tk.CTkFrame(config.app, fg_color="transparent")
    frame.grid(row=config.frame_number, column=0, padx=0, pady=0, sticky="ew")
    config.frame_number += 1
    return frame


def make_label(frame, col, text, sticky="w"):
    label = tk.CTkLabel(frame, text=f"{text}:", font=config.font)
    label.grid(row=0, column=col, padx=config.padx, pady=config.pady, sticky=sticky)
    return label


def make_entry(frame, col, value="", width=None, sticky="w", placeholder=""):
    w = width if width else config.entry_width
    entry = tk.CTkEntry(frame, placeholder_text=placeholder, font=config.font, width=w)
    entry.grid(row=0, column=col, padx=config.padx, pady=config.pady, sticky=sticky)

    if value:
        entry.insert(0, value)

    return entry


def make_button(frame, col, text, command, color="grey", text_color=None, hover_color=None, sticky="w"):
    button = tk.CTkButton(frame, text=text, command=command, font=config.font,
                          fg_color=color, text_color=text_color, hover_color=hover_color, )

    button.grid(row=0, column=col, padx=config.padx, pady=config.pady, sticky=sticky)
    return button


def make_select(frame, col, values, sticky="w"):
    select = tk.CTkComboBox(frame, values=values, state="readonly", width=config.select_width, font=config.font)
    select.set(values[0])
    select.grid(row=0, column=col, padx=config.padx, pady=config.pady, sticky=sticky)
    return select


def make_checkbox(frame, col, sticky="w"):
    checkbox = tk.CTkCheckBox(frame, font=config.font, text="", onvalue=True, offvalue=False, width=1)
    checkbox.grid(row=0, column=col, padx=config.padx, pady=config.pady, sticky=sticky)
    return checkbox


def fill_widgets():
    for key in G:
        value = G[key]["default"]

        if G[key].get("reverse"):
            value = not value

        set_widget(G[key]["widget"], value, G[key]["type"], G[key].get("choices"))


def set_widget(widget, value, wtype, extra):
    if wtype == "entry":
        set_entry(widget, value)
    elif wtype == "checkbox":
        set_checkbox(widget, value)
    elif wtype == "select":
        set_select(widget, value, extra)


def set_entry(widget, value):
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
