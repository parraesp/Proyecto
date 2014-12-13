from src.Instalacion import Instalacion
import os
import csv
__author__ = 'alberto'


class conexion_instalacion():
    def __init__(self):
        self.__instalaciones = self.__listar_instalaciones()

    def sacar_instalacion(self, instalacionID):
        valor = -1
        cont = 0
        encontrado = False
        while(cont < len(self.__instalaciones) and not(encontrado)):
            if self.__instalaciones[cont].get_instalacion_id() == instalacionID:
                encontrado = True
                valor = self.__instalaciones[cont]
            else:
                cont = cont+1
        return valor

    def __listar_instalaciones(self):
        instalaciones = []
        with open(os.path.dirname(__file__)+'/files/instalaciones.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                instalacion = Instalacion(row[0], row[1], row[2])
                instalaciones.append(instalacion)
        f.close()
        return instalaciones