# Modules
import config
import frames

# Libraries
import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

app = tk.CTk()
app.geometry(f"{config.width}x{config.height}")
app.grid_columnconfigure(0, weight=1)
config.prepare(app)


# ---


frames.frame_input()
frames.frame_words()
frames.frame_position()
frames.frame_font()
frames.frame_decorations()
frames.frame_frames()
frames.frame_output()

app.mainloop()
