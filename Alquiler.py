__author__ = 'Ricardo'

class Alquiler():
    def isDevuelto(self):
        return self.__devuelto

    def get_reserva(self):
        return self.__reserva

    def get_instalaciones(self):
        return self.__instalaciones

    def aniadirInstalacion(self,instalacion):
        self.__instalaciones.append(instalacion)

    def set_devuelto(self,devuelto):
        self.__devuelto = devuelto

    reserva = property(get_reserva)
    instalaciones = property(get_instalaciones)
    devuelto = property(isDevuelto,set_devuelto)

    def __init__(self,reserva):
        self.__reserva = reserva
        self.__instalaciones = []
        self.__devuelto = False

    def __str__(self):
        texto = self.__reserva.fecha+','
        for i in self.__instalaciones:
            texto += i.id +','
        texto +=str(self.devuelto)
        return texto