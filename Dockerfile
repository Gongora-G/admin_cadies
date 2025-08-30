# Utiliza una imagen oficial de Python como base
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del proyecto al contenedor
COPY . /app

# Expone el puerto que usa el servidor
EXPOSE 65432

# Comando para ejecutar el servidor
CMD ["python", "servidor.py"]
