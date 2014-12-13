from src.Alquiler import Alquiler
import os

__author__ = 'alberto'
import csv
from datetime import datetime


class ConexionAlquiler():
    """
    Modelo para la clase alquiler
    """
    def __init__(self, reservas, instalaciones):
        """
        Constructor de la conexion alquiler

        :param reservas: conexion de reservas
        :param instalaciones: conexion de alquileres
        """
        self.reservas = reservas
        self.instalaciones = instalaciones
        self.__alquileres = self.__listar_alquileres()

    def guardar_alquiler(self, alquiler):
        """
        Guarda un alquiler en el club y en el fichero

        :param alquiler: alquiler a guardar
        """
        f = open(os.path.dirname(__file__)+'/files/alquileres.csv', 'a+')
        self.guardar_alquiler_fichero(alquiler, f)
        f.close()
        self.__alquileres.append(alquiler)

    def sacar_alquiler(self, reserva):
        """
        Obtiene un alquiler del modelo

        :param reserva: reserva asociada
        :return: alquiler
        """
        valor = -1
        cont = 0
        encontrado = False
        while cont < len(self.__alquileres) and not encontrado:
            if self.__alquileres[cont].get_reserva() == reserva:
                encontrado = True
                valor = self.__alquileres[cont]
            else:
                cont += 1
        return valor

    def devolver_alquiler(self, reserva):
        """
        Devuelve un alquiler y lo guarda en fichero

        :param reserva: reserva asociada
        :return: alquiler devuelto
        """
        valor = -1
        cont = 0
        encontrado = False
        while cont < len(self.__alquileres and not encontrado):
            if self.__alquileres[cont].get_reserva() == reserva:
                encontrado = True
                self.__alquileres[cont].set_devuelto(True)
                valor = self.__alquileres[cont]
            else:
                cont += 1

        f = open(os.path.dirname(__file__)+'/files/alquileres.csv', "w")
        for alq in self.__alquileres:
            self.guardar_alquiler_fichero(alq, f)
        f.close()
        return valor

    @staticmethod
    def guardar_alquiler_fichero(alquiler, fichero):
        """
        Metodo para guadar un alquiler en fichero

        :param alquiler: alquiler a guardar
        :param fichero: fichero para guardar
        """
        texto = ''
        texto += alquiler.get_reserva().get_socio().get_dni()+'\t'
        texto += str(alquiler.get_reserva().get_fecha().strftime("%d/%m/%y %H:%M"))+'\t'
        for ins in alquiler.get_instalaciones():
            texto += str(ins.get_instalacion_id())+'\t'
        texto += str(alquiler.is_devuelto())+'\n'
        fichero.write(texto)

    def __listar_alquileres(self):
        """
        Obtiene los alquileres existente del fichero.

        :return: lista de alquileres
        :rtype: list
        """
        alquileres = []
        with open(os.path.dirname(__file__)+'/files/alquileres.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                fecha = datetime.strptime(row[1], "%d/%m/%y %H:%M")
                reserva = self.reservas.sacar_reserva(row[0], fecha)
                alquiler = Alquiler(reserva)
                for i in range(2, len(row)-1, 1):
                    instalacion = self.instalaciones.sacar_instalacion(row[i])
                    alquiler.aniadir_instalacion(instalacion)
                if row[len(row)-1] == 'True':
                    alquiler.set_devuelto(True)
                else:
                    alquiler.set_devuelto(False)
                alquileres.append(alquiler)
        f.close()
        return alquileres
