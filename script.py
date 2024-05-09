import time
import keyboard
import pyautogui
import pygetwindow as gw
from tqdm import tqdm

import base64
import images_base64
from PIL import Image
import io


# Mensagens de inicialização e carregamento
print("O script está sendo iniciado...")

# Função para simular o carregamento inicial com uma barra de progresso
def carregar_com_barra():
    print("Carregando o script...")
    # Define o número total de iterações para a barra de progresso
    total_iteracoes = 100
    # Cria uma barra de progresso com 100 iterações
    with tqdm(total=total_iteracoes, desc="Carregando", position=0, leave=True) as barra:
        # Simula o carregamento
        for _ in range(total_iteracoes):
            time.sleep(0.02)  # Simula um pequeno atraso
            barra.update(1)  # Atualiza a barra de progresso

# Chama a função para carregar o script com a barra de progresso
carregar_com_barra()

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
    except KeyboardInterrupt:
        print("A leitura do código de barras foi interrompida pelo usuário.")
    except Exception as e:
        print("Erro durante a leitura do código de barras:", e)

# Função para processar a tecla pressionada
def press_tecla(tecla):
    try:
        # Ignora as teclas "backspace" e "tab"
        if tecla.name not in ["backspace", "tab", "shift"]:
            # Processa o código de barras e executa ações com base nas teclas pressionadas
            retorno = bar_code(tecla)

            # Se a tecla "ctrl" foi pressionada, alterna entre as janelas
            if retorno == "ctrl":
                pyautogui.press("backspace", presses=5)  # Simula a exclusão do texto anterior
                alternar_janela()  # Alterna entre as janelas sensatta e classificação
    except KeyboardInterrupt:
        print("A pressão de tecla foi interrompida pelo usuário.")
    except Exception as e:
        print("Erro durante o processamento da tecla:", e)

# Função para alternar entre as janelas sensatta e classificação
def alternar_janela():
    try:
        # Obtém as referências das janelas
        classificacao = gw.getWindowsWithTitle('Classificação - Linha de Cortes')
        sensatta_classificacao_final = gw.getWindowsWithTitle('Classificação Final')
        mensagem = gw.getWindowsWithTitle('Mensagem')

        # Verifica se todas as janelas foram encontradas
        if classificacao and sensatta_classificacao_final:
            
            mensagem = mensagem[0]
            classificacao = classificacao[0]
            sensatta_classificacao_final = sensatta_classificacao_final[0]

            # Verifica se a janela sensatta_classificacao_final está ativas
            if sensatta_classificacao_final.isActive or mensagem.isActive:
                # Ativa a janela de classificação e clica no campo de crachá
                ativar_janela_e_clicar(classificacao, clicar_no_campo_cracha)
            else:
                # Se a janela sensatta_classificacao_final não estiver ativa, ativa-a
                ativar_janela_e_clicar(sensatta_classificacao_final, processar_erro_sensatta)
            
            time.sleep(0.2)
        else:
            print("Algumas das janelas não foram encontradas.")
    except KeyboardInterrupt:
        print("A alternância de janelas foi interrompida pelo usuário.")
    except Exception as e:
        print("Erro durante a alternância de janelas:", e)

def decode_base64_image(base64_string):
    image_data = io.BytesIO(base64.b64decode(base64_string))
    image = Image.open(image_data)
    return image

# Função para esperar até que uma imagem específica apareça na tela
def esperar_por_imagem(imagem, timeout=1):
    tempo_inicial = time.time()
    while True:
        if pyautogui.locateCenterOnScreen(imagem) is not None:
            return True
        elif time.time() - tempo_inicial > timeout:
            return False

# Função para ativar uma janela e executar uma função após a ativação
def ativar_janela_e_clicar(janela, funcao=None):
    try:
        janela.activate()
        janela.restore()
        if funcao:
            funcao()
            
    except KeyboardInterrupt:
        print("A ativação de janela foi interrompida pelo usuário.")
    except Exception as e:
        print("Erro ao ativar janela e clicar:", e)

# Função para processar o erro sensatta
def processar_erro_sensatta():
    try:
        mensagem = gw.getWindowsWithTitle('Mensagem')
        if mensagem:
            mensagem[0].activate()
            mensagem[0].restore()
            
            button_ok_sen = images_base64.img_ok_sen
            button_ok_sen_2 = images_base64.img_ok_sen_2
           # button_on_sen_3 = 

            b1 = decode_base64_image(button_ok_sen)
            b2 = decode_base64_image(button_ok_sen_2)

            if esperar_por_imagem(b1) or esperar_por_imagem(b2):
                pyautogui.press("enter")

    except KeyboardInterrupt:
        print("O processamento de erro sensatta foi interrompido pelo usuário.")
    except Exception as e:
        print("Erro ao processar o erro sensatta:", e)

# Função para clicar no campo de crachá
def clicar_no_campo_cracha():
    try:
        cadastro_erro = gw.getWindowsWithTitle("Cadastro")
        if cadastro_erro:
            time.sleep(0.2)

            button_ok_classificacao = images_base64.img_ok
            button_ok = decode_base64_image(button_ok_classificacao)
            ref_ok = pyautogui.locateCenterOnScreen(button_ok)
            if ref_ok:
                pyautogui.click(ref_ok)

            button_ok_classificacao2 = images_base64.img_ok_2
            button_ok2 = decode_base64_image(button_ok_classificacao2)
            ref_ok2 = pyautogui.locateCenterOnScreen(button_ok2)
            if ref_ok2:
                pyautogui.click(ref_ok2)
        
        cracha_img = images_base64.img_cracha
        c = decode_base64_image(cracha_img)

        referencia_pos = pyautogui.locateCenterOnScreen(c)
        if esperar_por_imagem(c):
            pyautogui.click(referencia_pos)
    
    except KeyboardInterrupt:
        print("O clique no campo de crachá foi interrompido pelo usuário.")
    except Exception as e:
        print("Erro ao clicar no campo crachá:", e)

# Monitora a pressão das teclas e chama a função press_tecla quando uma tecla é pressionada
keyboard.on_press(lambda key: press_tecla(key))

# Mensagem de conclusão do carregamento
print("Script carregado com sucesso.")

try:
    # Aguarda a pressão da tecla "esc" para encerrar o programa
    keyboard.wait('esc')
except KeyboardInterrupt:
    print("A espera pela tecla 'esc' foi interrompida pelo usuário.")
except Exception as e:
    print("Erro durante a espera pela tecla 'esc':", e)
