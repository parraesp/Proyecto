__author__ = 'francisco'

import time

class Socio():
    def __init__(self, DNI, nombre, apellidos, movil, correo ,*otros):
        self.__DNI = str(DNI)
        self.__nombre = str(nombre)
        self.__apellidos = str(apellidos)
        self.__movil = str(movil)
        self.__correo = str(correo)
        if (len(otros) == 2):
            self.__fechaAlta = otros[0]
            self.__estado = bool(otros[1])
        else:
            self.__fechaAlta = str(time.strftime("%d/%m/%y"))
            self.__estado = True

    def __str__(self):
        return 'DNI: ' + self.__DNI + ', fecha: ' + self.__fechaAlta + ', estado: ' + str(self.__estado)

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

    def cambiar_estado(self):
        self.__estado = False

    def set_fechaAlta(self,fecha):
        self.__fechaAlta = fecha
    #public void darAltaSocioExistente() {
        #ponemos fechabaja a null y fecha alta a la fecha de hoy para no tener qie volver a crear el socio
        #fechaBaja = null;
        #fechaAlta = time.strftime("%d/%m/%y");
    #}

    DNI = property(get_DNI)
    nombre = property(get_nombre)
    apellidos = property(get_apellidos)
    movil = property(get_movil)
    correo = property(get_correo)
    fechaAlta = property(get_fechaAlta,set_fechaAlta)
    estado = property(get_estado)

