class Control:
    def __init__(self):
        self._tv=0

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
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()

#set Canal
    def setCanal(self, canal):
        self._tv.setCanal(canal)

#set Volumen
    def setVolumen(self, volumen):
        self._tv.setVolumen(volumen)  
    
    def enlazar(self, tv):
        self._tv=tv
        self._tv.setControl(self)

#get y set tv
    def setTv(self, tv):
        self._tv=tv
    def getTv(self):
        return self._tv