'''
Yokyu Liu
Translator GUI
'''

import tkinter as tk
from panel import *
from transl_extract import TranlsExtract as tr
from tkinter.filedialog import askopenfilename


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.view = View(self.root)

    def run(self):
        self.root.title("翻譯者")
        self.root.geometry("900x600")
        self.root.mainloop()


class View:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.side_panel = SidePanel(root)
        self.main_panel = MainPanel(root)
        self.text_panel = TextPanel(self.main_panel)
        self.view_panel = ViewPanel(self.main_panel)

        #Binding Buttons
        self.side_panel.translate_button.bind("<Button>", self.translate_text)
        self.side_panel.upload_button.bind("<Button>", self.upload_file)
        self.side_panel.clear_button.bind("<Button>", self.clear_input)
        self.side_panel.clear2_button.bind("<Button>", self.clear_output)
        self.side_panel.setting_button.bind("<Button>", self.setting)

    #Button Actions	
    def translate_text(self, event):
        text = self.text_panel.text_area.get('1.0', 'end-1c')
        translated_text = tr.transl_text(text)
        self.write_view(translated_text)

    def upload_file(self, event):
        try:
            filename = askopenfilename()
            translated_text = tr.transl_file(filename)
            self.write_view(translated_text)

        except:
            pass

    def clear_input(self, event):
        self.text_panel.text_area.delete('1.0', 'end')

    def clear_output(self, event):
        self.view_panel.view_label.configure(state='normal')
        self.view_panel.view_label.delete('1.0', 'end-1c')
        self.view_panel.view_label.configure(state='disabled')

    def setting(self, event):
        #Add Language settings
        #Add Font Change settings
        #Add Font Size settings
        print("Setting button was hit")


    #Helpful Fucntiosn Move to another file later
    def write_view(self, text):
        self.view_panel.view_label.configure(state='normal')
        self.view_panel.view_label.delete('1.0', 'end-1c')
        self.view_panel.view_label.insert('1.0', text)
        self.view_panel.view_label.configure(state='disabled')

