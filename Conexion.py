__author__ = 'alberto'
from Socio import Socio

def guardar_socio(socio):
    f = open('socios.csv','a')
    texto =''
    texto+=socio.DNI+'\t'
    texto+=socio.nombre+'\t'
    texto+=socio.apellidos+'\t'
    texto+=socio.movil+'\t'
    texto+=socio.correo+'\t'
    texto+=socio.fechaAltaI+'\t'
    texto+=str(socio.estado)+'\n'
    f.write(texto)