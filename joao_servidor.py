import socket
import threading
import json
from Crypto.Cipher import AES
import os

# Dicionário para armazenar as chaves de criptografia dos clientes
chaves_clientes = {}

# Função para criptografar dados
def criptografar(chave, dados):
    cifra = AES.new(chave, AES.MODE_EAX)
    nonce = cifra.nonce
    dados_criptografados, tag = cifra.encrypt_and_digest(dados)
    return nonce + tag + dados_criptografados  # Inclui a `tag` para validar a integridade

# Função para descriptografar dados
def descriptografar(chave, dados):
    nonce = dados[:16]  # O nonce tem 16 bytes
    tag = dados[16:32]  # A tag tem 16 bytes
    dados_criptografados = dados[32:]

    cifra = AES.new(chave, AES.MODE_EAX, nonce=nonce)
    dados_descriptografados = cifra.decrypt_and_verify(dados_criptografados, tag)  # Valida a `tag`
    return dados_descriptografados

# Função para lidar com um cliente
def lidar_com_cliente(soquete_cliente, endereco_cliente):
    print(f"[+] Cliente {endereco_cliente} conectado.")

    # Gera uma chave segura para o cliente
    chave = os.urandom(16)
    chaves_clientes[endereco_cliente] = chave

    # Envia a chave criptografada com AES para o cliente
    soquete_cliente.send(chave)

    while True:
        try:
            dados = soquete_cliente.recv(4096)
            if not dados:
                break

            # Descriptografar dados recebidos
            dados_descriptografados = descriptografar(chave, dados)
            dicionario_recebido = json.loads(dados_descriptografados.decode())

            print(f"[*] Dados recebidos de {endereco_cliente}: {dicionario_recebido}")

            # Resposta ao cliente
            resposta = {"status": "sucesso", "dados": dicionario_recebido}
            
            # Criptografar e enviar resposta
            resposta_criptografada = criptografar(chave, json.dumps(resposta).encode())
            soquete_cliente.send(resposta_criptografada)

        except Exception as erro:
            print(f"[-] Erro com {endereco_cliente}: {erro}")
            break

    print(f"[-] Cliente {endereco_cliente} desconectado.")
    soquete_cliente.close()
    del chaves_clientes[endereco_cliente]

# Configuração do servidor
ip_servidor = "0.0.0.0"
porta_servidor = 12345

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((ip_servidor, porta_servidor))
servidor.listen(5)
print(f"[*] Servidor escutando em {ip_servidor}:{porta_servidor}")

while True:
    soquete_cliente, endereco_cliente = servidor.accept()
    thread_cliente = threading.Thread(target=lidar_com_cliente, args=(soquete_cliente, endereco_cliente))
    thread_cliente.start()
