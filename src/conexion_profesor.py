from src.Profesor import Profesor
import os

__author__ = 'alberto'
import csv
import shutil
from tempfile import NamedTemporaryFile


class ConexionProfesor():
    """
    Modelo de la clase profesor
    """
    def __init__(self):
        """
        Constructor de clase
        """
        self.__profesores = self.__listar_profesores()

    def guardar_profesor(self, profesor):
        """
        Guarda un profesor en el fichero

        :param profesor: profesor a guardar
        """
        f = open(os.path.dirname(__file__)+'/files/profesores.csv', 'a+')
        texto = ''
        texto += profesor.dni+'\t'
        texto += profesor.nombre+'\t'
        texto += profesor.apellidos+'\t'
        texto += profesor.movil+'\t'
        texto += profesor.correo+'\t'
        texto += profesor.fecha_alta+'\t'
        texto += str(profesor.estado)+'\t'
        texto += str(profesor.get_salario())+'\t'
        texto += profesor.get_jornada()+'\n'
        f.write(texto)
        f.close()
        self.__profesores.append(profesor)

    def sacar_profesor(self, dni):
        """
        Obtiene los datos de un profesor

        :param dni: dni del profesor
        :return: profesor
        """
        valor = -1
        cont = 0
        encontrado = False
        while cont < len(self.__profesores) and not encontrado:
            if self.__profesores[cont].dni == dni:
                encontrado = True
                valor = self.__profesores[cont]
            else:
                cont += 1
        return valor

    def dar_baja_profesor(self, dni):
        """
        Da de baja a un profesor y guarda los datos en el fichero

        :param dni: dni del profesor
        """
        cont = 0
        encontrado = False
        while cont < len(self.__profesores) and not encontrado:
            if self.__profesores[cont].dni == dni:
                encontrado = True
            else:
                cont += 1
        self.__profesores[cont].cambiar_estado()
        tempfile = NamedTemporaryFile(delete=False)

        with open(os.path.dirname(__file__)+'/files/profesores.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if row[0] == self.__profesores[cont].dni:
                    row[6] = False
                    writer.writerow(row)
                else:
                    writer.writerow(row)
        shutil.move(tempfile.name, os.path.dirname(__file__)+'/files/profesores.csv')
        csvFile.close()
        tempfile.close()

    def cambiar_profesor(self, dni, nombre, apellidos, movil, correo, sueldo, jornada):
        """
        Edita los datos de un profesor y lo guardar en un fichero

        :param dni: dni del profesor
        :param nombre: nuevo nombre
        :param apellidos: nuevo apellidos
        :param movil: nuevo telefono
        :param correo: nuevo correo
        :param sueldo: nuevo sueldo
        :param jornada: nueva joranda
        """
        cont = 0
        encontrado = False
        while cont < len(self.__profesores) and not encontrado:
            if self.__profesores[cont].dni == dni:
                encontrado = True
            else:
                cont += 1
        self.__profesores[cont].set_nombre(nombre)
        self.__profesores[cont].set_apellidos(apellidos)
        self.__profesores[cont].set_movil(movil)
        self.__profesores[cont].set_correo(correo)
        self.__profesores[cont].set_salario(sueldo)
        self.__profesores[cont].set_jornada(jornada)

        tempfile = NamedTemporaryFile(delete=False)

        with open(os.path.dirname(__file__)+'/files/profesores.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if row[0] == self.__profesores[cont].dni:
                    row[0] = dni
                    row[1] = nombre
                    row[2] = apellidos
                    row[3] = movil
                    row[4] = correo
                    row[7] = sueldo
                    row[8] = jornada
                    writer.writerow(row)
                else:
                    writer.writerow(row)
        shutil.move(tempfile.name, os.path.dirname(__file__)+'/files/profesores.csv')
        csvFile.close()
        tempfile.close()

    @staticmethod
    def __listar_profesores():
        """
        Obtiene todas los profesores existentes desde el fichero

        :return: lista profesores
        :rtype: list
        """
        profesores = []
        with open(os.path.dirname(__file__)+'/files/profesores.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                profesor = Profesor(row[0], row[1], row[2], row[3], row[4], row[7], row[8], row[5], row[6])
                profesores.append(profesor)
        return profesores
