__author__ = 'Ricardo'
from Conexion import *
from Socio import Socio

class Club():
    def alta_socio(self,DNI,nombre,apellidos,movil,correo):
        #verificar datos
        socio = Socio(DNI,nombre,apellidos,movil,correo)
        guardar_socio(socio)

    def eliminar_socio(self,DNI):
        socio = self.obtener_socio(DNI)
        return socio

    def obtener_socio(self,DNI):
        socio = sacar_socio(DNI)
        return socio

    