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
root.geometry("90x900")
root.attributes("-topmost",True)

root.title("Python Guides")
root["bg"] = "black"

import p6

root.mainloop()