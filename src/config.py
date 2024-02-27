# Modules
import utils

# Libraries
import customtkinter as tk

# Standard
import json
import subprocess

app = None
width = 820
height = 720

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
    "input_path": {"name": "input", "type": "entry"},
    "words": {"name": "words", "type": "entry"},
    "font_name": {"name": "font", "type": "entry"},
    "font_size": {"name": "fontsize", "type": "entry"},
    "font_color": {"name": "fontcolor", "type": "entry"},
    "top": {"name": "top", "type": "entry"},
    "bottom": {"name": "bottom", "type": "entry"},
    "left": {"name": "left", "type": "entry"},
    "right": {"name": "right", "type": "entry"},
    "bgcolor": {"name": "bgcolor", "type": "entry"},
    "opacity": {"name": "opacity", "type": "entry"},
    "padding": {"name": "padding", "type": "entry"},
    "radius": {"name": "radius", "type": "entry"},
    "delay": {"name": "delay", "type": "entry"},
    "filter_name": {"name": "filter", "type": "select"},
    "frames": {"name": "frames", "type": "entry"},
    "outline": {"name": "outline", "type": "entry"},
    "output_path": {"name": "output", "type": "entry"},
    "format_name": {"name": "format", "type": "select"},
    "fill_words": {"name": "fillwords", "type": "checkbox"},
    "fill_gen": {"name": "fillgen", "type": "checkbox"},
    "deep_fry": {"name": "deepfry", "type": "checkbox"},
    "vertical": {"name": "vertical", "type": "checkbox"},
    "horizontal": {"name": "horizontal", "type": "checkbox"},
    "descender": {"name": "descender", "type": "checkbox"},
    "outline_width": {"name": "outlinewidth", "type": "entry"},
    "outline_top": {"name": "no_outline_top", "type": "checkbox", "reverse": True},
    "outline_bottom": {"name": "no_outline_bottom", "type": "checkbox", "reverse": True},
    "outline_left": {"name": "no_outline_left", "type": "checkbox", "reverse": True},
    "outline_right": {"name": "no_outline_right", "type": "checkbox", "reverse": True},
    "seed": {"name": "seed", "type": "entry"},
    "frame_seed": {"name": "frameseed", "type": "entry"},
    "filter_seed": {"name": "filterseed", "type": "entry"},
    "word_seed": {"name": "wordseed", "type": "entry"},
    "framelist": {"name": "framelist", "type": "entry"},
    "frameopts": {"name": "frameopts", "type": "entry"},
    "repeat_random": {"name": "repeatrandom", "type": "checkbox"},
    "repeat_filter": {"name": "repeatfilter", "type": "checkbox"},
    "wrap": {"name": "wrap", "type": "entry"},
    "nowrap": {"name": "nowrap", "type": "checkbox"},
    "nogrow": {"name": "nogrow", "type": "checkbox"}
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
