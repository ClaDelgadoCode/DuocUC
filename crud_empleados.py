import os
import json
os.system("cls")

def cargar_jason(url_archivo):
    with open(url_archivo, 'r') as archivo:
        return json.load(archivo)
    
empleados = cargar_jason('empleados.json')

print(empleados)