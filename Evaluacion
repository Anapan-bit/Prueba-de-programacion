import csv
from datetime import datetime
import os

# Archivo donde se almacenarán los datos
FILENAME = 'vehiculos.csv'

# Definir el menú
def mostrar_menu():
    print("Menú:")
    print("1. Guardar")
    print("2. Buscar")
    print("3. Listar")
    print("4. Imprimir")
    print("5. Salir")

# Guardar
def guardar_vehiculo():
    os.system('cls')
    patente = input("Ingrese la patente (6 caracteres): ")
    if len(patente) != 6:
        print("La patente debe tener 6 caracteres.")
        return
    
    marca = input("Ingrese la marca (mínimo 3 caracteres): ")
    if len(marca) < 3:
        print("La marca debe tener al menos 3 caracteres.")
        return
    
    modelo = input("Ingrese el modelo (mínimo 3 caracteres): ")
    if len(modelo) < 3:
        print("El modelo debe tener al menos 3 caracteres.")
        return
    
    año = int(input("Ingrese el año del vehículo (entre 1980 y 2024): "))
    if año <= 1980 or año > 2024:
        os.system('cls')
        print("El año debe ser mayor a 1980 o menos al actual.")
        input("Presione una tecla para continuar...")
        os.system('cls')
        return
    
    valor = int(input("Ingrese el valor (mínimo 500.000): "))
    if valor < 500000:
        print("El valor debe ser mínimo 500.000.")
        return

    # Guardar datos en el archivo CSV
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([patente, marca, modelo, año, valor, "no"])
    
    os.system('cls')
    print("Vehículo guardado exitosamente.")
    input("Presione una tecla para continuar...")
    os.system('cls')
