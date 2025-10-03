import sys , os
import tkinter as tk
from tkinter import ttk , filedialog

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..' , 'Objects')))
from variables import general_variables , open_fileExplorer

general_vars = general_variables()
file_explorer = open_fileExplorer()

class project_folder_panel():
    def __init__(self , root):
        self.root = root
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        #
        self.path_tree = ttk.Treeview(self.root , columns=("fullpath",), show="tree")
        self.path_tree.grid(row=0 , column=0 , sticky="nsew")
        #

        #print(self.path_tree.get_children())

class menu ():
    def __init__(self , master_root , frame_root : project_folder_panel):
        self.root = master_root
        self.frame_root = frame_root
        self.path_tree = self.frame_root.path_tree
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.filemenu = tk.Menu(self.menu , tearoff=False)
        self.editmenu = tk.Menu(self.menu , tearoff=False)
        self.settingsMenu = tk.Menu(self.menu , tearoff=False)

        self.menu.add_cascade(label="File" , menu=self.filemenu)
        self.menu.add_cascade(label="Edit" , menu=self.editmenu)
        self.menu.add_cascade(label="Settings" , menu=self.settingsMenu)

        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open" , command = self.open_project_folder)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save")
        self.filemenu.add_command(label="Save as")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit" , command=self.root.quit)

        self.editmenu.add_command(label="Copy")
        self.editmenu.add_command(label="Cut")
        self.editmenu.add_command(label="Paste")


        self.settingsMenu.add_command(label="Open")
        self.settingsMenu.add_separator()
        self.settingsMenu.add_command(label="Templates path")
        self.settingsMenu.add_command(label="Project path")
    
    def open_project_folder(self):
        path = file_explorer.open_folder()
        general_vars.update_path("pro" , path)
        file_explorer.add_tree(self.frame_root.path_tree , path)
        for i in general_vars.get_pathes().keys():
            print(f"{i} : {general_vars.get_pathes()[i]}")
        print("--------------------------------------")

# root = tk.Tk()
# app = menu(root)
# app.open_project_folder()
# root.mainloop()