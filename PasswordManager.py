# PasswordManager.py
import os
import sys
import json
import keyring
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import ttk

class PasswordManager:
    def __init__(self):
        self.DB_FILE = "passwords.json"
        self.key = self._get_or_create_key()

    def _get_or_create_key(self):
        key_str = keyring.get_password("pdf_encryptor", "encryption_key")
        if not key_str:
            key = Fernet.generate_key()
            key_str = key.decode()
            keyring.set_password("pdf_encryptor", "encryption_key", key_str)
        try:
            Fernet(key_str.encode())
        except ValueError:
            key = Fernet.generate_key()
            key_str = key.decode()
            keyring.set_password("pdf_encryptor", "encryption_key", key_str)
        return key_str.encode()

    def _get_cipher(self):
        return Fernet(self.key)

    def save_password(self, password_name, password):
        cipher = self._get_cipher()
        encrypted = cipher.encrypt(password.encode()).decode()
        data = self._load_db()
        data[password_name] = encrypted
        self._save_db(data)

    def get_password(self, password_name):
        data = self._load_db()
        if password_name not in data:
            return None
        try:
            cipher = self._get_cipher()
            return cipher.decrypt(data[password_name].encode()).decode()
        except:
            return None

    def get_all_passwords(self):
        return self._load_db()

    def delete_password(self, password_name):
        data = self._load_db()
        if password_name in data:
            del data[password_name]
            self._save_db(data)

    def _load_db(self):
        if not os.path.exists(self.DB_FILE):
            return {}
        with open(self.DB_FILE, "r") as f:
            return json.load(f)

    def _save_db(self, data):
        with open(self.DB_FILE, "w") as f:
            json.dump(data, f)

class PasswordDatabaseWindow(tk.Toplevel):
    def __init__(self, parent, pm, target_entries=None):
        super().__init__(parent)
        self.pm = pm
        self.parent = parent
        self.target_entries = target_entries
        self.title("Správa hesel")
        self.geometry("400x300")
        
        self.listbox = tk.Listbox(
            self,
            bg=parent.current_palette.get("entry_bg", "#FFFFFF"),  # Fallback na bílou
            fg=parent.current_palette.get("fg", "#000000"),         # Fallback na černou
            selectbackground=parent.current_palette.get("accent", "#2196F3"),
            selectforeground="white",
            relief="flat"
        )
        
        self.listbox.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Použít", command=self.use_password).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Odstranit", command=self.delete_selected_password).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Zrušit", command=self.destroy).pack(side=tk.LEFT, padx=5)
        
        self._load_passwords()
    
    def _load_passwords(self):
        self.listbox.delete(0, tk.END)
        passwords = self.pm.get_all_passwords()
        for name in passwords.keys():
            self.listbox.insert(tk.END, name)
    
    def use_password(self):
        selection = self.listbox.curselection()
        if selection:
            password_name = self.listbox.get(selection[0])
            password = self.pm.get_password(password_name)
            if password and self.target_entries:
                for entry in self.target_entries:
                    entry.delete(0, tk.END)
                    entry.insert(0, password)
                self.destroy()
    
    def delete_selected_password(self):
        selection = self.listbox.curselection()
        if selection:
            password_name = self.listbox.get(selection[0])
            self.pm.delete_password(password_name)
            self._load_passwords()
            messagebox.showinfo("Info", f"Heslo '{password_name}' bylo odstraněno.")