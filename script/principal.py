# Importa as bibliotecas necessárias
import time
import keyboard
import pyautogui
import pygetwindow as gw

# Lista para armazenar os dígitos lidos
lista = []

# Coordenadas para mover o cursor do mouse
x, y = 707, 239

# Função para ler o código de barras e processar as teclas pressionadas
def bar_code(tecla):
    global lista
    letra = tecla.name
    
    try:
        # Se for um dígito, adiciona à lista
        if tecla.name.isdigit():
            lista.append(letra)
            print("Número:", lista)
        # Se for a tecla "enter", combina os dígitos e retorna o código de barras
        elif tecla.name == "enter":
            num_barcode = "".join(lista)
            print("Enter:", lista)
            lista.clear()  # Esvazia a lista após cada leitura do código de barras
            return num_barcode
        # Se não for um dígito, adiciona à lista
        elif not tecla.name.isdigit():
            lista.append(letra)
            print("Letra:", lista)
    except:
        print("ERRO DE LEITURA")
    return None

# Função para processar a tecla pressionada
def press_tecla(tecla):
    # Ignora as teclas "backspace" e "tab"
    if tecla.name == "backspace" or tecla.name == "tab":
        return
    
    # Processa o código de barras e executa ações com base nas teclas pressionadas
    retorno = bar_code(tecla)

    # Se a tecla "ctrl" foi pressionada, alterna entre as janelas
    if retorno == "ctrl":
        pyautogui.press("backspace", presses=5)  # Simula a exclusão do texto anterior
        alternar_janela()  # Alterna entre as janelas sensatta e classificação

    # Se a tecla "tab" foi pressionada, executa ações específicas
    elif retorno == "tab":
        pyautogui.press("enter")  # Simula a tecla "enter"
        pyautogui.moveTo(x, y)  # Move o cursor do mouse para as coordenadas especificadas
        pyautogui.click()  # Simula um clique do mouse

# Função para alternar entre as janelas sensatta e classificação
def alternar_janela():
    # Obtém as instâncias das janelas sensatta e classificação
    sensatta = gw.getWindowsWithTitle('WhatsApp')[0]
    classificacao = gw.getWindowsWithTitle('Spotify Free')[0]

    # Verifica se a janela sensatta está ativa e a maximiza, caso contrário, ativa e maximiza a janela classificação
    if sensatta.isActive:
        classificacao.activate()
        classificacao.maximize()
    else:
        sensatta.activate()
        sensatta.maximize()

    # Aguarda um curto período de tempo antes de continuar
    time.sleep(0.5)

# Monitora a pressão das teclas e chama a função press_tecla quando uma tecla é pressionada
keyboard.on_press(lambda key: press_tecla(key))

# Aguarda a pressão da tecla "esc" para encerrar o programa
keyboard.wait('esc')
