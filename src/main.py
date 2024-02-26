# Modules
import config
from config import G
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


def render():
    command = ["gifmaker"]

    def add_arg(var, flag):
        value = var.get()

        if value:
            command.extend([f"--{flag}", value])

    add_arg(G.input_path, "input")
    add_arg(G.words, "words")
    add_arg(G.font_name, "font")
    add_arg(G.font_size, "fontsize")
    add_arg(G.font_color, "fontcolor")
    add_arg(G.top, "top")
    add_arg(G.bottom, "bottom")
    add_arg(G.left, "left")
    add_arg(G.right, "right")
    add_arg(G.bgcolor, "bgcolor")
    add_arg(G.opacity, "opacity")
    add_arg(G.padding, "padding")
    add_arg(G.radius, "radius")
    add_arg(G.delay, "delay")
    add_arg(G.filter_name, "filter")
    add_arg(G.frames, "frames")
    add_arg(G.outline, "outline")
    add_arg(G.output_path, "output")
    add_arg(G.format_name, "format")

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


def msg(message: str) -> None:
    print(message, file=sys.stderr)

# ---


def frame_input():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, 0, col, "Input")
    col += 1

    G.input_path = w.make_entry(frame, 0, col, placeholder="Path to a file", sticky="ew")
    col += 1

    w.make_button(frame, 0, col, "Browse", lambda: browse(input_path))
    col += 1

    w.make_button(frame, 0, col, "Render", lambda: render(),
                  color="lightblue", text_color="black", hover_color=("blue", "white"))
    col += 1


def frame_font():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Font")
    col += 1

    G.font_name = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Font Size")
    col += 1

    G.font_size = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Font Color")
    col += 1

    G.font_color = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Background")
    col += 1

    G.bgcolor = w.make_entry(frame, 0, col)
    col += 1


def frame_decorations():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Outline")
    col += 1

    G.outline = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Opacity")
    col += 1

    G.opacity = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Padding")
    col += 1

    G.padding = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Radius")
    col += 1

    G.radius = w.make_entry(frame, 0, col)
    col += 1


def frame_words():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, 0, col, "Words")
    col += 1

    G.words = w.make_entry(frame, 0, col, placeholder="Words to put on the frames", sticky="ew")
    col += 1


def frame_position():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Top")
    col += 1

    G.top = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Bottom")
    col += 1

    G.bottom = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Left")
    col += 1

    G.left = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Right")
    col += 1

    G.right = w.make_entry(frame, 0, col)
    col += 1


def frame_frames():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Delay")
    col += 1

    G.delay = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Frames")
    col += 1

    G.frames = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Filter")
    col += 1

    G.filter_name = w.make_entry(frame, 0, col)
    col += 1


def frame_output():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, 0, col, "Output")
    col += 1

    G.output_path = w.make_entry(frame, 0, col, sticky="ew")
    col += 1

    w.make_label(frame, 0, col, "Format")
    col += 1

    G.format_name = w.make_entry(frame, 0, col)
    col += 1


frame_input()
frame_words()
frame_position()
frame_font()
frame_decorations()
frame_frames()
frame_output()

app.mainloop()
