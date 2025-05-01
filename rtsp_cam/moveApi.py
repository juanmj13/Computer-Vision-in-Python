import requests
from requests.auth import HTTPBasicAuth

# Configure for yor camera
ip = '192.168.1.108'  # IP
user = 'admin'        # User
password = 'AetoArch1'  # Password

# Base URL
base_url = f"http://{ip}/cgi-bin/ptz.cgi"

# Comando para mover la cámara hacia la izquierda
url = f"{base_url}?action=start&code=Left&arg1=0&arg2=1&arg3=0"

# Autenticación básica
response = requests.get(url, auth=HTTPBasicAuth(user, password))

if response.status_code == 200:
    print("Comando enviado correctamente.")
else:
    print(f"Error: {response.status_code} - {response.text}")
