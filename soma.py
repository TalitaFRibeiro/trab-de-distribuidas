import socket 
import traceback
# Cria um socket TCP/IP 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
 
# Liga o socket a um endereço e porta 
server_socket.bind(('localhost', 8080)) 
 
# Define o número máximo de conexões em fila 
server_socket.listen(5) 
 
print("Servidor soma pronto e aguardando conexões...") 
 
while True:
# Aceita uma nova conexão 
    client_socket, client_address = server_socket.accept() 
    print(f"Conexão soma estabelecida com {client_address}") 
 
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
    except(ValueError):
        print(f"Erro de formatação nos dados recebidos: {decoded_data}")
        response = ValueError
        print(f"Mensagem erro inteiros: {traceback.format_exc()}")
        client_socket.send("Formato inválido. Envie dois números separados por espaço.".encode('utf-8'))
        continue
    else:
        soma = num1 + num2
        print(f"Recebido no soma: {decoded_data}") 
        
            # Envia uma resposta ao cliente 
        response = str(soma)
        client_socket.send(response.encode('utf-8')) 
    finally:
        arquivo = open("soma.txt","a")
        print(f"[{client_address}] soma {num1} + {num2} = {response}",file=arquivo)
        arquivo.close()
        client_socket.close()
        print("Desconectado soma")
     
   
    

client_socket.close()