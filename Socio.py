__author__ = 'francisco'

import time

class Socio():
    def __init__(self, DNI, nombre, apellidos, movil, correo):
        self.__DNI = str(DNI)
        self.__nombre = str(nombre)
        self.__apellidos = str(apellidos)
        self.__movil = str(movil)
        self.__correo = str(correo)
        self.__fechaAlta = str(time.strftime("%d/%m/%y"))
        self.__estado = True


    def darBaja(self):
        #nos da la fecha del sistema para que la cambiemos por el null que teniamos puesto antes de dar de baja a un socio
        self.__estado = False

    def get_DNI(self):
        return self.__DNI


    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos


    def get_movil(self):
        return self.__movil

    def get_correo(self):
        return self.__correo

    def get_fechaAlta(self):
        return self.__fechaAlta

    def get_estado(self):
        return self.__estado

    def set_DNI(self,DNI):
        self.__DNI = DNI

    def __str__(self):
        texto =''
        texto+='\nDNI: '+ self.DNI
        texto+='\nNombre: '+ self.nombre
        texto+='\nApellidos: '+ self.apellidos
        texto+='\nMovil: '+ self.movil
        texto+='\nCorreo: '+ self.correo
        return texto

    DNI = property(get_DNI)
    nombre = property(get_nombre)
    apellidos = property(get_apellidos)
    movil = property(get_movil)
    correo = property(get_correo)
    fechaAlta = property(get_fechaAlta)
    estado = property(get_estado)

