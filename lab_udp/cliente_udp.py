import socket  # Importa el módulo socket para comunicación en red


# Dirección IP del servidor UDP (localhost)
UDP_IP = "127.0.0.1"
# Puerto donde el servidor UDP está escuchando
UDP_PORT = 5005


# Crea un socket UDP
# socket.AF_INET indica que se usará IPv4
# socket.SOCK_DGRAM indica que será un socket UDP (no orientado a conexión)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Mensaje que se enviará al servidor
message = "Hola servidor UDP!"
# Envía el mensaje al servidor usando el método sendto()
# .encode() convierte el string a bytes, que es lo que espera el socket
# El segundo parámetro es una tupla con la IP y el puerto de destino
client_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))


# Espera la respuesta del servidor
# recvfrom(1024) recibe hasta 1024 bytes y devuelve una tupla:
#   - data: los datos recibidos (en bytes)
#   - server: una tupla (IP, puerto) del servidor que envió la respuesta
data, server = client_socket.recvfrom(1024)
# Muestra la respuesta del servidor decodificando los bytes a string
print("Respuesta del servidor:", data.decode())
