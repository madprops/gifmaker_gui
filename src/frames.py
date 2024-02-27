import config
from config import G
import widgets as w
import render


def frame_input():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, col, "Input")
    col += 1

    G["input_path"]["widget"] = w.make_text(frame, col, placeholder="Path to a file", sticky="ew")
    col += 1

    w.make_button(frame, col, "Browse", lambda: w.browse(G["input_path"]["widget"]))
    col += 1

    w.make_button(frame, col, "Render", lambda: render.render(),
                  color="lightblue", text_color="black", hover_color=("blue", "white"))
    col += 1


def frame_font():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, col, "Font")
    col += 1

    G["font_name"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Font Size")
    col += 1

    G["font_size"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Font Color")
    col += 1

    G["font_color"]["widget"] = w.make_text(frame, col, width=config.bigger_width)
    col += 1

    w.make_label(frame, col, "BG Color")
    col += 1

    G["bgcolor"]["widget"] = w.make_text(frame, col, width=config.bigger_width)
    col += 1


def frame_decorations():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, col, "Outline")
    col += 1

    G["outline"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Opacity")
    col += 1

    G["opacity"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Padding")
    col += 1

    G["padding"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Radius")
    col += 1

    G["radius"]["widget"] = w.make_text(frame, col)
    col += 1


def frame_words():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, col, "Words")
    col += 1

    G["words"]["widget"] = w.make_text(frame, col, placeholder="Words to put on the frames", sticky="ew")
    col += 1


def frame_position():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, col, "Top")
    col += 1

    G["top"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Bottom")
    col += 1

    G["bottom"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Left")
    col += 1

    G["left"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Right")
    col += 1

    G["right"]["widget"] = w.make_text(frame, col)
    col += 1


def frame_frames():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, col, "Delay")
    col += 1

    G["delay"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Frames")
    col += 1

    G["frames"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Filter")
    col += 1

    G["filter_name"]["widget"] = w.make_select(frame, col)
    col += 1


def frame_output():
    frame = w.make_frame()
    frame.grid_columnconfigure(1, weight=1)
    col = 0

    w.make_label(frame, col, "Output")
    col += 1

    G["output_path"]["widget"] = w.make_text(frame, col, sticky="ew", placeholder="Where to save the file")
    col += 1

    w.make_label(frame, col, "Format")
    col += 1

    G["format_name"]["widget"] = w.make_select(frame, col)
    col += 1


def frame_checkboxes():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, col, "Fill Words")
    col += 1

    G["fill_words"]["widget"] = w.make_checkbox(frame, col)
    col += 1

    w.make_label(frame, col, "Fill Gen")
    col += 1

    G["fill_gen"]["widget"] = w.make_checkbox(frame, col)
    col += 1

    w.make_label(frame, col, "Descenders")
    col += 1

    G["descender"]["widget"] = w.make_checkbox(frame, col)
    col += 1

    w.make_label(frame, col, "Deep Fry")
    col += 1

    G["deep_fry"]["widget"] = w.make_checkbox(frame, col)
    col += 1

    w.make_label(frame, col, "Vertical")
    col += 1

    G["vertical"]["widget"] = w.make_checkbox(frame, col)
    col += 1

    w.make_label(frame, col, "Horizontal")
    col += 1

    G["horizontal"]["widget"] = w.make_checkbox(frame, col)
    col += 1


def frame_outline():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, col, "OutLn Width")
    col += 1

    G["outline_width"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "OutLn Top")
    col += 1

    G["outline_top"]["widget"] = w.make_checkbox(frame, col)
    G["outline_top"]["widget"].select()
    col += 1

    w.make_label(frame, col, "OutLn Bottom")
    col += 1

    G["outline_bottom"]["widget"] = w.make_checkbox(frame, col)
    G["outline_bottom"]["widget"].select()
    col += 1

    w.make_label(frame, col, "OutLn Left")
    col += 1

    G["outline_left"]["widget"] = w.make_checkbox(frame, col)
    G["outline_left"]["widget"].select()
    col += 1

    w.make_label(frame, col, "OutLn Right")
    col += 1

    G["outline_right"]["widget"] = w.make_checkbox(frame, col)
    G["outline_right"]["widget"].select()
    col += 1


def frame_seeds():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, col, "Seed")
    col += 1

    G["seed"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Frame Seed")
    col += 1

    G["frame_seed"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Word Seed")
    col += 1

    G["word_seed"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Filter Seed")
    col += 1

    G["filter_seed"]["widget"] = w.make_text(frame, col)
    col += 1


def frame_opts():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, col, "Frame List")
    col += 1

    G["framelist"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Frame Opts")
    col += 1

    G["frameopts"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "Repeat Random")
    col += 1

    G["repeat_random"]["widget"] = w.make_checkbox(frame, col)
    col += 1

    w.make_label(frame, col, "Repeat Filter")
    col += 1

    G["repeat_filter"]["widget"] = w.make_checkbox(frame, col)
    col += 1


def frame_someboxes():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, col, "Wrap")
    col += 1

    G["wrap"]["widget"] = w.make_text(frame, col)
    col += 1

    w.make_label(frame, col, "No Wrap")
    col += 1

    G["nowrap"]["widget"] = w.make_checkbox(frame, col)
    col += 1

    w.make_label(frame, col, "No Grow")
    col += 1

    G["nogrow"]["widget"] = w.make_checkbox(frame, col)
    col += 1


def frame_files():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, col, "Script")
    col += 1

    G["script"]["widget"] = w.make_text(frame, col, width=config.path_width)
    col += 1

    w.make_label(frame, col, "Random File")
    col += 1

    G["random_file"]["widget"] = w.make_text(frame, col, width=config.path_width)
    col += 1

    w.make_label(frame, col, "Word File")
    col += 1

    G["word_file"]["widget"] = w.make_text(frame, col, width=config.path_width)
    col += 1

def frame_stuff():
    frame = w.make_frame()
    col = 0

    w.make_label(frame, col, "Align")
    col += 1

    G["align"]["widget"] = w.make_select(frame, col)
    col += 1

    w.make_label(frame, col, "Remake")
    col += 1

    G["remake"]["widget"] = w.make_checkbox(frame, col)
    col += 1

    w.make_label(frame, col, "Loop")
    col += 1

    G["loop"]["widget"] = w.make_checkbox(frame, col)
    col += 1