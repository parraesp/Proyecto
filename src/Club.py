from src.Conexion import Conexion
from src.Socio import Socio
from src.Reserva import Reserva
from src.Torneo import Torneo
from src.Alquiler import Alquiler
from src.Profesor import Profesor
from src.Clase import Clase
__author__ = 'Ricardo'
from datetime import *
import re


class Club():
    """
    Controlador de la aplicacion
    """
    def __init__(self):
        """
        Constructor de la clase club
        """
        self.__conexion = Conexion()

    def alta_socio(self, dni, nombre, apellidos, movil, correo):
        """
        Da de alta a un socio en el club

        :param dni: dni del socio
        :param nombre: nombre del socio
        :param apellidos: apellidos del socio
        :param movil: numero de contacto del socio
        :param correo: correo del socio
        """
        socio = Socio(dni, nombre, apellidos, movil, correo)
        if self.obtener_socio(dni) == -1:
            self.__conexion.guardar_socio(socio)

    def alta_profesor(self, dni, nombre, apellidos, movil, correo, salario, jornada):
        """
        Da de alta a un profesor en el club

        :param dni: dni del profesor
        :param nombre: nombre del profesor
        :param apellidos: apellidos del profesor
        :param movil: numero de contacto del profesor
        :param correo: correo del profesor
        :param salario: salario del profesor
        :param jornada: tipo de jornada del profesor
        """
        profesor = Profesor(dni, nombre, apellidos, movil, correo, salario, jornada)
        if self.obtener_profesor(dni) == -1:
            self.__conexion.guardar_profesor(profesor)

    def editar_socio(self, dni, nombre, apellidos, movil, correo):
        """
        Edita los datos de un socio

        :param dni: dni del socio
        :param nombre: nombre del socio
        :param apellidos: apellidos del socio
        :param movil: numero de contacto del socio
        :param correo: correo del socio
        """
        self.__conexion.cambiar_socio(dni, nombre, apellidos, movil, correo)

    def editar_profesor(self, dni, nombre, apellidos, movil, correo, sueldo, jornada):
        """
        Da de alta a un profesor en el club

        :param dni: dni del profesor
        :param nombre: nombre del profesor
        :param apellidos: apellidos del profesor
        :param movil: numero de contacto del profesor
        :param correo: correo del profesor
        :param salario: salario del profesor
        :param jornada: tipo de jornada del profesor
        """
        self.__conexion.cambiar_profesor(dni, nombre, apellidos, movil, correo, sueldo, jornada)

    def obtener_socio(self, dni):
        """
        Devuelve un socio del club

        :param dni: dni del socio
        :return: socio
        """
        socio = self.__conexion.sacar_socio(dni)
        return socio

    def obtener_profesor(self, dni):
        """
        Devuelve a un profesor del club

        :param dni: dni del profesor
        :return: profesor
        """
        profesor = self.__conexion.sacar_profesor(dni)
        return profesor

    def dar_baja_socio(self, dni):
        """
        Da de baja a un socio del club

        :param dni: dni del socio
        :return: socio dado de baja
        """
        socio = self.__conexion.sacar_socio(dni)
        if socio != -1:
            self.__conexion.dar_baja_socio(socio)
        return socio

    def dar_baja_profesor(self, dni):
        """
        Da de baja a un profesor del club

        :param dni: dni del profesor
        """
        if self.obtener_profesor(dni) != -1:
            self.__conexion.dar_baja_profesor(dni)

    def crear_reserva(self, dni, fecha, instalacion_id):
        """
        Crea una reserva para un socio

        :param dni: dni del socio que reserva
        :param fecha: fecha de la reserva
        :param instalacion_id: instlacion que se quiere reservar
        :return: reserva realizada
        """
        socio = self.__conexion.sacar_socio(dni)
        fecha = datetime.strptime(fecha, "%d/%m/%y %H")
        reserva = -1
        if socio != -1 and self.__conexion.verificar_reserva(fecha, instalacion_id):
            instalacion = self.__conexion.sacar_instalacion(instalacion_id)
            reserva = Reserva(socio, fecha, instalacion)
            self.__conexion.guardar_reserva(reserva)
        return reserva

    def consultar_reserva(self, dni, fecha):
        """
        Devuelve los datos de una reserva existente

        :param dni: dni del socio que reservo
        :param fecha: fecha de la reserva
        :return: reserva
        """
        fecha = datetime.strptime(fecha, "%d/%m/%y %H")
        reserva = self.__conexion.sacar_reserva(dni, fecha)
        return reserva

    def cancelar_reserva(self, dni, fecha):
        """
        Cancela una reserva ya creada en el club

        :param dni: dni del socio que realizo la reserva
        :param fecha: fecha de la reserva
        :return: reserva cancelada
        """
        reserva = self.consultar_reserva(dni, fecha)
        fecha = datetime.strptime(fecha, "%d/%m/%y %H")
        if self.consultar_alquiler(reserva) != -1:
            self.devolver_alquiler(reserva)
        self.__conexion.borrar_reserva(dni, fecha)
        return reserva

    def crear_torneo(self, nombre, socios, fecha):
        """
        Crea un torneo nuevo en el club.

        :param nombre: nombre del torneo
        :param socios: socios participantes en el torneo
        :param fecha: fecha de inicio del torneo
        :return: torneo creado
        """
        fecha_aux = datetime.strptime(fecha, "%d/%m/%y %H")
        self.crear_reserva(socios[0].dni, fecha_aux.strftime("%d/%m/%y %H"), 'inst02')
        i = 0
        while i < 7:
            fecha_aux += timedelta(days=1)
            if self.__conexion.verificar_reserva(fecha_aux, 'inst02'):
                self.crear_reserva(socios[0].dni, fecha_aux.strftime("%d/%m/%y %H"), 'inst02')
                i += 1
        torneo = Torneo(nombre, socios)
        self.__conexion.guardar_torneo(torneo)

    def consultar_torneo(self, nombre):
        """
        Devuelve los datos de un torneo ya creado

        :param nombre: nombre del torneo
        :return:torneo
        """
        return self.__conexion.sacar_torneo(nombre)

    def introducir_resultado(self, nombre, partido, resultado):
        """
        Introduce los datos en un partido de un torneo

        :param nombre: nombre del torneo
        :param partido: partido del torneo
        :param resultado: resultado del partido
        """
        torneo = self.__conexion.sacar_torneo(nombre)
        self.__conexion.poner_resultado(torneo, partido, resultado)

    def borrar_torneo(self, nombre):
        """
        Borra un torneo existente en el club

        :param nombre: nombre del torneo
        :return: torneo borrado
        """
        torneo = self.__conexion.sacar_torneo(nombre)
        self.__conexion.borrar_torneo(torneo)
        return torneo

    def cancelar_clase(self, profesor, socio, fecha):
        """
        Cancela una clase ya creada en el club

        :param profesor: dni del profesor
        :param socio: dni dle socio
        :param fecha: fecha de la clase
        :return: clase cancelada
        """
        self.cancelar_reserva(socio, fecha)
        fecha = datetime.strptime(fecha, "%d/%m/%y %H")
        return self.__conexion.borrar_clase(profesor, fecha)

    def obtener_clase(self, profesor, socio, fecha):
        """
        Devuelve los datos de una clase del club

        :param profesor: dni del profesor
        :param socio: dni del socio
        :param fecha: fecha de la clase
        :return: clase
        """
        fecha = datetime.strptime(fecha, "%d/%m/%y %H")
        clase = self.__conexion.sacar_clase(profesor, socio, fecha)
        return clase

    def registrar_clase(self, profesor, reserva):
        """
        Registra una clase en el club

        :param profesor: dni del profesor
        :param reserva: reserva asociada a la clase
        """
        clase = Clase(profesor, reserva)
        self.__conexion.guardar_clase(clase)

    def crear_alquiler(self, reserva, ids):
        """
        Crea un alquiler para una reserva

        :param reserva: reserva asociada
        :param ids: conjunto de instalaciones a alquilar
        """
        alquiler = Alquiler(reserva)
        for id_ind in ids:
            instalacion = self.__conexion.sacar_instalacion(id_ind)
            if instalacion != -1:
                alquiler.aniadir_instalacion(instalacion)
        self.__conexion.guardar_alquiler(alquiler)

    def devolver_alquiler(self, reserva):
        """
        Devuelve un alquiler

        :param reserva: reserva asociada al alquiler
        """
        self.__conexion.devolver_alquiler(reserva)

    def consultar_alquiler(self, reserva):
        """
        Devuelve los datos de un alquiler

        :param reserva: reserva asociada
        :return: alquiler
        """
        return self.__conexion.sacar_alquiler(reserva)

    @staticmethod
    def validar_dni(dni):
        """
        Metodo que valida un dni. Solo validad que tenga 8 digitos y una letra

        :param dni: dni a validar
        :return: valido o no
        :rtype: bool
        """
        error = True
        dni = dni.upper()
        if len(dni) == 9:
            letra = dni[8]
            num = dni[:8]
            if 'A' <= letra <= 'Z':
                for n in num:
                    if not str(n).isdigit():
                        error = False
            else:
                error = False
        else:
            error = False
        return error

    @staticmethod
    def validar_email(email):
        """
        Metodo que valida un email

        :param email: email a validar
        :return: valido o no
        :rtype: bool
        """
        if re.match('^[(a-z0-9_\-\.)]+@[(a-z0-9_\-\.)]+\.[(a-z)]{2,4}$', email.lower()):
            result = True
        else:
            result = False
        return result

    @staticmethod
    def validar_telefono(telefono):
        """
        Valida un telefono

        :param telefono: telefono a validar
        :return: valido o no
        :rtype: bool
        """
        if len(telefono) == 9 and telefono.isdigit():
            result = True
        else:
            result = False
        return result

    def validar_instalacion(self, instalacion_id):
        """
        Valida una instalacion existente en el club

        :param instalacion_id: id de la instalacion a validar
        :return: valido o no
        :rtype: bool
        """
        valida = True
        if self.__conexion.sacar_instalacion(instalacion_id) == -1:
            valida = False
        return valida

    @staticmethod
    def validar_fecha(fecha):
        """
        Valida el formato de una fecha

        :param fecha: fecha a validar
        :return: valido o no
        :rtype: bool
        """
        result = False
        try:
            if datetime.strptime(fecha, '%d/%m/%y %H'):
                result = True
        except ValueError:
            pass
        return result
