import socket
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
PORTSOP = [8080,8081,8082,8083]
PORT = 8000
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = 'localhost'
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
mensagem_parada = "--1"
sinal_parada = 0
MAX_THREADS = 5

#vira cliente



def isola_cliente(conn, addr):
    print(f"[Novo cliente] {addr} conectado.")

    connectado = True

    while connectado:
        try:
            data = conn.recv(1024)
            if not data:
                break
            decoded_data = data.decode('utf-8')
            if(decoded_data==mensagem_parada):
                global sinal_parada
                sinal_parada = 1
                break
            mensagem = vira_cliente(decoded_data)
            conn.send(mensagem.encode('utf-8'))
            
            print(f"Recebido de {addr}: {decoded_data}")
            if(decoded_data == DISCONNECT_MESSAGE):
                connectado = False
                print("Proxxy Desconectado")
                break
        except UnicodeDecodeError as e:
            print("Caractere não reconhecível")
    conn.close()
    
    
        
         

           


def start():
    server.listen()
    threads = []
    print(f"[Ouvindo pelo proxy] Proxy no endereço {SERVER}")
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        while True:
            
            conn, addr = server.accept()
            print(f"do proxy ouvindo o cliente {conn} conn e addr {addr}")
            executor.submit(isola_cliente, conn, addr)
            #thread = threading.Thread(target=isola_cliente,args=(conn, addr))
            #threads.append(thread)
            #thread.start()
            print(f"[Começando proxy] {threading.active_count()- 1}")
        
        
        

def vira_cliente(decoded_data):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    pedido = decoded_data.split(" ",3)
    if (len(pedido) < 3):
        return "Formato de mensagem inválido."
    operador = pedido[0] 
    try:
        arg1 = int(pedido[1])
        arg2 = int(pedido[2])
    except ValueError:
        return "Argumentos inválidos. Por favor, envie números inteiros."
    mensagem = str(arg1) + " " +str(arg2)
    try:
        if("soma" in operador):
            cliente.connect((SERVER,8080))
            cliente.send(mensagem.encode('utf-8'))
            
        elif("sub" in operador):
            cliente.connect((SERVER,8081))
            cliente.send(mensagem.encode('utf-8'))
        elif("multi" in operador):
            cliente.connect((SERVER,8082))
            cliente.send(mensagem.encode('utf-8'))
        elif("divi" in decoded_data):
            cliente.connect((SERVER,8083))
            cliente.send(mensagem.encode('utf-8'))
        else:
            return "Operação não Permitida"
        
        
    except Exception as e:
        return f"Erro ao conectar ao servidor de operação: {str(e)}"
    else:
        response = cliente.recv(1024)
        response_decoded = response.decode('utf-8')
        cliente.close()
        return response_decoded
    finally:
        cliente.close()


start()
