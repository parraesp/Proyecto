__author__ = 'Ricardo'


class Instalacion():
    """
    Clase para gestionar las instalaciones del club.
    """
    def get_descripcion(self):
        """
        Devuelve la descripcion de la instalacion

        :return: descripcion
        """
        return self.__descripcion

    def get_instalacion_id(self):
        """
        Devuelve el id de la instalcion

        :return: id
        """
        return self.__instalacion_id

    def __init__(self, instalacion_id, descripcion, precio):
        """
        Constructor de la clase

        :param instalacion_id: id de la instalacion
        :param descripcion: descripcion de la instalacion
        :param precio: precio de la instalacion
        """
        self.__instalacion_id = instalacion_id
        self.__precio = precio
        self.__descripcion = descripcion

    def __str__(self):
        """
        Metodo to string

        :return: string de instalacion
        """
        return self.get_instalacion_id() + ','+self.get_descripcion()
