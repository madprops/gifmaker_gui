# Modules
import config
import frames
import widgets

config.prepare()

frames.frame_input()
frames.frame_words()
frames.frame_position()
frames.frame_font()
frames.frame_decorations()
frames.frame_frames()
frames.frame_output()
frames.frame_checkboxes()
frames.frame_outline()
frames.frame_seeds()
frames.frame_opts()

widgets.fill_widgets()
config.app.mainloop()
