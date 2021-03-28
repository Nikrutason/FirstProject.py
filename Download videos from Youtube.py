import tkinter as tk
import pafy
import tkinter.filedialog as fd
from tkinter import messagebox as mbox
import os


def up():
    try:
        url = name.get()
        v = pafy.new(url)
        streams = v.streams
        availabels_streams = {}
        count = 1
        tk.Label(win, text="Starting").grid(column=0, row=3)
        for stream in range(len(streams)):
            availabels_streams[count] = streams[stream]
            if stream == len(streams)-1:
                pup = name_path.get()
                os.chdir(pup)
                d = streams[count-1].download()
            else:
                count += 1
        return mbox.showinfo("Congratulation", "Download sucesseful")

    except:
        return mbox.showerror("Error!", "Check the input is correct")


def ready():
    pathy = fd.askdirectory(title="Choose the path", initialdir="/")
    if pathy:
        name_path.delete(0, len(name_path.get())-1)
        name_path.insert(0, str(pathy))


win = tk.Tk()
win.geometry("500x150")
win.title("Качаем с Youtube")

tk.Label(win, text="URL-видео:", font=("Arial Black", 15)).grid(row=0, column=0, stick="w")
name = tk.Entry(win, width=50)
name.grid(row=0, column=1, stick="w")
tk.Label(win, text="Choose the path:", font=("Arial black", 15)).grid(column=0, row=1)
name_path = tk.Entry(win, width=35)
name_path.grid(column=1, row=1, stick="w")
name_path.insert(0, "C:\\")
tk.Button(win, text="Path", width=10, command=ready).grid(column=1, row=1, stick="e")
tk.Button(win, text="Download", width=15, command=up).grid(column=1, row=2, stick="w")
win.mainloop()
