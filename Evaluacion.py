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

# Buscar
def buscar_vehiculo():
    os.system('cls')
    patente = input("Ingrese la patente del vehículo a buscar: ")
    os.system('cls')
    encontrado = False
    
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == patente:
                encontrado = True
                año = int(row[3])
                años_transcurridos = datetime.now().year - año
                print(f"Patente: {row[0]}, Marca: {row[1]}, Modelo: {row[2]}, Año: {row[3]}, Valor: {row[4]}, ¿Vendido?: {row[5]}")
                print(f"Años transcurridos desde fabricación: {años_transcurridos}")
                input("Presione una tecla para continuar...")
                os.system('cls')
                break
    
    if not encontrado:
        print("Vehículo no encontrado.")
        input("Presione una tecla para continuar...")
        os.system('cls')

# Listar
def listar_vehiculos():
    os.system('cls')
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Patente: {row[0]}, Marca: {row[1]}, Modelo: {row[2]}, Año: {row[3]}, Valor: {row[4]}, ¿Vendido?: {row[5]}")
            
        input("Presione una tecla para continuar...")
        os.system('cls')

# Comprar vehiculo
def imprimir_contrato():
    os.system('cls')
    patente = input("Ingrese la patente del vehículo a vender: ")
    encontrado = False
    vehiculos = []

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            vehiculos.append(row)
            if row[0] == patente and row[5] == "no":
                encontrado = True
                datos_vehiculo = row
                break
    
    if not encontrado:
        print("Vehículo no encontrado o ya vendido.")
        input("Presione una tecla para continuar...")
        os.system('cls')
        return
    
    confirmar = input("¿Confirma la venta del vehículo? (si/no): ")
    if confirmar.lower() != "si":
        print("Venta cancelada.")
        input("Presione una tecla para continuar...")
        os.system('cls')
        return
    
    # Generar número de contrato
    numero_contrato = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Imprimir contrato
    os.system('cls')
    print("Contrato de Compraventa")
    print(f"Número de contrato: {numero_contrato}")
    print(f"Patente: {datos_vehiculo[0]}, Marca: {datos_vehiculo[1]}, Modelo: {datos_vehiculo[2]}, Año: {datos_vehiculo[3]}, Valor: {datos_vehiculo[4]}")
    
    # Actualizar el estado del vehículo a "vendido"
    for vehiculo in vehiculos:
        if vehiculo[0] == patente:
            vehiculo[5] = "si"
    
    # Guardar cambios en el archivo CSV
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(vehiculos)
    
    print("Vehículo vendido exitosamente.")
    input("Presione una tecla para continuar...")
    os.system('cls')

# Mostrar menú
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            guardar_vehiculo()
        elif opcion == "2":
            buscar_vehiculo()
        elif opcion == "3":
            listar_vehiculos()
        elif opcion == "4":
            imprimir_contrato()
        elif opcion == "5":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")
            input("Presione una tecla para continuar...")
            os.system('cls')

if __name__ == "__main__":
    main()