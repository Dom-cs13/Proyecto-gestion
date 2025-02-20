class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            tmp = self.cabeza
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
    
    def recorrer(self):
        datos = []
        tmp = self.cabeza
        while tmp is not None:
            datos.append(tmp.dato)
            tmp = tmp.siguiente
        return datos
