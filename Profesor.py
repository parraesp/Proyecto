__author__ = 'alberto'
from Socio import Socio

class Profesor(Socio):
    def __init__(self, DNI, nombre, apellidos, movil, correo , salario, jornada, *otros):
        if(len(otros)==2):
            Socio.__init__(self,DNI,nombre,apellidos,movil,correo,otros[0],otros[1])
        else:
            Socio.__init__(self,DNI,nombre,apellidos,movil,correo)
        self.__salario = int(salario)
        self.__jornada = str(jornada)

    def set_salario(self,salario):
        self.__salario = salario

    def set_jornada(self,jornada):
        self.__jornada = jornada

    def get_salario(self):
        return self.__salario

    def get_jornada(self):
        return self.__jornada