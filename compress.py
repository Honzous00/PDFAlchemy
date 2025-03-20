# compress.py
import os
import sys
import threading
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class PDFCompressor(ttk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.current_palette = main_app.current_palette
        self.input_files = []
        self.output_dir = ""
        
        # Ghostscript cesta s ošetřením pro PyInstaller
        try:
            base_path = sys._MEIPASS  # Pro EXE verzi
        except AttributeError:
            base_path = os.path.abspath(".")  # Pro normální běh
        self.ghostscript_path = os.path.join(sys._MEIPASS, "gs_bin", "gswin64c.exe")
        
        self.create_widgets()
        self.configure_styles()

    def configure_styles(self):
        self.style = ttk.Style()
        self.style.configure("TButton", 
            background=self.current_palette["accent"],
            foreground="white",
            font=("Segoe UI", 10, "bold")
        )
        self.style.map("TButton",
            background=[
                ("active", self.current_palette["hover"]),
                ("pressed", self.current_palette["hover"])
            ]
        )

    def create_widgets(self):
        main_frame = ttk.Frame(self, padding=10)
        main_frame.pack(expand=True, fill=tk.BOTH)

        ttk.Label(main_frame, text="Komprese PDF", font=("Segoe UI", 14, "bold")).pack(pady=10)

        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=tk.X, padx=20, pady=5)
        
        ttk.Button(file_frame, text="Vybrat PDF", command=self.select_files).pack(side=tk.LEFT)
        self.file_label = ttk.Label(file_frame, text="Žádné soubory vybrány")
        self.file_label.pack(side=tk.LEFT, padx=5)

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, padx=20, pady=20)
        ttk.Button(
            button_frame, 
            text="Spustit kompresi", 
            command=self.start_compression
        ).pack(expand=True, fill=tk.X)

    def select_files(self):
        self.input_files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        if self.input_files:
            self.file_label.config(text=f"Vybráno souborů: {len(self.input_files)}")

    def start_compression(self):
        if not self.input_files:
            messagebox.showerror("Chyba", "Nejprve vyberte PDF soubory!")
            return
            
        # Vyber výstupní složku v hlavním vlákně
        self.output_dir = filedialog.askdirectory(title="Vyberte výstupní složku")
        if not self.output_dir:
            return

        if not os.path.exists(self.ghostscript_path):
            messagebox.showerror("Chyba", 
                f"Ghostscript nenalezen!\nHledaná cesta: {self.ghostscript_path}"
            )
            return

        # Spustit kompresi s progresem
        self.main_app.status_bar.config(text="🔄 Spouštím kompresi...")
        threading.Thread(target=self.compress_files, daemon=True).start()

    def compress_files(self):
        try:
            total = len(self.input_files)
            for i, input_path in enumerate(self.input_files, 1):
                output_name = f"compressed_{os.path.basename(input_path)}"
                output_path = os.path.join(self.output_dir, output_name)
                
                # Aktualizace stavu PŘED kompresí
                self.main_app.after(0, self._update_status, 
                    f"🔁 Komprimuji {i}/{total}: {os.path.basename(input_path)}"
                )
                
                command = [
                    f'"{self.ghostscript_path}"',
                    "-sDEVICE=pdfwrite",
                    "-dPDFSETTINGS=/screen",
                    "-dNOPAUSE",
                    "-dBATCH",
                    f'-sOutputFile="{output_path}"',
                    f'"{input_path}"'
                ]
                
                # Spuštění a zachycení výstupu
                subprocess.run(
                    " ".join(command),
                    shell=True,
                    check=True,
                    stdout=subprocess.DEVNULL,  # Potlačit výpis do konzole
                    stderr=subprocess.PIPE
                )
                
                # Okamžitá aktualizace po dokončení souboru
                self.main_app.after(0, self._update_status,
                    f"✅ Hotovo {i}/{total}: {os.path.basename(input_path)}",
                    "success"
                )

            # Finální zpráva
            self.main_app.after(0, self._update_status,
                "✅ Všechny soubory komprimovány",
                "success"
            )

        except Exception as e:
            self.main_app.after(0, self._update_status,
                f"❌ Chyba: {str(e)}",
                "error"
            )
    def _update_status(self, text, style=None):
        """Univerzální metoda pro aktualizaci stavového řádku"""
        self.main_app.status_bar.config(text=text)
        
        if style == "success":
            self.main_app.status_bar.config(background="#C8E6C9", foreground="#000000")
        elif style == "error":
            self.main_app.status_bar.config(background="#FFCDD2", foreground="#000000")
        else:
            self.main_app.status_bar.config(
                background=self.main_app.current_palette["bg"],
                foreground=self.main_app.current_palette["fg"]
            )
        
        # Okamžité překreslení UI
        self.main_app.status_bar.update_idletasks()     
        
    def reset(self):
        self.input_files = []
        self.file_label.config(text="Žádné soubory vybrány")
        
    def update_theme(self, palette):
        self.current_palette = palette
        self.configure_styles()