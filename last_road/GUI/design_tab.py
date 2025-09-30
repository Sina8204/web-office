# frame1 = tk.Frame(paned_window, width=200, height=300, bg="lightgray")
# paned_window.add(frame1)

# frame2 = tk.Frame(paned_window, width=200, height=300, bg="white")
# paned_window.add(frame2)

import tkinter as tk
from tkinter import ttk
from Objects.treeview_class import manager , inspector
#from Objects.toplevel_classes import add_tag_toplevel
import sys , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..' , 'Objects')))
from Objects.toplevel_classes import add_tag_toplevel


class tags():
    def __init__(self , root , inspector : inspector):
        self.root = root
        self.inspect = inspector
        #
        self.buttons_frame = tk.Frame(self.root , bg="blue")
        self.buttons_frame.grid(row=0)
        self.manager_frame = tk.Frame(self.root , bg="yellow")
        self.manager_frame.grid(row=1)
        self.button_add_tag = tk.Button(self.buttons_frame , text="Add tag" , command=self.open_tags_list_topelevel).grid(row=0)
        self.button_delete_tag = tk.Button(self.buttons_frame , text="Delete" , command=self.delete_tag).grid(row=0 , column=1)
        self.entry_selected_tag = tk.Entry(self.buttons_frame)
        self.entry_selected_tag.grid(row=0 , column=2)
        self.tags_manager = manager(self.manager_frame ,  self.inspect , "browse" )
    def add_tag(self , item):
        #self.p = self.tags_manager.creat_parent(self.entry_selected_tag.get())
        self.tags_manager.add_child(item)

    def delete_tag(self):
        self.tags_manager.delete_tag()
    
    def open_tags_list_topelevel(self):
        self.tags_list = tk.Toplevel()
        self.tags_list.title("Add tag")
        self.tags_list.geometry("480x640")
        self.tags_list_gui = add_tag_toplevel(self.tags_list , self.tags_manager , self.tags_list)
    

class design_gui_class():
    def __init__(self , root):
        self.root = root
        #creat parent panedWindow
        self.main_pw = tk.PanedWindow(self.root , orient=tk.HORIZONTAL) # main panedWindow
        self.main_pw.pack(fill="both" , expand=1)
        #creat child pannedWindow
        self.tags_foolder_pw = tk.PanedWindow(self.main_pw , orient=tk.VERTICAL) #this panedWindow get include tags and project foolder frame
        self.web_pw = tk.PanedWindow(self.main_pw) #this panedWindow get include web frame
        self.inspector_pw = tk.PanedWindow(self.main_pw) #this panedWindow get include inspector frame
        #adding child panedWindow to parent panedWindow
        self.main_pw.add(self.tags_foolder_pw)
        self.main_pw.add(self.web_pw)
        self.main_pw.add(self.inspector_pw)
        #creating frames
        self.tags_frame = tk.Frame(self.tags_foolder_pw , bg="white" , width=250 , height=400) #tags frame
        self.project_folder_frame = tk.Frame(self.tags_foolder_pw , bg="red" , width=250) #project folder frame
        self.web_frame = tk.Frame(self.web_pw , bg="gray" , width=750) #web frame 
        self.inspector_frame = tk.Frame(self.inspector_pw , bg="blue" , width=250) #inspector frame
        #adding frames to theme panedWindow
        self.tags_foolder_pw.add(self.tags_frame) #adding tags frame to tags_foolder_pw
        self.tags_foolder_pw.add(self.project_folder_frame) #adding project folder to tags_foolder_pw
        self.web_pw.add(self.web_frame) #adding web frame to web_pw
        self.inspector_pw.add(self.inspector_frame) #adding inspector frame to inspector_pw
        #
        self.inspector_gui = inspector(self.inspector_frame)
        self.tags_gui = tags(self.tags_frame , self.inspector_gui)
        
        






