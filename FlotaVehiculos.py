from ListaEnlasadasS import ListaEnlazada
from Vehiculo import Vehiculo
class FlotaVehiculos:
    def __init__(self):
        self.vehiculos = ListaEnlazada() 

    def registrar_vehiculo(self, vehiculo):
        self.vehiculos.insertar(vehiculo)
        print(f"Vehículo con placa {vehiculo.placa} registrado exitosamente.")

    def eliminar_vehiculo(self, placa):
        if self.vehiculos.eliminar(placa):
            print(f"Vehículo con placa {placa} eliminado exitosamente.")
        else:
            print(f"No se encontró un vehículo con placa {placa}.")

    def buscar_vehiculo(self, placa):
        vehiculo = self.vehiculos.buscar(placa)
        if vehiculo:
            print("Información del vehículo:")
            print(vehiculo)
        else:
            print(f"No se encontró un vehículo con placa {placa}.")

    def listar_vehiculos(self):
        print("Listado de vehículos registrados:")
        self.vehiculos.mostrar()