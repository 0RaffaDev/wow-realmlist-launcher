import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json
from PIL import Image, ImageTk

# ======================
# CONFIG
# ======================

VERSION = "v3.3"
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
root.title("Azeroth Launcher")

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

# -------- NOVEDADES (CARDS) --------

# -------- NOVEDADES (CARDS) --------

def render_novedades():
    clear_content()

    # ======================
    # DATA
    # ======================

    noticia_principal = {
    "titulo": "🚀 Azeroth Launcher v3.3",
    "texto": (
        "Actualización enfocada en identidad visual y experiencia de usuario.\n\n"
        "✨ Novedades principales:\n"
        "• Nueva sección de Novedades\n"
        "• Cards visuales\n"
        "• Mejor jerarquía de información y lectura más clara\n\n"
        "Este update marca un antes y un después en el launcher, "
    ),
    "img": "assets/v33.png"
}


    noticias_anteriores = [
          {
            "titulo": "🛠 Próximamente – v4.0",
            "texto": (
                "La siguiente gran actualización del launcher.\n\n"
                "🔮 En desarrollo:\n"
                "• Agregar / quitar servidores desde la interfaz\n"
                "• Mejoras en la sección Perfil\n"
                "• Gestión visual de addons\n"
                "Esta versión marcará el salto funcional del launcher."
            ),
            "img": ""
        },
        {
            "titulo": "👤 v3.2 – Sección Perfil",
            "texto": (
                "Primera implementación de la sección Perfil.\n\n"
                "• Estructura visual del perfil de usuario\n"
                "• Preparado para estadísticas por servidor\n"
                "• Base para preferencias personales y configuraciones futuras\n\n"
                "Este update sienta las bases del sistema de usuarios del launcher."
        ),
        "img": "assets/v32.png"
        },
        {
            "titulo": "🎨 v3.1 – Rediseño de Interfaz",
            "texto": (
                "Rediseño completo de la interfaz principal.\n\n"
                "• Nueva Topbar con navegación clara\n"
                "• Sidebar más limpia y funcional\n"
                "• Hover effects modernos y consistentes\n\n"
                "El launcher adopta una estética más oscura, moderna y estilo Blizzard."
            ),
            "img": "assets/v31.png"
        },
        {
            "titulo": "🔥 v1.0 – Lanzamiento Inicial",
            "texto": (
                "Primera versión funcional del Azeroth Launcher.\n\n"
                "El comienzo del proyecto y la base de todo lo que vino después.\n"
                "•Cambio de Realmlist (Unica Funcion)"
            ),
            "img": ""
        },
      
]


    index = {"value": 0}

    # ======================
    # LAYOUT BASE
    # ======================

    container = tk.Frame(content, bg="#0e0e0e")
    container.pack(fill="both", expand=True, padx=40, pady=30)

    # ======================
    # CARD PRINCIPAL (3D)
    # ======================

    shadow = tk.Frame(container, bg="#000000")
    shadow.pack(fill="x", pady=(0, 30), padx=(6, 6))

    main_card = tk.Frame(
        shadow,
        bg="#1f1f1f",
        padx=40,
        pady=30,
        highlightbackground="#3a3a3a",
        highlightthickness=1
    )
    main_card.pack(fill="x", padx=(0, 6), pady=(0, 6))

    # Imagen principal
    try:
        img = Image.open(noticia_principal["img"]).resize((960, 240))
        photo = ImageTk.PhotoImage(img)
        img_lbl = tk.Label(main_card, image=photo, bg="#1f1f1f")
        img_lbl.image = photo
        img_lbl.pack(fill="x", pady=(0, 20))
    except:
        pass

    tk.Label(
        main_card,
        text=noticia_principal["titulo"],
        fg="white",
        bg="#1f1f1f",
        font=("Segoe UI", 24, "bold"),
        anchor="w"
    ).pack(anchor="w", pady=(0, 15))

    tk.Label(
        main_card,
        text=noticia_principal["texto"],
        fg="#d0d0d0",
        bg="#1f1f1f",
        font=("Segoe UI", 13),
        justify="left",
        wraplength=900
    ).pack(anchor="w")

    # ======================
    # CARRUSEL (CARD 3D)
    # ======================

    carousel = tk.Frame(container, bg="#0e0e0e")
    carousel.pack(fill="x")

    btn_prev = tk.Button(
        carousel, text="◀", font=("Segoe UI", 18, "bold"),
        bg="#0e0e0e", fg="white", bd=0
    )
    btn_prev.pack(side="left", padx=10)

    card_shadow = tk.Frame(carousel, bg="#000000")
    card_shadow.pack(side="left", expand=True, padx=6, pady=6)

    card = tk.Frame(
        card_shadow,
        bg="#1f1f1f",
        padx=30,
        pady=20,
        highlightbackground="#3a3a3a",
        highlightthickness=1,
        width=600
    )
    card.pack(padx=(0, 6), pady=(0, 6))

    btn_next = tk.Button(
        carousel, text="▶", font=("Segoe UI", 18, "bold"),
        bg="#0e0e0e", fg="white", bd=0
    )
    btn_next.pack(side="left", padx=10)

    img_label = tk.Label(card, bg="#1f1f1f")
    img_label.pack(fill="x", pady=(0, 15))

    titulo = tk.Label(
        card, fg="white", bg="#1f1f1f",
        font=("Segoe UI", 18, "bold")
    )
    titulo.pack(anchor="w", pady=(0, 10))

    texto = tk.Label(
        card, fg="#bbbbbb", bg="#1f1f1f",
        font=("Segoe UI", 12),
        justify="left", wraplength=520
    )
    texto.pack(anchor="w")

    def render_card():
        n = noticias_anteriores[index["value"]]
        titulo.config(text=n["titulo"])
        texto.config(text=n["texto"])

        try:
            img = Image.open(n["img"]).resize((520, 160))
            photo = ImageTk.PhotoImage(img)
            img_label.config(image=photo)
            img_label.image = photo
        except:
            img_label.config(image="")

    def prev():
        index["value"] = (index["value"] - 1) % len(noticias_anteriores)
        render_card()

    def next_():
        index["value"] = (index["value"] + 1) % len(noticias_anteriores)
        render_card()

    btn_prev.config(command=prev)
    btn_next.config(command=next_)
    render_card()

def render_perfil():
    clear_content()

    card = tk.Frame(content, bg="#1c1c1c", padx=50, pady=40)
    card.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        card,
        text="PERFIL",
        font=("Segoe UI", 20, "bold"),
        fg="white",
        bg="#1c1c1c"
    ).pack(pady=(0, 15))

    tk.Label(
        card,
        text=(
            "Usuario: GRaffaDev\n\n"
            "Esta sección estará disponible en una futura versión.\n\n"
            "• Perfil por usuario\n"
            "• Preferencias\n"
            "• Estadísticas por servidor"
        ),
        font=("Segoe UI", 12),
        fg="#cccccc",
        bg="#1c1c1c",
       
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
        text="Gestión de addons próximamente.",
        fg="#cccccc",
        bg="#1c1c1c",
        font=("Segoe UI", 12)
    ).pack()

def render_about():
    clear_content()

    frame = tk.Frame(content, bg="#0e0e0e")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="Azeroth Launcher",
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

def change_section(sec):
    if sec == "Inicio":
        render_inicio()
    elif sec == "Novedades":
        render_novedades()
    elif sec == "Perfil":
        render_perfil()
    elif sec == "Addons":
        render_addons()
    elif sec == "About":
        render_about()

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
