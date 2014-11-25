__author__ = 'alberto'
import csv
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