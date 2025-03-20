# welcome_tab.py
import sys
import os
import webbrowser
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

class WelcomeTab(ttk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.create_content()

    def create_content(self):
        main_frame = ttk.Frame(self, padding=20)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Načtení loga s ošetřením chyb
        try:
            img = Image.open("logo.jpg")
            img = img.resize((48, 58), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(img)
            ttk.Label(main_frame, image=self.logo).pack(pady=10)
        except Exception as e:
            print(f"Chyba při načítání loga: {str(e)}")

        # Hlavní obsah
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(expand=True)

        ttk.Label(
            content_frame,
            text="PDF Toolkit",
            font=("Segoe UI", 24, "bold"),
            foreground=self.main_app.current_palette["accent"]
        ).pack(pady=10)
        
        # Verze
        ttk.Label(
            content_frame,
            text="Verze 1.0.1",
            font=("Segoe UI", 10)
        ).pack(pady=5)

        # Autoři
        ttk.Label(
            content_frame,
            text="Vytvořil: Jan Dvořák\n© 2025",
            font=("Segoe UI", 9),
            justify="center"
        ).pack(pady=10)

        ttk.Button(
            content_frame,
            text="GitHub Repozitář",
            command=lambda: webbrowser.open("https://github.com/Honzous00/PDFAlchemy"),
            style="WhiteLink.TButton"
        ).pack(pady=5)

        # Styly
        self.style = ttk.Style()
        self.style.configure(
            "WhiteLink.TButton",
            foreground="white",
            font=("Segoe UI", 9, "underline"),
            borderwidth=0
        )