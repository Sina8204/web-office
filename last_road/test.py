# from tkinter import Tk
# from tkhtmlview import HTMLLabel

# root = Tk()
# root.title("HTML Viewer Panel")
# root.geometry("500x400")

# html_code = """
# <h2 style='color:blue;'>سلام سینا!</h2>
# <p>این یک پنل ساده برای نمایش HTML در tkinter هست.</p>
# <ul>
#   <li>پشتیبانی از تگ‌های ساده</li>
#   <li>بدون جاوااسکریپت</li>
# </ul>
# """

# html_label = HTMLLabel(root, html=html_code)
# html_label.pack(fill="both", expand=True)

# root.mainloop()
###################################################################################
# import tkinter as tk

# root = tk.Tk()
# root.title("پنجره تست")
# root.geometry("300x200")

# label = tk.Label(root, text="سلام سینا!")
# label.pack()

# root.mainloop()
###################################################################################
# import webview

# # مسیر فایل HTML که شامل CSS و JS هست
# html_file = 'file:///D:/python projects/web office/sample.html'

# # ساخت پنجره
# webview.create_window("پنل HTML کامل", html_file, width=800, height=600)
# webview.start()

# from cefpython3 import cefpython as cef
# import tkinter as tk
# import sys

# class MainApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("پنل HTML با پشتیبانی کامل")
#         self.root.geometry("800x600")

#         # مقداردهی اولیه CEF
#         cef.Initialize()

#         # ساخت فریم برای جاسازی مرورگر
#         self.frame = tk.Frame(root, width=800, height=600)
#         self.frame.pack(fill=tk.BOTH, expand=True)

#         # گرفتن هندل پنجره برای جاسازی مرورگر
#         window_info = cef.WindowInfo()
#         window_info.SetAsChild(self.frame.winfo_id(), [0, 0, 800, 600])

#         # مسیر فایل HTML
#         html_path = "file:///D:/python projects/web office/sample.html"

#         # ساخت مرورگر و بارگذاری فایل HTML
#         self.browser = cef.CreateBrowserSync(window_info, url=html_path)

#         # اجرای حلقه CEF در کنار tkinter
#         self.root.after(10, self.loop_cef)

#     def loop_cef(self):
#         cef.MessageLoopWork()
#         self.root.after(10, self.loop_cef)

#     def on_close(self):
#         cef.Shutdown()
#         self.root.destroy()

# # اجرای برنامه
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MainApp(root)
#     root.protocol("WM_DELETE_WINDOW", app.on_close)
#     root.mainloop()
###################################################################################
# import tkinter as tk

# root = tk.Tk()
# root.title("پنل‌های قابل تغییر اندازه")
# root.geometry("800x500")

# # ساخت پنجره اصلی با جهت افقی
# paned = tk.PanedWindow(root, orient=tk.HORIZONTAL)
# paned.pack(fill=tk.BOTH, expand=True)

# # پنل سمت چپ
# left_panel = tk.Frame(paned, bg="lightgreen", width=200)
# paned.add(left_panel)

# # پنل سمت راست
# right_panel = tk.Frame(paned, bg="lightblue")
# paned.add(right_panel)

# # افزودن ویجت‌ها
# tk.Label(left_panel, text="منوی کناری").pack(pady=10)
# tk.Label(right_panel, text="محتوای اصلی").pack(pady=10)

# root.mainloop()
###################################################################################

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title("پنل‌های تب‌دار")
# root.geometry("600x400")

# notebook = ttk.Notebook(root)
# notebook.pack(fill="both", expand=True)

# panel1 = tk.Frame(notebook, bg="lightyellow")
# panel2 = tk.Frame(notebook, bg="lightgray")
# panel3 = tk.Frame(notebook, bg="lightblue")

# notebook.add(panel1, text="پنل ۱")
# notebook.add(panel2, text="پنل ۲")
# notebook.add(panel3, text="پنل ۳")

# tk.Label(panel1, text="محتوای پنل اول").pack(pady=20)
# tk.Label(panel2, text="محتوای پنل دوم").pack(pady=20)
# tk.Label(panel3, text="محتوای پنل سوم").pack(pady=20)

# root.mainloop()

#########################################################################
# import tkinter as tk

# class DraggableWidget(tk.Label):
#     def __init__(self, master, text, x, y):
#         super().__init__(master, text=text, bg="lightgray", relief="raised", bd=2)
#         self.place(x=x, y=y)
#         self.bind("<ButtonPress-1>", self.start_drag)
#         self.bind("<B1-Motion>", self.do_drag)
#         self._drag_data = {"x": 0, "y": 0}

#     def start_drag(self, event):
#         self._drag_data["x"] = event.x
#         self._drag_data["y"] = event.y

#     def do_drag(self, event):
#         dx = event.x - self._drag_data["x"]
#         dy = event.y - self._drag_data["y"]
#         x = self.winfo_x() + dx
#         y = self.winfo_y() + dy
#         self.place(x=x, y=y)

# class UIEditor:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("رابط طراحی فرم و مرحله")
#         self.root.geometry("1000x600")

#         # پنل ابزار سمت چپ
#         self.toolbox = tk.Frame(root, bg="lightblue", width=200, height=600)
#         self.toolbox.place(x=0, y=0)

#         # بوم طراحی وسط
#         self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
#         self.canvas.place(x=200, y=0)

#         self.toolbox.bind("<ButtonPress-1>", lambda e: self.start_drag(e, self.toolbox))
#         self.toolbox.bind("<B1-Motion>", lambda e: self.do_drag(e, self.toolbox))

#         self.canvas.bind("<ButtonPress-1>", lambda e: self.start_drag(e, self.canvas))
#         self.canvas.bind("<B1-Motion>", lambda e: self.do_drag(e, self.canvas))


#         # لیست ویجت‌های قابل کشیدن
#         self.widgets = ["Label", "Entry", "Button"]
#         for i, w in enumerate(self.widgets):
#             btn = tk.Button(self.toolbox, text=w, command=lambda w=w: self.spawn_widget(w))
#             btn.pack(pady=10, padx=10, fill="x")

#     def spawn_widget(self, widget_type):
#         x, y = 50, 50  # موقعیت اولیه روی بوم
#         if widget_type == "Label":
#             DraggableWidget(self.canvas, "برچسب", x, y)
#         elif widget_type == "Entry":
#             entry = tk.Entry(self.canvas)
#             entry.place(x=x, y=y, width=150)
#             entry.bind("<ButtonPress-1>", lambda e: self.start_drag(e, entry))
#             entry.bind("<B1-Motion>", lambda e: self.do_drag(e, entry))
#         elif widget_type == "Button":
#             btn = tk.Button(self.canvas, text="دکمه")
#             btn.place(x=x, y=y)
#             btn.bind("<ButtonPress-1>", lambda e: self.start_drag(e, btn))
#             btn.bind("<B1-Motion>", lambda e: self.do_drag(e, btn))

#     def start_drag(self, event, widget):
#         widget._drag_data = {"x": event.x, "y": event.y}

#     def do_drag(self, event, widget):
#         dx = event.x - widget._drag_data["x"]
#         dy = event.y - widget._drag_data["y"]
#         x = widget.winfo_x() + dx
#         y = widget.winfo_y() + dy
#         widget.place(x=x, y=y)

# # اجرای برنامه
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = UIEditor(root)
#     root.mainloop()
#################################################################################

# import tkinter as tk

# def open_tool_panel():
#     panel = tk.Toplevel()
#     panel.title("پنل ابزار")
#     panel.geometry("300x200")
#     panel.configure(bg="lightblue")

#     tk.Label(panel, text="ابزارها", bg="lightblue").pack(pady=10)
#     tk.Button(panel, text="ابزار ۱").pack(pady=5)
#     tk.Button(panel, text="ابزار ۲").pack(pady=5)

# root = tk.Tk()
# root.title("پنجره اصلی")
# root.geometry("600x400")

# tk.Button(root, text="باز کردن پنل ابزار", command=open_tool_panel).pack(pady=20)

# root.mainloop()
#########################################################################################

# import tkinter as tk
# from tkinter import ttk
# import json
# import os

# class DraggableNotebook(ttk.Notebook):
#     def __init__(self, master):
#         super().__init__(master)
#         self.bind("<ButtonPress-1>", self.on_press)
#         self.bind("<B1-Motion>", self.on_drag)
#         self._drag_index = None

#     def on_press(self, event):
#         self._drag_index = self.index("@%d,%d" % (event.x, event.y))

#     def on_drag(self, event):
#         try:
#             target_index = self.index("@%d,%d" % (event.x, event.y))
#             if target_index != self._drag_index:
#                 self._swap_tabs(self._drag_index, target_index)
#                 self._drag_index = target_index
#         except:
#             pass

#     def _swap_tabs(self, i1, i2):
#         tab1 = self.tabs()[i1]
#         tab2 = self.tabs()[i2]
#         text1 = self.tab(tab1, "text")
#         text2 = self.tab(tab2, "text")
#         widget1 = self.nametowidget(tab1)
#         widget2 = self.nametowidget(tab2)

#         self.forget(i1)
#         self.insert(i1, widget2, text=text2)
#         self.forget(i2)
#         self.insert(i2, widget1, text=text1)

# class WorkspaceManager:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Workspace قابل چیدمان")
#         self.root.geometry("900x600")

#         self.layout_file = "layout.json"

#         # نوار ابزار بالا
#         self.toolbar = tk.Frame(root, bg="#e0e0e0", height=40)
#         self.toolbar.pack(side="top", fill="x")

#         tk.Button(self.toolbar, text="➕ افزودن تب", command=self.add_tab).pack(side="left", padx=5, pady=5)
#         tk.Button(self.toolbar, text="💾 ذخیره چیدمان", command=self.save_layout).pack(side="left", padx=5)
#         tk.Button(self.toolbar, text="🔄 بارگذاری مجدد", command=self.reload_layout).pack(side="left", padx=5)

#         # دفترچه تب‌ها
#         self.notebook = DraggableNotebook(root)
#         self.notebook.pack(fill="both", expand=True)

#         self.load_layout()

#     def add_tab(self, name="تب جدید"):
#         frame = tk.Frame(self.notebook, bg="white")
#         tk.Label(frame, text=f"محتوای {name}").pack(pady=20)
#         self.notebook.add(frame, text=name)
#         self.save_layout()

#     def save_layout(self):
#         layout = [self.notebook.tab(tab_id, "text") for tab_id in self.notebook.tabs()]
#         with open(self.layout_file, "w", encoding="utf-8") as f:
#             json.dump(layout, f, ensure_ascii=False, indent=2)

#     def load_layout(self):
#         if os.path.exists(self.layout_file):
#             with open(self.layout_file, "r", encoding="utf-8") as f:
#                 layout = json.load(f)
#             for name in layout:
#                 self.add_tab(name)

#     def reload_layout(self):
#         self.notebook.forget("all")
#         self.load_layout()

# # اجرای برنامه
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = WorkspaceManager(root)
#     root.mainloop()

#########################################################################################
# import tkinter as tk
# from tkinter import ttk
# from cefpython3 import cefpython as cef
# import sys
# import os

# class MainApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("800x600")
#         self.root.title("نمایش HTML داخل برنامه")

#         # ساخت تب‌ها
#         self.notebook = ttk.Notebook(root)
#         self.notebook.pack(fill="both", expand=True)

#         # تب HTML
#         self.html_tab = tk.Frame(self.notebook)
#         self.notebook.add(self.html_tab, text="HTML Viewer")

#         # پنل مرورگر
#         self.browser_frame = tk.Frame(self.html_tab, width=800, height=600)
#         self.browser_frame.pack(fill="both", expand=True)

#         # مقداردهی اولیه CEF
#         self.init_browser()

#         # اجرای حلقه ترکیبی
#         self.root.after(10, self.cef_loop)

#     def init_browser(self):
#         cef.Initialize()
#         window_info = cef.WindowInfo()
#         hwnd = self.browser_frame.winfo_id()
#         window_info.SetAsChild(hwnd, [0, 0, 800, 600])

#         html_path = os.path.abspath("GUI\VideoQuickNote_QuickLearning.html")
#         html_url = f"file://{html_path}"
#         self.browser = cef.CreateBrowserSync(window_info, url=html_url)

#     def cef_loop(self):
#         cef.MessageLoopWork()
#         self.root.after(10, self.cef_loop)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MainApp(root)
#     root.mainloop()

#######################################treeview#####################################
# import tkinter as tk
# from tkinter import ttk
# import json

# root = tk.Tk()
# root.title("درگ و دراپ با انتخاب چندگانه صحیح")
# root.geometry("500x400")

# tree = ttk.Treeview(root, selectmode="browse")
# tree.pack(fill=tk.BOTH, expand=True)

# # افزودن آیتم‌ها
# folder1 = tree.insert("", "end", text="پوشه اول")
# tree.insert(folder1, "end", text="فایل ۱")
# tree.insert(folder1, "end", text="فایل ۲")

# folder2 = tree.insert("", "end", text="پوشه دوم")
# tree.insert(folder2, "end", text="فایل A")
# tree.insert(folder2, "end", text="فایل B")

# # تنظیم رنگ‌ها
# #tree.tag_configure("highlight", background="lightblue")
# tree.tag_configure("hover_target", background="lightcyan")

# dragging_items = []
# hovered_item = None

# def on_tree_select(event):
#     # پاک‌کردن هایلایت‌های قبلی
#     for item in tree.get_children():
#         tree.item(item, tags=())

# def on_button_press(event):
#     # تأخیر کوتاه برای اطمینان از ثبت انتخاب نهایی
#     root.after(10, start_drag)

# def start_drag():
#     global dragging_items
#     dragging_items = tree.selection()
#     for item in dragging_items:
#         tree.item(item, tags=("highlight",))

# def on_mouse_motion(event):
#     global hovered_item
#     current_hover = tree.identify_row(event.y)

#     if hovered_item and hovered_item != current_hover:
#         tree.item(hovered_item, tags=())

#     if current_hover:
#         tree.item(current_hover, tags=("hover_target",))
#         hovered_item = current_hover
#     else:
#         hovered_item = None

# def is_descendant(item, target):
#     # بررسی اینکه آیا target فرزند یا نوه‌ی item هست
#     children = tree.get_children(item)
#     if target in children:
#         return True
#     for child in children:
#         if is_descendant(child, target):
#             return True
#     return False

# def on_button_release(event):
#     global dragging_items, hovered_item
#     target_item = tree.identify_row(event.y)

#     if target_item:
#         for item in dragging_items:
#             # جلوگیری از جابجایی آیتم به خودش یا فرزندانش
#             if item == target_item or is_descendant(item, target_item):
#                 print("❌ نمی‌توان آیتم را داخل خودش یا فرزندانش منتقل کرد.")
#                 continue
#             tree.move(item, target_item, "end")
#         save_tree_state()
#     else:
#         print("هیچ آیتم مقصدی انتخاب نشده.")

#     for item in dragging_items:
#         tree.item(item, tags=())
#     if hovered_item:
#         tree.item(hovered_item, tags=())
#     dragging_items = []
#     hovered_item = None


# def save_tree_state():
#     def recurse(item):
#         children = tree.get_children(item)
#         return {
#             "text": tree.item(item)["text"],
#             "children": [recurse(child) for child in children]
#         }

#     structure = [recurse(child) for child in tree.get_children("")]
#     with open("tree_state.json", "w", encoding="utf-8") as f:
#         json.dump(structure, f, ensure_ascii=False, indent=2)
#     print("✅ وضعیت درخت ذخیره شد.")

# tree.bind("<<TreeviewSelect>>", on_tree_select)
# tree.bind("<ButtonPress-1>", on_button_press) #select items to move
# tree.bind("<B1-Motion>", on_mouse_motion) #highlight hover item
# tree.bind("<ButtonRelease-1>", on_button_release) #move items

# root.mainloop()

############################################################################


import tkinter as tk

def update_entry():
    selected_indices = listbox.curselection()
    if selected_indices:
        selected_items = [listbox.get(i) for i in selected_indices]
        entry.config(state='normal')  # فعال‌سازی برای تغییر متن
        entry.delete(0, tk.END)
        entry.insert(0, ", ".join(selected_items))
        entry.config(fg='black', state='readonly')  # غیرفعال‌سازی مجدد
    else:
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.insert(0, "no selected")
        entry.config(fg='gray', state='readonly')

def on_select(event):
    update_entry()

root = tk.Tk()
root.title("لیست باکس با نوار نمایش انتخاب")

# نوار نمایش بالا (غیرفعال برای تایپ)
entry = tk.Entry(root, font=("Arial", 14), fg='gray', state='readonly')
entry.insert(0, "no selected")
entry.pack(padx=10, pady=10)

# لیست باکس با انتخاب چندگانه
listbox = tk.Listbox(root, font=("Arial", 14), height=6, selectmode=tk.EXTENDED)
items = ["سیب", "پرتقال", "موز", "هلو", "انگور", "آلبالو"]
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(padx=10, pady=10)

listbox.bind("<<ListboxSelect>>", on_select)
#update_entry()

root.mainloop()



# import tkinter as tk
# from tkinter import messagebox

# # تابع جست‌وجو
# def search():
#     query = entry.get()
#     if query:
#         results_list.delete(0, tk.END)
#         # شبیه‌سازی نتایج جست‌وجو
#         dummy_results = [f"نتیجه {i+1} برای '{query}'" for i in range(5)]
#         for result in dummy_results:
#             results_list.insert(tk.END, result)
#     else:
#         messagebox.showwarning("هشدار", "لطفاً عبارتی برای جست‌وجو وارد کنید.")

# # ساخت پنجره اصلی
# root = tk.Tk()
# root.title("منوی جست‌وجو")
# root.geometry("400x300")

# # فیلد ورودی
# entry = tk.Entry(root, font=("Arial", 14))
# entry.pack(pady=10)

# # دکمه جست‌وجو
# search_button = tk.Button(root, text="جست‌وجو", command=search, font=("Arial", 12))
# search_button.pack(pady=5)

# # لیست نتایج
# results_list = tk.Listbox(root, font=("Arial", 12), height=10)
# results_list.pack(pady=10, fill=tk.BOTH, expand=True)

# # اجرای برنامه
# root.mainloop()
