import tkinter as tk
from tkinter import ttk
from Objects.tree_view import manager

class tags_manager_panel_gui():
    def __init__(self , root):
        self.root = root
        self.root.columnconfigure(0 , weight=1)
        self.root.rowconfigure(1 , weight=1)
        ######################### <Frames> #########################
        self.buttons_frame = tk.Frame(root , bg="red")
        self.buttons_frame.columnconfigure(0 , weight=1)
        self.buttons_frame.columnconfigure(1 , weight=1)
        self.buttons_frame.grid(row=0 , column=0 , sticky="ew")

        self.manager_frame = tk.Frame(root , bg="blue")
        self.manager_frame.rowconfigure(1 , weight=1)
        self.manager_frame.columnconfigure(0 , weight=1)
        self.manager_frame.grid(row=1 , column=0 , sticky="nsew")
        ######################### <widgets> #########################
        self.button_add = tk.Button(self.buttons_frame , text="Add")
        self.button_delete = tk.Button(self.buttons_frame , text="Delete")
        self.button_add.grid(row=0 , column=0 , padx=5 , pady=5, sticky="ew")
        self.button_delete.grid(row=0 , column=1 , padx=5 , pady=5 , sticky="ew")

        self.tags_manager = manager(self.manager_frame)

class inspector_panel_gui():
    def __init__(self , root):
        self.root = root
        self.root.columnconfigure(0 , weight=1)
        self.root.rowconfigure(1 , weight=1)

        #++++++++++++++++++++++++ <Frames> #++++++++++++++++++++++++
        self.detail_frame = tk.Frame(self.root)
        self.detail_frame.columnconfigure(1 , weight=1)
        self.detail_frame.grid(row=0 , column=0 , sticky="ew")

        self.css_styles_frame = tk.Frame(self.root)
        self.css_styles_frame.columnconfigure(0 , weight=1)
        self.css_styles_frame.columnconfigure(1 , weight=0)
        self.css_styles_frame.rowconfigure(1 , weight=1)
        self.css_styles_frame.grid(row=1 , column=0 , sticky="nsew")

        self.general_tools_frame = tk.Frame(self.css_styles_frame)
        self.general_tools_frame.columnconfigure(0 , weight=1)
        self.general_tools_frame.columnconfigure(1 , weight=1)
        self.general_tools_frame.columnconfigure(2 , weight=1)

        self.styles_frame = tk.Frame(self.css_styles_frame)
        self.styles_frame.columnconfigure(0, weight=1)  # ستون بوم
        self.styles_frame.columnconfigure(1, weight=0)  # ستون بوم
        self.styles_frame.rowconfigure(1, weight=1)  # سطر بوم و اسکرول‌بار

        self.general_tools_frame.grid(row=0 , column=0 , sticky="ew")
        self.styles_frame.grid(row=1 , column=0 , sticky="nsew")
        #++++++++++++++++++++++++ <widgets> #++++++++++++++++++++++++
        self.class_label = tk.Label(self.detail_frame , text="Class : " , font=("Arial" , 14))
        self.id_label = tk.Label(self.detail_frame , text="ID : " , font=("Arial" , 14))
        self.name_label = tk.Label(self.detail_frame , text="Name : " , font=("Arial" , 14))
        self.path_label = tk.Label(self.detail_frame , text="Path :" , font=("Arial" , 14))
        self.call_type_label = tk.Label(self.detail_frame , text="Call type :" , font=("Arial" , 14))

        self.class_entry = tk.Entry(self.detail_frame , font=("Arial" , 14))
        self.id_entry = tk.Entry(self.detail_frame , font=("Arial" , 14))
        self.name_entry = tk.Entry(self.detail_frame , font=("Arial" , 14) , state="readonly")
        self.path_entry = tk.Entry(self.detail_frame , font=("Arial" , 14) , state="readonly")

        self.call_type_combobox = ttk.Combobox(self.detail_frame , values=["id" , "class" , "name"] , state="readonly")

        self.class_label.grid(row=0 , column= 0)
        self.id_label.grid(row=1 , column= 0)
        self.name_label.grid(row=2 , column= 0)
        self.path_label.grid(row=3 , column= 0)
        self.call_type_label.grid(row=4 , column=0)

        self.class_entry.grid(row=0 , column= 1 , sticky="ew")
        self.id_entry.grid(row=1 , column= 1 , sticky="ew")
        self.name_entry.grid(row=2 , column= 1 , sticky="ew")
        self.path_entry.grid(row=3 , column= 1 , sticky="ew")
        self.call_type_combobox.grid(row=4 , column=1 , sticky="ew" )

        #///////////////////////////////////////////////////////////////
        self.button_general_exert = tk.Button(self.general_tools_frame , text="General exert")
        self.button_add_style = tk.Button(self.general_tools_frame , text="Add style")
        self.button_Delet = tk.Button(self.general_tools_frame , text="Delete style")

        self.button_general_exert.grid(row=0 , column=0 , padx=5 , pady=5 , sticky="ew")
        self.button_add_style.grid(row=0 , column=1 , padx=5 , pady=5 , sticky="ew")
        self.button_Delet.grid(row=0 , column=2 , padx=5 , pady=5 , sticky="ew")

        #///////////////////////////////////////////////////////////////
        self.styles_canvas = tk.Canvas(self.styles_frame)
        self.scrollbar = ttk.Scrollbar(self.styles_frame, orient="vertical", command=self.styles_canvas.yview)

        self.styles_canvas.grid(row=1, column=0, sticky="nsew")
        self.scrollbar.grid(row=1, column=1, sticky="ns")

        self.styles_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame = ttk.Frame(self.styles_canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: (
                self.styles_canvas.update_idletasks(),
                self.styles_canvas.configure(scrollregion=self.styles_canvas.bbox("all"))
            )
        )

        self.canvas_window = self.styles_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.styles_canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        for i in range(50):
            tk.Label(self.scrollable_frame, text=f"test {i}").pack()
    def _on_mousewheel(self, event):
        bbox = self.styles_canvas.bbox("all")
        if bbox:
            canvas_height = self.styles_canvas.winfo_height()
            content_height = bbox[3] - bbox[1]
            if content_height > canvas_height:
                self.styles_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class design_gui_class():
    def __init__(self , root):
        self.root = root
        #
        #++++++++++++++++++++++++ <PandWindows> #++++++++++++++++++++++++
        self.main_pw = tk.PanedWindow(self.root)
        self.main_pw.pack(fill=tk.BOTH , expand=1)

        self.tagsManager_and_projectFolder_pw = tk.PanedWindow(self.main_pw , orient=tk.VERTICAL)
        self.web_pw = tk.PanedWindow(self.main_pw)
        self.inspector_pw = tk.PanedWindow(self.main_pw)

        self.main_pw.add(self.tagsManager_and_projectFolder_pw)
        self.main_pw.add(self.web_pw)
        self.main_pw.add(self.inspector_pw)
        #++++++++++++++++++++++++ <Frames> #++++++++++++++++++++++++
        self.tags_manager_frame = tk.Frame(self.tagsManager_and_projectFolder_pw , bg="blue" , width=250)
        self.project_folder_frame = tk.Frame(self.tagsManager_and_projectFolder_pw , bg="green" , width=250)
        self.web_review_frame = tk.Frame(self.web_pw , bg="yellow" , width=600)
        self.inspector_frame = tk.Frame(self.inspector_pw , bg="blue")

        self.tagsManager_and_projectFolder_pw.add(self.tags_manager_frame)
        self.tagsManager_and_projectFolder_pw.add(self.project_folder_frame)
        self.web_pw.add(self.web_review_frame)
        self.inspector_pw.add(self.inspector_frame)
        #++++++++++++++++++++++++ <widgets> #++++++++++++++++++++++++
        self.tags_manger = tags_manager_panel_gui(self.tags_manager_frame)
        self.inspector = inspector_panel_gui(self.inspector_frame)