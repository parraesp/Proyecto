__author__ = 'Ricardo'


class Torneo():
    """
    Clase para gestinar los torneos del club
    """
    def __init__(self, nombre, socios):
        """
        Constructor de la clase

        :param nombre: nombre del torneo
        :param socios: socios que participan
        """
        self.__nombre = nombre
        self.__socios = socios
        self.__resultados = {'p1': '', 'p2': '', 'p3': '', 'p4': '', 'p5': '', 'p6': '', 'p7': ''}

    def get_nombre(self):
        """
        Devuelve el nombre del torneo

        :return: nombre del torneo
        """
        return self.__nombre

    def get_socios(self):
        """
        Devuelve la lista de socios que participan en el torneo

        :return: lista de socios
        """
        return self.__socios

    def get_resultados(self):
        """
        Devuelve los resultados del torneo

        :return: resultados
        """
        return self.__resultados

    def set_resultado(self, partido, dni):
        """
        Establece un resultado en un partido

        :param partido: partido
        :param dni: dni del ganador
        """
        self.__resultados[partido] = dni

    def __str__(self):
        texto = 'Nombre: ' + self.get_nombre() + ', Resultados: '
        for r in self.__resultados:
            texto += r + ' : ' + self.__resultados[r] + ', '
        return texto
