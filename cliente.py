import socket 

PORT = 8000
# Cria um socket TCP/IP 
ipp = 'localhost'
ADDR = (ipp,PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
 
try: 
    # Conecta ao servidor 
    client_socket.connect(ADDR) 
    while True:
        # Envia uma mensagem 
        try:
            operacao = input("Qual operação:\n 1:Soma \n 2:Subração\n 3:Multiplicação\n4:Divisão\n -1:Sair\n")
            if(operacao == "-1"):
                fim = "!DISCONNECT"
                client_socket.send(fim.encode('utf-8')) 
                break 
            
            if(operacao == "1"):
                operador = "soma"
            elif(operacao == "2"):
                operador = "subtra"
            elif(operacao == "3"):
                operador = "multipl"
            elif(operacao == "4"):
                operador = "divi"
            else:
                raise Exception
            op1 = float(input("Primeiro operando:\n"))
            op2 = float(input("Segundo operando:\n"))
        except:    
            print("Digite uma operação válida")
        else:
            
            message = operador + " " + str(op1) + " " + str(op2)
            client_socket.send(message.encode('utf-8')) 
            
            
        
            # Recebe a resposta do servidor 
            response = client_socket.recv(1024) 
            print(f"Resposta do servidor: {response.decode('utf-8')}") 
 
except ConnectionRefusedError as e: 
    print(f"Erro de conexão: {e}") 
 
except UnicodeEncodeError as e: 
    print(f"Erro de codificação: {e}") 
 
finally: 
    # Fecha o socket 
    client_socket.close()
