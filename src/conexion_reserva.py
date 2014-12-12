from src.Reserva import Reserva
from datetime import *
import csv
import os
__author__ = 'alberto'


class conexion_reserva():
    def __init__(self, socios, instalaciones):
        self.__socios = socios
        self.__instalaciones = instalaciones
        self.__reservas = self.__listar_reservas()

    def guardar_reserva(self, reserva):
        f = open(os.path.dirname(__file__)+'/files/reservas.csv', 'a+')
        texto = ''
        texto += str(reserva.socio.get_DNI())+'\t'
        texto += str(reserva.fecha.strftime("%d/%m/%y %H:%M"))+'\t'
        texto += str(reserva.instalacion.get_instalacion_id())+'\n'
        f.write(texto)
        f.close()
        self.__reservas.append(reserva)

    def sacar_reserva(self, DNI, fecha):
        valor = -1
        cont = 0
        encontrado = False
        while(cont < len(self.__reservas) and not(encontrado)):
            if(self.__reservas[cont].fecha == fecha and
               self.__reservas[cont].socio.DNI == DNI):
                encontrado = True
                valor = self.__reservas[cont]
            else:
                cont = cont+1
        return valor

    def verificar_reserva(self, fecha):
        cont = 0
        verf = True
        while(cont < len(self.__reservas) and verf):
            if(self.__reservas[cont].fecha == fecha):
                verf = False
            else:
                cont = cont+1
        return verf

    def borrar_reserva(self, DNI, fecha):
        reserva = self.sacar_reserva(DNI, fecha)
        if (reserva != -1):
            self.__reservas.remove(reserva)
            f = open(os.path.dirname(__file__)+'/files/reservas.csv', 'r')
            reservas = f.readlines()
            f.close()

            f = open(os.path.dirname(__file__)+'/files/reservas.csv', 'w')
            for res in reservas:
                resAux = res.split("\t")
                if resAux[1] == fecha.strftime("%d/%m/%y %H:%M") and resAux[0] == DNI:
                    continue
                f.write(res)
            f.close()

    def __listar_reservas(self):
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