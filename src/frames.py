# Modules
import widgets as w
import render
from framedata import FrameData
import action


def get_d() -> FrameData:
    return FrameData(w.make_frame(), 0)


def frame_input() -> None:
    d = get_d()
    d.frame.grid_columnconfigure(1, weight=1)
    w.add("input", d)
    w.make_button(d, "Menu", lambda: action.action_button()),
    w.make_button(d, "Render", lambda: render.render(),
                  color="lightblue", text_color="black", hover_color=("blue", "white"))


def frame_font() -> None:
    d = get_d()
    w.add("font", d)
    w.add("fontsize", d)
    w.add("fontcolor", d)
    w.add("bgcolor", d)


def frame_decorations() -> None:
    d = get_d()
    w.add("outline", d)
    w.add("delay", d)
    w.add("opacity", d)
    w.add("padding", d)
    w.add("radius", d)


def frame_words() -> None:
    d = get_d()
    d.frame.grid_columnconfigure(1, weight=1)
    w.add("words", d)
    w.add("separator", d)


def frame_position() -> None:
    d = get_d()
    w.add("top", d)
    w.add("bottom", d)
    w.add("left", d)
    w.add("right", d)
    w.add("width", d)
    w.add("height", d)


def frame_frames() -> None:
    d = get_d()
    w.add("frames", d)
    w.add("filter", d)
    w.add("filterlist", d)
    w.add("filteropts", d)


def frame_output() -> None:
    d = get_d()
    d.frame.grid_columnconfigure(1, weight=1)
    w.add("output", d)
    w.add("format", d)


def frame_checkboxes() -> None:
    d = get_d()
    w.add("fillwords", d)
    w.add("fillgen", d)
    w.add("descender", d)
    w.add("deepfry", d)
    w.add("vertical", d)
    w.add("horizontal", d)


def frame_outline() -> None:
    d = get_d()
    w.add("outlinewidth", d)
    w.add("no_outline_top", d)
    w.add("no_outline_bottom", d)
    w.add("no_outline_left", d)
    w.add("no_outline_right", d)


def frame_seeds() -> None:
    d = get_d()
    w.add("seed", d)
    w.add("frameseed", d)
    w.add("wordseed", d)
    w.add("filterseed", d)
    w.add("colorseed", d)


def frame_opts() -> None:
    d = get_d()
    w.add("framelist", d)
    w.add("frameopts", d)
    w.add("repeatrandom", d)
    w.add("repeatfilter", d)


def frame_someboxes() -> None:
    d = get_d()
    w.add("wrap", d)
    w.add("nowrap", d)
    w.add("nogrow", d)
    w.add("randomlist", d)


def frame_files() -> None:
    d = get_d()
    w.add("script", d)
    w.add("randomfile", d)
    w.add("wordfile", d)


def frame_stuff() -> None:
    d = get_d()
    w.add("align", d)
    w.add("remake", d)
    w.add("loop", d)
    w.add("order", d)
