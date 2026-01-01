# TurboEDIT

A minimalist text editor inspired by **MS EDIT / DOS**, written in **Python + Kivy**.

Blue background, white pixel text, keyboard-driven workflow, no unnecessary UI.
This project is made as a DIY tool and a portfolio example.

---

## ✨ Features

* Pixel font **Press Start 2P**
* Blue background / white text (old-school style)
* Keyboard shortcuts:

  * **F1** — open file
  * **F2** — save file
  * **Ctrl+C** — copy
  * **Ctrl+X** — cut
  * **Ctrl+V** — paste
* Full keyboard support (Backspace, Enter, arrow keys)
* Works on Linux and Windows
* Can be compiled into **ELF / EXE** binaries

---

## 📦 Project structure

```
TurboEDIT/
 ├─ ms_edit_kivy.py
 ├─ PressStart2P-Regular.ttf
 └─ README.md
```

---

## 🐧 Linux (Mint / Ubuntu / Debian)

### 1️⃣ Install venv support

```bash
sudo apt update
sudo apt install python3-venv
```

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install --upgrade pip
pip install kivy pyinstaller
```

---

### ▶️ Run from source

```bash
python ms_edit_kivy.py
```

---

### 🔨 Build ELF binary

```bash
rm -rf build dist *.spec

pyinstaller \
  --onefile \
  --name TurboEDIT \
  --add-data "PressStart2P-Regular.ttf:." \
  ms_edit_kivy.py
```

Output binary:

```
dist/TurboEDIT
```

Run:

```bash
chmod +x dist/TurboEDIT
./dist/TurboEDIT
```

---

## 🪟 Windows

### 1️⃣ Install dependencies

```bat
pip install kivy pyinstaller
```

### 2️⃣ Build EXE

```bat
pyinstaller --onefile --windowed --name TurboEDIT --collect-all kivy --add-data "PressStart2P-Regular.ttf;." ms_edit_kivy.py
```

Output:

```
dist\TurboEDIT.exe
```

---

## ⚠️ Important notes

* Builds must be done **on the target OS**
* After changing name or version, always clean previous builds:

```bash
rm -rf build dist *.spec
```

---

## 🎯 Philosophy

> Limitations are style.

TurboEDIT is inspired by the DOS era, 8-bit aesthetics, and simple tools.
No distractions — just text, keyboard, and speed.

---

## 🧱 Future ideas

* status bar `Ln / Col`
* filename in window title
* `*` indicator for unsaved changes
* TurboTERM — a custom Linux terminal emulator

---

## 🗿 Author

A DIY tool made with respect for old-school computing.

**TurboEDIT** — when the 8-bit spirit lives in 2026.
