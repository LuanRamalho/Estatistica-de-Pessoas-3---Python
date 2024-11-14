import tkinter as tk
from tkinter import ttk

def calcular_estatisticas():
    total_pesquisadas = sum(int(entry.get() or 0) for entry in entradas.values())
    total_label.config(text=f"Total de Pessoas Pesquisadas: {total_pesquisadas}")
    
    # Limpa os widgets de resultado antes de recalcular
    for widget in frame_resultados.winfo_children():
        widget.destroy()
    
    # Calcula e exibe as estatísticas para cada disciplina
    for disciplina, entry in entradas.items():
        quantidade = int(entry.get() or 0)
        porcentagem = (quantidade / total_pesquisadas * 100) if total_pesquisadas > 0 else 0

        frame_resultado = ttk.Frame(frame_resultados)
        frame_resultado.pack(fill="x", padx=5, pady=2)
        
        label_disciplina = tk.Label(frame_resultado, text=disciplina, font=("Arial", 12), bg="#F0F8FF", fg="#2E4A62")
        label_disciplina.pack(side="left", padx=(0, 10))
        
        barra_progresso = ttk.Progressbar(frame_resultado, length=200, mode="determinate", value=porcentagem, maximum=100)
        barra_progresso.pack(side="left", padx=5, fill="x", expand=True)
        
        label_porcentagem = tk.Label(frame_resultado, text=f"{porcentagem:.2f}%", font=("Arial", 12), bg="#F0F8FF", fg="#2E4A62")
        label_porcentagem.pack(side="left", padx=10)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Estatísticas de Preferências de Disciplinas")
janela.geometry("500x600")
janela.configure(bg="#F0F8FF")

# Configuração do Frame com a barra de rolagem
frame_principal = ttk.Frame(janela, padding=10)
frame_principal.pack(fill="both", expand=True)

canvas = tk.Canvas(frame_principal, bg="#F0F8FF")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

frame_interno = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame_interno, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Estilo dos widgets
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#F0F8FF", foreground="#2E4A62")
style.configure("TButton", font=("Arial", 12, "bold"), background="#5F9EA0", foreground="#FFFFFF")
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#4682B4", foreground="#FFFFFF")
style.configure("Treeview", background="#FFFFFF", rowheight=25)

# Label principal
titulo = tk.Label(frame_interno, text="Estatísticas de Preferências de Disciplinas", font=("Arial", 16, "bold"), bg="#4682B4", fg="#FFFFFF")
titulo.pack(pady=10, fill="x")

# Dicionário para armazenar os campos de entrada de cada disciplina
entradas = {}
disciplinas = [
    'Português', 'Inglês', 'Espanhol', 'Matemática', 'Biologia', 'História', 
    'Geografia', 'Informática', 'Filosofia', 'Sociologia', 'Física', 'Química', 
    'Geometria', 'Trigonometria'
]

# Criação dos campos de entrada
for disciplina in disciplinas:
    frame = ttk.Frame(frame_interno)
    frame.pack(pady=5)
    
    label = tk.Label(frame, text=f"{disciplina}:", font=("Arial", 12), bg="#F0F8FF", fg="#2E4A62")
    label.pack(side="left")
    
    entrada = tk.Entry(frame, width=5, font=("Arial", 12), fg="#2E4A62", bg="#E6F7FF")
    entrada.insert(0, "0")
    entrada.pack(side="left", padx=5)
    entradas[disciplina] = entrada

# Botão para calcular as estatísticas
botao_calcular = tk.Button(frame_interno, text="Calcular Estatísticas", command=calcular_estatisticas, font=("Arial", 12, "bold"), bg="#5F9EA0", fg="#FFFFFF", relief="raised")
botao_calcular.pack(pady=10)

# Exibição do total de pessoas pesquisadas
total_label = tk.Label(frame_interno, text="Total de Pessoas Pesquisadas: 0", font=("Arial", 12, "bold"), bg="#F0F8FF", fg="#2E4A62")
total_label.pack(pady=5)

# Frame para resultados das estatísticas
frame_resultados = ttk.Frame(frame_interno)
frame_resultados.pack(fill="both", expand=True, padx=5, pady=5)

# Função para ajustar a rolagem
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame_interno.bind("<Configure>", on_frame_configure)

janela.mainloop()
