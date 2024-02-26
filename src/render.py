# Modules
from config import G
import utils

# Standard
import subprocess


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

    utils.msg("Running Gifmaker")
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print("Command executed successfully")
        print("Standard Output:")
        print(result.stdout)
    else:
        print(f"Command failed with return code: {result.returncode}")
        print("Standard Error:")
        print(result.stderr)
