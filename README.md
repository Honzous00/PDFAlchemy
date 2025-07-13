# PDF Alchemy

## All-in-One PDF Toolkit for Encryption, Decryption, and Compression

PDF Alchemy is a versatile desktop application designed to simplify common PDF manipulation tasks. It provides a user-friendly graphical interface (GUI) for encrypting, decrypting, and compressing PDF files. This project combines Python scripting to deliver an efficient and intuitive tool.

-----

### Features

  * **PDF Encryption:** Secure your sensitive PDF documents with a password.
  * **PDF Decryption:** Remove password protection from your PDFs (requires the correct password).
  * **PDF Compression:** Reduce the file size of your PDFs, ideal for sharing or archiving.
  * **Intuitive GUI:** Easy-to-use interface built with `tkinter` and `ttkthemes`.
  * **Password Management:** Securely save and retrieve frequently used passwords via `keyring`.
  * **Cross-platform (Python script):** Runs on various operating systems with Python installed.
  * **Standalone Executable:** Available as a single `.exe` file for Windows users, eliminating the need for Python installation and external dependencies like Ghostscript.

-----

### 🇬🇧 English Version

### Installation and Usage

#### Standalone Executable (Recommended for Windows Users)

For the simplest way to use PDF Alchemy on Windows, download the latest `.exe` file from the [Releases](https://github.com/Honzous00/PDFAlchemy/releases) section of this repository.

1.  **Download:** Go to the [Releases](https://github.com/Honzous00/PDFAlchemy/releases) page and download the `PDF_Alchemy.exe` (or similar named) file under the latest release.

2.  **Run:** Execute the downloaded `.exe` file. It's a portable application, so no installation is required; it will run directly.

      * **Note on Ghostscript:** The necessary Ghostscript binaries are **included within the `.exe` package**, meaning you **do not need to install Ghostscript separately**.

#### From Source (For Developers or Advanced Users)

If you wish to run the application from source code, or contribute to its development, follow these steps:

1.  **Prerequisites:**

      * **Python:** Ensure you have Python 3.x installed (Python 3.8+ is recommended).
      * **Git:** For cloning the repository.
      * **Ghostscript:** This is **crucial for the compression functionality** when running from source. Download and install Ghostscript (version 10.0 or newer is recommended) from the [official Ghostscript website](https://www.ghostscript.com/download/gsdnld.html). Make sure the `gswin64c.exe` (on Windows) or `gs` (on Linux/macOS) executable is accessible in your system's PATH, or **update the `ghostscript_path` variable in `compress.py`** to point to its exact location.
          * **Windows example in `compress.py`:**
            ```python
            self.ghostscript_path = r"C:\\Program Files\\gs\\gs10.05.0\\bin\\gswin64c.exe"  # Adjust to your path!
            ```
          * **Linux/macOS example (if needed):**
            ```python
            self.ghostscript_path = "/usr/local/bin/gs" # Common path, verify yours
            ```

2.  **Clone the Repository:**

    ```bash
    git clone https://github.com/YourUsername/PDF-Alchemy.git
    cd PDF-Alchemy
    ```

3.  **Install Dependencies:**

      * It's highly recommended to use a virtual environment:
        ```bash
        python -m venv venv
        # On Windows
        venv\Scripts\activate
        # On macOS/Linux
        source venv/bin/activate
        ```
      * Install the required Python packages:
        ```bash
        pip install -r requirements.txt
        ```
        (If `requirements.txt` is not provided, you'll need to create it based on the `import` statements in `main.py`, `PasswordManager.py`, `compress.py`, `decryptor.py`, `encryptor.py`, `welcome_tab.py`. Key dependencies include `Pillow`, `PyMuPDF` (fitz), `keyring`, `cryptography`, `ttkthemes`.)

4.  **Run the Application:**

    ```bash
    python main.py
    ```

-----

### Project Structure

```
.
├── main.py                     # Main application entry point and GUI setup
├── encryptor.py                # Module for PDF encryption logic
├── decryptor.py                # Module for PDF decryption logic
├── compress.py                 # Module for PDF compression logic (uses Ghostscript)
├── welcome_tab.py              # Module for the welcome/info tab
├── PasswordManager.py          # Module for secure password storage and retrieval using keyring
├── logo.jpg                    # Application logo (if included)
├── requirements.txt            # Python dependencies (create if not present)
├── PDF_Alchemy_Setup.exe       # Example of standalone executable (in Releases)
└── README.md                   # This file
```

-----

### License

This project is licensed under the MIT License - see the `LICENSE` file for details.


-----

### 🇨🇿 Česká Verze

## PDF Alchemy

## Komplexní PDF Nástroj pro šifrování, dešifrování a komprimaci

PDF Alchemy je univerzální desktopová aplikace navržená pro zjednodušení běžných úloh s PDF dokumenty. Poskytuje uživatelsky přívětivé grafické rozhraní (GUI) pro šifrování, dešifrování a komprimaci souborů PDF. Tento projekt kombinuje Python skriptování s cílem poskytnout efektivní a intuitivní nástroj.

-----

### Vlastnosti

  * **Šifrování PDF:** Zabezpečte své citlivé PDF dokumenty heslem.
  * **Dešifrování PDF:** Odstraňte ochranu heslem ze svých PDF (vyžaduje správné heslo).
  * **Komprimace PDF:** Zmenšete velikost souborů PDF, ideální pro sdílení nebo archivaci.
  * **Intuitivní GUI:** Snadno použitelné rozhraní vytvořené pomocí `tkinter` a `ttkthemes`.
  * **Správa hesel:** Bezpečné ukládání a načítání často používaných hesel pomocí `keyring`.
  * **Multiplatformní (Python skript):** Běží na různých operačních systémech s nainstalovaným Pythonem.
  * **Samostatný spustitelný soubor:** K dispozici jako jediný `.exe` soubor pro uživatele Windows, což eliminuje potřebu instalace Pythonu a externích závislostí, jako je Ghostscript.

-----

### Instalace a použití

#### Samostatný spustitelný soubor (Doporučeno pro uživatele Windows)

Nejjednodušší způsob, jak používat PDF Alchemy ve Windows, je stáhnout si nejnovější soubor `.exe` ze sekce [Releases](https://github.com/Honzous00/PDFAlchemy/releases) tohoto repozitáře.

1.  **Stáhněte:** Přejděte na stránku [Releases](https://github.com/Honzous00/PDFAlchemy/releases) a stáhněte soubor `PDF_Alchemy.exe` (nebo podobně pojmenovaný) pod nejnovějším vydáním.

2.  **Spusťte:** Spusťte stažený soubor `.exe`. Jedná se o přenosnou aplikaci, takže není nutná žádná instalace; spustí se přímo.

      * **Poznámka ke Ghostscriptu:** Potřebné binární soubory Ghostscriptu jsou **zahrnuty v balíčku `.exe`**, což znamená, že **nemusíte instalovat Ghostscript zvlášť**.

#### Ze zdrojového kódu (Pro vývojáře nebo pokročilé uživatele)

Pokud chcete aplikaci spustit ze zdrojového kódu nebo přispět k jejímu vývoji, postupujte takto:

1.  **Předpoklady:**

      * **Python:** Ujistěte se, že máte nainstalovaný Python 3.x (doporučena je verze 3.8 nebo novější).
      * **Git:** Pro klonování repozitáře.
      * **Ghostscript:** Toto je **klíčové pro funkci komprimace** při spouštění ze zdrojového kódu. Stáhněte a nainstalujte Ghostscript (doporučena je verze 10.0 nebo novější) z [oficiálních stránek Ghostscriptu](https://www.ghostscript.com/download/gsdnld.html). Ujistěte se, že spustitelný soubor `gswin64c.exe` (ve Windows) nebo `gs` (v Linuxu/macOS) je přístupný ve vašem systémovém PATH, nebo **aktualizujte proměnnou `ghostscript_path` v souboru `compress.py`**, aby ukazovala na jeho přesné umístění.
          * **Příklad pro Windows v `compress.py`:**
            ```python
            self.ghostscript_path = r"C:\\Program Files\\gs\\gs10.05.0\\bin\\gswin64c.exe"  # Upravte na vaši cestu!
            ```
          * **Příklad pro Linux/macOS (pokud je potřeba):**
            ```python
            self.ghostscript_path = "/usr/local/bin/gs" # Běžná cesta, ověřte si vaši
            ```

2.  **Klonování repozitáře:**

    ```bash
    git clone https://github.com/YourUsername/PDF-Alchemy.git
    cd PDF-Alchemy
    ```

3.  **Instalace závislostí:**

      * Důrazně se doporučuje použít virtuální prostředí:
        ```bash
        python -m venv venv
        # Na Windows
        venv\Scripts\activate
        # Na macOS/Linux
        source venv/bin/activate
        ```
      * Nainstalujte požadované Python balíčky:
        ```bash
        pip install -r requirements.txt
        ```
        (Pokud soubor `requirements.txt` není dodán, budete jej muset vytvořit na základě `import` příkazů v `main.py`, `PasswordManager.py`, `compress.py`, `decryptor.py`, `encryptor.py`, `welcome_tab.py`. Mezi klíčové závislosti patří `Pillow`, `PyMuPDF` (fitz), `keyring`, `cryptography`, `ttkthemes`.)

4.  **Spuštění aplikace:**

    ```bash
    python main.py
    ```

-----

### Struktura projektu

```
.
├── main.py                     # Hlavní vstupní bod aplikace a nastavení GUI
├── encryptor.py                # Modul pro logiku šifrování PDF
├── decryptor.py                # Modul pro logiku dešifrování PDF
├── compress.py                 # Modul pro logiku komprimace PDF (používá Ghostscript)
├── welcome_tab.py              # Modul pro uvítací/informační záložku
├── PasswordManager.py          # Modul pro bezpečné ukládání a načítání hesel pomocí keyringu
├── logo.jpg                    # Logo aplikace (pokud je součástí)
├── requirements.txt            # Python závislosti (vytvořte, pokud nejsou přítomny)
├── PDF_Alchemy_Setup.exe       # Příklad samostatného spustitelného souboru (v sekci Releases)
└── README.md                   # Tento soubor
```

-----

### Licence

Tento projekt je licencován pod licencí MIT - podrobnosti naleznete v souboru `LICENSE`.

-----
