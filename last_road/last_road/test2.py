# from cefpython3 import cefpython as cef
# import sys
# import os

# def main():
#     cef.Initialize()
    
#     # مسیر فایل HTML
#     html_file = os.path.abspath("web.html")
#     url = f"file://{html_file}"

#     # ساخت پنجره مرورگر
#     browser = cef.CreateBrowserSync(url=url,
#                                     window_title="My HTML Viewer")

#     cef.MessageLoop()
#     cef.Shutdown()

# if __name__ == "__main__":
#     main()
#################################################################
# import webbrowser
# import os

# # مسیر فایل HTML
# html_file = os.path.abspath("web.html")

# # باز کردن در مرورگر پیش‌فرض
# webbrowser.open(f"file://{html_file}")
#################################################################

import tkinter as tk
import os
import webbrowser
from cefpython3 import cefpython as cef
import threading

# مسیر فایل HTML
html_file = os.path.abspath("web.html")
html_url = f"file://{html_file}"

def open_with_cef():
    def cef_runner():
        cef.Initialize()
        cef.CreateBrowserSync(url=html_url, window_title="CEF Viewer")
        cef.MessageLoop()
        cef.Shutdown()
    threading.Thread(target=cef_runner).start()

def open_with_default_browser():
    webbrowser.open(html_url)

def open_with_custom_browser():
    browser_path = browser_entry.get().strip()
    if browser_path:
        try:
            browser = webbrowser.get(f'"{browser_path}" %s')
            browser.open(html_url)
        except webbrowser.Error:
            print("مسیر مرورگر معتبر نیست یا اجرا نشد.")
    else:
        print("لطفاً مسیر مرورگر را وارد کنید.")

# رابط گرافیکی با Tkinter
root = tk.Tk()
root.title("HTML Viewer")

btn_cef = tk.Button(root, text="اجرا با CEF", command=open_with_cef, width=30)
btn_cef.pack(pady=10)

btn_browser = tk.Button(root, text="اجرا با مرورگر پیش‌فرض", command=open_with_default_browser, width=30)
btn_browser.pack(pady=10)

# Entry برای مسیر مرورگر دلخواه
browser_entry = tk.Entry(root, width=50)
browser_entry.pack(pady=5)
browser_entry.insert(0, "C:/Program Files/Google/Chrome/Application/chrome.exe")  # مسیر نمونه

btn_custom = tk.Button(root, text="اجرا با مرورگر دلخواه", command=open_with_custom_browser, width=30)
btn_custom.pack(pady=10)

root.mainloop()
