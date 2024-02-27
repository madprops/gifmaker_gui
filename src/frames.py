from config import args
import widgets as w
import render


def frame_input():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    d = {"col": 0}

    w.add(frame, "input", d)

    w.make_button(frame, d, "Browse", lambda: w.browse(args["input_path"]["widget"]))

    w.make_button(frame, d, "Render", lambda: render.render(),
                  color="lightblue", text_color="black", hover_color=("blue", "white"))


def frame_font():
    frame = w.make_frame()
    d = {"col": 0}

    w.add(frame, "font", d)
    w.add(frame, "fontsize", d)
    w.add(frame, "fontcolor", d)
    w.add(frame, "bgcolor", d)


def frame_decorations():
    frame = w.make_frame()
    d = {"col": 0}

    w.add(frame, "outline", d)
    w.add(frame, "delay", d)
    w.add(frame, "opacity", d)
    w.add(frame, "padding", d)
    w.add(frame, "radius", d)


def frame_words():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    d = {"col": 0}

    w.add(frame, "words", d)


def frame_position():
    frame = w.make_frame()
    d = {"col": 0}

    w.add(frame, "top", d)
    w.add(frame, "bottom", d)
    w.add(frame, "left", d)
    w.add(frame, "right", d)
    w.add(frame, "width", d)
    w.add(frame, "height", d)


def frame_frames():
    frame = w.make_frame()
    d = {"col": 0}

    w.add(frame, "frames", d)
    w.add(frame, "filter", d)
    w.add(frame, "filterlist", d)
    w.add(frame, "filteropts", d)


def frame_output():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    d = {"col": 0}

    w.add(frame, "output", d)
    w.add(frame, "format", d)


def frame_checkboxes():
    frame = w.make_frame()
    d = {"col": 0}

    w.add(frame, "fillwords", d)
    w.add(frame, "fillgen", d)
    w.add(frame, "descender", d)
    w.add(frame, "deepfry", d)
    w.add(frame, "vertical", d)
    w.add(frame, "horizontal", d)


def frame_outline():
    frame = w.make_frame()
    d = {"col": 0}

    w.add(frame, "outlinewidth", d)
    w.add(frame, "no_outline_top", d)
    w.add(frame, "no_outline_bottom", d)
    w.add(frame, "no_outline_left", d)
    w.add(frame, "no_outline_right", d)


def frame_seeds():
    frame = w.make_frame()
    d = {"col": 0}

    w.add(frame, "seed", d)
    w.add(frame, "frameseed", d)
    w.add(frame, "wordseed", d)
    w.add(frame, "filterseed", d)


def frame_opts():
    frame = w.make_frame()
    d = {"col": 0}

    w.add(frame, "framelist", d)
    w.add(frame, "frameopts", d)
    w.add(frame, "repeatrandom", d)
    w.add(frame, "repeatfilter", d)


def frame_someboxes():
    frame = w.make_frame()
    d = {"col": 0}

    w.add(frame, "wrap", d)
    w.add(frame, "nowrap", d)
    w.add(frame, "nogrow", d)
    w.add(frame, "randomlist", d)


def frame_files():
    frame = w.make_frame()
    d = {"col": 0}

    w.add(frame, "script", d)
    w.add(frame, "randomfile", d)
    w.add(frame, "wordfile", d)


def frame_stuff():
    frame = w.make_frame()
    d = {"col": 0}

    w.add(frame, "align", d)
    w.add(frame, "remake", d)
    w.add(frame, "loop", d)
    w.add(frame, "separator", d)
    w.add(frame, "order", d)
