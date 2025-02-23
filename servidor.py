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

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # cria o objeto socket protocolo afinet ipv4; SOCKSTREAM define TCP
localhost = "0.0.0.0" # define ip do servidor
porta = 12345  # define a portas

# vincula o socket a um endereço e porta
server_socket.bind((localhost, porta))   # associa o socket a um endereço e porta
server_socket.listen(1) # define o limite de conexões em 1 ativo por vez


print("Servidor rodando em %s:%d" % (localhost, porta))

#aceita a conexão
conexao, endereco = server_socket.accept()  # aceita a conexão do cliente

print("Conexão de %s:%d" % (endereco[0], endereco[1]))
print("Aguardando mensagem...")

chave_publica, chave_privada = generate_keys()




print(conexao)

#recebe a mensagem do cliente
dados = conexao.recv(1024).decode()  # decode converte bytes para string
print("Mensagem recebida: %s" % dados)



conexao.send(chave_publica.encode())  # encode converte string para bytes e envia para o cliente
dados = conexao.recv(1024).decode()  # decode converte bytes para string
dadosDesencrypt = decrypt(chave_privada, dados)
print("Mensagem recebida: %s" % dadosDesencrypt)

conexao.close()  # fecha a conexão

server_socket.close()  # fecha o socket