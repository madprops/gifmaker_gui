import config
from config import G
import widgets as w
import render


def frame_input():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, 0, col, "Input")
    col += 1

    G["input_path"]["widget"] = w.make_entry(frame, 0, col, placeholder="Path to a file", sticky="ew")
    col += 1

    w.make_button(frame, 0, col, "Browse", lambda: w.browse(G["input_path"]["widget"]))
    col += 1

    w.make_button(frame, 0, col, "Render", lambda: render.render(),
                  color="lightblue", text_color="black", hover_color=("blue", "white"))
    col += 1


def frame_font():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Font")
    col += 1

    G["font_name"]["widget"] = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Font Size")
    col += 1

    G["font_size"]["widget"] = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Font Color")
    col += 1

    G["font_color"]["widget"] = w.make_entry(frame, 0, col, width=config.bigger_width)
    col += 1

    w.make_label(frame, 0, col, "BG Color")
    col += 1

    G["bgcolor"]["widget"] = w.make_entry(frame, 0, col, width=config.bigger_width)
    col += 1


def frame_decorations():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Outline")
    col += 1

    G["outline"]["widget"] = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Opacity")
    col += 1

    G["opacity"]["widget"] = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Padding")
    col += 1

    G["padding"]["widget"] = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Radius")
    col += 1

    G["radius"]["widget"] = w.make_entry(frame, 0, col)
    col += 1


def frame_words():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, 0, col, "Words")
    col += 1

    G["words"]["widget"] = w.make_entry(frame, 0, col, placeholder="Words to put on the frames", sticky="ew")
    col += 1


def frame_position():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Top")
    col += 1

    G["top"]["widget"] = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Bottom")
    col += 1

    G["bottom"]["widget"] = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Left")
    col += 1

    G["left"]["widget"] = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Right")
    col += 1

    G["right"]["widget"] = w.make_entry(frame, 0, col)
    col += 1


def frame_frames():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Delay")
    col += 1

    G["delay"]["widget"] = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Frames")
    col += 1

    G["frames"]["widget"] = w.make_entry(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Filter")
    col += 1

    G["filter_name"]["widget"] = w.make_select(frame, 0, col, ["empty"])
    col += 1


def frame_output():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, 0, col, "Output")
    col += 1

    G["output_path"]["widget"] = w.make_entry(frame, 0, col, sticky="ew", placeholder="Where to save the file")
    col += 1

    w.make_label(frame, 0, col, "Format")
    col += 1

    G["format_name"]["widget"] = w.make_select(frame, 0, col, ["empty"])
    col += 1


def frame_checkboxes_1():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Fill Words")
    col += 1

    G["fill_words"]["widget"] = w.make_checkbox(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Fill Gen")
    col += 1

    G["fill_gen"]["widget"] = w.make_checkbox(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Descenders")
    col += 1

    G["descender"]["widget"] = w.make_checkbox(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Deep Fry")
    col += 1

    G["deep_fry"]["widget"] = w.make_checkbox(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Vertical")
    col += 1

    G["vertical"]["widget"] = w.make_checkbox(frame, 0, col)
    col += 1

    w.make_label(frame, 0, col, "Horizontal")
    col += 1

    G["horizontal"]["widget"] = w.make_checkbox(frame, 0, col)
    col += 1


def frame_outline():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, 0, col, "Outline Top")
    col += 1

    G["outline_top"]["widget"] = w.make_checkbox(frame, 0, col)
    G["outline_top"]["widget"].select()
    col += 1

    w.make_label(frame, 0, col, "Outline Bottom")
    col += 1

    G["outline_bottom"]["widget"] = w.make_checkbox(frame, 0, col)
    G["outline_bottom"]["widget"].select()
    col += 1

    w.make_label(frame, 0, col, "Outline Left")
    col += 1

    G["outline_left"]["widget"] = w.make_checkbox(frame, 0, col)
    G["outline_left"]["widget"].select()
    col += 1

    w.make_label(frame, 0, col, "Outline Right")
    col += 1

    G["outline_right"]["widget"] = w.make_checkbox(frame, 0, col)
    G["outline_right"]["widget"].select()
    col += 1
