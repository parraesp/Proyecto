from src.Clase import Clase
import os
__author__ = 'alberto'
import csv
import shutil
from tempfile import NamedTemporaryFile
from datetime import datetime


class ConexionClase():
    """
    Modelo para la clase Clase
    """
    def __init__(self, profesores, reservas):
        """
        Constructor del modelo

        :param profesores: modelo de profesores
        :param reservas: modelo de reserva
        """
        self.__profesores = profesores
        self.__reservas = reservas
        self.__clases = self.__listar_clases()

    def sacar_clase(self, profesor, socio, fecha):
        """
        Obtiene la clase del modelo

        :param profesor: dni del profesor
        :param socio: dni del socio
        :param fecha: fecha de la clase
        :return: clase
        """
        valor = -1
        cont = 0
        encontrado = False
        while cont < len(self.__clases) and not encontrado:
            if(self.__clases[cont].get_profesor().dni == profesor
               and self.__clases[cont].get_reserva().get_fecha() == fecha
               and self.__clases[cont].get_reserva().get_socio().get_dni() == socio):
                encontrado = True
                valor = self.__clases[cont]
            else:
                cont += 1
        return valor

    def guardar_clase(self, clase):
        """
        Guarda una clase de forma absoluta.

        :param clase: clase a guardar
        """
        f = open(os.path.dirname(__file__)+'/files/clases.csv', 'a+')
        texto = ''
        texto += clase.get_profesor().get_dni()+'\t'
        texto += clase.get_reserva().get_socio().get_dni()+"\t"
        texto += str(clase.get_reserva().get_fecha().strftime("%d/%m/%y %H:%M"))+'\n'
        f.write(texto)
        f.close()
        self.__clases.append(clase)

    @staticmethod
    def borrar_clase(profesor, fecha):
        """
        Borra una clase del fichero

        :param profesor: dni del profesor
        :param fecha: fehca de la clase
        """
        tempfile = NamedTemporaryFile(delete=False)

        with open(os.path.dirname(__file__)+'/files/clases.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if row[0] != profesor and row[2] != str(fecha):
                    writer.writerow(row)
        shutil.move(tempfile.name, os.path.dirname(__file__)+'/files/clases.csv')
        csvFile.close()
        tempfile.close()

    def __listar_clases(self):
        """
        Obtiene un lista de todas las clases existentes en el fichero

        :return: lista de clases
        :rtype: list
        """
        clases = []
        with open(os.path.dirname(__file__)+'/files/clases.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                fecha = datetime.strptime(row[2], "%d/%m/%y %H:%M")
                clase = Clase(self.__profesores.sacar_profesor(row[0]), self.__reservas.sacar_reserva(row[1], fecha))
                clases.append(clase)
        f.close()
        return clases
