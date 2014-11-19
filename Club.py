__author__ = 'Ricardo'
from Socio import Socio
from Conexion import *

class Club():
    def alta_socio(self,DNI,nombre,apellidos,movil,correo):
        #verificar datos
        socio = Socio(DNI,nombre,apellidos,movil,correo)
        guardar_socio(socio)
