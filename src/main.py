import customtkinter as tk
from tkinter import filedialog
import subprocess, sys

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

width = 800
height = 400
padx = 8
pady = 8

font_size = 16
font_family = "sans"
entry_width = 90

app = tk.CTk()
app.geometry(f"{width}x{height}")
app.grid_columnconfigure(0, weight=1)
font = tk.CTkFont(family=font_family, size=font_size)
frame_number = 0

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
outline = None
delay = None
filter_name = None
frames = None
outline = None

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

def make_frame():
    global frame_number
    frame = tk.CTkFrame(app, fg_color="transparent")
    frame.grid(row=frame_number, column=0, padx=0, pady=0, sticky="ew")
    frame_number += 1
    return frame

def make_label(frame, row, col, text, sticky="w"):
    label = tk.CTkLabel(frame, text=f"{text}:", font=font)
    label.grid(row=row, column=col, padx=padx, pady=pady, sticky=sticky)
    return label

def make_entry(frame, row, col, placeholder, width=entry_width, sticky="w"):
    entry = tk.CTkEntry(frame, placeholder_text=placeholder, font=font, width=width)
    entry.grid(row=row, column=col, padx=padx, pady=pady, sticky=sticky)
    return entry

def make_button(frame, row, col, text, command, color="grey", text_color=None, hover_color=None, sticky="w"):
    button = tk.CTkButton(frame, text=text, command=command, font=font, \
        fg_color=color, text_color=text_color, hover_color=hover_color, )

    button.grid(row=row, column=col, padx=padx, pady=pady, sticky=sticky)
    return button

def make_select(frame, row, col, values, sticky="w"):
    select = tk.CTkComboBox(frame, values=values, state="readonly", width=100, font=font)
    select.set(values[0])
    select.grid(row=row, column=col, padx=padx, pady=pady, sticky=sticky)
    return select

# ---

def frame_input():
    global input_path
    frame = make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    make_label(frame, 0, col, "Input")
    col += 1

    input_path = make_entry(frame, 0, col, "Path to a file", sticky="ew")
    col += 1

    make_button(frame, 0, col, "Browse", lambda: browse(input_path))
    col += 1

    make_button(frame, 0, col, "Render", lambda: render(), \
        color="lightblue", text_color="black", hover_color=("blue", "white"))
    col += 1

def frame_font():
    global font_name, font_size, font_color, bgcolor
    frame = make_frame()
    col = 0

    make_label(frame, 0, col, "Font")
    col += 1

    font_name = make_entry(frame, 0, col, "")
    text(font_name, "sans")
    col += 1

    make_label(frame, 0, col, "Font Size")
    col += 1

    font_size = make_entry(frame, 0, col, "")
    text(font_size, 50)
    col += 1

    make_label(frame, 0, col, "Font Color")
    col += 1

    font_color = make_entry(frame, 0, col, "")
    text(font_color, "white")
    col += 1

    make_label(frame, 0, col, "Background")
    col += 1

    bgcolor = make_entry(frame, 0, col, "")
    text(font_name, "")
    col += 1

def frame_decorations():
    global opacity, padding, radius, outline
    frame = make_frame()
    col = 0

    make_label(frame, 0, col, "Outline")
    col += 1

    outline = make_entry(frame, 0, col, "")
    text(font_name, "")
    col += 1

    make_label(frame, 0, col, "Opacity")
    col += 1

    opacity = make_entry(frame, 0, col, "")
    text(font_name, "")
    col += 1

    make_label(frame, 0, col, "Padding")
    col += 1

    padding = make_entry(frame, 0, col, "")
    text(font_name, "")
    col += 1

    make_label(frame, 0, col, "Radius")
    col += 1

    radius = make_entry(frame, 0, col, "")
    text(font_name, "")
    col += 1

def frame_words():
    global words
    frame = make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    make_label(frame, 0, col, "Words")
    col += 1

    words = make_entry(frame, 0, col, "Words to put on the frames", sticky="ew")
    col += 1

def frame_position():
    global top, bottom, left, right
    frame = make_frame()
    col = 0

    make_label(frame, 0, col, "Top")
    col += 1

    top = make_entry(frame, 0, col, "")
    col += 1

    make_label(frame, 0, col, "Bottom")
    col += 1

    bottom = make_entry(frame, 0, col, "")
    col += 1

    make_label(frame, 0, col, "Left")
    col += 1

    left = make_entry(frame, 0, col, "")
    col += 1

    make_label(frame, 0, col, "Right")
    col += 1

    right = make_entry(frame, 0, col, "")
    col += 1

def frame_frames():
    global filter_name, delay, frames
    frame = make_frame()
    col = 0

    make_label(frame, 0, col, "Delay")
    col += 1

    delay = make_entry(frame, 0, col, "")
    col += 1

    make_label(frame, 0, col, "Frames")
    col += 1

    frames = make_entry(frame, 0, col, "")
    col += 1

    make_label(frame, 0, col, "Filter")
    col += 1

    filter_name = make_entry(frame, 0, col, "")
    col += 1

frame_input()
frame_words()
frame_position()
frame_font()
frame_decorations()
frame_frames()

app.mainloop()