import os
from Vehiculo import Vehiculo
from ListaEnlasadas import ListasCircular
from Mantenimiento import Mantenimiento
from ListaEnlasadasS import ListaEnlazada


ListaCarros = ListasCircular()
mantenimientoC = ListaEnlazada()

while True:
    os.system("cls")
    print("\n===== SISTEMA DE GESTIÓN DE VEHÍCULOS =====")
    print("1. Agregar vehículo")
    print("2. Listar todos los vehículos")
    print("3. Buscar un vehículo por placa")
    print("4. Eliminar un vehículo por placa")
    print("5. Ver historial de mantenimientos")
    print("6. Calcular costo total de mantenimientos")
    print("7. Salir")

    opcion = input("\nIngrese la opción deseada: ")

    if opcion == "1":
        placa = input("Placa: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        año = input("Año: ")
        kilometraje = input("Kilometraje: ")
        vehiculo = Vehiculo(placa, marca, modelo, año, kilometraje )
        fechaM = input("Fecha de mantenimiento (YYYY-MM-DD): ")
        descripcion = input("Descripción del mantenimiento: ")
        costo = input("Costo del mantenimiento: ")
        mantenimiento = Mantenimiento(fechaM, descripcion, costo) 
        mantenimientoC.insertar(mantenimiento)
        ListaCarros.insertar(vehiculo)
        print(f"Vehículo con placa {placa} agregado correctamente.")

    elif opcion == "2":
        ListaCarros.mostrar()

    elif opcion == "3":
        placa = input("Ingrese la placa del vehículo a buscar: ")
        vehiculo = ListaCarros.buscarPorPlaca(placa)
        if vehiculo:
            print("\n=== VEHÍCULO ENCONTRADO ===")
            print(vehiculo)
        else:
            print(f"No se encontró un vehículo con placa {placa}.")

    elif opcion == "4":
        if ListaCarros.Eliminar(): 
            print("Vehículo eliminado correctamente.")
        else:
            print("No se pudo eliminar el vehículo.")

    elif opcion == "5":
        ListaCarros.mostrarMantenimientos()

    elif opcion == "6":
        ListaCarros.calcularCostoTotalMantenimientos()

    elif opcion == "7":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")

    input("\nPresione Enter para continuar...")
