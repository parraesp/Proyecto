from tempfile import NamedTemporaryFile
from datetime import *

__author__ = 'alberto'
import csv
import shutil
from Socio import Socio
from Instalacion import Instalacion
from Reserva import Reserva
from Profesor import Profesor
from Alquiler import Alquiler

class Conexion():

    def __listar_socios(self):
        socios = []
        with open('socios.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                socio = Socio(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                socios.append(socio)
        f.close()
        return socios

    def __listar_instalaciones(self):
        instalaciones = {}
        with open('instalaciones.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                    instalacion = Instalacion(row[0],row[1],row[2])
                    instalaciones[row[0]] = instalacion
        f.close()
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
        f.close()
        return reservas

    def __listar_alquileres(self):
        alquileres = []
        with open('alquileres.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                fecha = datetime.strptime(row[0], "%d/%m/%y %H:%M")
                reserva = self.sacar_reserva(fecha)
                alquiler = Alquiler(reserva)
                for i in range(1,len(row)-1,1):
                    instalacion = self.sacar_instalacion(row[i])
                    alquiler.aniadirInstalacion(instalacion)
                if (row[len(row)-1] == 'True'):
                    alquiler.devuelto = True
                else:
                    alquiler.devuelto = False
                alquileres.append(alquiler)
        f.close()
        return alquileres

    def __listar_profesores(self):
        profesores = []
        with open('profesores.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                profesor = Profesor(row[0],row[1],row[2],row[3],row[4],row[7],row[8],row[5],row[6])
                profesores.append(profesor)
        return profesores

    def __init__(self):
        self.__socios = self.__listar_socios()
        self.__instalaciones = self.__listar_instalaciones()
        #self.__profesores = self.__listar_profesores()
        self.__reservas = self.__listar_reservas()
        self.__alquileres = self.__listar_alquileres()
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
        self.__socios.append(socio)

    def guardar_profesor(self,profesor):
        f = open('profesores.csv','a+')
        texto =''
        texto+=profesor.DNI+'\t'
        texto+=profesor.nombre+'\t'
        texto+=profesor.apellidos+'\t'
        texto+=profesor.movil+'\t'
        texto+=profesor.correo+'\t'
        texto+=profesor.fechaAlta+'\t'
        texto+=str(profesor.estado)+'\t'
        texto+=str(profesor.get_salario())+'\t'
        texto+=profesor.get_jornada()+'\n'
        f.write(texto)
        f.close()
        self.__profesores.append(profesor)

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

    def sacar_profesor(self,DNI):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__socios) and not(encontrado)):
            if(self.__profesores[cont].DNI==DNI):
                encontrado = True
                valor=self.__profesores[cont]
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
        #Ahora lo cambiamos en el archivo
        tempfile = NamedTemporaryFile(delete=False)

        with open('socios.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if(row[0]==self.__socios[cont].DNI):
                    row[6]=False
                    writer.writerow(row)
                else:
                    writer.writerow(row)
        shutil.move(tempfile.name, 'socios.csv')
        csvFile.close()
        tempfile.close()

    def dar_baja_profesor(self,DNI):
        cont = 0
        encontrado = False
        while(cont<len(self.__profesores) and not(encontrado)):
            if(self.__profesores[cont].DNI==DNI):
                encontrado = True
            else:
                cont=cont+1
        self.__profesores[cont].cambiar_estado()
        #Ahora lo cambiamos en el archivo
        tempfile = NamedTemporaryFile(delete=False)

        with open('profesores.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if(row[0]==self.__profesores[cont].DNI):
                    row[6]=False
                    writer.writerow(row)
                else:
                    writer.writerow(row)
        shutil.move(tempfile.name, 'profesores.csv')
        csvFile.close()
        tempfile.close()

    def sacar_instalacion(self,instalacionID):
        return self.__instalaciones.get(instalacionID,-1)

    def guardar_reserva(self,reserva):
        f = open('reservas.csv','a+')
        texto =''
        texto+= str(reserva.socio.DNI)+'\t'
        texto+=str(reserva.fecha.strftime("%d/%m/%y %H:%M"))+'\t'
        texto+=str(reserva.instalacion.id)+'\n'
        f.write(texto)
        f.close()
        self.__reservas.append(reserva)

    def sacar_reserva(self,fecha):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__reservas) and not(encontrado)):
            if(self.__reservas[cont].fecha==fecha.strftime("%d/%m/%y %H:%M")):
                encontrado = True
                valor=self.__reservas[cont]
            else:
                cont=cont+1
        return valor

    def borrar_reserva(self,fecha):
        borrado = False
        reserva = self.sacar_reserva(fecha)
        if (reserva != -1):
            borrado = True
            self.__reservas.remove(reserva)
            f = open("reservas.csv","r")
            reservas = f.readlines()
            f.close()

            f = open("reservas.csv","w")
            for res in reservas:
                resAux = res.split("\t")
                if resAux[1]!=fecha.strftime("%d/%m/%y %H:%M"):
                    f.write(res)
            f.close()
        return borrado

    def guardar_alquiler(self,alquiler):
        f = open('alquileres.csv','a+')
        texto =''
        texto+= str(alquiler.reserva.fecha)+'\t'
        insts = alquiler.instalaciones
        for i in insts:
            texto+=str(i.id)+'\t'
        texto+=str(alquiler.devuelto)+'\n'
        f.write(texto)
        f.close()
        self.__alquileres.append(alquiler)


    def cambiar_socio(self,DNI,nombre,apellidos,movil,correo):
        cont = 0
        encontrado = False
        while(cont<len(self.__socios) and not(encontrado)):
            if(self.__socios[cont].DNI==DNI):
                encontrado = True
            else:
                cont=cont+1
        self.__socios[cont].set_nombre(nombre)
        self.__socios[cont].set_apellidos(apellidos)
        self.__socios[cont].set_movil(movil)
        self.__socios[cont].set_correo(correo)
        print self.__socios[cont]
        #Ahora lo cambiamos en el archivo
        tempfile = NamedTemporaryFile(delete=False)

        with open('socios.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if(row[0]==self.__socios[cont].DNI):
                    row[0]=DNI
                    row[1]=nombre
                    row[2]=apellidos
                    row[3]=movil
                    row[4]=correo
                    writer.writerow(row)
                else:
                    writer.writerow(row)
        shutil.move(tempfile.name, 'socios.csv')
        csvFile.close()
        tempfile.close()

    def cambiar_profesor(self,DNI,nombre,apellidos,movil,correo,sueldo,jornada):
        cont = 0
        encontrado = False
        while(cont<len(self.__profesores) and not(encontrado)):
            if(self.__profesores[cont].DNI==DNI):
                encontrado = True
            else:
                cont=cont+1
        self.__profesores[cont].set_nombre(nombre)
        self.__profesores[cont].set_apellidos(apellidos)
        self.__profesores[cont].set_movil(movil)
        self.__profesores[cont].set_correo(correo)
        self.__profesores[cont].set_salario(sueldo)
        self.__profesores[cont].set_jornada(jornada)
        print self.__profesores[cont]
        #Ahora lo cambiamos en el archivo
        tempfile = NamedTemporaryFile(delete=False)

        with open('profesores.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if(row[0]==self.__profesores[cont].DNI):
                    row[0]=DNI
                    row[1]=nombre
                    row[2]=apellidos
                    row[3]=movil
                    row[4]=correo
                    row[7]=sueldo
                    row[8]=jornada
                    writer.writerow(row)
                else:
                    writer.writerow(row)
        shutil.move(tempfile.name, 'socios.csv')
        csvFile.close()
        tempfile.close()


