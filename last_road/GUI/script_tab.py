# frame1 = tk.Frame(paned_window, width=200, height=300, bg="lightgray")
# paned_window.add(frame1)

# frame2 = tk.Frame(paned_window, width=200, height=300, bg="white")
# paned_window.add(frame2)

import tkinter as tk
from tkinter import ttk

class script_gui_class():
    def __init__(self , root):
        self.root = root
        #
        self.label = tk.Label(self.root , text="here is script tab")
        self.label.pack()



