class Control:
    def __init__(self,tv):
        self._tv=tv

#encendido y apagado control
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()

#Canales control
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()

#volumen control
    def volumenUp(self):
        self._tv.volumenUp
    def volumenDown(self):
        self._tv.volumenDown()

#set Canal
    def setCanal(self):
        self._tv.setCanal()

#set Volumen
    def setVolumen(self):
        self._tv.setVolumen()  
    
    def enlazar(self, tv):
        self._tv=tv
        self._tv.setControl(self)

#get y set tv
    def setTv(self, tv):
        self._tv=tv
    def get(self):
        return self._tv