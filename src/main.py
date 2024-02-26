# Modules
import config
import widgets as w

# Libraries
import customtkinter as tk
from tkinter import filedialog

# Standard
import subprocess
import sys

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

app = tk.CTk()
app.geometry(f"{config.width}x{config.height}")
app.grid_columnconfigure(0, weight=1)
config.prepare(app)

# GLOBALS

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

# ---


def render():
    if not input_path.get():
        msg("No input file")
        return

    command = ["gifmaker"]

    def add_arg(var, flag):
        value = var.get()

        if value:
            command.extend([f"--{flag}", value])

    add_arg(input_path, "input")
    add_arg(words, "words")
    add_arg(font_name, "font")
    add_arg(font_size, "fontsize")
    add_arg(font_color, "fontcolor")
    add_arg(top, "top")
    add_arg(bottom, "bottom")
    add_arg(left, "left")
    add_arg(right, "right")
    add_arg(bgcolor, "bgcolor")
    add_arg(opacity, "opacity")
    add_arg(padding, "padding")
    add_arg(radius, "radius")
    add_arg(delay, "delay")
    add_arg(filter_name, "filter")
    add_arg(frames, "frames")
    add_arg(outline, "outline")
    add_arg(output_path, "output")
    add_arg(format_name, "format")

    msg("Running Gifmaker")
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print("Command executed successfully")
        print("Standard Output:")
        print(result.stdout)
    else:
        print(f"Command failed with return code: {result.returncode}")
        print("Standard Error:")
        print(result.stderr)


def browse(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)


def text(widget, value):
    widget.insert(0, value)


def msg(message: str) -> None:
    print(message, file=sys.stderr)

# ---


def frame_input():
    global input_path
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, 0, col, "Input")
    col += 1

    input_path = w.make_entry(frame, 0, col, "Path to a file", sticky="ew")
    col += 1

    w.make_button(frame, 0, col, "Browse", lambda: browse(input_path))
    col += 1

    w.make_button(frame, 0, col, "Render", lambda: render(),
                  color="lightblue", text_color="black", hover_color=("blue", "white"))
    col += 1


def frame_font():
    global font_name, font_size, font_color, bgcolor
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Font")
    col += 1

    font_name = w.make_entry(frame, 0, col, "")
    text(font_name, "sans")
    col += 1

    w.make_label(frame, 0, col, "Font Size")
    col += 1

    font_size = w.make_entry(frame, 0, col, "")
    text(font_size, 50)
    col += 1

    w.make_label(frame, 0, col, "Font Color")
    col += 1

    font_color = w.make_entry(frame, 0, col, "")
    text(font_color, "white")
    col += 1

    w.make_label(frame, 0, col, "Background")
    col += 1

    bgcolor = w.make_entry(frame, 0, col, "")
    text(font_name, "")
    col += 1


def frame_decorations():
    global opacity, padding, radius, outline
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Outline")
    col += 1

    outline = w.make_entry(frame, 0, col, "")
    text(font_name, "")
    col += 1

    w.make_label(frame, 0, col, "Opacity")
    col += 1

    opacity = w.make_entry(frame, 0, col, "")
    text(font_name, "")
    col += 1

    w.make_label(frame, 0, col, "Padding")
    col += 1

    padding = w.make_entry(frame, 0, col, "")
    text(font_name, "")
    col += 1

    w.make_label(frame, 0, col, "Radius")
    col += 1

    radius = w.make_entry(frame, 0, col, "")
    text(font_name, "")
    col += 1


def frame_words():
    global words
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, 0, col, "Words")
    col += 1

    words = w.make_entry(frame, 0, col, "Words to put on the frames", sticky="ew")
    col += 1


def frame_position():
    global top, bottom, left, right
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Top")
    col += 1

    top = w.make_entry(frame, 0, col, "")
    col += 1

    w.make_label(frame, 0, col, "Bottom")
    col += 1

    bottom = w.make_entry(frame, 0, col, "")
    col += 1

    w.make_label(frame, 0, col, "Left")
    col += 1

    left = w.make_entry(frame, 0, col, "")
    col += 1

    w.make_label(frame, 0, col, "Right")
    col += 1

    right = w.make_entry(frame, 0, col, "")
    col += 1


def frame_frames():
    global filter_name, delay, frames
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Delay")
    col += 1

    delay = w.make_entry(frame, 0, col, "")
    col += 1

    w.make_label(frame, 0, col, "Frames")
    col += 1

    frames = w.make_entry(frame, 0, col, "")
    col += 1

    w.make_label(frame, 0, col, "Filter")
    col += 1

    filter_name = w.make_entry(frame, 0, col, "")
    col += 1


def frame_output():
    global output_path, format_name
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, 0, col, "Output")
    col += 1

    output_path = w.make_entry(frame, 0, col, "", sticky="ew")
    col += 1

    w.make_label(frame, 0, col, "Format")
    col += 1

    format_name = w.make_entry(frame, 0, col, "")
    col += 1


frame_input()
frame_words()
frame_position()
frame_font()
frame_decorations()
frame_frames()
frame_output()

app.mainloop()
