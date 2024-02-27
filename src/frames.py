from config import args
import widgets as w
import render


def frame_input():
    d = {"frame": w.make_frame(), "col": 0}
    d["frame"].grid_columnconfigure(1, weight=1)

    w.add("input", d)

    w.make_button(d, "Browse", lambda: w.browse(args["input_path"]["widget"]))

    w.make_button(d, "Render", lambda: render.render(),
                  color="lightblue", text_color="black", hover_color=("blue", "white"))


def frame_font():
    d = {"frame": w.make_frame(), "col": 0}

    w.add("font", d)
    w.add("fontsize", d)
    w.add("fontcolor", d)
    w.add("bgcolor", d)


def frame_decorations():
    d = {"frame": w.make_frame(), "col": 0}

    w.add("outline", d)
    w.add("delay", d)
    w.add("opacity", d)
    w.add("padding", d)
    w.add("radius", d)


def frame_words():
    d = {"frame": w.make_frame(), "col": 0}
    d["frame"].grid_columnconfigure(1, weight=1)

    w.add("words", d)


def frame_position():
    d = {"frame": w.make_frame(), "col": 0}

    w.add("top", d)
    w.add("bottom", d)
    w.add("left", d)
    w.add("right", d)
    w.add("width", d)
    w.add("height", d)


def frame_frames():
    d = {"frame": w.make_frame(), "col": 0}

    w.add("frames", d)
    w.add("filter", d)
    w.add("filterlist", d)
    w.add("filteropts", d)


def frame_output():
    d = {"frame": w.make_frame(), "col": 0}
    d["frame"].grid_columnconfigure(1, weight=1)

    w.add("output", d)
    w.add("format", d)


def frame_checkboxes():
    d = {"frame": w.make_frame(), "col": 0}

    w.add("fillwords", d)
    w.add("fillgen", d)
    w.add("descender", d)
    w.add("deepfry", d)
    w.add("vertical", d)
    w.add("horizontal", d)


def frame_outline():
    d = {"frame": w.make_frame(), "col": 0}

    w.add("outlinewidth", d)
    w.add("no_outline_top", d)
    w.add("no_outline_bottom", d)
    w.add("no_outline_left", d)
    w.add("no_outline_right", d)


def frame_seeds():
    d = {"frame": w.make_frame(), "col": 0}

    w.add("seed", d)
    w.add("frameseed", d)
    w.add("wordseed", d)
    w.add("filterseed", d)


def frame_opts():
    d = {"frame": w.make_frame(), "col": 0}

    w.add("framelist", d)
    w.add("frameopts", d)
    w.add("repeatrandom", d)
    w.add("repeatfilter", d)


def frame_someboxes():
    d = {"frame": w.make_frame(), "col": 0}

    w.add("wrap", d)
    w.add("nowrap", d)
    w.add("nogrow", d)
    w.add("randomlist", d)


def frame_files():
    d = {"frame": w.make_frame(), "col": 0}

    w.add("script", d)
    w.add("randomfile", d)
    w.add("wordfile", d)


def frame_stuff():
    d = {"frame": w.make_frame(), "col": 0}

    w.add("align", d)
    w.add("remake", d)
    w.add("loop", d)
    w.add("separator", d)
    w.add("order", d)
