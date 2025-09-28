import sys , os
import tkinter as tk
from tkinter import ttk
import json

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

class inspector ():
    def __init__(self , root):
        self.root = root
        self.root.columnconfigure(0, weight=1)  # اجازه کشش به ستون ۰ در ریشه
        self.root.rowconfigure(1, weight=1)
        self.parameters_list = []
        #
        self.tagName_frame = tk.Frame(self.root) #this frame is for name and path of item clicked
        self.tagName_frame.columnconfigure(1, weight=1)
        self.style_frame = tk.Frame(self.root) #this frame is for load style(css) of item clicked
        self.style_frame.grid_rowconfigure(0, weight=0)  # سطر دکمه Test
        self.style_frame.grid_rowconfigure(1, weight=1)  # سطر بوم و اسکرول‌بار
        self.style_frame.grid_columnconfigure(0, weight=1)  # ستون بوم
        self.style_frame.grid_columnconfigure(1, weight=0)  # ستون اسکرول‌بار

        self.tagName_frame.grid(row=0 , column=0, sticky="ew")
        self.style_frame.grid(row=1 , column=0 , sticky= "nsew")

        self.name_label = tk.Label(self.tagName_frame , text="Name" , font=("Arial", 14))
        self.tagName_entry = tk.Entry(self.tagName_frame , font=("Arial", 14) , state='readonly')
        self.path_label = tk.Label(self.tagName_frame , text="Path" , font=("Arial", 14))
        self.pathEntry = tk.Entry(self.tagName_frame  , state="readonly")
        #
        self.name_label.grid(row=0 , column=0)
        self.tagName_entry.grid(row=0 , column=1  , sticky="ew")
        self.path_label.grid(row=1 , column=0)
        self.pathEntry.grid(row=1 , column=1  , sticky="ew")
        #####################style frame details#######################
        self.general_exert = tk.Button(self.style_frame , text="Exert all" , command=self.exert_all)
        self.general_exert.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.styles_canvas = tk.Canvas(self.style_frame)
        self.scrollbar = ttk.Scrollbar(self.style_frame, orient="vertical", command=self.styles_canvas.yview)

        # استفاده از grid برای کنترل بهتر
        self.styles_canvas.grid(row=1, column=0, sticky="nsew")
        self.scrollbar.grid(row=1, column=1, sticky="ns")

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
        
        #####################style frame details#######################
        

    def add_style(self , style_name : str , value_mode ):
        style_widget_frame = tk.Frame(self.scrollable_frame , bd=5, relief="ridge")
        style_widget_frame.pack(pady=5 , fill=tk.X , expand=True)

        styleName_entry = tk.Entry(style_widget_frame , width=10)
        value_style = tk.Entry(style_widget_frame , width=10)
        colon_lb = tk.Label(style_widget_frame , text= " : ")

        # تعریف دکمه با lambda برای ارسال entryها به تابع
        exert_button = tk.Button(
            style_widget_frame,
            text="Exert",
            command=lambda e1=styleName_entry, e2=value_style: self.style_exerter(e1, e2)
        )

        exert_button.pack(side="left" , padx=5)
        styleName_entry.pack(side="left")
        colon_lb.pack(side="left")
        value_style.pack(side="left")

        styleName_entry.insert(0 , style_name)
        value_style.insert(0 , value_mode)

        
    def style_exerter(self, styleName_entry, value_style):
        style_path = self.pathEntry.get()
        name_style = styleName_entry.get()
        style = load_styles(style_path)
        json_file = style["json"]
        json_file["style"][name_style] = value_style.get()
        with open(style_path, "w+", encoding="utf-8") as f:
            json.dump(json_file, f, ensure_ascii=False, indent=4)
        # print(f"Updated style: {name_style} = {value_style.get()}")
    
    def exert_all(self):
        style_path = self.pathEntry.get() #get template path from path entry
        style = load_styles(style_path)
        json_file = style["json"]
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
                    #print(f"{style_name} : {style_value}")
                    name_style = style_name
                    json_file["style"][name_style] = style_value
                    with open(style_path, "w+", encoding="utf-8") as f:
                        json.dump(json_file, f, ensure_ascii=False, indent=4)


    def _on_mousewheel(self, event):
        self.styles_canvas.yview_scroll(int(-1*(event.delta/120)), "units")



class manager():
    def __init__(self , root  , inspect : inspector , select_mode = "browse" , hover_background_color = "lightcyan" ):
        self.root = root
        self.inspect = inspect
        self.select_mode = select_mode
        self.hover_background_color = hover_background_color
        self.item_clicked = "html"
        self.dragging_items = []
        self.hovered_item = None
        self.is_dragging = False
        #
        self.tree = ttk.Treeview(self.root , selectmode = self.select_mode)
        self.tree.grid(row=1)
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
    def delete_tag(self):
        self.selected_items = self.tree.selection()
        #for item in selected_items:
        if self.selected_items:
            self.tree.delete(self.selected_items)

    
    def on_item_clicked(self , event):
        self.tree.after(10, lambda: self.start_drag_item(event))
        self.is_dragging = False

    def start_drag_item(self , event):
        self.load_template_detail_inspector()
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


    def load_template_detail_inspector(self):
        self.item_clicked = self.tree.item(self.tree.selection())['text']
        self.inspect.tagName_entry.config(state='normal')
        self.inspect.pathEntry.config(state='normal')
        self.inspect.tagName_entry.delete(0, tk.END)
        self.inspect.tagName_entry.insert(0, self.item_clicked)
        self.inspect.pathEntry.delete(0, tk.END)
        self.inspect.pathEntry.insert(0, f"templates/{self.item_clicked}.json")
        self.inspect.tagName_entry.config(state='readonly')
        self.inspect.pathEntry.config(state='readonly')
        self.get_style = load_styles(self.inspect.pathEntry.get())
        
        self.clear_widgets()
        if self.get_style != None:
            self.get_style = load_styles(self.inspect.pathEntry.get())["style"]
            for style in self.get_style["keys"]:
                self.inspect.add_style(style , self.get_style["style"][style])
        else :
            self.nothing_style = tk.Label(self.inspect.scrollable_frame , text= "There is nothing style")
            self.nothing_style.pack()

    def __call__(self):
        return self.item_clicked
# root = tk.Tk()
# root.title("test")
# root.geometry("300x400")
# manager(root)
# root.mainloop()