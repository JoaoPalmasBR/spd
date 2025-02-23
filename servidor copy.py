import socket

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

#recebe a mensagem do cliente
dados = conexao.recv(1024).decode()  # decode converte bytes para string
print("Mensagem recebida: %s" % dados)

conexao.send("Mensagem recebida!".encode())  # encode converte string para bytes e envia para o cliente


conexao.close()  # fecha a conexão

server_socket.close()  # fecha o socket