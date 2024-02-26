# Libraries
import customtkinter as tk

app = None
width = 800
height = 400

padx = 8
pady = 8

font_size = 16
font_family = "sans"
entry_width = 90

font = None
frame_number = 0


def prepare(app_o):
    global app, font

    app = app_o
    font = tk.CTkFont(family=font_family, size=font_size)
