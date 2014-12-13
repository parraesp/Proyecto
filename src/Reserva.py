__author__ = 'Ricardo'


class Reserva():

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def get_socio(self):
        return self.__socio

    def set_socio(self, socio):
        self.__socio = socio

    def get_instalacion(self):
        return self.__instalacion

    def set_instalacion(self, instalacion):
        self.__instalacion = instalacion

    def __init__(self, socio, fecha, instalacion):
        self.__socio = socio
        self.__fecha = fecha
        self.__instalacion = instalacion

    def __str__(self):
        return 'Socio: ' + self.__socio.__str__() + ' Fecha: '+str(self.__fecha) + \
               ' Instalacion: '+self.__instalacion.__str__()