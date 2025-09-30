import os
import tkinter as tk
from tkinter import ttk
import sys , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..' , 'Objects')))
from treeview_class import manager
import json


class add_tag_toplevel():
    def __init__(self , root , tree : manager , window : tk.Toplevel):
        self.root = root #Master
        self.tree = tree
        self.window = window
        #Creat Search ui frame
        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(fill=tk.X , padx=10 , pady=10)
        #Creat templates ui frame
        self.template_frame = tk.Frame(self.root)
        self.template_frame.pack(fill=tk.BOTH , expand=True , padx=10 , pady=10)
        #Creat and Adding widgets to search frame
        self.button_add = tk.Button(self.search_frame , text="Add" , command=self.add_item_to_treeview) #creat button
        self.entry_template_name = tk.Entry(self.search_frame , font=("Arial", 14) ) #creat entry
        #
        self.button_add.grid(row=0 , column=0) #adding button to search frame
        self.search_frame.columnconfigure(1 , weight = 1)
        self.entry_template_name.grid(row=0 , column=1 , padx=5 , sticky='ew') #adding entry to search frame
        #creat and adding widgets to template frame
        self.template_notebook = ttk.Notebook(self.template_frame) #creat notebook
        self.template_notebook.pack(fill=tk.BOTH , expand=True) #adding notebook to template frame
        #creat frames for notebook tabs
        self.internal_templates = tk.Frame(self.template_notebook) #internal templates are loaded in this frame
        self.external_templates = tk.Frame(self.template_notebook) #external templates are loaded in this frame
        #
        self.template_notebook.add(self.internal_templates , text="Ready templates") #adding internal templates frame to notebook 1st tab
        self.template_notebook.add(self.external_templates , text="Project templates") #adding external templates frame to notebook 2nd tab
        #
        self.scrolbar_internal_temps = tk.Scrollbar(self.internal_templates)
        self.scrolbar_internal_temps.pack( fill=tk.Y , side=tk.RIGHT)
        self.internal_temps_list = tk.Listbox(self.internal_templates , yscrollcommand=self.scrolbar_internal_temps.set)
        self.read_internal_templates("templates" , self.internal_temps_list)
        self.internal_temps_list.pack(fill=tk.BOTH , expand=True)
        self.scrolbar_internal_temps.config(command=self.internal_temps_list.yview)
        #Actions
        self.internal_temps_list.bind("<<ListboxSelect>>", self.on_select)
        self.update_search_entry()
    
    #Methods
    def read_internal_templates(self , folder_path , list : tk.Listbox):
        for file_name in os.listdir(folder_path):
            full_path = os.path.join(folder_path , file_name)
            if os.path.isfile(full_path):
                name_without_format = os.path.splitext(file_name)[0]
                list.insert(tk.END , name_without_format)
                # print(f"File name : {name_without_format}")
                # print(f"Path : {full_path}")
                # print("_________________________________")
        
    def update_search_entry(self):
        self.selected_tag_item = self.internal_temps_list.curselection()
        if self.selected_tag_item:
            #selected_items = [listbox.get(i) for i in selected_indices]
            self.selected_item = self.internal_temps_list.get(self.selected_tag_item)
            self.entry_template_name.config(state='normal')  # فعال‌سازی برای تغییر متن
            self.entry_template_name.delete(0, tk.END)
            #self.entry_template_name.insert(0, ", ".join(selected_items))
            self.entry_template_name.insert(0,self.selected_item)
            self.entry_template_name.config(fg='black', state='readonly')  # غیرفعال‌سازی مجدد
        else:
            self.entry_template_name.config(state='normal')
            self.entry_template_name.delete(0, tk.END)
            self.entry_template_name.insert(0, "no selected")
            self.entry_template_name.config(fg='gray', state='readonly')
    def on_select(self , event):
        self.update_search_entry()
    
    def save_tree_state(self, Name, Path):
        def recurse(name, path):
            return {name: path}
        
        structure = recurse(Name, Path)

        try:
            if os.path.exists("temp_pathes.json") and os.path.getsize("temp_pathes.json") > 0:
                with open("temp_pathes.json", "r", encoding="utf-8") as f:
                    existing_data = json.load(f)
            else:
                existing_data = {}
        except json.JSONDecodeError:
            existing_data = {}

        existing_data.update(structure)

        with open("temp_pathes.json", "w", encoding="utf-8") as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)

        print("✅ وضعیت درخت ذخیره شد.")

    def add_item_to_treeview(self):
        self.selected_temp = self.entry_template_name.get()
        if self.selected_temp in self.internal_temps_list.get(0 , tk.END):
            self.tree.add_child(self.selected_temp)
            self.save_tree_state(self.selected_temp , f"templates/{self.selected_temp}.json")
            self.window.destroy()


# root = tk.Tk()
# root.title("test")
# root.geometry("200x100")
# app = add_tag_toplevel(root)
# root.mainloop()