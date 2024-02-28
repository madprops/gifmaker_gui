# Modules
import config
import frames
import widgets
import utils

# Standard
import time

# Performance
last_time = 0.0


def get_time() -> float:
    return time.time()


def show_seconds(name: str, start: float, end: float) -> None:
    num = round(start - end, 3)
    label = utils.colortext("blue", name)
    utils.msg(f"{label}: {num} seconds")


def check_time(name: str) -> None:
    global last_time
    now = get_time()
    show_seconds(name, now, last_time)
    last_time = now


def main() -> None:
    global last_time
    start_time = get_time()
    last_time = start_time

    config.prepare(__file__)
    check_time("Prepare Config")

    frames.frame_input()
    frames.frame_output()
    frames.frame_words()
    frames.frame_position()
    frames.frame_font()
    frames.frame_frames()
    frames.frame_decorations()
    frames.frame_outline()
    frames.frame_checkboxes()
    frames.frame_seeds()
    frames.frame_opts()
    frames.frame_someboxes()
    frames.frame_files()
    frames.frame_stuff()
    check_time("Make Frames")

    widgets.fill_widgets()
    check_time("Fill Widgets")

    config.app.mainloop()


if __name__ == "__main__":
    main()
