import time
import keyboard
import pyautogui
import pygetwindow as gw

# Mensagens de inicialização e carregamento
print("O script está sendo iniciado...")

# Lista para armazenar os dígitos lidos
lista = []

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
    except Exception as e:
        print("Erro durante a leitura do código de barras:", e)

# Função para processar a tecla pressionada
def press_tecla(tecla):
    try:
        # Ignora as teclas "backspace" e "tab"
        if tecla.name not in ["backspace", "tab"]:
            # Processa o código de barras e executa ações com base nas teclas pressionadas
            retorno = bar_code(tecla)

            # Se a tecla "ctrl" foi pressionada, alterna entre as janelas
            if retorno == "ctrl":
                pyautogui.press("backspace", presses=5)  # Simula a exclusão do texto anterior
                alternar_janela()  # Alterna entre as janelas sensatta e classificação
    except Exception as e:
        print("Erro durante o processamento da tecla:", e)

# Função para alternar entre as janelas sensatta e classificação
def alternar_janela():
    try:
        # Obtém as instâncias das janelas sensatta e classificação
        sensatta = gw.getWindowsWithTitle('*C:\\Program Files\\Notepad++\\change.log - Notepad++ [Administrator]')[0]
        classificacao = gw.getWindowsWithTitle('Classificação - Linha de Cortes')[0]

        # Verifica se a janela sensatta está ativa e a maximiza, caso contrário, ativa e maximiza a janela classificação
        if sensatta.isActive:
            classificacao.activate()
            classificacao.restore()
            time.sleep(0.3)
            clicar_no_campo_cracha()
        else:
            sensatta.activate()
            sensatta.maximize()

        # Aguarda um curto período de tempo antes de continuar
        time.sleep(0.3)
    except Exception as e:
        print("Erro durante a alternância de janelas:", e)

def clicar_no_campo_cracha():
    try:
        ref_button_1 = pyautogui.locateCenterOnScreen('ok.png')
        referencia_erro = ref_button_1

        # Verificando qual botão está disponível e configurando a referência de erro
        if referencia_erro:
            erro_pos = (referencia_erro[0], referencia_erro[1])  
            pyautogui.moveTo(erro_pos[0], erro_pos[1])
            pyautogui.click()

        time.sleep(0.2)

        referencia_pos = pyautogui.locateCenterOnScreen('cracha.png')
        if referencia_pos:
            cracha_pos = (referencia_pos[0] + 10, referencia_pos[1] + 100) 
            pyautogui.moveTo(cracha_pos[0], cracha_pos[1])
            pyautogui.click()
        else:
            print("Elemento de referência não encontrado na tela.")
    except Exception as e:
        print("Erro ao clicar no campo crachá:", e)

# Monitora a pressão das teclas e chama a função press_tecla quando uma tecla é pressionada
keyboard.on_press(lambda key: press_tecla(key))

# Mensagem de conclusão do carregamento
print("Script carregado com sucesso.")

try:
    # Aguarda a pressão da tecla "esc" para encerrar o programa
    keyboard.wait('esc')
except Exception as e:
    print("Erro durante a espera pela tecla 'esc':", e)
