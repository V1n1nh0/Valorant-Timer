from PIL import ImageGrab
import tkinter as tk
import time
import keyboard 

# Define a função de contagem regressiva
def countdown(remaining):
    global timer_label, timer_running
    if remaining <= 0:
        timer_running = False
        timer_label.configure(text="Acabou!")
    else:
        timer_label.configure(text=f"Tempo restante: {remaining}")
        remaining -= 1
        timer_label.after(1000, countdown, remaining)
        

# Define a função para iniciar o temporizador
def start_timer():
    global timer_label, timer_running
    # Se o temporizador já estiver rodando, saia da função
    if timer_running:
        return
    # Configura a variável de controle para evitar que o temporizador seja iniciado novamente
    timer_running = True
    # Limpa o rótulo de contagem regressiva, se houver uma
    try:
        timer_label.destroy()
    except:
        pass
    # Cria um rótulo para mostrar a contagem regressiva
    timer_label = tk.Label(root, font=('Arial', 24))
    timer_label.pack()
    # Inicia a contagem regressiva
    countdown(45)

# Define a função para verificar a presença da cor e iniciar o temporizador
def check_color():
    global timer_running
    # Captura a imagem da região da tela
    image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    #image.save("teste.png")
    # Verifica se a cor desejada está presente na imagem
    if any(color in image.getdata() for color in [(170, 0, 0), (169, 0, 0), (124, 0, 0)]):
        if not timer_running:
            start_timer()
            timer_running = True
            # Aguarda 45 segundos antes de permitir que o temporizador seja iniciado novamente
            root.after(45000, lambda: setattr(timer_running, False))
    # Chama a função novamente após um intervalo de tempo definido (0.1 segundo)
    root.after(100, check_color)

# Função para minimizar a janela quando uma combinação de teclas for pressionada
def minimize_window(e):
    root.iconify()  # Minimiza a janela

# Função para alternar a visibilidade da janela
def toggle_window_visibility():
    if root.state() == 'normal':
        root.withdraw()  # Esconde a janela
    else:
        root.deiconify()  # Mostra a janela

# Cria a janela principal
root = tk.Tk()

# Configs da janela
root.geometry("300x50")
root.title("Timer Valorants :)")
root.attributes("-alpha", 0.1)  # Define a transparência da janela (0.0 a 1.0)

# Define as coordenadas da região original em pixels (para um monitor 1680x1050)
x1_original, y1_original, x2_original, y2_original = 788, 70, 919, 117

# Captura as dimensões reais do monitor
monitor_width, monitor_height = 1680, 1050  # Substitua pelas dimensões do seu monitor

# Calcula a proporção de redimensionamento para largura e altura
x_ratio = monitor_width / 1680
y_ratio = monitor_height / 1050

# Redimensiona as coordenadas originais com base na proporção
x1 = int(x1_original * x_ratio)
y1 = int(y1_original * y_ratio)
x2 = int(x2_original * x_ratio)
y2 = int(y2_original * y_ratio)

# Variável de controle para verificar se o temporizador está rodando ou não
timer_running = False

# Chama a função para verificar a presença da cor e iniciar o temporizador
check_color()

# Deixar a janela  sempre na frente das outras
root.wm_attributes("-topmost", 1)
root.overrideredirect(True)

# FECHA E ABRE QUANDO VC APERTAR INSERT
keyboard.add_hotkey('insert', toggle_window_visibility)

# Inicia o loop principal da janela
root.mainloop()