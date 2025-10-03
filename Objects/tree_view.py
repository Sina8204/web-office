import sys , os
import tkinter as tk
from tkinter import ttk
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..' , 'Objects')))
from variables import general_variables , open_fileExplorer

general_vars = general_variables()
file_explorer = open_fileExplorer()

def load_styles(path):
    existing_data = {}
    try:
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path , "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        else :
            existing_data = {}
    except json.JSONDecodeError:
        existing_data = {}
    keys = []
    styles = {}
    if "style" in existing_data.keys():
        keys = existing_data["style"].keys()
        styles = {"style" : existing_data["style"]  , "keys" : keys}
        return {"json" : existing_data , "style" : styles , "keys" : keys}
    else :
        return None


class manager():
    #def __init__(self , root  , inspect : inspector , select_mode = "browse" , hover_background_color = "lightcyan" ):
    def __init__(self , root , inspector , select_mode = "browse" , hover_background_color = "lightcyan" ):
        self.root = root
        self.inspect = inspector
        self.select_mode = select_mode
        self.hover_background_color = hover_background_color
        self.item_clicked = "html"
        self.dragging_items = []
        self.hovered_item = None
        self.is_dragging = False
        #
        self.tree = ttk.Treeview(self.root , selectmode = self.select_mode , height=20)
        self.tree.grid(row=1 , column=0 , sticky="nsew")
        #
        self.tree.tag_configure("hover_target", background="lightcyan")
        self.tree.bind("<ButtonPress-1>", self.on_item_clicked) #select items to draging
        self.tree.bind("<ButtonRelease-1>", self.on_button_release) #droping
        self.tree.bind("<B1-Motion>", self.on_mouse_motion) #highlight hovered item
    
    def creat_parent(self , name : str):
        self.parent = self.tree.insert("", "end", text=name)
        self.tree.item(self.parent , open=True)
        return self.parent
    def add_child(self , name : str):
        self.tree.insert(self.tree.selection() , "end", text=name)
        self.tree.item(self.tree.selection() , open=True)
        #print(self.tree.item())
    
    def get_all_tree_childeren(self , tree : ttk.Treeview, item):
        names = []
        children = tree.get_children(item)
        for child in children:
            name = tree.item(child, 'text')
            names.append(name)
            names.extend(self.get_all_tree_childeren(tree, child))
        return names
    def delete_tag(self):
        self.selected_items = self.tree.selection()
        selected_item_name = self.tree.item(self.selected_items , 'text')
        print (f"{selected_item_name} : {self.get_all_tree_childeren(self.tree , self.selected_items)}")
        #for item in selected_items:
        if self.selected_items:
            for child in self.get_all_tree_childeren(self.tree , self.selected_items):
                if child in general_vars.get_inputed_templates():
                    general_vars.delete_tree_item(child)
            print (f"check : [{selected_item_name}] == [{general_vars.get_inputed_templates()}]")
            if selected_item_name in general_vars.get_inputed_templates():
                print("removing...")
                general_vars.delete_tree_item(selected_item_name)
                print(f"{selected_item_name} was deleted ")
            self.tree.delete(self.selected_items)

    
    def on_item_clicked(self , event):
        self.tree.after(10, lambda: self.start_drag_item(event))
        self.is_dragging = False

    def start_drag_item(self , event):
        #self.load_template_detail_inspector()
        self.load_style_selected_template_in_inspector()
        self.dragging_items = self.tree.selection()
        for item in self.dragging_items:
            self.tree.item(item, tags=("highlight"))
    #
    def is_descendant(self , item, target):
        # بررسی اینکه آیا target فرزند یا نوه‌ی item هست
        self.children = self.tree.get_children(item)
        if target in self.children:
            return True
        for child in self.children:
            if self.is_descendant(child, target):
                return True
        return False
    #
    def on_mouse_motion(self , event):
        if not self.dragging_items:
            return
        self.is_dragging = True
        self.current_hover = self.tree.identify_row(event.y)

        if self.hovered_item and self.hovered_item != self.current_hover:
            self.tree.item(self.hovered_item, tags=())

        if self.current_hover:
            self.tree.item(self.current_hover, tags=("hover_target",))
            self.hovered_item = self.current_hover
        else:
            self.hovered_item = None

    def on_button_release(self , event):
        if not self.is_dragging:
            return  # فقط انتخاب بوده، نه درگ
        
        self.target_item = self.tree.identify_row(event.y)
        if self.target_item:
            for item in self.dragging_items:
                # جلوگیری از جابجایی آیتم به خودش یا فرزندانش
                if item == self.target_item or self.is_descendant(item, self.target_item):
                    print("❌ نمی‌توان آیتم را داخل خودش یا فرزندانش منتقل کرد.")
                    continue
                self.tree.move(item, self.target_item, "end")
                
            #save_tree_state()
        else:
            print("هیچ آیتم مقصدی انتخاب نشده.")
        for item in self.dragging_items:
            self.tree.item(item, tags=())
        if self.hovered_item:
            self.tree.item(self.hovered_item, tags=())
        self.dragging_items = []
        self.hovered_item = None
        self.is_dragging = True
    
    def clear_widgets(self):
        for widget in self.inspect.scrollable_frame.winfo_children():
            widget.destroy()
        
    def load_style_selected_template_in_inspector(self):
        self.item_clicked = self.tree.item(self.tree.selection())['text'] ############### انتخاب قالب های خارجی تعیین شود
        path_temp = f"{general_vars.get_pathes()["in_temps_path"]}/{self.item_clicked}.json"
        item_info = {}
        style = {}
        print(self.item_clicked)
        if os.path.exists(path_temp) :
            print(path_temp)
            with open(path_temp , "r" , encoding='utf-8') as f:
                item_info = json.load(f)
            style = item_info["style"]
            print(f"Item info : {item_info}")
            print(f"STYLE : {style}")
            # print(f"STYLE : {list(style["style"].keys())}")
            self.inspect.input_item_info(item_info , path_temp)
            self.clear_widgets()
            for style_name in list(style.keys()):
                self.inspect.add_style(style_name , style[style_name]["value"] , writable = style[style_name]["state"])


    



    # def clear_widgets(self):
    #     for widget in self.inspect.scrollable_frame.winfo_children():
    #         widget.destroy()


    # def load_template_detail_inspector(self):
    #     self.item_clicked = self.tree.item(self.tree.selection())['text']
    #     self.inspect.tagName_entry.config(state='normal')
    #     self.inspect.pathEntry.config(state='normal')
    #     self.inspect.tagName_entry.delete(0, tk.END)
    #     self.inspect.tagName_entry.insert(0, self.item_clicked)
    #     self.inspect.pathEntry.delete(0, tk.END)
    #     self.inspect.pathEntry.insert(0, f"templates/{self.item_clicked}.json")
    #     self.inspect.tagName_entry.config(state='readonly')
    #     self.inspect.pathEntry.config(state='readonly')
    #     self.get_style = load_styles(self.inspect.pathEntry.get())
        
    #     self.clear_widgets()
    #     if self.get_style != None:
    #         self.get_style = load_styles(self.inspect.pathEntry.get())["style"]
    #         for style in self.get_style["keys"]:
    #             self.inspect.add_style(style , self.get_style["style"][style])
    #     else :
    #         self.nothing_style = tk.Label(self.inspect.scrollable_frame , text= "There is nothing style")
    #         self.nothing_style.pack()

    def __call__(self):
        return self.item_clicked