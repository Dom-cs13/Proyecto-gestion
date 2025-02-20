import os
from Vehiculo import Vehiculo
from ListaEnlasadas import ListasCircular
from Mantenimiento import Mantenimiento

ListaCarros = ListasCircular()

while True:
    os.system("cls")
    print("\n===== SISTEMA DE GESTIÓN DE VEHÍCULOS =====")
    print("1. Agregar vehículo")
    print("2. Agregar mantenimiento")
    print("3. Listar todos los vehículos")
    print("4. Buscar un vehículo por placa")
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
        vehiculo = Vehiculo(placa, marca, modelo, año, kilometraje)
        ListaCarros.insertar(vehiculo)
        print(f"Vehículo con placa {placa} agregado correctamente.")

    elif opcion == "2":
        placa = input("Ingrese la placa del vehículo: ")
        vehiculo = ListaCarros.buscarPorPlaca(placa)
        if vehiculo:
            fechaM = input("Fecha de mantenimiento (YYYY-MM-DD): ")
            descripcion = input("Descripción del mantenimiento: ")
            costo = input("Costo del mantenimiento: ")
            try:
                mantenimiento = Mantenimiento(fechaM, descripcion, costo)
                vehiculo.agregar_mantenimiento(mantenimiento) 
                print("Mantenimiento agregado correctamente.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print(f"No se encontró un vehículo con placa {placa}.")

    elif opcion == "3":
        ListaCarros.mostrar()

    elif opcion == "4":
        placa = input("Ingrese la placa del vehículo a buscar: ")
        vehiculo = ListaCarros.buscarPorPlaca(placa)
        if vehiculo:
            print("\n=== VEHÍCULO ENCONTRADO ===")
            print(vehiculo)
        else:
            print(f"No se encontró un vehículo con placa {placa}.")

    elif opcion == "5":
        placa = input("Ingrese la placa del vehículo: ")
        vehiculo = ListaCarros.buscarPorPlaca(placa)
        if vehiculo:
            historial = vehiculo.consultar_historial()  
            if historial:
                for i, mant in enumerate(historial, 1):
                    print(f"\nMantenimiento {i}: {mant}")
            else:
                print("No hay mantenimientos registrados para este vehículo.")
        else:
            print(f"No se encontró un vehículo con placa {placa}")

    elif opcion == "6":
        placa = input("Ingrese la placa del vehículo: ")
        vehiculo = ListaCarros.buscarPorPlaca(placa)
        if vehiculo:
            costo_total = vehiculo.calcular_costo_total_mantenimientos()   
            print(f"\nCosto total de mantenimientos: ${costo_total:.2f}")
        else:
            print(f"No se encontró un vehículo con placa {placa}.")

    elif opcion == "7":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")

    input("\nPresione Enter para continuar...")