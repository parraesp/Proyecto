__author__ = 'alberto'
import csv
from Socio import Socio

class Conexion():
    def __init__(self):
        self.__socios = listar_socios()
        self.__instalaciones = listar_instalaciones()
        self.__materiales = listar_materiales()
        self.__profesores = listar_profesores()
        self.__reservas = listar_reservas()
        self.__alquileres = listar_alquileres()
        self.__clases = listar_clases()

    def guardar_socio(socio):
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

    def sacar_socio(DNI):
        valor = -1
        with open('socios.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                if(row[0]==DNI):
                    valor = row
        return valor

    def guardar_reserva(reserva):
        f = open('reservas.csv','a+')
        texto =''
        texto+=reserva.socio.DNI+'\t'
        texto+=reserva.fecha+'\t'
        texto+=reserva.instalacion.id+'\n'
        f.write(texto)
        f.close()