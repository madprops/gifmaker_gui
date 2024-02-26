# Modules
import config

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


def make_label(frame, row, col, text, sticky="w"):
    label = tk.CTkLabel(frame, text=f"{text}:", font=config.font)
    label.grid(row=row, column=col, padx=config.padx, pady=config.pady, sticky=sticky)
    return label


def make_entry(frame, row, col, value="", width=config.entry_width, sticky="w", placeholder=""):
    entry = tk.CTkEntry(frame, placeholder_text=placeholder, font=config.font, width=width)
    entry.grid(row=row, column=col, padx=config.padx, pady=config.pady, sticky=sticky)

    if value:
        entry.insert(0, value)

    return entry


def make_button(frame, row, col, text, command, color="grey", text_color=None, hover_color=None, sticky="w"):
    button = tk.CTkButton(frame, text=text, command=command, font=config.font,
                          fg_color=color, text_color=text_color, hover_color=hover_color, )

    button.grid(row=row, column=col, padx=config.padx, pady=config.pady, sticky=sticky)
    return button


def make_select(frame, row, col, values, sticky="w"):
    select = tk.CTkComboBox(frame, values=values, state="readonly", width=100, font=config.font)
    select.set(values[0])
    select.grid(row=row, column=col, padx=config.padx, pady=config.pady, sticky=sticky)
    return select
