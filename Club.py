__author__ = 'Ricardo'
from Conexion import *
from Socio import Socio
from Reserva import Reserva
from Conexion import Conexion

class Club():
    def __init__(self):
        self.__conexion = Conexion()

    def alta_socio(self,DNI,nombre,apellidos,movil,correo):
        #verificar datos
        socio = Socio(DNI,nombre,apellidos,movil,correo)
        guardar_socio(socio)

    def eliminar_socio(self,DNI):
        socio = self.obtener_socio(DNI)
        return socio

    def obtener_socio(self,DNI):
        socio = sacar_socio(DNI)
        return socio

    def crear_reserva(self,DNI,fecha,instalacion):
        #verificar datos
        socio = sacar_socio(DNI)
        reserva = Reserva(socio,fecha,instalacion)
        guardar_reserva(reserva)
