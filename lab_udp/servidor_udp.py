import socket  # Importa el módulo socket para comunicación en red


# Dirección IP donde el servidor UDP escuchará (localhost)
UDP_IP = "127.0.0.1"
# Puerto donde el servidor UDP recibirá los mensajes
UDP_PORT = 5005


# Crea un socket UDP
# socket.AF_INET indica que se usará IPv4
# socket.SOCK_DGRAM indica que será un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Asocia el socket a la IP y puerto definidos
server_socket.bind((UDP_IP, UDP_PORT))


# Muestra que el servidor está listo y escuchando
print(f"Servidor UDP escuchando en {UDP_IP}:{UDP_PORT}")


# Bucle infinito para recibir mensajes continuamente
while True:
    # Espera y recibe un datagrama (mensaje UDP)
    # recvfrom(1024) recibe hasta 1024 bytes y devuelve:
    #   - data: los datos recibidos (en bytes)
    #   - addr: una tupla (IP, puerto) del cliente que envió el mensaje
    data, addr = server_socket.recvfrom(1024)
    # Muestra el mensaje recibido y la dirección del cliente
    print(f"Mensaje recibido de {addr}: {data.decode()}")
    # Envía una respuesta de confirmación al cliente
    server_socket.sendto("Mensaje recibido".encode(), addr)
