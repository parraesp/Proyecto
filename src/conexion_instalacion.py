from src.Instalacion import Instalacion
import os
import csv
__author__ = 'alberto'


class ConexionInstalacion():
    """
    Modelo de la clase instalacion
    """
    def __init__(self):
        """
        Constructor de la clase
        """
        self.__instalaciones = self.__listar_instalaciones()

    def sacar_instalacion(self, instalacion_id):
        """
        Obtiene una instalacion

        :param instalacion_id: id de la instalacion
        :return: instalacion
        """
        valor = -1
        cont = 0
        encontrado = False
        while cont < len(self.__instalaciones) and not encontrado:
            if self.__instalaciones[cont].get_instalacion_id() == instalacion_id:
                encontrado = True
                valor = self.__instalaciones[cont]
            else:
                cont += 1
        return valor

    @staticmethod
    def __listar_instalaciones():
        """
        Obtiene todas las instalaciones desde el fichero

        :return: lista instalaciones
        :rtype: list
        """
        instalaciones = []
        with open(os.path.dirname(__file__)+'/files/instalaciones.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                instalacion = Instalacion(row[0], row[1], row[2])
                instalaciones.append(instalacion)
        f.close()
        return instalaciones
