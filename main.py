# main.py
import sys
import os
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from welcome_tab import WelcomeTab
from encryptor import PDFEncryptor
from decryptor import PDFDecryptor
from compress import PDFCompressor
from PasswordManager import PasswordManager

class PDFToolkit(ThemedTk):
    def __init__(self):
        super().__init__()
        self.current_tab_index = 0
        self.modules = []  # Pro ukládání modulů
        self.pm = PasswordManager()
        
        # Palety barev
        self.light_palette = {
            "bg": "#F8F9FA",
            "fg": "#212529",
            "accent": "#2196F3",
            "hover": "#1976D2",
            "tab_bg": "#E3F2FD",
            "tab_fg": "#1565C0",
            "status_ok": "#2ECC71",   # Zelená pro úspěch
            "status_error": "#E74C3C", # Červená pro chyby   
            "entry_bg": "#FFFFFF",                         
        }
        
        self.dark_palette = {
            "bg": "#1A1A1A",
            "fg": "#FFFFFF",
            "accent": "#2ECC71",
            "hover": "#239B56",
            "tab_bg": "#2D2D2D",
            "tab_fg": "#27AE60",
            "status_ok": "#27AE60",
            "status_error": "#C0392B",
            "entry_bg": "#2D2D2D"            
        }
        
        self.current_palette = self.light_palette
        
        # Nastavení hlavního okna
        self.title("PDF Toolkit")
        self.geometry("600x450")
        self.minsize(600, 450)
        self.maxsize(600, 450)
        
        self.status_bar = None 
        
        self.configure_styles()
        self.create_widgets()
        self.setup_modules()

    def configure_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Styly pro záložky
        self.style.configure("TNotebook", background=self.current_palette["bg"])
        self.style.configure("TNotebook.Tab", 
            background=self.current_palette["tab_bg"],
            foreground=self.current_palette["tab_fg"],
            padding=[15, 5],
            font=("Segoe UI", 9, "bold")
        )
        
        # Společné styly
        self.style.configure("TButton", padding=5, font=("Segoe UI", 9))
        self.style.map("TButton",
            background=[("active", self.current_palette["hover"])]
        )

    def create_widgets(self):
        # Hlavní kontejner
        main_frame = ttk.Frame(self)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Notebook se záložkami
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(expand=True, fill=tk.BOTH)
        
        # Tlačítko pro změnu motivu
        # self.theme_btn = ttk.Button(
            # main_frame, 
            # text="🌓", 
            # width=3, 
            # command=self.toggle_theme,
            # style="TButton"
        # )
        #self.theme_btn.pack_forget()
        
        # Status bar (přidej na konec metody)
        self.status_bar = ttk.Label(
            self,
            text="Připraveno",
            anchor=tk.W,
            font=("Segoe UI", 9),
            foreground=self.current_palette["fg"],
            background=self.current_palette["bg"]
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

    def setup_modules(self):
        self.welcome_tab = WelcomeTab(self.notebook, self)
        self.encryptor = PDFEncryptor(self.notebook, self)
        self.decryptor = PDFDecryptor(self.notebook, self)
        self.compressor = PDFCompressor(self.notebook, self)
        
        # Změň pořadí přidávání
        self.notebook.add(self.welcome_tab, text="Úvod")
        self.notebook.add(self.encryptor, text="Šifrování")
        self.notebook.add(self.decryptor, text="Dešifrování")
        self.notebook.add(self.compressor, text="Komprimace")

    def on_tab_changed(self, event):
        previous_index = self.current_tab_index
        current_index = self.notebook.index("current")
        
        if previous_index < len(self.modules):
            self.modules[previous_index].reset()
        
        self.current_tab_index = current_index


    def toggle_theme(self):
        self.current_palette = self.dark_palette if self.current_palette == self.light_palette else self.light_palette
        
        # Aktualizace stylů
        self.style.configure("TNotebook.Tab", 
            background=self.current_palette["tab_bg"],
            foreground=self.current_palette["tab_fg"]
        )
        
        # Aktualizace modulů
        for module in [self.encryptor, self.decryptor, self.compressor]:
            module.update_theme(self.current_palette)

if __name__ == "__main__":
    app = PDFToolkit()
    app.mainloop()