__author__ = 'alberto'
import csv
from Socio import Socio
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
                valor = Socio(row[0],row[1],row[2],row[3],row[4])
    f.close()
    return valor

def borrar_socio(DNI):
    with open('socios.csv','w+') as f:
        content = csv.reader(f, delimiter='\t')
        for row in content:
            csv.writer(f, delimiter='\t')
            if(row[0]==DNI):
                valor = Socio(row[0],row[1],row[2],row[3],row[4])
    f.close()