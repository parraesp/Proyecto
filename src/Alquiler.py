__author__ = 'Ricardo'


class Alquiler():
    """
    Clase para gestionar los alquileres de los socios
    """
    def is_devuelto(self):
        """
        Devuelve si el alquiler esta devuelto

        :return: devuelto
        :rtype: bool
        """
        return self.__devuelto

    def get_reserva(self):
        """
        Devuleva la reserva relacionada con el alquiler

        :return: reserva
        """
        return self.__reserva

    def get_instalaciones(self):
        """
        Devuelve el conjunto de instalaciones alquiladas

        :return: instalaciones
        :rtype: list
        """
        return self.__instalaciones

    def aniadir_instalacion(self, instalacion):
        """
        Aniade una instalacion a la lista de instalaciones

        :param instalacion: tipo instalacion
        """
        self.__instalaciones.append(instalacion)

    def set_devuelto(self, devuelto):
        """
        Establece si se ha devuelto el alquiler

        :param devuelto: bool
        """
        self.__devuelto = devuelto

    def __init__(self, reserva):
        """
        Constructor de la clase alquiler

        :param reserva: tipo reserva
        """
        self.__reserva = reserva
        self.__instalaciones = []
        self.__devuelto = False

    def __str__(self):
        """
        Metodo to string.
        """
        texto = self.__reserva.__str__()+','
        for i in self.__instalaciones:
            texto += str(i.__str__())
        texto += str(self.__devuelto)
        return texto
