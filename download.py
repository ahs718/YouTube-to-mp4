from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


# Functions
def select_path():
    # Prompts user to select path from the file explorer
    path = filedialog.askdirectory()
    path_label.configure(text=path)



# App frame
screen = Tk()
title = screen.title("Youtube to mp4")
canvas = Canvas(screen, width=480, height=300)
canvas.pack()


# App loop
screen.mainloop()
