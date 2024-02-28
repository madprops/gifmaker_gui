# Modules
import utils

# Libraries
import customtkinter as ctk  # type: ignore

# Standard
import json
import subprocess
from typing import Dict, Any
from pathlib import Path

app: ctk.CTkFrame = None
width = 960
height = 730

padx = 6
pady = 10
frame_padx = 16
frame_pady = 1

font_size = 16
font_family = "mono"
text_width = 60
select_width = 110
bigger_width = 110
path_width = 150
dialog_color = "#252933"

font = None
frame_number = 0
root = None

args: Dict[str, Any] = {
    "input": {"label": "Input ", "type": "text", "sticky": "ew", "placeholder": "Path to a file (gif, webm, mp4, jpg, png)"},
    "output": {"label": "Output", "type": "text", "sticky": "ew", "placeholder": "You can leave it empty to save in the default directory"},
    "words": {"label": "Words ", "type": "text", "sticky": "ew", "placeholder": "Words to put on the frames | [random] [number] [repeat]"},
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
    "colorseed": {"label": "Color Seed", "type": "text"},
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


def prepare(main_file) -> None:
    global app, font, root
    root = Path(main_file).parent.parent
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    app = ctk.CTk()
    app.geometry(f"{width}x{height}")
    app.grid_columnconfigure(0, weight=1)
    font = ctk.CTkFont(family=font_family, size=font_size)
    get_defaults()


def get_defaults() -> None:
    command = ["gifmaker", "--arguments"]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        arguments = json.loads(result.stdout)

        for key in args:
            args[key]["default"] = arguments[key]["value"]
            args[key]["choices"] = arguments[key].get("choices")
            args[key]["help"] = arguments[key]["help"]
    else:
        utils.msg(result.stderr)
        return
