# Libraries
import customtkinter as tk  # type: ignore


class FrameData:
    def __init__(self, frame: tk.CTkFrame, col: int) -> None:
        self.frame = frame
        self.col = col
