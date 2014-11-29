__author__ = 'Ricardo'
class Reserva():

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self,fecha):
        self.__fecha = fecha

    def get_socio(self):
        return self.__socio

    def set_socio(self,socio):
        self.__socio = socio

    def get_instalacion(self):
        return self.__instalacion

    def set_instalacion(self,instalacion):
        self.__instalacion = instalacion

    fecha = property(get_fecha,set_fecha)
    instalacion = property(get_instalacion,set_instalacion)
    socio = property(get_socio,set_socio)

    def __init__(self,socio, fecha, instalacion):
        self.__socio = socio
        self.__fecha = fecha
        self.__instalacion = instalacion


