import csv
import random
import re

vehiculos = []

def valpatente(patente):
    # Patente válida debe tener el formato xxxx-00 o xx-0000
    return bool(re.match(r'^[A-Za-z]{4}\d{2}$', patente) or re.match(r'^[A-Za-z]{2}\d{4}$', patente))

def valmarca(marca):
    return 2 <= len(marca) <= 10

def valprecio(precio):
    return precio >= 5000000
