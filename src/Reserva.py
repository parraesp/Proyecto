__author__ = 'Ricardo'


class Reserva():
    """
    Clase para gestionar las reservas del club
    """
    def get_fecha(self):
        """
        Devuelve la fecha de la reserva

        :return: fecha
        """
        return self.__fecha

    def get_socio(self):
        """
        Devuleve el socio que realizo la reserva

        :return: socio
        """
        return self.__socio

    def get_instalacion(self):
        """
        Devuelve la instalacion de la reserva

        :return: instalacion
        """
        return self.__instalacion

    def __init__(self, socio, fecha, instalacion):
        """
        Constructor de la clase reserva

        :param socio: socio que reserva
        :param fecha: fecha de la reserva
        :param instalacion: instalacion de la reserva
        """
        self.__socio = socio
        self.__fecha = fecha
        self.__instalacion = instalacion

    def __str__(self):
        """
        Metodo to string

        :return: string de reserva
        """
        return 'Socio: ' + self.__socio.__str__() + ' Fecha: '+str(self.__fecha) + \
               ' Instalacion: '+self.__instalacion.__str__()
