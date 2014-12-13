from src.Reserva import Reserva
from datetime import *
import csv
import os
__author__ = 'alberto'


class ConexionReserva():
    """
    Modelo de la clase reserva
    """
    def __init__(self, socios, instalaciones):
        """
        Constructor de la clase

        :param socios: modelo de socios
        :param instalaciones: modelo de instalaciones
        """
        self.__socios = socios
        self.__instalaciones = instalaciones
        self.__reservas = self.__listar_reservas()

    def guardar_reserva(self, reserva):
        """
        Guarda una reserva en el fichero y en el club

        :param reserva: reserva a guardar
        """
        f = open(os.path.dirname(__file__)+'/files/reservas.csv', 'a+')
        texto = ''
        texto += str(reserva.get_socio().get_dni())+'\t'
        texto += str(reserva.get_fecha().strftime("%d/%m/%y %H:%M"))+'\t'
        texto += str(reserva.get_instalacion().get_instalacion_id())+'\n'
        f.write(texto)
        f.close()
        self.__reservas.append(reserva)

    def sacar_reserva(self, dni, fecha):
        """
        Obtiene los datos de una reserva

        :param dni: dni del socio
        :param fecha: fecha de la reserva
        :return: reserva
        """
        valor = -1
        cont = 0
        encontrado = False
        while cont < len(self.__reservas) and not encontrado:
            if(self.__reservas[cont].get_fecha() == fecha and
               self.__reservas[cont].get_socio().get_dni() == dni):
                encontrado = True
                valor = self.__reservas[cont]
            else:
                cont += 1
        return valor

    def verificar_reserva(self, fecha, instalacion_id):
        """
        Verifica los datos de un reserva para no repetirla

        :param fecha: fecha de la reserva
        :param instalacion_id: instalacion a reservas
        :return: reserva valida
        :rtype: bool
        """
        cont = 0
        verf = True
        while cont < len(self.__reservas) and verf:
            if(self.__reservas[cont].get_fecha() == fecha and
                    self.__reservas[cont].get_instalacion().get_instalacion_id() == instalacion_id):
                verf = False
            else:
                cont += 1
        return verf

    def borrar_reserva(self, dni, fecha):
        """
        Borra una reserva del fichero y del club

        :param dni: socio que reservo
        :param fecha: fecha de la reserva
        """
        reserva = self.sacar_reserva(dni, fecha)
        if reserva != -1:
            self.__reservas.remove(reserva)
            f = open(os.path.dirname(__file__)+'/files/reservas.csv', 'r')
            reservas = f.readlines()
            f.close()

            f = open(os.path.dirname(__file__)+'/files/reservas.csv', 'w')
            for res in reservas:
                res_aux = res.split("\t")
                if res_aux[1] == fecha.strftime("%d/%m/%y %H:%M") and res_aux[0] == dni:
                    continue
                f.write(res)
            f.close()

    def __listar_reservas(self):
        """
        Obtiene todas las reservas existentes desde el fichero

        :return: lista reservas
        :rtype: list
        """
        reservas = []
        with open(os.path.dirname(__file__)+'/files/reservas.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                socio = self.__socios.sacar_socio(row[0])
                fecha = datetime.strptime(row[1], "%d/%m/%y %H:%M")
                instalacion = self.__instalaciones.sacar_instalacion(row[2])
                reserva = Reserva(socio, fecha, instalacion)
                reservas.append(reserva)
        f.close()
        return reservas
