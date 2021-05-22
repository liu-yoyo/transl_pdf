'''
Yokyu Liu
Window Panel Configurations
'''

import tkinter as tk
from tkinter import scrolledtext

class MainPanel():
    def __init__(self, root):
        #Main Panel Configurations
        self.main_panel = tk.Frame(root, width=700, height=50, bg='forest green')
        self.main_panel.pack(expand=True, fill='both', side='left')
        self.main_panel.pack_propagate(0)

class SidePanel():
    def __init__(self, root):
        #Sidebar Panel Configurations
        self.sidebar_panel = tk.Frame(root, width=200, bg='#E0E0E0', height=500, relief='sunken', borderwidth=2)
        self.sidebar_panel.pack(expand=False, fill='both', side='right', anchor='nw')
        self.sidebar_panel.pack_propagate(0)        

        #Player control panel confirguations. Lives in sidebar panel.
        self.control_panel = tk.LabelFrame(self.sidebar_panel, bg='#E0E0E0', text='選項', padx=5, pady=5)
        self.control_panel.pack(padx=5, pady=5)

        self.translate_button = tk.Button(self.control_panel, text='翻譯')
        self.translate_button.config(width=30, height=2)
        self.translate_button.pack(pady=10)

        self.upload_button = tk.Button(self.control_panel, text='上傳文件')
        self.upload_button.config(width=30, height=2)
        self.upload_button.pack(pady=10)

        self.clear_button = tk.Button(self.control_panel, text='清除輸入')
        self.clear_button.config(width=30, height=2)
        self.clear_button.pack(pady=10)

        self.clear2_button = tk.Button(self.control_panel, text='清晰的翻譯')
        self.clear2_button.config(width=30, height=2)
        self.clear2_button.pack(pady=10)

        self.setting_button = tk.Button(self.control_panel, text='設定')
        self.setting_button.config(width=30, height=2)
        self.setting_button.pack(pady=10)

class MainPanel():
    def __init__(self, root):
        #Creates the Main Panel
        self.main_panel = tk.Frame(root, width=700, height=50)
        self.main_panel.pack(expand=True, fill='both', side='right')
        self.main_panel.pack_propagate(0)

class TextPanel(tk.Frame):
    def __init__(self, root):
        #Creates a frame to hold text area
        self.text_panel = tk.Frame(root.main_panel)
        self.text_panel.pack(expand=True, fill='both', side='top')

        self.text_area = scrolledtext.ScrolledText(root.main_panel)
        self.text_area.pack(fill='both')

class ViewPanel(tk.Frame):
    def __init__(self, root):
        #Creates a frame to hold the view area
        self.view_panel = tk.Frame(root.main_panel, relief='sunken', borderwidth=1)
        self.view_panel.pack(expand=True, fill='both', side='bottom')

        self.view_label = scrolledtext.ScrolledText(self.view_panel, state='disabled', bg='#F8F8FF')
        self.view_label.pack(fill='both')