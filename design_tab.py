import sys , os
import tkinter as tk
import json
from tkinter import ttk
from Objects.tree_view import manager
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..' , 'Objects')))
from Objects.topePanel import addTemplate_topePanel
from Objects.menu_objects import project_folder_panel , menu

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..' , 'Objects')))
# from variables import general_variables

class tags_manager_panel_gui():
    def __init__(self , root , inspector):
        self.root = root
        self.inspect = inspector
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
        self.button_add = tk.Button(self.buttons_frame , text="Add" , command=self.open_addTag_panel)
        self.button_delete = tk.Button(self.buttons_frame , text="Delete" , command=self.delete_selected_item)
        self.button_add.grid(row=0 , column=0 , padx=5 , pady=5, sticky="ew")
        self.button_delete.grid(row=0 , column=1 , padx=5 , pady=5 , sticky="ew")

        self.tags_manager = manager(self.manager_frame , inspector=self.inspect)
    
    def open_addTag_panel(self):
        self.tags_list = tk.Toplevel()
        self.tags_list.title("Add tag")
        self.tags_list.geometry("480x640")
        self.addTag = addTemplate_topePanel(self.tags_list , self.tags_manager , self.tags_list)
    
    def delete_selected_item(self):
        self.tags_manager.delete_tag()
    



class inspector_panel_gui():
    def __init__(self , root):
        self.root = root
        self.root.columnconfigure(0 , weight=1)
        self.root.rowconfigure(1 , weight=1)
        self.check_vars = {}
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
        self.button_general_exert = tk.Button(self.general_tools_frame , text="General exert" , command=self.exert_all)
        self.button_add_style = tk.Button(self.general_tools_frame
                                            , text="Add style" ,
                                            command=lambda : self.add_style(name="" , value="" , writable=True))
        self.button_Delet = tk.Button(self.general_tools_frame , text="Delete style" , command=self.style_delete)

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
        
    def input_item_info(self , info , path):
        class_value = info["class"]
        id = info["id"]
        name = info["name"]
        self.class_entry.delete(0 , tk.END)
        self.class_entry.insert(0 , class_value)
        self.id_entry.delete(0 , tk.END)
        self.id_entry.insert(0 , id)
        self.name_entry.config(state="normal")
        self.path_entry.config(state="normal")
        self.name_entry.delete(0 , tk.END)
        self.name_entry.insert(0 , name)
        self.path_entry.delete(0 , tk.END)
        self.path_entry.insert(0 , path)
        self.name_entry.config(state="readonly")
        self.path_entry.config(state="readonly")

    def style_exerter(self , key , value , writable = True):
        print(f"entry name : {key}\nentry value : {value}")
        path_json = self.path_entry.get()
        info_and_style = {}
        style = {}
        if key != "" and value != "":
            if os.path.exists(path_json):
                with open(path_json , 'r' , encoding='utf-8') as f:
                    info_and_style = json.load(f)
                style = info_and_style["style"].copy()
                if key in list(style.keys()):
                    style[key]["value"] = value
                    style[key]["state"] = int(writable)
                else :
                    style.update({key : {"value" : value , "state" : writable}})
                info_and_style["style"] = style
                with open(path_json , 'w' , encoding='utf-8') as f:
                    json.dump(info_and_style , f , ensure_ascii=False , indent=4)
            else:
                print(f"there is't any json file in '{path_json}' path!!")
        else :
            print("Styles can not have empty field !!")

    def exert_all(self):
        path_json = self.path_entry.get()
        info_and_style = {}
        style = {}
        if os.path.exists(path_json):
                with open(path_json , 'r' , encoding='utf-8') as f:
                    info_and_style = json.load(f)
                style = info_and_style["style"].copy()
        else:
            print(f"there is't any json file in path : {path_json}")
            return
        
        for child in self.scrollable_frame.winfo_children(): #read all children of self.scrollable_frame as list
        # بررسی اینکه آیا child یک فریم است
            if isinstance(child, tk.Frame):
                entries = child.winfo_children() #get children of scrollable_frame frame readed
                style_name = None 
                style_value = None
                for widget in entries:
                    if isinstance(widget, tk.Entry):
                        if style_name is None:
                            style_name = widget.get()
                        else:
                            style_value = widget.get()
                if style_name and style_value:
                    name_style = style_name
                    style[name_style]["value"] = style_value
                    info_and_style["style"] = style.copy()
                    with open(path_json, "w+", encoding="utf-8") as f:
                        json.dump(info_and_style, f, ensure_ascii=False, indent=4)

    def add_style(self , name , value = "" , writable = True):
        if self.path_entry.get() == "":
            print("No items selected !!!\n\tSelect an item")
            return
        style_widget_frame = tk.Frame(self.scrollable_frame , bd=5, relief="ridge")
        style_widget_frame.pack(pady=5 , fill=tk.X , expand=True)
        styleName_entry = tk.Entry(style_widget_frame , width=10)
        
        value_style = tk.Entry(style_widget_frame , width=10)
        colon_lb = tk.Label(style_widget_frame , text= " : ")

        check_btn_delete = tk.Checkbutton(style_widget_frame)
        self.check_vars.update({str(check_btn_delete) : tk.IntVar()})
        check_btn_delete.config(variable=self.check_vars[str(check_btn_delete)])
        #print(self.check_vars)
        
        # تعریف دکمه با lambda برای ارسال entryها به تابع
        exert_button = tk.Button(
        style_widget_frame,
        text="Exert",
        command=lambda: self.style_exerter(styleName_entry.get(), value_style.get() , writable=writable)
        )


        check_btn_delete.pack(side="left", padx=5)
        exert_button.pack(side="left" , padx=5)
        styleName_entry.pack(side="left" , padx=5)
        colon_lb.pack(side="left", padx=5)
        value_style.pack(side="left", padx=5)
        
        styleName_entry.insert(0 , name)
        value_style.insert(0 , value)
        if writable:
            styleName_entry.config(state="normal")
        else :
            styleName_entry.config(state="readonly")

        self.update_scrollregion()
    def exert_style_after_removing(self , nameStyle):
        path_json = self.path_entry.get()
        info_and_style = {}
        style = {}
        if os.path.exists(path_json):
            with open(path_json , 'r' , encoding='utf-8') as f:
                info_and_style = json.load(f)
            style = info_and_style["style"].copy()
            if nameStyle in style:
                if style[nameStyle]["state"]:
                    style.pop(nameStyle)
                    info_and_style["style"] = style.copy()
                    with open(path_json , 'w' , encoding='utf-8') as f:
                        json.dump(info_and_style , f , ensure_ascii=False , indent=4)
                    return True  # حذف انجام شده
                else:
                    print("You cannot remove styles that state parameter is on!! ")
                    return False  # حذف انجام نشده
            else:
                print("Style not found!")
                return True
        else:
            print(f"There isn't any json file in '{path_json}' path!!")
            return False

    def style_delete (self):
        child_list = self.scrollable_frame.winfo_children()
        for child in child_list: #read all children of self.scrollable_frame as list
        # بررسی اینکه آیا child یک فریم است
            if isinstance(child, tk.Frame):
                    entries = child.winfo_children() #get children of scrollable_frame frame readed
                    style_name = None
                    for widget in entries:
                        if isinstance(widget, tk.Entry):
                            if style_name is None:
                                style_name = widget.get()

                        if isinstance(widget , tk.Checkbutton):
                            if self.check_vars[str(widget)].get():
                                if self.exert_style_after_removing(style_name):
                                    child.destroy()
                                    self.check_vars.pop(str(widget))
                                else:
                                    print(f"Style '{style_name}' could not be removed. Frame not deleted.")
                            break
    
    def update_scrollregion(self):
        bbox = self.styles_canvas.bbox("all")
        if bbox:
            canvas_height = self.styles_canvas.winfo_height()
            content_height = bbox[3] - bbox[1]
            if content_height > canvas_height:
                self.styles_canvas.config(scrollregion=bbox)
            else:
                # اگر محتوا کوچکتر از بوم بود، اسکرول رو غیرفعال کن
                self.styles_canvas.config(scrollregion=(0, 0, 0, canvas_height))

    def _on_mousewheel(self, event):
        bbox = self.styles_canvas.bbox("all")
        if bbox:
            canvas_height = self.styles_canvas.winfo_height()
            content_height = bbox[3] - bbox[1]
            if content_height > canvas_height:
                self.styles_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class design_gui_class():
    def __init__(self , root , menu_root):
        self.root = root
        self.menu_root = menu_root
        #
        #++++++++++++++++++++++++ <PandWindows> #++++++++++++++++++++++++
        self.main_pw = tk.PanedWindow(self.root)
        self.main_pw.pack(fill=tk.BOTH , expand=1)

        self.tagsManager_and_projectFolder_pw = tk.PanedWindow(self.main_pw , orient=tk.VERTICAL , width=250)
        self.web_pw = tk.PanedWindow(self.main_pw , width=700)
        self.inspector_pw = tk.PanedWindow(self.main_pw)

        self.main_pw.add(self.tagsManager_and_projectFolder_pw)
        self.main_pw.add(self.web_pw)
        self.main_pw.add(self.inspector_pw)
        #++++++++++++++++++++++++ <Frames> #++++++++++++++++++++++++
        self.tags_manager_frame = tk.Frame(self.tagsManager_and_projectFolder_pw , bg="blue")
        self.project_folder_frame = tk.Frame(self.tagsManager_and_projectFolder_pw , bg="green")
        self.web_review_frame = tk.Frame(self.web_pw , bg="yellow")
        self.inspector_frame = tk.Frame(self.inspector_pw , bg="blue")

        self.tagsManager_and_projectFolder_pw.add(self.tags_manager_frame)
        self.tagsManager_and_projectFolder_pw.add(self.project_folder_frame)
        self.web_pw.add(self.web_review_frame)
        self.inspector_pw.add(self.inspector_frame)
        #++++++++++++++++++++++++ <widgets> #++++++++++++++++++++++++
        
        self.inspector = inspector_panel_gui(self.inspector_frame)
        self.tags_manger = tags_manager_panel_gui(self.tags_manager_frame , self.inspector)
        self.project_folder = project_folder_panel(self.project_folder_frame)
        menu(self.menu_root , self.project_folder)