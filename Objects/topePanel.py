import sys , os
import tkinter as tk
from tkinter import ttk

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..' , 'Objects')))
# from variables import general_variables


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..' , 'Objects')))
from tree_view import manager

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..' , 'Objects')))
from variables import general_variables , open_fileExplorer

import json

general_vars = general_variables()
file_explorer = open_fileExplorer()

class addTemplate_topePanel():
    def __init__(self , root , tree : manager , window : tk.Toplevel):
        self.root = root
        #
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
        self.read_internal_templates("in", self.internal_temps_list)
        self.internal_temps_list.pack(fill=tk.BOTH , expand=True)
        self.scrolbar_internal_temps.config(command=self.internal_temps_list.yview)
        
        self.scrolbar_external_temps = tk.Scrollbar(self.external_templates)
        self.scrolbar_external_temps.pack( fill=tk.Y , side=tk.RIGHT)
        self.external_temps_list = tk.Listbox(self.external_templates , yscrollcommand=self.scrolbar_external_temps.set)
        self.read_internal_templates("ex", self.external_temps_list)
        self.external_temps_list.pack(fill=tk.BOTH , expand=True)
        self.scrolbar_external_temps.config(command=self.external_temps_list.yview)
        #Actions
        self.template_notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)
        self.internal_temps_list.bind("<<ListboxSelect>>", self.on_select_internal_temps_list)
        self.external_temps_list.bind("<<ListboxSelect>>", self.on_select_external_temps_list)
        self.update_search_entry()
    
    #Methods
    def read_internal_templates(self , temp_mod : str , list : tk.Listbox):
        self.read_path = general_vars.get_pathes()
        self.folder_path = ""
        if temp_mod =="in":
            self.folder_path = self.read_path["in_temps_path"]
        else :
            self.folder_path = self.read_path["ex_temps_path"]
        print(f"folder path : {self.folder_path}")
        for file_name in os.listdir(self.folder_path):
            full_path = os.path.join(self.folder_path , file_name)
            if os.path.isfile(full_path):
                name_without_format = os.path.splitext(file_name)[0]
                list.insert(tk.END , name_without_format)
                # print(f"File name : {name_without_format}")
                # print(f"Path : {full_path}")
                # print("_________________________________")
        
    def update_search_entry(self , internal_temp = True):
        if internal_temp:
            self.selected_tag_item = self.internal_temps_list.curselection()
            print(f"internal item selected : {self.selected_tag_item}")
        else :
            self.selected_tag_item = self.external_temps_list.curselection()
            print(f"external item selected : {self.selected_tag_item}")
        
        if self.selected_tag_item:
            #selected_items = [listbox.get(i) for i in selected_indices]
            if internal_temp:
                self.selected_item = self.internal_temps_list.get(self.selected_tag_item)
            else :
                self.selected_item = self.external_temps_list.get(self.selected_tag_item)
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
    
    def update_search_entry_in(self , internal_temp = True):
        if internal_temp:
            self.selected_tag_item = self.internal_temps_list.curselection()
            print(f"internal item selected : {self.selected_tag_item}")
        else :
            self.selected_tag_item = self.external_temps_list.curselection()
            print(f"external item selected : {self.selected_tag_item}")
        
        if self.selected_tag_item:
            #selected_items = [listbox.get(i) for i in selected_indices]
            if internal_temp:
                self.selected_item = self.internal_temps_list.get(self.selected_tag_item)
            else :
                self.selected_item = self.external_temps_list.get(self.selected_tag_item)
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
    def on_tab_changed(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")

        if tab_text == "Ready templates":
            self.internal_temps_list.selection_set(0)  # انتخاب آیتم اول
            self.internal_temps_list.event_generate("<<ListboxSelect>>")
        elif tab_text == "Project templates":
            self.external_temps_list.selection_set(0)
            self.external_temps_list.event_generate("<<ListboxSelect>>")



    def on_select_internal_temps_list(self , event):
        self.update_search_entry(True)
    
    def on_select_external_temps_list(self , event):
        self.update_search_entry(False)
    

    def add_item_to_treeview(self):
        self.selected_temp = self.entry_template_name.get()
        if self.selected_temp in self.internal_temps_list.get(0 , tk.END):
            self.tree.add_child(self.selected_temp)
            general_vars.save_tree_state(self.selected_temp , f"{general_vars.get_pathes()["in_temps_path"]}/{self.selected_temp}.json")
            self.window.destroy()
        elif self.selected_temp in self.external_temps_list.get(0 , tk.END):
            self.tree.add_child(self.selected_temp)
            general_vars.save_tree_state(self.selected_temp , f"{general_vars.get_pathes()["project_path"]}/templates/{self.selected_temp}.json")
            self.window.destroy()
        else:
            print(f"There isn't any template with '{self.selected_temp} name !!'")

# root = tk.Tk()
# app = addTemplate_topePanel(root , ttk.Treeview(root))
# root.mainloop()