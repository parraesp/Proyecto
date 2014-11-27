__author__ = 'alberto'
import csv
from Socio import Socio
from Instalacion import Instalacion
from Reserva import Reserva
from datetime import *

class Conexion():

    def __listar_socios(self):
        socios = []
        with open('socios.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                socio = Socio(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                socios.append(socio)
        return socios

    def __listar_instalaciones(self):
        instalaciones = []
        with open('instalaciones.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                instalacion = Instalacion(row[0],row[1],row[2])
                instalaciones.append(instalacion)
        return instalaciones

    def __listar_reservas(self):
        reservas = []
        with open('reservas.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                socio = self.sacar_socio(row[0])
                instalacion = self.sacar_instalacion(row[2])
                reserva = Reserva(socio,row[1],instalacion)
                reservas.append(reserva)
        return reservas

    def __init__(self):
        self.__socios = self.__listar_socios()
        self.__instalaciones = self.__listar_instalaciones()
        #self.__profesores = self.__listar_profesores()
        self.__reservas = self.__listar_reservas()
        #self.__alquileres = self.__listar_alquileres()
        #self.__clases = self.__listar_clases()

    def guardar_socio(self,socio):
        f = open('socios.csv','a+')
        texto =''
        texto+=socio.DNI+'\t'
        texto+=socio.nombre+'\t'
        texto+=socio.apellidos+'\t'
        texto+=socio.movil+'\t'
        texto+=socio.correo+'\t'
        texto+=socio.fechaAlta+'\t'
        texto+=str(socio.estado)+'\n'
        f.write(texto)
        f.close()

    def sacar_socio(self,DNI):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__socios) and not(encontrado)):
            if(self.__socios[cont].DNI==DNI):
                encontrado = True
                valor=self.__socios[cont]
            else:
                cont=cont+1
        return valor

    def dar_baja_socio(self,DNI):
        cont = 0
        encontrado = False
        while(cont<len(self.__socios) and not(encontrado)):
            if(self.__socios[cont].DNI==DNI):
                encontrado = True
            else:
                cont=cont+1
        self.__socios[cont].cambiar_estado()
        print self.__socios[cont]
        #Ahora lo cambiamos en el archivo

    def sacar_instalacion(self,instalacionID):
        instalacion = False
        with open('instalaciones.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                if(row[0]==instalacionID):
                    instalacion =  Instalacion(row[0],row[1],row[2])
        return instalacion

    def guardar_reserva(self,reserva):
        f = open('reservas.csv','a+')
        texto =''
        texto+= str(reserva.socio[0])+'\t'
        texto+=str(reserva.fecha.strftime("%d/%m/%y %H:%M"))+'\t'
        texto+=str(reserva.instalacion.id)+'\n'
        f.write(texto)
        f.close()
        self.__reservas.append(reserva)

