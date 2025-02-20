from datetime import datetime
from Mantenimiento import Mantenimiento
from ListaEnlasadasS import ListaEnlazada

class Vehiculo:
    def __init__(self, placa, marca, modelo, año, kilometraje):
        self.placa = placa 
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.historialMantenimiento = ListaEnlazada()

    def agregar_mantenimiento(self, mantenimiento):
        if isinstance(mantenimiento, Mantenimiento):
            self.historialMantenimiento.insertar(mantenimiento)
        else:
            print("Error: El mantenimiento debe ser una instancia de la clase Mantenimiento.")

    def consultar_historial(self):
        return self.historialMantenimiento.recorrer()

    def calcular_costo_total_mantenimientos(self):
        return sum(m.costo for m in self.consultar_historial())

    def __str__(self):
        return (f"Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, "
                f"Año: {self.año}, Kilometraje: {self.kilometraje}\n"
                f"Cantidad de mantenimientos: {len(self.consultar_historial())}")
