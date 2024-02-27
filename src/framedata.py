# Libraries
import customtkinter as ctk  # type: ignore


class FrameData:
    def __init__(self, frame: ctk.CTkFrame, col: int) -> None:
        self.frame = frame
        self.col = col
