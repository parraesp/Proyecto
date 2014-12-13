__author__ = 'Ricardo'


class Torneo():
    def __init__(self, nombre, socios):
        self.__nombre = nombre
        self.__socios = socios
        self.__resultados = {'p1': '', 'p2': '', 'p3': '', 'p4': '', 'p5': '', 'p6': '', 'p7': ''}

    def get_nombre(self):
        return self.__nombre

    def get_socios(self):
        return self.__socios

    def get_resultados(self):
        return self.__resultados

    def set_resultado(self, partido, dni):
        self.__resultados[partido] = dni
