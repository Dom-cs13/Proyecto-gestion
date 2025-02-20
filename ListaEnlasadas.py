from Vehiculo import Vehiculo
from Mantenimiento import Mantenimiento

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListasCircular:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza  
        else:
            tmp = self.cabeza
            while tmp.siguiente != self.cabeza:  
                tmp = tmp.siguiente
            tmp.siguiente = nuevo 
            nuevo.siguiente = self.cabeza 

    def mostrar(self):
        if self.cabeza is None:
            print("No hay vehículos registrados.")
            return
        tmp = self.cabeza
        print("\n=== LISTADO DE VEHÍCULOS REGISTRADOS ===")
        i = 1
        while True:
            print(f"\nVehículo {i}: {tmp.dato}")
            tmp = tmp.siguiente
            i += 1
            if tmp == self.cabeza:
                break

    def buscarPorPlaca(self, placa):
        if self.cabeza is None:
            return None
        tmp = self.cabeza
        while True:
            if tmp.dato.placa == placa:
                return tmp.dato
            tmp = tmp.siguiente
            if tmp == self.cabeza:
                break
        return None