from tempfile import NamedTemporaryFile

__author__ = 'alberto'
import csv
import shutil
from Socio import Socio
from Instalacion import Instalacion
from Reserva import Reserva
from Clase import Clase
from Alquiler import Alquiler
from Profesor import Profesor
from datetime import *

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
    def __listar_clases(self):
        clases = []
        with open('clases.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                fecha = datetime.strptime(row[1], "%d/%m/%y %H:%M")
                clase = Clase(self.sacar_profesor(row[0]),self.sacar_reserva(fecha))
                clases.append(clase)
        f.close()
        return clases

    def __listar_instalaciones(self):
        instalaciones = []
        with open('instalaciones.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                instalacion = Instalacion(row[0],row[1],row[2])
                instalaciones.append(instalacion)
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

    def __listar_profesores(self):
        profesores = []
        with open('profesores.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                profesor = Profesor(row[0],row[1],row[2],row[3],row[4],row[7],row[8],row[5],row[6])
                profesores.append(profesor)
        return profesores

    def __listar_alquileres(self):
        alquileres = []
        with open('alquileres.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                fecha = datetime.strptime(row[1], "%d/%m/%y %H:%M")
                reserva = self.sacar_reserva(row[0],fecha)
                alquiler = Alquiler(reserva)
                for i in range(2,len(row)-1,1):
                    instalacion = self.sacar_instalacion(row[i])
                    alquiler.aniadirInstalacion(instalacion)
                if (row[len(row)-1] == 'True'):
                    alquiler.devuelto = True
                else:
                    alquiler.devuelto = False
                alquileres.append(alquiler)
        f.close()
        return alquileres

    def __init__(self):
        self.__socios = self.__listar_socios()
        self.__instalaciones = self.__listar_instalaciones()
        self.__profesores = self.__listar_profesores()
        self.__reservas = self.__listar_reservas()
        self.__alquileres = self.__listar_alquileres()
        self.__clases = self.__listar_clases()

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
        while(cont<len(self.__profesores) and not(encontrado)):
            if(self.__profesores[cont].DNI==DNI):
                encontrado = True
                valor=self.__profesores[cont]
            else:
                cont=cont+1
        return valor

    def dar_baja_socio(self,socio):
        ind = self.__socios.index(socio)
        self.__socios[ind].cambiar_estado()
        #Ahora lo cambiamos en el archivo
        tempfile = NamedTemporaryFile(delete=False)

        with open('socios.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if(row[0]==self.__socios[ind].DNI):
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
        instalacion = False
        with open('instalaciones.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                if(row[0]==instalacionID):
                    instalacion =  Instalacion(row[0],row[1],row[2])
        f.close()
        return instalacion

    def sacar_clase(self,profesor, fecha):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__clases) and not(encontrado)):
            if(self.__clases[cont].get_profesor().DNI==profesor and self.__clases[cont].get_reserva().get_fecha()==fecha):
                encontrado = True
                valor=self.__clases[cont]
            else:
                cont=cont+1
        return valor

    def guardar_reserva(self,reserva):
        f = open('reservas.csv','a+')
        texto =''
        texto+= str(reserva.socio.DNI)+'\t'
        texto+=str(reserva.fecha)+'\t'
        texto+=str(reserva.instalacion.id)+'\n'
        f.write(texto)
        f.close()
        self.__reservas.append(reserva)

    def guardar_clase(self,clase):
        f = open('clases.csv','a+')
        texto =''
        texto+= clase.get_profesor().get_DNI()+'\t'
        texto+= str(clase.get_reserva().get_fecha().strftime("%d/%m/%y %H:%M"))+'\n'
        f.write(texto)
        f.close()
        self.__clases.append(clase)

    def sacar_reserva(self,DNI, fecha):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__reservas) and not(encontrado)):
            if(self.__reservas[cont].fecha==fecha.strftime("%d/%m/%y %H:%M") and
            self.__reservas[cont].socio.DNI == DNI):
                encontrado = True
                valor=self.__reservas[cont]
            else:
                cont=cont+1
        return valor

    def borrar_reserva(self,DNI,fecha):
        borrado = False
        reserva = self.sacar_reserva(DNI,fecha)
        if (reserva != -1):
            borrado = True
            self.__reservas.remove(reserva)
            f = open("reservas.csv","r")
            reservas = f.readlines()
            f.close()

            f = open("reservas.csv","w")
            for res in reservas:
                resAux = res.split("\t")
                if resAux[1]!=fecha.strftime("%d/%m/%y %H:%M") and resAux[0] != DNI:
                    f.write(res)
            f.close()
        return borrado

    def guardar_alquiler(self,alquiler):
        f = open('alquileres.csv','a+')
        self.guardar_alquiler_fichero(alquiler,f)
        f.close()
        self.__alquileres.append(alquiler)

    def sacar_alquiler(self,reserva):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__alquileres) and not(encontrado)):
            if(self.__alquileres[cont].reserva == reserva):
                encontrado = True
                valor=self.__alquileres[cont]
            else:
                cont=cont+1
        return valor

    def devolver_alquiler(self,reserva):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__alquileres) and not(encontrado)):
            if(self.__alquileres[cont].reserva == reserva):
                encontrado = True
                self.__alquileres[cont].devuelto = True
                valor=self.__alquileres[cont]
            else:
                cont=cont+1

        f = open("alquileres.csv","w")
        for alq in self.__alquileres:
            self.guardar_alquiler_fichero(alq,f)
        f.close()
        return valor

    def guardar_alquiler_fichero(self,alquiler,fichero):
        texto =''
        texto +=alquiler.reserva.socio.DNI+'\t'
        texto+= str(alquiler.reserva.fecha)+'\t'
        for ins in alquiler.instalaciones:
            texto+=str(ins.id)+'\t'
        texto+=str(alquiler.devuelto)+'\n'
        fichero.write(texto)

    def borrar_clase(self,profesor,fecha):
        tempfile = NamedTemporaryFile(delete=False)

        with open('clases.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if(row[0]!=profesor and row[1]!=str(fecha)):
                    writer.writerow(row)
        shutil.move(tempfile.name, 'clases.csv')
        csvFile.close()
        tempfile.close()

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
        shutil.move(tempfile.name, 'profesores.csv')
        csvFile.close()
        tempfile.close()