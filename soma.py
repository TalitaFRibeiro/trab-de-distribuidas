import socket 
 
# Cria um socket TCP/IP 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
 
# Liga o socket a um endereço e porta 
server_socket.bind(('localhost', 8080)) 
 
# Define o número máximo de conexões em fila 
server_socket.listen(5) 
 
print("Servidor pronto e aguardando conexões...") 
 
while True:
# Aceita uma nova conexão 
    client_socket, client_address = server_socket.accept() 
    print(f"Conexão estabelecida com {client_address}") 
 
    # Recebe dados do cliente 
    data = client_socket.recv(1024) 
    if not data:
        break 
    # Decodifica a mensagem recebida 
    decoded_data = data.decode('utf-8') 
    try:
        num1,num2 = decoded_data.split(" ",2)
        num1 = int(num1)
        num2 = int(num2)
    except(ValueError):
        print(f"Erro de formatação nos dados recebidos: {decoded_data}")
        client_socket.send("Formato inválido. Envie dois números separados por espaço.".encode('utf-8'))
        continue
    soma = num1 + num2
    print(f"Recebido no soma: {decoded_data}") 
    
        # Envia uma resposta ao cliente 
    response = str(soma)
    client_socket.send(response.encode('utf-8')) 
     
   
    

client_socket.close()