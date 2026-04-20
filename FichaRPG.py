import customtkinter as ctk
from pathlib import Path

ficha = Path(__file__).parent / "fichaRPG.txt"
linhas = []

locais = [
    'nome',
    'vida total',
    'vida atual',
    'sanidade total',
    'sanidade atual',
    'esgrima',
    'inteligencia',
    'resistencia',
    'reflexos',
    'agilidade',
    'regeneração',
    'força',
    'velocidade',
    'energia',
    'precisão',
    'furtividade'
]

def pegar_ficha():
    with open(ficha, 'r') as f:
        linhas = f.readlines()
    return linhas

def salvar_ficha():
    with open(ficha, 'w') as f:
        for linha in linhas:
            f.write(linha)
    mostrar_atributos()

def mostrar_atributos():
    if len(linhas) < len(locais):
        return
    for widget in frame_atributos.winfo_children():
        widget.destroy()

    for i in range(len(locais)):
        if (i == 0):
            label = ctk.CTkLabel(frame_atributos, text=linhas[i].strip(), font=("Arial", 20), anchor="w")
            label.pack(fill="x", pady=(0, 10))
            continue
        if (i == 1):
            label = ctk.CTkLabel(frame_atributos, text="Vida: " + linhas[i+1].strip() + "/" + linhas[i].strip(), anchor="w")
            label.pack(fill="x")
            continue
        if (i == 3):
            label = ctk.CTkLabel(frame_atributos, text="Sanidade: " + linhas[i+1].strip() + "/" + linhas[i].strip(), anchor="w")
            label.pack(fill="x", pady=(0, 10))
            continue
        if (i == 2 or i == 4):
            continue
        label = ctk.CTkLabel(frame_atributos, text=locais[i].capitalize() + ": " + linhas[i].strip(), anchor="w")
        label.pack(fill="x")

def alterar_atributo_valor(atributo, valor):
    linhas[atributo] = str(int(linhas[atributo])+int(valor)) + '\n'
    salvar_ficha()

def alterar_atributo(indice):
    def salvar(valor):
        linhas[indice] = valor + '\n'
        salvar_ficha()
        janela.destroy()
    janela = ctk.CTkToplevel(app)
    janela.title("Alterar Atributo")
    janela.geometry("300x400")
    janela.grab_set()
    label = ctk.CTkLabel(janela, text=locais[indice].capitalize() + ": " + linhas[indice].strip(), anchor="w")
    label.pack(pady=10, fill="x", padx=10)
    entrada = ctk.CTkEntry(janela, placeholder_text="Valor")
    entrada.pack(pady=10)
    botao = ctk.CTkButton(janela, text="Alterar", command=lambda: salvar(entrada.get()))
    botao.pack(pady=10)

def editar_ficha_toda():
    janela = ctk.CTkToplevel(app)
    janela.title("Criar/Alterar ficha")
    janela.geometry("300x400")
    janela.grab_set()
    label_titulo = ctk.CTkLabel(janela, text="Criar/Alterar ficha")
    label_titulo.pack(pady=10)

    scroll = ctk.CTkScrollableFrame(janela)
    scroll.pack(fill="both", expand=True, padx=10)

    entries = []
    for i, campo in enumerate(locais):
        label = ctk.CTkLabel(scroll, text=campo.capitalize())
        label.pack(anchor="w")

        entry = ctk.CTkEntry(scroll, placeholder_text=campo.capitalize())
        if i < len(linhas):
            entry.insert(0, linhas[i].strip())
        entry.pack(fill="x", pady=(0, 8))

        entries.append(entry)
    def salvar():
        global linhas
        with open(ficha, 'w') as f:
            for entry in entries:
                f.write(entry.get() + '\n')
        linhas = pegar_ficha()
        mostrar_atributos()
        janela.destroy()

    botao_ok = ctk.CTkButton(janela, text="OK", command=salvar)
    botao_ok.pack(pady=10)

if Path(ficha).is_file():
    linhas = pegar_ficha()   

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Administrador de ficha (WAR)")

frame_atributos = ctk.CTkScrollableFrame(master=app)
frame_atributos.pack(pady=20, padx=(20, 10), fill="both", expand=True, side="left")

frame_controles = ctk.CTkScrollableFrame(master=app)

frame_mudar_vida = ctk.CTkFrame(frame_controles, border_width=2, border_color="gray")
frame_mudar_vida.pack(pady=10, padx=10, ipadx=10, ipady=10)
ctk.CTkLabel(frame_mudar_vida, text="Alterar Vida", anchor="w").pack(pady=(5, 0), fill="x", padx=10)
entrada_vida = ctk.CTkEntry(frame_mudar_vida, placeholder_text="Valor")
entrada_vida.pack(pady=10)
botao_vida = ctk.CTkButton(frame_mudar_vida, text="Mudar Vida", command=lambda: alterar_atributo_valor(2, entrada_vida.get()))
botao_vida.pack(pady=10)

frame_mudar_sanidade = ctk.CTkFrame(frame_controles, border_width=2, border_color="gray")
frame_mudar_sanidade.pack(pady=10, padx=10, ipadx=10, ipady=10)
ctk.CTkLabel(frame_mudar_sanidade, text="Alterar Sanidade", anchor="w").pack(pady=(5, 0), fill="x", padx=10)
entrada_sanidade = ctk.CTkEntry(frame_mudar_sanidade, placeholder_text="Valor")
entrada_sanidade.pack(pady=10)
botao_sanidade = ctk.CTkButton(frame_mudar_sanidade, text="Mudar Sanidade", command=lambda: alterar_atributo_valor(4, entrada_sanidade.get()))
botao_sanidade.pack(pady=10)

frame_mudar_atributo = ctk.CTkFrame(frame_controles, border_width=2, border_color="gray")
frame_mudar_atributo.pack(pady=10, padx=10, ipadx=10, ipady=10)
ctk.CTkLabel(frame_mudar_atributo, text="Alterar Atributo", anchor="w").pack(pady=(5, 0), fill="x", padx=10)
selecao = ctk.CTkOptionMenu(frame_mudar_atributo, values=locais)
selecao.pack(pady=10)
mudar_atributo_button = ctk.CTkButton(frame_mudar_atributo, text="Mudar Atributo", command=lambda: alterar_atributo(locais.index(selecao.get())))
mudar_atributo_button.pack(pady=10)

frame_mudar_ficha_toda = ctk.CTkFrame(frame_controles, border_width=2, border_color="gray")
frame_mudar_ficha_toda.pack(pady=10, padx=10, ipadx=10, ipady=10)
ctk.CTkLabel(frame_mudar_ficha_toda, text="Mudar Ficha Toda", anchor="w").pack(pady=(5, 0), fill="x", padx=10)
botao_mudar_ficha = ctk.CTkButton(frame_mudar_ficha_toda, text="Mudar Atributo", command=lambda: editar_ficha_toda())
botao_mudar_ficha.pack(pady=10)

frame_controles.pack(pady=20, padx=(10, 20), fill="both", expand=True, side="left")

if (Path(ficha).is_file() == False):
    editar_ficha_toda()
elif len(linhas) >= len(locais):
    mostrar_atributos()

app.mainloop()
