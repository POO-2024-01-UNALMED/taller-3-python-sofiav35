class Marca:
    def __init__(self, nombre):
        self._nombre=nombre

  #Métodos get y set de Marca.      
    def getNombre(self):
        return self._nombre
    def setNombre(self, nuevoNombre):
        self._nombre=nuevoNombre