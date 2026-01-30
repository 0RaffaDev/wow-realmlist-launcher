import tkinter as tk
from tkinter import messagebox, filedialog
import os
import json
from PIL import Image, ImageTk


VERSION = "v3.1"
AUTHOR = "GRaffaDev"
CONFIG_FILE = "config.json"

REALMS = {
    "🔥 Warmane": "set realmlist logon.warmane.com",
    "⚔️ UltimoWoW": "set realmlist logon.ultimowow.com",
    "🇦🇷 WowPatagonia": "set realmlist logon.wow-patagonia.win"
}

# ======================
# ⚙️ CONFIG
# ======================

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

config = load_config()

# ======================
# 🔧 FUNCIONES WOW
# ======================

def seleccionar_wow():
    path = filedialog.askopenfilename(
        title="Seleccioná Wow.exe",
        filetypes=[("Wow.exe", "Wow.exe")]
    )
    if not path:
        return

    base_dir = os.path.dirname(path)
    realmlist_path = os.path.join(base_dir, "Data", "esES", "realmlist.wtf")

    if not os.path.exists(realmlist_path):
        messagebox.showerror("Error", "No se encontró realmlist.wtf")
        return

    config["wow_path"] = path
    config["realmlist_path"] = realmlist_path
    save_config(config)
    messagebox.showinfo("Listo", "WoW configurado correctamente")

def cambiar_realm(nombre):
    if "wow_path" not in config:
        messagebox.showwarning("Configurar", "Primero configurá WoW")
        return
    try:
        with open(config["realmlist_path"], "w") as f:
            f.write(REALMS[nombre])
        os.startfile(config["wow_path"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ======================
# 🧠 UI STATE
# ======================

current_section = "Novedades"

# ======================
# 🖱️ HOVER GLOBAL
# ======================

def hover_on(e):
    e.widget.config(bg="#333333", cursor="hand2")

def hover_off(e, original="#252525"):
    e.widget.config(bg=original, cursor="")

def hover_top_on(e):
    e.widget.config(bg="#2b2b2b", cursor="hand2")

def hover_top_off(e):
    e.widget.config(bg="#1f1f1f", cursor="")

# ======================
# 🖥️ UI
# ======================

root = tk.Tk()
root.title("WoW Launcher")

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700

# Centrar ventana
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w // 2) - (WINDOW_WIDTH // 2)
y = (screen_h // 2) - (WINDOW_HEIGHT // 2)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")

root.resizable(False, False)

# ======================
# 📦 LAYOUT
# ======================

topbar = tk.Frame(root, bg="#1f1f1f", height=55)
topbar.pack(side="top", fill="x")

body = tk.Frame(root, bg="#121212")
body.pack(fill="both", expand=True)

sidebar = tk.Frame(body, bg="#181818", width=260)
sidebar.pack(side="left", fill="y")

content = tk.Frame(body, bg="#0e0e0e")
content.pack(side="right", fill="both", expand=True)

# ======================
# 🔁 CONTENT RENDER
# ======================

def render_content():
    for widget in content.winfo_children():
        widget.destroy()

    # Canvas para fondo animado
    canvas = tk.Canvas(content, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.update()  # fuerza tamaño real


    # Cargar imagen
    bg_img = Image.open(r"C:\Users\Gonzalo\Desktop\script wow\fondo_wow.jpg")

    # Tamaño grande tipo launcher
    bg_img = bg_img.resize((1200, 800))
    bg_photo = ImageTk.PhotoImage(bg_img)

    bg = canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    canvas.image = bg_photo  # evita que desaparezca

    # Movimiento lento
    def mover():
        canvas.move(bg, -0.2, 0)
        x1, y1, x2, y2 = canvas.bbox(bg)
        if x2 < canvas.winfo_width():
            canvas.move(bg, canvas.winfo_width(), 0)
        canvas.after(40, mover)

    mover()

    # Overlay oscuro (simula blur)
    overlay = tk.Frame(canvas, bg="#0e0e0e")
    canvas.create_window(
    canvas.winfo_width() // 2,
    canvas.winfo_height() // 2,
    window=overlay,
    width=canvas.winfo_width(),
    height=canvas.winfo_height()
)


    # Título sección
    title = tk.Label(
        overlay,
        text=current_section,
        font=("Segoe UI", 22, "bold"),
        fg="white",
        bg="#0e0e0e"
    )
    title.pack(pady=(40, 10))

    # Texto ejemplo
    text = tk.Label(
        overlay,
        text="Bienvenido al launcher\nPróximamente novedades, addons y más",
        fg="#cccccc",
        bg="#0e0e0e",
        font=("Segoe UI", 13),
        justify="center"
    )
    text.pack()


# ======================
# 🔝 TOPBAR
# ======================

def change_section(name):
    global current_section
    current_section = name
    render_content()

for sec in ["Novedades", "Addons", "Perfil", "About"]:
    btn = tk.Button(
        topbar,
        text=sec,
        bg="#1f1f1f",
        fg="white",
        bd=0,
        font=("Segoe UI", 12, "bold"),
        command=lambda s=sec: change_section(s)
    )
    btn.bind("<Enter>", hover_top_on)
    btn.bind("<Leave>", hover_top_off)
    btn.pack(side="left", padx=25, pady=10)

# ======================
# 🎮 SIDEBAR (SERVERS)
# ======================

tk.Label(
    sidebar,
    text="SERVERS",
    fg="#aaaaaa",
    bg="#181818",
    font=("Segoe UI", 11, "bold")
).pack(pady=(20, 15))

btn_config = tk.Button(
    sidebar,
    text="⚙️ Configurar WoW",
    command=seleccionar_wow,
    bg="#252525",
    fg="white",
    bd=0,
    height=2,
    font=("Segoe UI", 11, "bold")
)
btn_config.bind("<Enter>", hover_on)
btn_config.bind("<Leave>", lambda e: hover_off(e, "#252525"))
btn_config.pack(fill="x", padx=15, pady=(0, 20))

for nombre in REALMS:
    btn = tk.Button(
        sidebar,
        text=nombre,
        command=lambda n=nombre: cambiar_realm(n),
        bg="#252525",
        fg="white",
        bd=0,
        height=3,
        font=("Segoe UI", 12, "bold"),
        anchor="w",
        padx=15
    )
    btn.bind("<Enter>", hover_on)
    btn.bind("<Leave>", lambda e: hover_off(e, "#252525"))
    btn.pack(fill="x", padx=15, pady=8)

# ======================
# 🚀 START
# ======================

render_content()
root.mainloop()
