import tkinter as tk
from tkinter import ttk

class manager():
    def __init__(self , root  , select_mode = "browse" , hover_background_color = "lightcyan"):
        self.root = root
        self.select_mode = select_mode
        self.hover_background_color = hover_background_color
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
# root = tk.Tk()
# root.title("test")
# root.geometry("300x400")
# manager(root)
# root.mainloop()