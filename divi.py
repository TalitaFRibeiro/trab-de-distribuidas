import socket 
 
# Cria um socket TCP/IP 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
 
# Liga o socket a um endereço e porta 
server_socket.bind(('localhost', 8083)) 
 
# Define o número máximo de conexões em fila 
server_socket.listen(5) 
 
print("Servidor divisão pronto e aguardando conexões...") 
 
while True:
# Aceita uma nova conexão 
    client_socket, client_address = server_socket.accept() 
    print(f"Conexão em divisão estabelecida com {client_address}") 
 
    # Recebe dados do cliente 
    data = client_socket.recv(1024) 
    if not data:
        break 
    # Decodifica a mensagem recebida 
    decoded_data = data.decode('utf-8') 
    try:
        num1,num2 = decoded_data.split(" ",2)
        num1 = float(num1)
        num2 = float(num2)
        if(num2 == 0):
            raise ValueError
    except(ValueError):
        print(f"Erro de formatação nos dados recebidos: {decoded_data}")
        response = "Operação inválida"
        client_socket.send("Formato inválido. Divisor não pode ser zero".encode('utf-8'))
       
        print("Desconectei")
    else:
        soma = num1/num2
        print(f"Recebido no subtra: {decoded_data}") 
        
            # Envia uma resposta ao cliente 
        response = str(soma)
        client_socket.send(response.encode('utf-8')) 
        
        
    finally:
        client_socket.close()
        arquivo = open("divi.txt","a")
        print(f"[{client_address}] divisão {num1} / {num2} = {response}",file=arquivo)
        arquivo.close()
        print("Desconectado divisão")
   
    

client_socket.close()