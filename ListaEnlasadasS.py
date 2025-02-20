class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.actual = None
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.actual = self.cabeza
        else:
            tmp = self.cabeza
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
    
    def mostrar(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return
        tmp = self.cabeza
        print("\n=== LISTADO DE MANTENIMIENTOS ===")
        i = 1
        while tmp is not None:
            print(f"\nMantenimiento {i}:")
            print(tmp.dato)
            tmp = tmp.siguiente
            i += 1
        print("\n")