# Libraries
import customtkinter as tk

app = None
width = 820
height = 600

padx = 8
pady = 8

font_size = 16
font_family = "sans"
entry_width = 90
select_width = 110

font = None
frame_number = 0


def prepare():
    global app, font

    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("green")
    app = tk.CTk()
    app.geometry(f"{width}x{height}")
    app.grid_columnconfigure(0, weight=1)
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
    fill_words = None
    fill_gen = None
    deep_fry = None
    vertical = None
    horizontal = None
    descender = None
    outline_top = None
    outline_bottom = None
    outline_left = None
    outline_right = None
