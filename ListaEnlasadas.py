from Vehiculo import Vehiculo
from Mantenimiento import Mantenimiento
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListasCircular:  
    def __init__(self):
        self.cabeza = None
        self.actual = None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
            self.actual = self.cabeza
        else:
            tmp = self.cabeza
            while tmp.siguiente != self.cabeza:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.siguiente = self.cabeza
 
    def mostrar(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return
        tmp = self.cabeza
        print("\n=== LISTADO DE VEHÍCULOS ===")
        i = 1
        while True:
            print(f"\nVehículo {i}:")
            print(tmp.dato)
            tmp = tmp.siguiente
            i += 1
            if tmp == self.cabeza:
                break
    
    def mostrarSiguiente(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return
        
        print("\n=== VEHÍCULO ACTUAL ===")
        print(self.actual.dato)
        self.actual = self.actual.siguiente
    
    def Buscar(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return None
        
        placa = input("Ingrese la placa a buscar: ")
        tmp = self.cabeza
        while True:
            if tmp.dato.placa == placa:
                print("\n=== VEHÍCULO ENCONTRADO ===")
                print(tmp.dato)
                return tmp.dato
            tmp = tmp.siguiente
            if tmp == self.cabeza:
                print(f"No se encontró un vehículo con placa {placa}")
                break
        return None

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

    def Eliminar(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return False
        
        placa = input("Ingrese la placa del vehículo a eliminar: ")
        if self.cabeza.dato.placa == placa:
            if self.cabeza.siguiente == self.cabeza:
                self.cabeza = None
                self.actual = None
                print(f"Vehículo con placa {placa} eliminado correctamente")
                return True
            else:
                tmp = self.cabeza
                while tmp.siguiente != self.cabeza:
                    tmp = tmp.siguiente
                tmp.siguiente = self.cabeza.siguiente
                if self.actual == self.cabeza:
                    self.actual = self.cabeza.siguiente
                self.cabeza = self.cabeza.siguiente
                print(f"Vehículo con placa {placa} eliminado correctamente")
                return True
        
        tmp = self.cabeza
        while tmp.siguiente != self.cabeza:
            if tmp.siguiente.dato.placa == placa:
                if self.actual == tmp.siguiente:
                    self.actual = self.actual.siguiente
                tmp.siguiente = tmp.siguiente.siguiente
                print(f"Vehículo con placa {placa} eliminado correctamente")
                return True
            tmp = tmp.siguiente
        
        print(f"No se encontró un vehículo con placa {placa}")
        return False

    def agregarMantenimiento(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return
            
        placa = input("Ingrese la placa del vehículo: ")
        vehiculo = self.buscarPorPlaca(placa)
        
        if vehiculo:
            print(f"Agregando mantenimiento al vehículo con placa {placa}")
            fechaM = input("Fecha Mantenimiento: ")
            descripcion = input("Descripción: ")
            costo = input("Costo: ")
            
            nuevo_mantenimiento = Mantenimiento(fechaM, descripcion, costo)
            vehiculo.agregar_mantenimiento(nuevo_mantenimiento)
            print("Mantenimiento agregado correctamente")
        else:
            print(f"No se encontró un vehículo con placa {placa}")

    def mostrarMantenimientos(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return
            
        placa = input("Ingrese la placa del vehículo: ")
        vehiculo = self.buscarPorPlaca(placa)
        
        if vehiculo:
            historial = vehiculo.consultar_historial()
            if not historial:
                print(f"El vehículo con placa {placa} no tiene mantenimientos registrados")
                return
                
            print(f"\n=== HISTORIAL DE MANTENIMIENTOS DEL VEHÍCULO {placa} ===")
            for i, mant in enumerate(historial, 1):
                print(f"\nMantenimiento {i}:")
                print(mant)
        else:
            print(f"No se encontró un vehículo con placa {placa}")

    def calcularCostoTotalMantenimientos(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return
            
        placa = input("Ingrese la placa del vehículo: ")
        vehiculo = self.buscarPorPlaca(placa)
        
        if vehiculo:
            costo_total = vehiculo.calcular_costo_total_mantenimientos()
            print(f"\nCosto total de mantenimientos del vehículo {placa}: ${costo_total:.2f}")
        else:
            print(f"No se encontró un vehículo con placa {placa}")

 
