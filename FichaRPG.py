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
    'regeneracao',
    'forca',
    'velocidade',
    'energia',
    'precisao',
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

linhas = pegar_ficha()   

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def alterar_atributo(atributo, valor):
    linhas[atributo] = str(int(linhas[atributo])+int(valor)) + '\n'
    salvar_ficha()

app = ctk.CTk()
app.title("Basic CustomTkinter App")

frame_atributos = ctk.CTkScrollableFrame(master=app)
frame_atributos.pack(pady=20, padx=(20, 10), fill="both", expand=True, side="left")

frame_controles = ctk.CTkFrame(master=app)
frame_controles.pack(pady=20, padx=(10, 20), fill="both", expand=True, side="left")

frame_mudar_vida = ctk.CTkFrame(frame_controles)
frame_mudar_vida.pack(pady=10, padx=10, ipadx=10, ipady=10)

entrada_vida = ctk.CTkEntry(frame_mudar_vida, placeholder_text="Valor")
entrada_vida.pack(pady=10)

botao_vida = ctk.CTkButton(frame_mudar_vida, text="Mudar Vida", command=lambda: alterar_atributo(2, entrada_vida.get()))
botao_vida.pack(pady=10)


frame_mudar_sanidade = ctk.CTkFrame(frame_controles)
frame_mudar_sanidade.pack(pady=10, padx=10, ipadx=10, ipady=10)

entrada_sanidade = ctk.CTkEntry(frame_mudar_vida, placeholder_text="Valor")
entrada_sanidade.pack(pady=10)

botao_sanidade = ctk.CTkButton(frame_mudar_vida, text="Mudar Sanidade", command=lambda: alterar_atributo(4, entrada_sanidade.get()))
botao_sanidade.pack(pady=10)

def mostrar_atributos():
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

mostrar_atributos()

def editar_ficha_toda():
    janela = ctk.CTkToplevel(app)
    janela.title("Erro")
    janela.geometry("300x400")
    janela.grab_set()
    label_titulo = ctk.CTkLabel(janela, text="Criar ficha")
    label_titulo.pack(pady=10)

    scroll = ctk.CTkScrollableFrame(janela)
    scroll.pack(fill="both", expand=True, padx=10)

    entries = []
    for campo in locais:
        label = ctk.CTkLabel(scroll, text=campo.capitalize())
        label.pack(anchor="w")

        entry = ctk.CTkEntry(scroll, placeholder_text=campo.capitalize())
        entry.pack(fill="x", pady=(0, 8))

        entries.append(entry)
    def salvar():
        with open(ficha, 'w') as f:
            for entry in entries:
                f.write(entry.get() + '\n')
        janela.destroy()

    botao_ok = ctk.CTkButton(janela, text="OK", command=salvar)
    botao_ok.pack(pady=10)

if (Path(ficha).is_file() == False):
    editar_ficha_toda()

app.mainloop()
