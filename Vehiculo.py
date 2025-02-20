from datetime import datetime
from Mantenimiento import Mantenimiento

class Vehiculo:
    def __init__(self, placa, marca, modelo, año, kilometraje):
        self.placa = placa 
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.historialMantenimiento = []

    @property
    def año(self):
        return self._año
    
    @año.setter
    def año(self, año):
        anio_actual = datetime.now().year
        try:
            año = int(año)
            if 1900 < año <= anio_actual:
                self._año = año
            else:
                print(f"Año no válido. Debe estar entre 1900 y {anio_actual}. Se asignará 2000 por defecto.")
                self._año = 2000  
        except ValueError:
            print("Año no válido. Debe ser un número entero. Se asignará 2000 por defecto.")
            self._año = 2000

    @property
    def kilometraje(self):
        return self._kilometraje
    
    @kilometraje.setter
    def kilometraje(self, kilometraje):
        try:
            kilometraje = float(kilometraje)
            if kilometraje >= 0:
                self._kilometraje = kilometraje
            else:
                print("Kilometraje erróneo, no debe ser negativo. Se asignará 0 por defecto.")
                self._kilometraje = 0
        except ValueError:
            print("Kilometraje no válido. Debe ser un número. Se asignará 0 por defecto.")
            self._kilometraje = 0

    @property
    def placa(self):
        return self._placa
    
    @placa.setter
    def placa(self, placa):
        if isinstance(placa, str) and len(placa) == 6 and placa[:3].isalpha() and placa[3:].isdigit():
            self._placa = placa.upper()
        else:
            print("Placa no válida. Debe tener 3 letras seguidas de 3 números (Ej: ABC123). Se asignará 'AAA000' por defecto.")
            self._placa = "AAA000"

    @property
    def historialMantenimiento(self):
        return self._historialMantenimiento
    
    @historialMantenimiento.setter
    def historialMantenimiento(self, historialMantenimiento):
        if isinstance(historialMantenimiento, list):
            self._historialMantenimiento = historialMantenimiento
        else:
            print("Error: El historial de mantenimiento debe ser una lista.")
            self._historialMantenimiento = []

    def agregar_mantenimiento(self, mantenimiento):
        if isinstance(mantenimiento, Mantenimiento):
            self.historialMantenimiento.append(mantenimiento)
        else:
            print("Error: El mantenimiento debe ser una instancia de la clase Mantenimiento.")

    def consultar_historial(self):
        return self.historialMantenimiento

    def calcular_costo_total_mantenimientos(self):
        return sum(mantenimiento.costo for mantenimiento in self.historialMantenimiento)
    
    def __str__(self):
        return (f"Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, "
                f"Año: {self.año}, Kilometraje: {self.kilometraje}\n"
                f"Cantidad de mantenimientos: {len(self.historialMantenimiento)}")
