__author__ = 'Ricardo'
from Conexion import *
from Socio import Socio
from Reserva import Reserva
from Conexion import Conexion
from datetime import *

class Club():
    def __init__(self):
        self.__conexion = Conexion()

    def alta_socio(self,DNI,nombre,apellidos,movil,correo):
        #verificar datos
        socio = Socio(DNI,nombre,apellidos,movil,correo)
        self.__conexion.guardar_socio(socio)

    def editar_socio(self,DNI,nombre,apellidos,movil,correo):
        self.__conexion.cambiar_socio(DNI,nombre,apellidos,movil,correo)

    def obtener_socio(self,DNI):
        socio = self.__conexion.sacar_socio(DNI)
        return socio

    def dar_baja_socio(self, DNI):
        self.__conexion.dar_baja_socio(DNI)


    def crear_reserva(self,DNI,fecha,instalacionID):
        #verificar datos
        socio = self.__conexion.sacar_socio(DNI)
        instalacion = self.__conexion.sacar_instalacion(instalacionID)
        fecha = datetime.strptime(fecha, "%d/%m/%y %H:%M")
        reserva = Reserva(socio,fecha,instalacion)
        self.__conexion.guardar_reserva(reserva)

    def obtener_instalacion(self,id):
        instalacion = self.__conexion.sacar_instalacion(id)
        return instalacion
