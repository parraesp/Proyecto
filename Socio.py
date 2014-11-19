__author__ = 'francisco'

from time import *

class Socio:
    def __int__(self, DNI, nombre, apellidos, movil, correo):
        self.DNI = DNI;
        self.nombre = nombre;
        self.apellidos = apellidos;
        self.movil = movil;
        self.correo = correo;
        self.fechaAlta =
        self.fechaBaja = fechaBaja;

    def get_DNI(self):
        return self.DNI


    def get_Nombre(self):
        return self.nombre


    def get_Apellidos(self):
        return self.apellidos


    def get_Movil(self):
        return self.movil

    def get_Correo(self):
        return self.correo

    def get_FechaAlta(self):
        return self.fechaAlta

    def get_FechaBaja(self):
        return self.fechaBaja

    #public void darAltaSocioExistente() {
        #ponemos fechabaja a null y fecha alta a la fecha de hoy para no tener qie volver a crear el socio
        #fechaBaja = null;
        #fechaAlta = time.strftime("%d/%m/%y");
    #}

    def introducirDatos(self, DNI, nombre, apellidos, movil, correo):
        self.DNI = DNI
        self.nombre = nombre
        self.apellidos = apellidos
        self.movil = movil
        self.correo = correo

    def darBaja(self):
        #nos da la fecha del sistema para que la cambiemos por el null que teniamos puesto antes de dar de baja a un socio
        self.fechaBaja = time.strftime("%d/%m/%y")



