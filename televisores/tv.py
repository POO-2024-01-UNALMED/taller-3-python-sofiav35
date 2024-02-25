class TV:
    _numTV=0
    def __init__(self, marca, estado):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._volumen=1
        self._precio=500
        self._control=0
        TV._numTV+=1
#metodos get y set numero de televisores
    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV=numTV
    def getNumTV():
        return TV._numTV

 #metodos get y set de marca.          
    def getMarca(self):
        return self._marca
    def setMarca(self, marca):
        self._marca=marca

#metodos get y set de canal.
    def getCanal(self):
        return self.canal
    def setCanal(self, canal):
        if (canal<=120) and (canal>=1) and (self._estado==True):
            self._canal=canal

#metodos get y set de precio. 
    def getPrecio(self):
        return self._precio
    def setPrecio(self, precio):
        self.precio=precio

#metodos get y set de volumen. 
    def getVolumen(self):
        return self._volumen
    def setVolumen(self, volumen):
        if(volumen>=0)and(volumen<=7)and(self._estado==True):
            self._volumen=volumen

#metodos get y set de control
    def getControl(self):
        return self._control
    def setControl(self, control):
        self._control=control

#Encendido y apagado
    def turnOn(self, estado):
       self._estado=False
    def turnOff(self, estado):
        self._estado=True

#metodos get y set del estado
    def getEstado(self):
        return self._estado
    def setEstado(self, estado):
        self._estado=estado

#Cambio de canal
    def canalUp(self,canal):
        if(canal<120)and(self._estado==True):
            self._canal+=1
    def canalDown(self, canal):
        if (canal>1)and(self._estado==True):
            self._canal-=1

#Cambio de volumen
    def volumenUp(self, volumen):
        if(volumen<7)and(self._estado==True):
            self._volumen+=1
    def volumenDown(self, volumen):
        if (volumen>0)and(self._estado==True):
            self._volumen-=1
      