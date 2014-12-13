from src.conexion_reserva import ConexionReserva
from src.conexion_profesor import ConexionProfesor
from src.conexion_alquiler import ConexionAlquiler
from src.conexion_clase import ConexionClase
from src.conexion_instalacion import ConexionInstalacion
from src.conexion_socio import ConexionSocio
from src.conexion_torneo import ConexionTorneo

__author__ = 'alberto'


class Conexion():
    """
    Modelo de la aplicacion, tiene el resto de conexiones necesarias para guardar los datos.
    Se encarga solo de conectarse con los modelos especificos.
    """
    def __init__(self):
        """
        Constructor de la clase conexion
        """
        self.__conexion_socio = ConexionSocio()
        self.__conexion_profesor = ConexionProfesor()
        self.__conexion_instalacion = ConexionInstalacion()
        self.__conexion_reserva = ConexionReserva(self.__conexion_socio, self.__conexion_instalacion)
        self.__conexion_alquiler = ConexionAlquiler(self.__conexion_reserva, self.__conexion_instalacion)
        self.__conexion_clase = ConexionClase(self.__conexion_profesor, self.__conexion_reserva)

        self.__conexion_torneo = ConexionTorneo(self.__conexion_socio)

    def guardar_socio(self, socio):
        """
        Guarda un socio
        :param socio: socio a guardar
        """
        self.__conexion_socio.guardar_socio(socio)

    def guardar_profesor(self, profesor):
        """
        Guarda un profesor en el club
        :param profesor: profesor a guardar
        """
        self.__conexion_profesor.guardar_profesor(profesor)

    def sacar_socio(self, dni):
        """
        Obtiene un socio del club

        :param dni: dni del socio
        :return: socio
        """
        return self.__conexion_socio.sacar_socio(dni)

    def sacar_profesor(self, dni):
        """
        Obtiene un profesor del club

        :param dni: dni del profesor
        :return: profesor
        """
        return self.__conexion_profesor.sacar_profesor(dni)

    def dar_baja_socio(self, socio):
        """
        Da de baja a un socio

        :param socio: socio
        """
        self.__conexion_socio.dar_baja_socio(socio)

    def dar_baja_profesor(self, dni):
        """
        Da de baja a un profesor en el club

        :param dni: dni del profesor
        """
        self.__conexion_profesor.dar_baja_profesor(dni)

    def sacar_instalacion(self, instalacion_id):
        """
        Obtiene una instalacion del club

        :param instalacion_id: id de la instalacion
        :return: instalacion
        """
        return self.__conexion_instalacion.sacar_instalacion(instalacion_id)

    def sacar_clase(self, profesor, dni, fecha):
        """
        Obtiene un clase del club

        :param profesor: dni del profesor
        :param dni: dni del socio
        :param fecha: fecha de la clase
        :return: clase
        """
        return self.__conexion_clase.sacar_clase(profesor, dni, fecha)

    def guardar_reserva(self, reserva):
        """
        Guarda una reserva en el club

        :param reserva: reserva a guardar
        """
        self.__conexion_reserva.guardar_reserva(reserva)

    def guardar_clase(self, clase):
        """
        Guarda una clase en el club

        :param clase: clase a guardar
        """
        self.__conexion_clase.guardar_clase(clase)

    def sacar_reserva(self, dni, fecha):
        """
        Obtiene una reserva del club

        :param dni: dni del socio que reservo
        :param fecha: fecha de la reserva
        :return: reserva
        """
        return self.__conexion_reserva.sacar_reserva(dni, fecha)

    def verificar_reserva(self, fecha, instalacion_id):
        """
        Verifica si una reserva existe ya para una fecha e instalacion dada

        :param fecha: fecha de la reserva
        :param instalacion_id: id de la isntalacion
        :return: reserve valida
        :rtype: bool
        """
        return self.__conexion_reserva.verificar_reserva(fecha, instalacion_id)

    def borrar_reserva(self, dni, fecha):
        """
        Borra una reserva del club

        :param dni: dni del socio
        :param fecha: fecha de la reserva
        :return: reserva borrada
        """
        return self.__conexion_reserva.borrar_reserva(dni, fecha)

    def guardar_alquiler(self, alquiler):
        """
        Guarda un alquiler en el club

        :param alquiler: alquiler a guardar
        """
        self.__conexion_alquiler.guardar_alquiler(alquiler)

    def sacar_alquiler(self, reserva):
        """
        Obtiene los datos de un alquiler

        :param reserva: reserva asociada
        :return: alquiler
        """
        return self.__conexion_alquiler.sacar_alquiler(reserva)

    def devolver_alquiler(self, reserva):
        """
        Devuelve un alquiler

        :param reserva: reserva asociada
        :return: alquiler devuelto
        """
        return self.__conexion_alquiler.devolver_alquiler(reserva)

    def borrar_clase(self, profesor, fecha):
        """
        Elimina una clase del club

        :param profesor: dni del profesor
        :param fecha: fecha de la clase
        """
        self.__conexion_clase.borrar_clase(profesor, fecha)

    def cambiar_socio(self, dni, nombre, apellidos, movil, correo):
        """
        Edita los datos de un socio

        :param dni: dni del socio
        :param nombre: nuevo nombre
        :param apellidos: nuevos apellidos
        :param movil: nuevo telefono
        :param correo: nuevo correo
        """
        self.__conexion_socio.cambiar_socio(dni, nombre, apellidos, movil, correo)

    def cambiar_profesor(self, dni, nombre, apellidos, movil, correo, sueldo, jornada):
        """
        Edita los datos de un profesor

        :param dni: dni del socio
        :param nombre: nuevo nombre
        :param apellidos: nuevos apellidos
        :param movil: nuevo telefono
        :param correo: nuevo correo
        :param sueldo: nuevo sueldo
        :param joranda: nueva jornada
        """
        self.__conexion_profesor.cambiar_profesor(dni, nombre, apellidos, movil, correo, sueldo, jornada)

    def guardar_torneo(self, torneo):
        """
        Guarda un torneo en el club

        :param torneo: torneo a guardar
        """
        self.__conexion_torneo.guardar_torneo(torneo)

    def sacar_torneo(self, nombre):
        """
        Obtiene los datos de un torneo existente

        :param nombre: nombre del torneo
        :return: torneo
        """
        return self.__conexion_torneo.sacar_torneo(nombre)

    def poner_resultado(self, torneo, partido, resultado):
        """
        Establece un resultado para un partido de un toreno

        :param torneo: nombre del torneo
        :param partido: partido el torneo
        :param resultado: resultado del torneo
        """
        self.__conexion_torneo.poner_resultado(torneo, partido, resultado)

    def borrar_torneo(self, torneo):
        """
        Elimina un torneo del club

        :param torneo: nombre del torneo
        """
        self.__conexion_torneo.borrar_torneo(torneo)
