# Usa Python 3.10 como base
FROM python:3.10

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
ADD main.py .
ADD models/ ./models/  
ADD data/ ./data/      

# Instalar dependencias necesarias
# Si usas un archivo requirements.txt, agrégalo y ejecuta pip install
# ADD requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Configurar un comando interactivo
CMD ["python", "-i", "./main.py"]
