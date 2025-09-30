import tkinter as tk
from tkinter import ttk
from Objects.tree_view import manager
from design_tab import tags_manager_panel_gui

# ########################### <design_tab_gui> ###########################
# root = tk.Tk()
# root.title("design tab")
# root.geometry("1280x720")

# #++++++++++++++++++++++++ <PandWindows> #++++++++++++++++++++++++
# main_pw = tk.PanedWindow(root)
# main_pw.pack(fill=tk.BOTH , expand=1)

# tagsManager_and_projectFolder_pw = tk.PanedWindow(main_pw , orient=tk.VERTICAL)
# web_pw = tk.PanedWindow(main_pw)
# inspector_pw = tk.PanedWindow(main_pw)

# main_pw.add(tagsManager_and_projectFolder_pw)
# main_pw.add(web_pw)
# main_pw.add(inspector_pw)
# #++++++++++++++++++++++++ <Frames> #++++++++++++++++++++++++
# tags_manager_frame = tk.Frame(tagsManager_and_projectFolder_pw , bg="blue" , width=250)
# project_folder_frame = tk.Frame(tagsManager_and_projectFolder_pw , bg="green" , width=250)
# web_review_frame = tk.Frame(web_pw , bg="yellow" , width=600)
# inspector_frame = tk.Frame(inspector_pw , bg="blue")

# tagsManager_and_projectFolder_pw.add(tags_manager_frame)
# tagsManager_and_projectFolder_pw.add(project_folder_frame)
# web_pw.add(web_review_frame)
# inspector_pw.add(inspector_frame)
# #++++++++++++++++++++++++ <widgets> #++++++++++++++++++++++++
# tags_manager_panel_gui(tags_manager_frame)
# root.mainloop()
########################### <design_tab_gui> ###########################

# ########################### <tags_manager_panel_gui> ###########################
# root = tk.Tk()
# root.title("design tab")
# root.geometry("400x600")

# root.columnconfigure(0 , weight=1)
# root.rowconfigure(1 , weight=1)
# #++++++++++++++++++++++++ <Frames> #++++++++++++++++++++++++
# buttons_frame = tk.Frame(root , bg="red")
# buttons_frame.columnconfigure(0 , weight=1)
# buttons_frame.columnconfigure(1 , weight=1)
# buttons_frame.grid(row=0 , column=0 , sticky="ew")

# manager_frame = tk.Frame(root , bg="blue")
# manager_frame.rowconfigure(1 , weight=1)
# manager_frame.columnconfigure(0 , weight=1)
# manager_frame.grid(row=1 , column=0 , sticky="nsew")
# #++++++++++++++++++++++++ <widgets> #++++++++++++++++++++++++
# button_add = tk.Button(buttons_frame , text="Add") #master = buttons_frame
# button_delete = tk.Button(buttons_frame , text="Delete") #master = buttons_frame
# button_add.grid(row=0 , column=0 , padx=5 , pady=5, sticky="ew")
# button_delete.grid(row=0 , column=1 , padx=5 , pady=5 , sticky="ew")

# tags_manager = manager(manager_frame) #master = manager_frame

# root.mainloop()
# ########################### <tags_manager_panel_gui> ###########################

# ########################### <inspector_panel_gui> ###########################
root = tk.Tk()
root.title("design tab")
root.geometry("400x600")

root.columnconfigure(0 , weight=1)
root.rowconfigure(1 , weight=1)

#++++++++++++++++++++++++ <Frames> #++++++++++++++++++++++++
detail_frame = tk.Frame(root)
detail_frame.columnconfigure(1 , weight=1)
detail_frame.grid(row=0 , column=0 , sticky="ew")

css_styles_frame = tk.Frame(root)
css_styles_frame.columnconfigure(0 , weight=1)
css_styles_frame.columnconfigure(1 , weight=0)
css_styles_frame.rowconfigure(1 , weight=1)
css_styles_frame.grid(row=1 , column=0 , sticky="nsew")

general_tools_frame = tk.Frame(css_styles_frame)
general_tools_frame.columnconfigure(0 , weight=1)
general_tools_frame.columnconfigure(1 , weight=1)
general_tools_frame.columnconfigure(2 , weight=1)

styles_frame = tk.Frame(css_styles_frame)
styles_frame.columnconfigure(0, weight=1)  # ستون بوم
styles_frame.columnconfigure(1, weight=0)  # ستون بوم
styles_frame.rowconfigure(1, weight=1)  # سطر بوم و اسکرول‌بار

general_tools_frame.grid(row=0 , column=0 , sticky="ew")
styles_frame.grid(row=1 , column=0 , sticky="nsew")
#++++++++++++++++++++++++ <widgets> #++++++++++++++++++++++++
class_label = tk.Label(detail_frame , text="Class : " , font=("Arial" , 14))
id_label = tk.Label(detail_frame , text="ID : " , font=("Arial" , 14))
name_label = tk.Label(detail_frame , text="Name : " , font=("Arial" , 14))
path_label = tk.Label(detail_frame , text="Path :" , font=("Arial" , 14))
call_type_label = tk.Label(detail_frame , text="Call type :" , font=("Arial" , 14))

class_entry = tk.Entry(detail_frame , font=("Arial" , 14))
id_entry = tk.Entry(detail_frame , font=("Arial" , 14))
name_entry = tk.Entry(detail_frame , font=("Arial" , 14) , state="readonly")
path_entry = tk.Entry(detail_frame , font=("Arial" , 14) , state="readonly")

call_type_combobox = ttk.Combobox(detail_frame , values=["id" , "class" , "name"] , state="readonly")

class_label.grid(row=0 , column= 0)
id_label.grid(row=1 , column= 0)
name_label.grid(row=2 , column= 0)
path_label.grid(row=3 , column= 0)
call_type_label.grid(row=4 , column=0)

class_entry.grid(row=0 , column= 1 , sticky="ew")
id_entry.grid(row=1 , column= 1 , sticky="ew")
name_entry.grid(row=2 , column= 1 , sticky="ew")
path_entry.grid(row=3 , column= 1 , sticky="ew")
call_type_combobox.grid(row=4 , column=1 , sticky="ew" )

#///////////////////////////////////////////////////////////////
button_general_exert = tk.Button(general_tools_frame , text="General exert")
button_add_style = tk.Button(general_tools_frame , text="Add style")
button_Delet = tk.Button(general_tools_frame , text="Delete style")

button_general_exert.grid(row=0 , column=0 , padx=5 , pady=5 , sticky="ew")
button_add_style.grid(row=0 , column=1 , padx=5 , pady=5 , sticky="ew")
button_Delet.grid(row=0 , column=2 , padx=5 , pady=5 , sticky="ew")

#///////////////////////////////////////////////////////////////
styles_canvas = tk.Canvas(styles_frame)
scrollbar = ttk.Scrollbar(styles_frame, orient="vertical", command=styles_canvas.yview)

styles_canvas.grid(row=1, column=0, sticky="nsew")
scrollbar.grid(row=1, column=1, sticky="ns")

styles_canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = ttk.Frame(styles_canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: (
        styles_canvas.update_idletasks(),
        styles_canvas.configure(scrollregion=styles_canvas.bbox("all"))
    )
)

canvas_window = styles_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

for i in range(50):
    tk.Label(scrollable_frame, text=f"test {i}").pack()

root.mainloop()
########################## <inspector_panel_gui> ###########################

# styles_canvas = tk.Canvas(styles_frame)
# scrollbar = ttk.Scrollbar(styles_frame, orient="vertical", command=styles_canvas.yview)
# # استفاده از grid برای کنترل بهتر
# styles_canvas.grid(row=1, column=0, sticky="nsew")
# scrollbar.grid(row=1, column=1, sticky="ns")

# styles_canvas.configure(yscrollcommand=scrollbar.set)

# scrollable_frame = tk.Frame(styles_canvas)
        
# # اتصال قاب داخلی به بوم
# scrollable_frame.bind(
#     "<Configure>",
#     lambda e: styles_canvas.configure(
#     scrollregion=styles_canvas.bbox("all")
#         )
#     )

# canvas_window = styles_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# for i in range(50):
#     tk.Label(scrollable_frame , text=f"test {i}")
# styles_canvas.bind_all("<MouseWheel>", _on_mousewheel)