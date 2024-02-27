# Modules
import utils

# Libraries
import customtkinter as tk

# Standard
import json
import subprocess

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

G = {
    "input_path": {"name": "input"},
    "words": {"name": "words"},
    "font_name": {"name": "font"},
    "font_size": {"name": "fontsize"},
    "font_color": {"name": "fontcolor"},
    "top": {"name": "top"},
    "bottom": {"name": "bottom"},
    "left": {"name": "left"},
    "right": {"name": "right"},
    "bgcolor": {"name": "bgcolor"},
    "opacity": {"name": "opacity"},
    "padding": {"name": "padding"},
    "radius": {"name": "radius"},
    "delay": {"name": "delay"},
    "filter_name": {"name": "filter"},
    "frames": {"name": "frames"},
    "outline": {"name": "outline"},
    "output_path": {"name": "output"},
    "format_name": {"name": "format"},
    "fill_words": {"name": "fillwords"},
    "fill_gen": {"name": "fillgen"},
    "deep_fry": {"name": "deepfry"},
    "vertical": {"name": "vertical"},
    "horizontal": {"name": "horizontal"},
    "descender": {"name": "descender"},
    "outline_top": {"name": "no_outline_top", "reverse": True},
    "outline_bottom": {"name": "no_outline_bottom", "reverse": True},
    "outline_left": {"name": "no_outline_left", "reverse": True},
    "outline_right": {"name": "no_outline_right", "reverse": True},
}


def prepare():
    global app, font, defaults

    command = ["gifmaker", "--mode", "defaults"]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        defaults = json.loads(result.stdout)

        for key in G:
            G[key]["default"] = defaults[G[key]["name"]]
    else:
        utils.msg("Error", result.stderr)
        return

    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("green")
    app = tk.CTk()
    app.geometry(f"{width}x{height}")
    app.grid_columnconfigure(0, weight=1)
    font = tk.CTkFont(family=font_family, size=font_size)
