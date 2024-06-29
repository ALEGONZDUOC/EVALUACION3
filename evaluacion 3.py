import csv
import random
import re

autos = []

def valpatente(patente):
    return bool(re.match(r'^[A-Za-z]{4}\d{2}$', patente) or re.match(r'^[A-Za-z]{2}\d{4}$', patente))

def valmarca(marca):
    return 2 <= len(marca) <= 10

def valprecio(precio):
    return precio >= 5000000

def grabauto():
    tipo = input("Ingrese el tipo de vehículo (SUV/Sedan/Hackback/Convertible/Minivan):  " ).lower()
    patente = input("Ingrese la patente del auto (formato xxxx00 o xx0000): ")
    while not valpatente(patente):
        print("Patente inválida. Debe tener el formato xxxx00 o xx0000.")
        patente = input("Ingrese la patente del auto (formato xxxx00 o xx0000): ")
    
    marca = input("Ingrese la marca del auto: ")
    while not valmarca(marca):
        print("Marca inválida. Debe tener entre 2 y 10 caracteres.")
        marca = input("Ingrese la marca del auto: ")

    precio = int(input("Ingrese el precio del auto: "))
    while not valprecio(precio):
        print("Precio inválido. Debe ser mayor o igual a $5.000.000.")
        precio = int(input("Ingrese el precio del auto: "))
    
    multas =  input("¿El vehículo tiene multa? Ingrese S para SI y N para NO):  " ).lower()
    if multas == "s":
        fecha_multa = input("Ingrese la fecha de multa:  " ).lower()
        monto_multa  = input("Ingrese el monto de la multa:  " ).lower()
    else:
        fecha_multa = "00-00-0000" 
        monto_multa = 0
    
    fecha_registro = input("Ingrese la fecha de registro del auto (DD-MM-AAAA): ")
    nombre_dueno = input("Ingrese el nombre del dueño del auto: ")

    auto = {
        "tipo": tipo,
        "patente": patente,
        "marca": marca,
        "precio": precio,
        "multas": multas,
        "fecha de registro": fecha_registro,
        "nombre del dueño": nombre_dueno
    }
    autos.append(auto)
    print("Auto grabado con éxito.")

def busauto():
    patente = input("Ingrese la patente del auto a buscar: ")
    for auto in autos:
        if auto["patente"] == patente:
            print("Auto encontrado:")
            for key, value in auto.items():
                print(f"{key}: {value}")
            return
    print("Auto no encontrado.")

def generar_certificado(auto, tipcert):
    valor = random.randint(1500, 3500)
    print(f"\nCertificado de {tipcert}")
    print(f"Patente: {auto['patente']}")
    print(f"Dueño: {auto['nombre del dueño']}")
    print(f"Valor del certificado: ${valor}")
    
    with open(f"{tipcert}_{auto['patente']}.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Certificado", "Patente", "Dueño", "Valor"])
        writer.writerow([tipcert, auto['patente'], auto["nombre del dueño"], valor])
    print(f"Archivo CSV generado: {tipcert}_{auto['patente']}.csv")

def impcert():
    patente = input("Ingrese la patente del auto: ")
    auto = next((a for a in autos if a["patente"] == patente), None)
    if auto:
        while True:
            print("\n****Menú de Certificados ****")
            print("1. Emisión de contaminantes")
            print("2. Anotaciones vigentes")
            print("3. Multas")
            print("4. Volver al menú principal")
            opcion = input("Seleccione el tipo de certificado a imprimir: ")
            
            if opcion == "1":
                generar_certificado(auto, "Emisión de contaminantes")
                break
            elif opcion == "2":
                generar_certificado(auto, "Anotaciones vigentes")
                break
            elif opcion == "3":
                generar_certificado(auto, "Multas")
                break
            elif opcion == "4":
                print("Volviendo al menú principal.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
    else:
        print("Auto no encontrado.")

def salir():
    print("\nGracias por usar nuestro programa")
    print("Gonzalez Alexander y Urzua Cristian")
    print("Versión: 1.0")
    exit()


