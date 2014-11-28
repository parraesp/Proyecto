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

    def alta_profesor(self,DNI,nombre,apellidos,movil,correo,salario,jornada):
        #verificar datos
        profesor = Profesor(DNI,nombre,apellidos,movil,correo,salario,jornada)
        self.__conexion.guardar_profesor(profesor)

    def editar_socio(self,DNI,nombre,apellidos,movil,correo):
        self.__conexion.cambiar_socio(DNI,nombre,apellidos,movil,correo)

    def editar_profesor(self,DNI,nombre,apellidos,movil,correo,sueldo, jornada):
        self.__conexion.cambiar_profesor(DNI,nombre,apellidos,movil,correo, sueldo, jornada)

    def obtener_socio(self,DNI):
        socio = self.__conexion.sacar_socio(DNI)
        return socio

    def obtener_profesor(self,DNI):
        profesor = self.__conexion.sacar_profesor(DNI)
        return profesor

    def dar_baja_socio(self, DNI):
        self.__conexion.dar_baja_socio(DNI)

    def dar_baja_profesor(self, DNI):
        self.__conexion.dar_baja_profesor(DNI)
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
