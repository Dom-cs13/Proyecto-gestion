from datetime import datetime

class Mantenimiento:
    def __init__(self, fechaM, descripcion, costo):
        self.fechaM = fechaM
        self.descripcion = descripcion
        self.costo = float(costo) 
    
    @property
    def descripcion(self):
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion
    
    @property
    def costo(self):
        return self._costo
    
    @costo.setter
    def costo(self, costo):
        if float(costo) < 0:
            print("Costo no válido")
            self._costo = 0
            return
        self._costo = float(costo)
    
    @property
    def fechaM(self):
        return self._fechaM
    
    @fechaM.setter
    def fechaM(self, fechaM):
        try:
            datetime.strptime(fechaM, "%Y-%m-%d")  
            self._fechaM = fechaM
        except ValueError:
            print("Formato de fecha incorrecto, debe ser YYYY-MM-DD")
            self._fechaM = fechaM
    
    def __str__(self):
        return f"Fecha: {self.fechaM}, Descripción: {self.descripcion}, Costo: {self.costo}"