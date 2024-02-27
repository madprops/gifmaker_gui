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
text_width = 60
select_width = 110
bigger_width = 110
path_width = 150

font = None
frame_number = 0

args = {
    "input": {"label": "Input", "type": "text", "sticky": "ew", "placeholder": "Path to a file (gif, webm, mp4, jpg, png)"},
    "output": {"label": "Output", "type": "text", "sticky": "ew", "placeholder": "You can leave it empty to save in the default directory"},
    "words": {"label": "Words", "type": "text", "sticky": "ew", "placeholder": "Words to put on the frames. Separate frames with semicolons. Keywords include [random]"},
    "font": {"label": "Font", "type": "text"},
    "fontsize": {"label": "Font Size", "type": "text"},
    "fontcolor": {"label": "Font Color", "type": "text", "width": bigger_width},
    "top": {"label": "Top", "type": "text"},
    "bottom": {"label": "Bottom", "type": "text"},
    "left": {"label": "Left", "type": "text"},
    "right": {"label": "Right", "type": "text"},
    "bgcolor": {"label": "BG Color", "type": "text", "width": bigger_width},
    "opacity": {"label": "Opacity", "type": "text"},
    "padding": {"label": "Padding", "type": "text"},
    "radius": {"label": "Radius", "type": "text"},
    "delay": {"label": "Delay", "type": "text"},
    "filter": {"label": "Filter", "type": "select"},
    "frames": {"label": "Frames", "type": "text"},
    "outline": {"label": "Outline", "type": "text"},
    "format": {"label": "Format", "type": "select"},
    "fillwords": {"label": "Fill Words", "type": "checkbox"},
    "fillgen": {"label": "Fill Gen", "type": "checkbox"},
    "deepfry": {"label": "Deep Fry", "type": "checkbox"},
    "vertical": {"label": "Vertical", "type": "checkbox"},
    "horizontal": {"label": "Horizontal", "type": "checkbox"},
    "descender": {"label": "Descender", "type": "checkbox"},
    "outlinewidth": {"label": "OL Width", "type": "text"},
    "no_outline_top": {"label": "No OL Top", "type": "checkbox"},
    "no_outline_bottom": {"label": "No OL Bottom", "type": "checkbox"},
    "no_outline_left": {"label": "No OL Left", "type": "checkbox"},
    "no_outline_right": {"label": "No OL Right", "type": "checkbox"},
    "seed": {"label": "Seed", "type": "text"},
    "frameseed": {"label": "Frame Seed", "type": "text"},
    "filterseed": {"label": "Filter Seed", "type": "text"},
    "wordseed": {"label": "Word Seed", "type": "text"},
    "framelist": {"label": "Frame List", "type": "text"},
    "frameopts": {"label": "Frame Opts", "type": "text", "width": bigger_width},
    "repeatrandom": {"label": "Repeat Random", "type": "checkbox"},
    "repeatfilter": {"label": "Repeat Filter", "type": "checkbox"},
    "wrap": {"label": "Wrap", "type": "text"},
    "nowrap": {"label": "No Wrap", "type": "checkbox"},
    "nogrow": {"label": "No Grow", "type": "checkbox"},
    "script": {"label": "Script", "type": "text", "width": path_width},
    "randomfile": {"label": "Random File", "type": "text", "width": path_width},
    "wordfile": {"label": "Word File", "type": "text", "width": path_width},
    "loop": {"label": "Loop", "type": "text"},
    "remake": {"label": "Remake", "type": "checkbox"},
    "align": {"label": "Align", "type": "select"},
    "width": {"label": "Width", "type": "text"},
    "height": {"label": "Height", "type": "text"},
    "separator": {"label": "Separator", "type": "text"},
    "order": {"label": "Order", "type": "select"},
    "randomlist": {"label": "Random List", "type": "text", "width": path_width},
    "filteropts": {"label": "Filter Opts", "type": "text", "width": bigger_width},
    "filterlist": {"label": "Filter List", "type": "text", "width": bigger_width},
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

        for key in args:
            args[key]["default"] = defaults[key]
            choices_key = f"_choices_{key}"

            if choices_key in defaults:
                args[key]["choices"] = defaults[choices_key]
    else:
        utils.msg("Error", result.stderr)
        return
