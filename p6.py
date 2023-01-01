import os
import random
import time
from tkinter import *
from tkinter import messagebox

root = Tk()

def Quit():
    pass
root.protocol("WM_DELETE_WINDOW", Quit)
root.wm_attributes("-alpha", 1)
root.overrideredirect(1)
root.geometry("2x900+780+0")
root.attributes("-topmost",True)

root.title("Python Guides")
root["bg"] = "yellow"

root.mainloop()