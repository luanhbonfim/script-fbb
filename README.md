# Leitor de Código de Barras

Este é um script em Python para ler e processar códigos de barras digitados pelo teclado/leitor. Ele foi desenvolvido para automatizar a leitura e processamento de códigos de barras em determinado contexto de uso.

## Funcionalidades

- Detecta e processa dígitos do teclado para formar códigos de barras.
- Combina os dígitos quando a tecla "Enter" é pressionada e retorna o código de barras.
- Alterna entre janelas específicas do sistema com base na tecla pressionada (no caso, a tecla "Ctrl" ou o próprio dígito "Ctrl" atráves do teclado).
- Realiza ações específicas dentro das janelas, como clicar em campos designados.

## Dependências

- Python 3.x
- Bibliotecas: `keyboard`, `pyautogui`, `pygetwindow`

## Utilização

1. **Instalação das Dependências**: Certifique-se de ter o Python 3.x instalado no seu sistema. Você pode instalar as bibliotecas necessárias utilizando o seguinte comando:

   ```bash
   pip install keyboard pyautogui pygetwindow
  
2. **Execução do Script:** Execute o script Python *`leitor_codigo_barras.py`* em seu terminal.

3. **Utilização do Script:** O script ficará aguardando a entrada do código de barras pelo teclado. Pressione os dígitos para formar o código desejado e pressione "Enter" para confirmar. O script executará as ações configuradas com base nos códigos de barras lidos.

4. **Encerramento do Script:** Para encerrar o script, pressione a tecla "Esc".

## Observações
- Este script foi desenvolvido para um contexto específico e pode precisar de ajustes para funcionar em outros ambientes.
- Certifique-se de que as imagens de referência (ok.png e cracha.png) estejam disponíveis no mesmo diretório do script ou forneça o caminho correto para elas.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou funcionalidades adicionais.

## Autor
Este script foi desenvolvido por `[Luan Henrique]`. Você pode entrar em contato com o autor através de `[luanhenrique.dev@gmail.com]`.
