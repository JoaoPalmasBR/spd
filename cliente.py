import socket
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from crypto import generate_keys

def encrypt(message, public_key):
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

def decrypt(private_key, encrypted_message):
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # cria o objeto socket protocolo afinet ipv4; SOCKSTREAM define TCP
localhost = '172.30.128.1' # define ip do servidor
porta = 12345  # define a porta

client_socket.connect((localhost, porta))  # conecta ao servidor

print("Conectado ao servidor em %s:%d" % (localhost, porta))
#client_socket.send("".encode())
#chave = client_socket.recv(1024).decode()

#envia a mensagem para o servidor
mensagem = "Olá, servidor!"
#mensagemEncrypt = encrypt(chave, mensagem)
#client_socket.send(mensagemEncrypt.encode())  # encode converte string para bytes e envia para o servidor

#recebe a mensagem do servidor
#dados = client_socket.recv(1024).decode()  # decode converte bytes para string
#print("Mensagem recebida: %s" % dados)

#client_socket.close()