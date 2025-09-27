# frame1 = tk.Frame(paned_window, width=200, height=300, bg="lightgray")
# paned_window.add(frame1)

# frame2 = tk.Frame(paned_window, width=200, height=300, bg="white")
# paned_window.add(frame2)

import tkinter as tk
from tkinter import ttk
from Objects.treeview_class import manager
#from Objects.toplevel_classes import add_tag_toplevel
import sys , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..' , 'Objects')))
from Objects.toplevel_classes import add_tag_toplevel


class tags():
    def __init__(self , root):
        self.root = root
        #
        self.buttons_frame = tk.Frame(self.root , bg="blue")
        self.buttons_frame.grid(row=0)
        self.manager_frame = tk.Frame(self.root , bg="yellow")
        self.manager_frame.grid(row=1)
        self.button_add_tag = tk.Button(self.buttons_frame , text="Add tag" , command=self.open_tags_list_topelevel).grid(row=0)
        self.button_delete_tag = tk.Button(self.buttons_frame , text="Delete" , command=self.delete_tag).grid(row=0 , column=1)
        self.entry_selected_tag = tk.Entry(self.buttons_frame)
        self.entry_selected_tag.grid(row=0 , column=2)
        self.tags_manager = manager(self.manager_frame , "browse")
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
    

class inspector ():
    def __init__(self , root):
        self.root = root
        self.root.columnconfigure(0, weight=1)  # اجازه کشش به ستون ۰ در ریشه
        self.root.rowconfigure(1, weight=1)
        #
        self.tagName_frame = tk.Frame(self.root)
        #self.tagName_frame.columnconfigure(0, weight=1)
        self.tagName_frame.columnconfigure(1, weight=1)
        self.style_frame = tk.Frame(self.root)
        self.style_frame.columnconfigure(0, weight=1)
        self.tagName_frame.grid(row=0 , column=0, sticky="ew")
        self.style_frame.grid(row=1 , column=0 , sticky= "nsew")

        self.name_label = tk.Label(self.tagName_frame , text="Name" , font=("Arial", 14))
        self.tagName_entry = tk.Entry(self.tagName_frame , font=("Arial", 14) , state="readonly")
        self.path_label = tk.Label(self.tagName_frame , text="Path" , font=("Arial", 14))
        self.pathEntry = tk.Entry(self.tagName_frame  , state="readonly")
        #
        self.name_label.grid(row=0 , column=0)
        self.tagName_entry.grid(row=0 , column=1  , sticky="ew")
        self.path_label.grid(row=1 , column=0)
        self.pathEntry.grid(row=1 , column=1  , sticky="ew")
        #
        self.styles_canvas = tk.Canvas(self.style_frame)
        self.scrollbar = ttk.Scrollbar(self.style_frame, orient="vertical", command=self.styles_canvas.yview)

        # استفاده از grid برای کنترل بهتر
        self.styles_canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # تنظیم نسبت کشش قاب
        self.style_frame.grid_rowconfigure(0, weight=1)
        self.style_frame.grid_columnconfigure(0, weight=1)

        self.styles_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame = tk.Frame(self.styles_canvas)
        
        # اتصال قاب داخلی به بوم
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.styles_canvas.configure(
                scrollregion=self.styles_canvas.bbox("all")
            )
        )

        self.canvas_window = self.styles_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.styles_canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        #
        for i in range(50):
            self.add_style("width" , "50")
        
    
    def add_style(self , style_name : str , value_mode ):
        # for i in range(30):
        #     tk.Entry(self.scrollable_frame).pack(pady=5, padx=10)
        self.style_widget_frame = tk.Frame(self.scrollable_frame , bd=5, relief="ridge")
        self.style_widget_frame.pack(pady=5 , fill=tk.X , expand=True)
        #
        self.exert_button = tk.Button(self.style_widget_frame , text="Exert")
        self.styleName_entry = tk.Entry(self.style_widget_frame , width=10)
        self.colon_lb = tk.Label(self.style_widget_frame , text= " : ")
        self.value_style = tk.Entry(self.style_widget_frame , width=10)
        
        self.exert_button.pack(side="left" , padx=5)
        self.styleName_entry.pack(side="left")
        self.colon_lb.pack(side="left")
        self.value_style.pack(side="left")

        self.styleName_entry.insert(0 , style_name)
        self.value_style.insert(0 , value_mode)
        
    def _on_mousewheel(self, event):
        self.styles_canvas.yview_scroll(int(-1*(event.delta/120)), "units")






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
        self.tags_gui = tags(self.tags_frame)
        self.inspector_gui = inspector(self.inspector_frame)






