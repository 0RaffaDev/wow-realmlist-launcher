import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json
from PIL import Image, ImageTk

# ======================
# CONFIG
# ======================

VERSION = "v3.2"
AUTHOR = "GRaffaDev"
CONFIG_FILE = "config.json"

REALMS = {
    "🔥 Warmane": "set realmlist logon.warmane.com",
    "⚔️ UltimoWoW": "set realmlist logon.ultimowow.com",
    "🇦🇷 WowPatagonia": "set realmlist logon.wow-patagonia.win"
}

# ======================
# UTIL
# ======================

def center_window(win, w, h):
    win.update_idletasks()
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    x = (sw // 2) - (w // 2)
    y = (sh // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")

# ======================
# HOVER
# ======================

def hover_on(e):
    e.widget.config(bg="#333333", cursor="hand2")

def hover_off(e, bg):
    e.widget.config(bg=bg, cursor="")

def hover_top_on(e):
    e.widget.config(bg="#2b2b2b", cursor="hand2")

def hover_top_off(e):
    e.widget.config(bg="#1f1f1f", cursor="")

# ======================
# CONFIG FILE
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
# WOW
# ======================

def seleccionar_wow():
    path = filedialog.askopenfilename(
        title="Seleccioná Wow.exe",
        filetypes=[("Wow.exe", "Wow.exe")]
    )
    if not path:
        return

    base_dir = os.path.dirname(path)
    realmlist = os.path.join(base_dir, "Data", "esES", "realmlist.wtf")

    if not os.path.exists(realmlist):
        messagebox.showerror("Error", "No se encontró realmlist.wtf")
        return

    config["wow_path"] = path
    config["realmlist_path"] = realmlist
    save_config(config)
    messagebox.showinfo("OK", "WoW configurado correctamente")

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
# UI
# ======================

root = tk.Tk()
root.title("WoW Launcher")

WINDOW_W = 1100
WINDOW_H = 700
center_window(root, WINDOW_W, WINDOW_H)

root.resizable(False, False)

# ======================
# LAYOUT
# ======================

topbar = tk.Frame(root, bg="#1f1f1f", height=55)
topbar.pack(fill="x")

body = tk.Frame(root, bg="#121212")
body.pack(fill="both", expand=True)

sidebar = tk.Frame(body, bg="#181818", width=260)
sidebar.pack(side="left", fill="y")

content = tk.Frame(body, bg="#0e0e0e")
content.pack(side="right", fill="both", expand=True)

current_section = "Inicio"

# ======================
# RENDER
# ======================

def clear_content():
    for w in content.winfo_children():
        w.destroy()

def render_inicio():
    clear_content()

    canvas = tk.Canvas(content, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.update()

    img = Image.open(r"C:\Users\Gonzalo\Desktop\script wow\fondo_wow.jpg")
    img = img.resize((1400, 700))
    photo = ImageTk.PhotoImage(img)

    bg = canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.image = photo

    def mover():
        canvas.move(bg, -0.3, 0)
        _, _, x2, _ = canvas.bbox(bg)
        if x2 <= canvas.winfo_width():
            canvas.move(bg, canvas.winfo_width(), 0)
        canvas.after(40, mover)

    mover()

def render_novedades():
    clear_content()

    card = tk.Frame(content, bg="#1c1c1c", padx=40, pady=30)
    card.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        card,
        text="NOVEDADES",
        fg="white",
        bg="#1c1c1c",
        font=("Segoe UI", 20, "bold")
    ).pack(pady=(0, 15))

    tk.Label(
        card,
        text=(
            "• Cambio rápido entre servidores\n"
            "• Launcher inspirado en Blizzard\n"
            "• Interfaz moderna y simple\n\n"
            "Se vienen mejoras visuales y addons 👀"
        ),
        fg="#cccccc",
        bg="#1c1c1c",
        font=("Segoe UI", 12),
        justify="left"
    ).pack()

def render_about():
    clear_content()

    frame = tk.Frame(content, bg="#0e0e0e")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="WoW Launcher",
        font=("Segoe UI", 22, "bold"),
        fg="white",
        bg="#0e0e0e"
    ).pack(pady=(0, 10))

    tk.Label(
        frame,
        text=f"Versión {VERSION}\nDesarrollado por {AUTHOR}",
        fg="#aaaaaa",
        bg="#0e0e0e",
        font=("Segoe UI", 12),
        justify="center"
    ).pack()
def render_perfil():
    clear_content()

    card = tk.Frame(content, bg="#1c1c1c", padx=40, pady=30)
    card.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        card,
        text="PERFIL",
        fg="white",
        bg="#1c1c1c",
        font=("Segoe UI", 20, "bold")
    ).pack(pady=(0, 15))

    tk.Label(
        card,
        text=(
            "Usuario: GRaffaDev\n"
            "Servidor preferido: WowPatagonia\n\n"
            "En el futuro:\n"
            "• Configuración de perfil\n"
            "• Preferencias\n"
            "• Estadísticas"
        ),
        fg="#cccccc",
        bg="#1c1c1c",
        font=("Segoe UI", 12),
        justify="left"
    ).pack()

def render_addons():
    clear_content()

    card = tk.Frame(content, bg="#1c1c1c", padx=40, pady=30)
    card.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        card,
        text="ADDONS",
        fg="white",
        bg="#1c1c1c",
        font=("Segoe UI", 20, "bold")
    ).pack(pady=(0, 15))

    tk.Label(
        card,
        text=(
            "• Detección automática de addons\n"
            "• Instalación y actualización (próximamente)\n"
            "• Compatibilidad WoW 3.3.5\n\n"
            "Sección en desarrollo 🔧"
        ),
        fg="#cccccc",
        bg="#1c1c1c",
        font=("Segoe UI", 12),
        justify="left"
    ).pack()


def change_section(sec):
    if sec == "Inicio":
        render_inicio()
    elif sec == "Novedades":
        render_novedades()
    elif sec == "About":
        render_about()
    elif sec == "Addons":
        render_addons()
    elif sec == "Perfil":
        render_perfil()
    else:
        clear_content()

# ======================
# TOPBAR
# ======================

for sec in ["Inicio", "Novedades", "Addons", "Perfil", "About"]:
    b = tk.Button(
        topbar,
        text=sec,
        bg="#1f1f1f",
        fg="white",
        bd=0,
        font=("Segoe UI", 12, "bold"),
        command=lambda s=sec: change_section(s)
    )
    b.bind("<Enter>", hover_top_on)
    b.bind("<Leave>", hover_top_off)
    b.pack(side="left", padx=25, pady=10)

# ======================
# SIDEBAR
# ======================

tk.Label(
    sidebar,
    text="SERVERS",
    fg="#aaaaaa",
    bg="#181818",
    font=("Segoe UI", 11, "bold")
).pack(pady=(20, 15))

btn_cfg = tk.Button(
    sidebar,
    text="⚙️ Configurar WoW",
    command=seleccionar_wow,
    bg="#252525",
    fg="white",
    bd=0,
    height=2,
    font=("Segoe UI", 11, "bold")
)
btn_cfg.bind("<Enter>", hover_on)
btn_cfg.bind("<Leave>", lambda e: hover_off(e, "#252525"))
btn_cfg.pack(fill="x", padx=15, pady=(0, 20))

for nombre in REALMS:
    b = tk.Button(
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
    b.bind("<Enter>", hover_on)
    b.bind("<Leave>", lambda e: hover_off(e, "#252525"))
    b.pack(fill="x", padx=15, pady=8)

# ======================
# START
# ======================

render_inicio()
root.mainloop()
