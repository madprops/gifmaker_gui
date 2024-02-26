# Modules
import config
from config import G
import widgets as w
import render

# Libraries
import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

app = tk.CTk()
app.geometry(f"{config.width}x{config.height}")
app.grid_columnconfigure(0, weight=1)
config.prepare(app)


# ---


def frame_input():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, 0, col, "Input")
    col += 1

    G.input_path = w.make_entry(frame, 0, col, placeholder="Path to a file", sticky="ew")
    col += 1

    w.make_button(frame, 0, col, "Browse", lambda: w.browse(G.input_path))
    col += 1

    w.make_button(frame, 0, col, "Render", lambda: render.render(),
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
