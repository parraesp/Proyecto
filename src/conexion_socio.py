from src.Socio import Socio
__author__ = 'alberto'
import csv
import shutil
import os
from tempfile import NamedTemporaryFile


class ConexionSocio():
    """
    Modelo de la clase socio
    """
    def __init__(self):
        """
        Constructor del modelo de socios
        """
        self.__socios = self.__listar_socios()

    @staticmethod
    def __listar_socios():
        """
        Obtiene todos los socios existentes del fichero

        :return: lista de socios
        :rtype: list
        """
        socios = []
        with open(os.path.dirname(__file__)+'/files/socios.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                socio = Socio(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                socios.append(socio)
        f.close()
        return socios

    def guardar_socio(self, socio):
        """
        Guarda un socio en el fichero y en el club

        :param socio: socio a guardar
        """
        f = open(os.path.dirname(__file__)+'/files/socios.csv', 'a+')
        texto = ''
        texto += socio.dni+'\t'
        texto += socio.nombre+'\t'
        texto += socio.apellidos+'\t'
        texto += socio.movil+'\t'
        texto += socio.correo+'\t'
        texto += socio.fecha_alta+'\t'
        texto += str(socio.estado)+'\n'
        f.write(texto)
        f.close()
        self.__socios.append(socio)

    def sacar_socio(self, dni):
        """
        Obtiene los datos de un socio

        :param dni: dni del socio
        :return: socio
        """
        valor = -1
        cont = 0
        encontrado = False
        while cont < len(self.__socios) and not encontrado:
            if self.__socios[cont].dni == dni:
                encontrado = True
                valor = self.__socios[cont]
            else:
                cont += 1
        return valor

    def dar_baja_socio(self, socio):
        """
        Da de baja a un socio, cambia su estado de a False

        :param socio: socio a dar de baja
        """
        ind = self.__socios.index(socio)
        self.__socios[ind].cambiar_estado()

        tempfile = NamedTemporaryFile(delete=False)

        with open(os.path.dirname(__file__)+'/files/socios.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if row[0] == self.__socios[ind].dni:
                    row[6] = False
                    writer.writerow(row)
                else:
                    writer.writerow(row)
        shutil.move(tempfile.name, os.path.dirname(__file__)+'/files/socios.csv')
        csvFile.close()
        tempfile.close()

    def cambiar_socio(self, dni, nombre, apellidos, movil, correo):
        """
        Edita los datos de un socio y los guarda de forma permanente

        :param dni: dni del socio
        :param nombre: nuevo nombre
        :param apellidos: nuevos apellidos
        :param movil: nuevo telefono
        :param correo: nuevo correo
        """
        cont = 0
        encontrado = False
        while cont < len(self.__socios) and not encontrado:
            if self.__socios[cont].dni == dni:
                encontrado = True
            else:
                cont += 1
        self.__socios[cont].set_nombre(nombre)
        self.__socios[cont].set_apellidos(apellidos)
        self.__socios[cont].set_movil(movil)
        self.__socios[cont].set_correo(correo)

        tempfile = NamedTemporaryFile(delete=False)

        with open(os.path.dirname(__file__)+'/files/socios.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if row[0] == self.__socios[cont].dni:
                    row[0] = dni
                    row[1] = nombre
                    row[2] = apellidos
                    row[3] = movil
                    row[4] = correo
                    writer.writerow(row)
                else:
                    writer.writerow(row)
        shutil.move(tempfile.name, os.path.dirname(__file__)+'/files/socios.csv')
        csvFile.close()
        tempfile.close()
