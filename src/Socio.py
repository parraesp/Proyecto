__author__ = 'francisco'
import time


class Socio():
    """
    Clase encargada de gestionar los socios del club
    """
    def __init__(self, dni, nombre, apellidos, movil, correo, *otros):
        """
        Constructor de la clase socio.

        :param: dni
        :param: nombre
        :param: apellidos
        :param: movil
        :param: correo
        :param: parametros a usar en caso de querer cargar un objeto de la persistencia en lugar de crear uno nuevo
        """
        self.__dni = str(dni)
        self.__nombre = str(nombre)
        self.__apellidos = str(apellidos)
        self.__movil = str(movil)
        self.__correo = str(correo)
        if len(otros) == 2:
            self.__fecha_alta = otros[0]
            self.__estado = bool(otros[1])
        else:
            self.__fecha_alta = str(time.strftime("%d/%m/%y"))
            self.__estado = True

    def __str__(self):
        """
        Devuelve los datos de un socio en forma de cadena

        :return: Socio
        """
        return 'dni: ' + self.__dni+' nombre: ' + self.__nombre + ' apellidos: ' + self.__apellidos \
               + ', fecha de alta: ' + self.__fecha_alta + ', estado: ' + str(self.__estado)\
               + ', correo: ' + str(self.correo) + ' movil: ' + self.__movil

    def get_dni(self):
        """
        Devuelve el dni de un socio

        :return: dni
        """
        return self.__dni

    def get_nombre(self):
        """
        Devuelve el nombre de un socio

        :return: nombre
        """
        return self.__nombre

    def get_apellidos(self):
        """
        Devuelve los apellidos de un socio

        :return: apellidos
        """
        return self.__apellidos

    def get_movil(self):
        """
        Devuelve el movil de un socio

        :return: movil
        """
        return self.__movil

    def get_correo(self):
        """
        Devuelve el correo electronico de un socio

        :return: correo
        """
        return self.__correo

    def get_fecha_alta(self):
        """
        Devuelve la fecha de alta de un socio

        :return: fecha_alta
        """
        return self.__fecha_alta

    def get_estado(self):
        """
        Devuelve el estado de un socio

        :return: estado
        """
        return self.__estado

    def cambiar_estado(self):
        """
        Asigna el estado del usuario a "dado de baja"
        """
        self.__estado = False

    def set_fecha_alta(self, fecha):
        """
        Asigna una nueva fecha de alta

        :param: fecha de alta
        """
        self.__fecha_alta = fecha

    def set_nombre(self, nombre):
        """
        Asigna un nuevo nombre a un socio

        :param: nombre
        """
        self.__nombre = nombre

    def set_apellidos(self, apellidos):
        """
        Asigna nuevo(s) apellido(s) al socio
        :param: apellido(s)
        """
        self.__apellidos = apellidos

    def set_correo(self, correo):
        """
        Asigna un nuevo correo electronico

        :param: correo electronico
        """
        self.__correo = correo

    def set_movil(self, movil):
        """
        Asigna un nuevo movil

        :param: movil
        """
        self.__movil = movil

    dni = property(get_dni)
    nombre = property(get_nombre)
    apellidos = property(get_apellidos)
    movil = property(get_movil)
    correo = property(get_correo)
    fecha_alta = property(get_fecha_alta, set_fecha_alta)
    estado = property(get_estado)
