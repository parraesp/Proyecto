__author__ = 'Ricardo'
from Conexion import *
from Socio import Socio
from Reserva import Reserva
from Conexion import Conexion
from datetime import *
from Clase import Clase
import re
from Alquiler import Alquiler

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
        socio = self.__conexion.sacar_socio(DNI)
        if (socio != -1):
            self.__conexion.dar_baja_socio(socio)
        return socio

    def dar_baja_profesor(self, DNI):
        self.__conexion.dar_baja_profesor(DNI)

    def crear_reserva(self,DNI,fecha,instalacionID):
        #verificar datos
        socio = self.__conexion.sacar_socio(DNI)
        instalacion = self.__conexion.sacar_instalacion(instalacionID)
        fecha = datetime.strptime(fecha, "%d/%m/%y %H")
        reserva = Reserva(socio,fecha,instalacion)
        self.__conexion.guardar_reserva(reserva)
        return reserva

    def consultar_reserva(self,fecha):
        fecha = datetime.strptime(fecha, "%d/%m/%y %H")
        reserva = self.__conexion.sacar_reserva(fecha)
        return reserva

    def cancelar_reserva(self,fecha):
        fecha = datetime.strptime(fecha, "%d/%m/%y %H")
        return self.__conexion.borrar_reserva(fecha)
    def cancelar_clase(self,profesor, fecha):
        #fecha = datetime.strptime(fecha, "%d/%m/%y %H")
        return self.__conexion.borrar_clase(profesor,fecha)

    def obtener_instalacion(self,id):
        instalacion = self.__conexion.sacar_instalacion(id)
        return instalacion

    def obtener_clase(self,profesor, fecha):
        clase = self.__conexion.sacar_clase(profesor,fecha)
        return clase

    def registrar_clase(self,profesor, reserva):
        clase = Clase(profesor,reserva)
        self.__conexion.guardar_clase(clase)

    def crear_alquiler(self,reserva,ids):
        alquiler = Alquiler(reserva)
        for id in ids:
            instalacion = self.__conexion.sacar_instalacion(id)
            if (instalacion != -1):
                alquiler.aniadirInstalacion(instalacion)
        self.__conexion.guardar_alquiler(alquiler)

    def devolver_alquiler(self,reserva):
        self.__conexion.devolver_alquiler(reserva)

    def consultar_alquiler(self,reserva):
        return self.__conexion.sacar_alquiler(reserva)

    def validarDNI(self,DNI):
        error = True
        DNI = DNI.upper()
        if len(DNI) == 9:
            letra = DNI[8]
            num = DNI[:8]
            if 'A' <= letra and 'Z' >= letra:
                for n in num:
                    if not str(n).isdigit():
                        error = False
            else:
               error = False
        else:
            error = False
        return error

    def validarEmail(self,email):
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',email.lower()):
	        result = True
        else:
	        result = False
        return result

    def validarTelefono(self,telefono):
        if len(telefono) == 9 and telefono.isdigit():
	        result = True
        else:
	        result = False
        return result

    def validarFecha(self,fecha):
        result = False
        try:
            if datetime.strptime(fecha,'%d/%m/%y %H'):
                result = True
        except:
            pass
        return result