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

# Link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter YouTube Link: ")

# Select Path for saving file
path_label = Label(screen, text="Select File Path for Video:")
select_btn = Button(screen, text="Select", command=select_path)

canvas.create_window(250, 130, window=path_label)
canvas.create_window(250, 180, window=select_btn)

# Add widgets to window
canvas.create_window(250, 20, window=link_label)
canvas.create_window(250, 70, window=link_field)

# Download buttons
download_btn = Button(screen, text="Download Video", command=download_file)
canvas.create_window(250, 240, window=download_btn)

# App loop
screen.mainloop()
