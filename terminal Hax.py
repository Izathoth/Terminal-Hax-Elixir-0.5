import os
import shutil
import subprocess
import schedule
import time
import re
import threading
import json

def carregar_comandos_externos(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as file:
            comandos = json.load(file)
            return comandos
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado.")
        return {}

def welcome_message():
    print("""
    +-------------------------+
    |                         |
    |       Terminal           |
    |      Hax-Elixir          |
    |                         |
    +-------------------------+
    """)

def lst(dir):
    try:
        arquivos = os.listdir(dir)
        for arquivo in arquivos:
            print(arquivo)
    except FileNotFoundError:
        print("Diretório não encontrado.")

def cpy(origem, destino):
    try:
        shutil.copy(origem, destino)
        print(f'Arquivo {origem} copiado para {destino}')
    except FileNotFoundError:
        print("Arquivo ou diretório não encontrado.")

def del_(arquivo):
    try:
        os.remove(arquivo)
        print(f'Arquivo {arquivo} deletado.')
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def exe(comando):
    try:
        result = subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())

def ren(origem, destino):
    try:
        os.rename(origem, destino)
        print(f'Arquivo {origem} renomeado para {destino}')
    except FileNotFoundError:
        print("Arquivo ou diretório não encontrado.")

def mov(origem, destino):
    try:
        shutil.move(origem, destino)
        print(f'Arquivo {origem} movido para {destino}')
    except FileNotFoundError:
        print("Arquivo ou diretório não encontrado.")

def mkdir(diretorio):
    try:
        os.makedirs(diretorio)
        print(f'Diretório {diretorio} criado.')
    except FileExistsError:
        print("O diretório já existe.")

def cat(arquivo_saida, *arquivos_entrada):
    try:
        with open(arquivo_saida, 'w') as arquivo_saida:
            for arquivo_entrada in arquivos_entrada:
                with open(arquivo_entrada, 'r') as arquivo:
                    arquivo_saida.write(arquivo.read())
                    arquivo_saida.write("\n")
        print(f'Arquivos {arquivos_entrada} concatenados em {arquivo_saida}')
    except FileNotFoundError as e:
        print(f"Erro: {e}")

def schd(intervalo, tarefa):
    def tarefa_envolvida():
        exe(tarefa)
    
    schedule.every(intervalo).seconds.do(tarefa_envolvida)

    while True:
        schedule.run_pending()
        time.sleep(1)

def interpretar_comando(comando, comandos_externos):
    if comando.startswith("lst |>"):
        diretorio = re.search(r'\{(.*?)\}', comando).group(1)
        lst(diretorio)
    elif comando.startswith("cpy >"):
        partes = re.findall(r'\{(.*?)\}', comando)
        cpy(partes[0], partes[1])
    elif comando.startswith("del |"):
        arquivo = re.search(r'\{(.*?)\}', comando).group(1)
        del_(arquivo)
    elif comando.startswith("exe $"):
        comando_executar = re.search(r'\{(.*?)\}', comando).group(1)
        exe(comando_executar)
    elif comando.startswith("ren >"):
        partes = re.findall(r'\{(.*?)\}', comando)
        ren(partes[0], partes[1])
    elif comando.startswith("mov >"):
        partes = re.findall(r'\{(.*?)\}', comando)
        mov(partes[0], partes[1])
    elif comando.startswith("mkdir |>"):
        diretorio = re.search(r'\{(.*?)\}', comando).group(1)
        mkdir(diretorio)
    elif comando.startswith("cat >"):
        partes = re.findall(r'\{(.*?)\}', comando)
        arquivo_saida = partes[0]
        arquivos_entrada = partes[1:]
        cat(arquivo_saida, *arquivos_entrada)
    elif comando.startswith("schd $"):
        partes = re.findall(r'\{(.*?)\}', comando)
        intervalo = int(partes[0])
        tarefa = partes[1]
        schd(intervalo, tarefa)
    else:
        for nome, cmd_info in comandos_externos.items():
            if cmd_info["comando"] in comando:
                print(f"Executando comando personalizado: {cmd_info['descricao']}")
                exe(cmd_info["comando"])
                break
        else:
            print("Comando não reconhecido.")

def main():
    welcome_message()
    comandos_externos = carregar_comandos_externos("cmds.exs")
    while True:
        comando = input("Digite um comando: ")
        if comando.lower() == "exit":
            break
        interpretar_comando(comando, comandos_externos)

if __name__ == "__main__":
    main()