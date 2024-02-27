# Modules
import config
import frames
import widgets

config.prepare()

frames.frame_input()
frames.frame_output()
frames.frame_words()
frames.frame_position()
frames.frame_font()
frames.frame_decorations()
frames.frame_frames()
frames.frame_checkboxes()
frames.frame_outline()
frames.frame_seeds()
frames.frame_opts()
frames.frame_someboxes()
frames.frame_files()
frames.frame_stuff()

widgets.fill_widgets()
config.app.mainloop()
