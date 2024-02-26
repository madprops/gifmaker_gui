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


class G:
    input_path = None
    words = None
    font_name = None
    font_size = None
    font_color = None
    top = None
    bottom = None
    left = None
    right = None
    bgcolor = None
    opacity = None
    padding = None
    radius = None
    delay = None
    filter_name = None
    frames = None
    outline = None
    output_path = None
    format_name = None
