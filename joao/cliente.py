import socket
import json
from Crypto.Cipher import AES

# Função para criptografar dados
def criptografar(chave, dados):
    cifra = AES.new(chave, AES.MODE_EAX)
    nonce = cifra.nonce
    dados_criptografados, tag = cifra.encrypt_and_digest(dados)
    return nonce + tag + dados_criptografados  # Inclui a `tag`

# Função para descriptografar dados
def descriptografar(chave, dados):
    nonce = dados[:16]
    tag = dados[16:32]
    dados_criptografados = dados[32:]

    cifra = AES.new(chave, AES.MODE_EAX, nonce=nonce)
    dados_descriptografados = cifra.decrypt_and_verify(dados_criptografados, tag)  # Valida a `tag`
    return dados_descriptografados

# Configuração do cliente
ip_servidor = "127.0.0.1"
porta_servidor = 12345

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ip_servidor, porta_servidor))

# Recebe a chave de criptografia do servidor
chave = cliente.recv(16)  # Chave de 16 bytes recebida do servidor
print("[*] Chave de criptografia recebida.")

# Dados a serem enviados
dados = {"nome": "Cliente1", "mensagem": "Olá, servidor!"}
dados_criptografados = criptografar(chave, json.dumps(dados).encode())

# Envia os dados criptografados
cliente.send(dados_criptografados)

# Recebe a resposta do servidor
resposta_criptografada = cliente.recv(4096)
resposta = json.loads(descriptografar(chave, resposta_criptografada).decode())

print(f"[+] Resposta do servidor: {resposta}")

cliente.close()
