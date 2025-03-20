# encryptor.py
import os
import sys
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter import StringVar, BooleanVar
import fitz
from PasswordManager import PasswordDatabaseWindow

class PDFEncryptor(ttk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app
        self.pm = main_app.pm
        self.current_palette = main_app.current_palette
        self.input_path = ""

        self.create_widgets()
        self.configure_styles()

    def configure_styles(self):
        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, font=("Segoe UI", 9))
        self.style.configure("Icon.TButton", width=5)  # Speciální styl pro ikonu

    def create_widgets(self):
        # Hlavní kontejner
        main_frame = ttk.Frame(self, padding=10)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        ttk.Label(main_frame, text="Šifrování PDF", font=("Segoe UI", 14, "bold")).pack(pady=10)        

        # Výběr souboru
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=tk.X, padx=20, pady=5)
        
        ttk.Button(file_frame, text="Vybrat PDF", command=self.select_file).pack(side=tk.LEFT)
        self.file_label = ttk.Label(file_frame, text="Žádný soubor vybrán")
        self.file_label.pack(side=tk.LEFT, padx=5)

        # Sekce pro heslo
        password_frame = ttk.Frame(main_frame)
        password_frame.pack(fill=tk.X, padx=20, pady=5)

        ttk.Label(password_frame, text="Heslo:").pack(side=tk.LEFT)
        self.entry_password = ttk.Entry(password_frame, show="*")
        self.entry_password.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Tlačítko správy hesel s větší ikonou
        ttk.Button(
            password_frame, 
            text="🗃️", 
            command=self.show_password_database,
            width=3
        ).pack(side=tk.LEFT)

        # Potvrzení hesla
        confirm_frame = ttk.Frame(main_frame)
        confirm_frame.pack(fill=tk.X, padx=20, pady=5)
        
        ttk.Label(confirm_frame, text="Potvrzení:").pack(side=tk.LEFT)
        self.entry_confirm = ttk.Entry(confirm_frame, show="*")
        self.entry_confirm.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        # Uložení hesla
        save_frame = ttk.Frame(main_frame)
        save_frame.pack(fill=tk.X, padx=20, pady=5)
        
        self.save_var = BooleanVar()
        self.save_check = ttk.Checkbutton(
            save_frame,
            text="Uložit jako:",
            variable=self.save_var,
            command=self.toggle_save_name
        )
        self.save_check.pack(side=tk.LEFT)
        
        self.save_name = ttk.Entry(save_frame, width=20, state=tk.DISABLED)
        self.save_name.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        # Síla šifrování
        strength_frame = ttk.Frame(main_frame)
        strength_frame.pack(fill=tk.X, padx=20, pady=5)
        
        self.strength = StringVar(value="aes_256")
        ttk.Label(strength_frame, text="Síla šifrování:").pack(side=tk.LEFT)
        ttk.Radiobutton(strength_frame, text="AES-256", variable=self.strength, value="aes_256").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(strength_frame, text="AES-128", variable=self.strength, value="aes_128").pack(side=tk.LEFT)

        # Hlavní tlačítko
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, padx=20, pady=20)
        ttk.Button(
            button_frame, 
            text="Zašifrovat", 
            command=self.start_process_thread
        ).pack(expand=True, fill=tk.X)

    # Zbytek metod zůstává stejný...
    def toggle_save_name(self):
        if self.save_var.get():
            self.save_name.config(state=tk.NORMAL)
        else:
            self.save_name.config(state=tk.DISABLED)
            self.save_name.delete(0, tk.END)

    def show_password_database(self):
        PasswordDatabaseWindow(self.main_app, self.pm, [self.entry_password, self.entry_confirm])
        self.entry_password.focus_set()

    def select_file(self):
        self.input_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.input_path:
            self.file_label.config(text=os.path.basename(self.input_path))
            if hasattr(self.main_app, 'status_bar'):
                self.main_app.status_bar.config(text="Soubor vybrán")

    def start_process_thread(self):
        input_path = self.input_path  # Lokální kopie
        password = self.entry_password.get()
        if not self.input_path:
            messagebox.showerror("Chyba", "Nejprve vyberte PDF soubor!")
            return

        password = self.entry_password.get()
        confirm = self.entry_confirm.get()
        
        if password != confirm:
            messagebox.showerror("Chyba", "Hesla se neshodují!")
            return

        if self.save_var.get() and self.save_name.get().strip():
            self.pm.save_password(self.save_name.get().strip(), password)
            self.save_name.delete(0, tk.END)

        threading.Thread(target=self.encrypt_pdf, args=(input_path, password), daemon=True).start()


    def encrypt_pdf(self, input_path, password):
        try:
            doc = fitz.open(self.input_path)
            encryption = fitz.PDF_ENCRYPT_AES_256 if self.strength.get() == "aes_256" else fitz.PDF_ENCRYPT_AES_128
            
            output_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")]
            )
            
            if output_path:
                doc.save(
                    output_path,
                    encryption=encryption,
                    owner_pw=password,
                    user_pw=password,
                    garbage=4
                )
                self.main_app.after(0, lambda: 
                    self.main_app.status_bar.config(
                        text="✅ Soubor úspěšně zašifrován",
                        foreground=self.current_palette["status_ok"]
                    )
                )
                
        except Exception as e:
            self.main_app.after(0, lambda: 
                self.main_app.status_bar.config(
                    text=f"❌ Chyba: {str(e)}",
                    foreground=self.current_palette["status_error"]
                )
            )
        finally:
            self.main_app.after(0, self.reset)
            if 'doc' in locals():
                doc.close()
                
    def reset(self):
        self.input_path = ""
        self.file_label.config(text="Žádný soubor vybrán")
        self.entry_password.delete(0, tk.END)
        self.entry_confirm.delete(0, tk.END)
        self.save_name.delete(0, tk.END)
        self.save_var.set(False)
        self.save_name.config(state=tk.DISABLED)
        
    def update_theme(self, palette):
        self.current_palette = palette