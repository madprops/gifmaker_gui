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

padx = 6
pady = 10

font_size = 16
font_family = "sans"
entry_width = 60
select_width = 110
bigger_width = 110

font = None
frame_number = 0

G = {
    "input_path": {"type": "entry", "name": "input"},
    "words": {"type": "entry", "name": "words"},
    "font_name": {"type": "entry", "name": "font"},
    "font_size": {"type": "entry", "name": "fontsize"},
    "font_color": {"type": "entry", "name": "fontcolor"},
    "top": {"type": "entry", "name": "top"},
    "bottom": {"type": "entry", "name": "bottom"},
    "left": {"type": "entry", "name": "left"},
    "right": {"type": "entry", "name": "right"},
    "bgcolor": {"type": "entry", "name": "bgcolor"},
    "opacity": {"type": "entry", "name": "opacity"},
    "padding": {"type": "entry", "name": "padding"},
    "radius": {"type": "entry", "name": "radius"},
    "delay": {"type": "entry", "name": "delay"},
    "filter_name": {"type": "select", "name": "filter"},
    "frames": {"type": "entry", "name": "frames"},
    "outline": {"type": "entry", "name": "outline"},
    "output_path": {"type": "entry", "name": "output"},
    "format_name": {"type": "select", "name": "format"},
    "fill_words": {"type": "checkbox", "name": "fillwords"},
    "fill_gen": {"type": "checkbox", "name": "fillgen"},
    "deep_fry": {"type": "checkbox", "name": "deepfry"},
    "vertical": {"type": "checkbox", "name": "vertical"},
    "horizontal": {"type": "checkbox", "name": "horizontal"},
    "descender": {"type": "checkbox", "name": "descender"},
    "outline_top": {"type": "checkbox", "name": "no_outline_top", "reverse": True},
    "outline_bottom": {"type": "checkbox", "name": "no_outline_bottom", "reverse": True},
    "outline_left": {"type": "checkbox", "name": "no_outline_left", "reverse": True},
    "outline_right": {"type": "checkbox", "name": "no_outline_right", "reverse": True},
}


def prepare():
    global app, font
    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("green")
    app = tk.CTk()
    app.geometry(f"{width}x{height}")
    app.grid_columnconfigure(0, weight=1)
    font = tk.CTkFont(family=font_family, size=font_size)
    get_defaults()


def get_defaults():
    command = ["gifmaker", "--mode", "defaults"]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        defaults = json.loads(result.stdout)

        for key in G:
            name = G[key]["name"]
            G[key]["default"] = defaults[name]
            choices_key = f"_choices_{name}"

            if choices_key in defaults:
                G[key]["choices"] = defaults[choices_key]
    else:
        utils.msg("Error", result.stderr)
        return
