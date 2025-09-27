import os
import tkinter as tk
from tkinter import ttk

from design_tab import design_gui_class
from html_tab import html_gui_class
from css_tab import css_gui_class
from script_tab import script_gui_class

def creat_folder(folder_name = "My project"):
    project_path = os.getcwd()
    folder_path = os.path.join(project_path , folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)



class web_office(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Web office")
        self.geometry("1280x720")
        #creat notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        #creat tabs
        self.design_tab = tk.Frame(self.notebook) #create design tab
        self.design = design_gui_class(self.design_tab) #adding design class gui to design tab
        #
        self.html_tab = tk.Frame(self.notebook) #create html tab
        self.html = html_gui_class(self.html_tab) #adding design html gui to design tab
        #
        self.css_tab = tk.Frame(self.notebook) #create css tab
        self.css = css_gui_class(self.css_tab) #adding design css gui to design tab
        #
        self.script_tab = tk.Frame(self.notebook) #create script tab
        self.script = script_gui_class(self.script_tab) #adding script css gui to design tab
        # Add tabs to the notebook
        self.notebook.add(self.design_tab , text="Design")
        self.notebook.add(self.html_tab , text="HTML")
        self.notebook.add(self.css_tab , text="CSS")
        self.notebook.add(self.script_tab , text="Script")
        

creat_folder("templates")
app = web_office()
app.mainloop()
