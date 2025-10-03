import os , sys
from tkinter import filedialog as fd
from tkinter import ttk
import json

class general_variables():
    def __init__(self):
        self.folder_path = "Pathes"
        self.json_file_name = "dic.json"
        self.file_path = os.path.join(self.folder_path , self.json_file_name)
        self.initial_data = {
            "project_path" : "" ,
            "in_temps_path" : "templates"
        }
        self.__project_path = self.initial_data["project_path"]
        self.initial_data.update({"ex_temps_path" : f"{self.__project_path}/templates"})
        self.initial_data.update({"tree_temp" : f"{self.__project_path}/tree_temps.json"})

        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
            pass
        else :
            with open(self.file_path , 'w' , encoding='utf-8') as file:
                json.dump(self.initial_data , file , ensure_ascii=False , indent=4)
        
        if os.path.exists(self.get_pathes()["tree_temp"]):
            pass
        else :
            with open(self.get_pathes()["tree_temp"] , 'w+' , encoding='utf-8') as file:
                file.write("")
    
    def get_pathes(self):
        self.path_dic = {}
        try :
            if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
                with open(self.file_path , "r", encoding="utf-8") as f:
                    self.path_dic = json.load(f)
            else :
                self.path_dic = {}
        except json.JSONDecodeError:
            self.path_dic = {}
        self.initial_data = self.path_dic.copy()
        return self.path_dic
    
    def add_path (self , name : str , value):
        self.ready_pathes = self.get_pathes()
        self.ready_pathes.update({name : value})
        self.add_dic = self.ready_pathes
        try :
            if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
                with open(self.file_path , "w", encoding="utf-8") as f:
                    json.dump(self.add_dic , f , ensure_ascii=False , indent=4)
        except json.JSONDecodeError:
            print ("Json file not founded")
    
    def update_path(self , key : str , value):
        current_path = self.get_pathes()

        if key == "pro":
            current_path["project_path"] = value
            
        elif key == "ex":
            current_path["ex_temps_path"] = value
        elif key in current_path.keys():
            current_path[key] = value
        else :
            print (f"the '{key}' is not in {current_path}")
        current_path["ex_temps_path"] = f"{current_path["project_path"]}/templates"
        current_path["tree_temp"] = f"{current_path["project_path"]}/tree_temps.json"
        if os.path.exists(self.file_path):
            pass
        else:
            with open(self.get_pathes()["tree_temp"] , 'w+' , encoding='utf-8') as file:
                file.write("")
        with open(self.file_path , "w", encoding="utf-8") as f:
            json.dump(current_path , f , ensure_ascii=False , indent=4)
    
    def get_inputed_templates(self):
        tree_path = self.get_pathes()["tree_temp"]

        try:
            if os.path.exists(tree_path) and os.path.getsize(tree_path) > 0:
                with open(tree_path, "r", encoding="utf-8") as f:
                    existing_data = json.load(f)
            else:
                existing_data = {}
        except json.JSONDecodeError:
            existing_data = {}
        
        return list(existing_data.keys())

    def save_tree_state(self, Name, Path):
        def recurse(name, path):
            return {name: path}
        
        structure = recurse(Name, Path)
        tree_path = self.get_pathes()["tree_temp"]

        try:
            if os.path.exists(tree_path) and os.path.getsize(tree_path) > 0:
                with open(tree_path, "r", encoding="utf-8") as f:
                    existing_data = json.load(f)
            else:
                existing_data = {}
        except json.JSONDecodeError:
            existing_data = {}

        print(f"last : {existing_data}\n------------------------------------")

        existing_data.update(structure)

        print(f"update : {existing_data}")
        with open(tree_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)

        print("the tree status was saved :)")
    
    def delete_tree_item(self , parent):
        print(f"removing {parent} ...")
        tree_path = self.get_pathes()["tree_temp"]
        try:
            if os.path.exists(tree_path) and os.path.getsize(tree_path) > 0:
                with open(tree_path, "r", encoding="utf-8") as f:
                    existing_data = json.load(f)
            else:
                existing_data = {}
        except json.JSONDecodeError:
            existing_data = {}
        existing_data.pop(parent)
        with open(tree_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)
        print("removing is fininahed")


class open_fileExplorer():
    def __init__(self):
        pass

    def open_folder(self , Titel = "Select a folder"):
        return fd.askdirectory(title=Titel)
    
    def open_file(self , Titel = "Select a file" , mode = False):
        if mode:
            return fd.askopenfilenames(title=Titel)
        else :
            return fd.askopenfilename(title=Titel)
    
    def build_tree(self , tree : ttk.Treeview , parent, path):
        try:
            items = sorted(os.listdir(path))
            for item in items:
                full_path = os.path.join(path, item)
                display_name = f"📁 {item}" if os.path.isdir(full_path) else f"📄 {item}"
                node = tree.insert(parent, 'end', text=display_name, values=[full_path])
                if os.path.isdir(full_path):
                    self.build_tree(tree, node, full_path)
        except PermissionError:
            pass
    
    def add_tree(self , tree : ttk.Treeview , path):
        folder_path = path
        if folder_path:
            tree.delete(*tree.get_children())
            root_name = os.path.basename(folder_path)
            root_node = tree.insert('', 'end', text=f"📁 {root_name}", values=[folder_path], open=True)
            self.build_tree(tree, root_node, folder_path)

# dialog = open_fileExplorer()
# path = dialog.open_file()
# print(path)

# js = general_variables()
# fe = open_fileExplorer()
# print(js.get_pathes())
# js.add_path("test" , 20)
# print("-------------------------------------")
# print(js.get_pathes())

    #     self.enternal_template_path = "templates"
    #     self.project_path = ""
    #     self.external_template_path = ""
    
    # def open_folder(self , path_save : str):
    #     path = fd.askdirectory(title="Select your location path")
    #     if path_save == "en_tp": #enternal_template
    #         self.enternal_template_path = path
    #     elif path_save == "ex_tp": #external_template
    #         self.external_template_path = path
    #     else :
    #         self.project_path = path
    #         self.external_template_path = f"{self.project_path}/templates"
    #         # print(self.project_path)
    #         #print(self.external_template_path)

