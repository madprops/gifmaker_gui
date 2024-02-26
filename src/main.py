# Modules
import config
import frames

config.prepare()

frames.frame_input()
frames.frame_words()
frames.frame_position()
frames.frame_font()
frames.frame_decorations()
frames.frame_frames()
frames.frame_output()

config.app.mainloop()
