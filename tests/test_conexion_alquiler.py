from unittest import TestCase
from src.Reserva import Reserva
from src.Socio import Socio
from src.Alquiler import Alquiler
from src.Instalacion import Instalacion
from mockito import mock, when
from datetime import *
from src.conexion_alquiler import ConexionAlquiler
from src.conexion_reserva import ConexionReserva
from src.conexion_instalacion import ConexionInstalacion
import os
__author__ = 'Ricardo'


class TestConexionAlquiler(TestCase):
    """
    Clases con los test unitarios del modelo de alquiler
    """
    def test_guardar_alquiler_fichero(self):
        """
        Test para guardar un alquiler en un fichero
        """
        socio = mock(Socio)
        when(socio).get_dni().thenReturn('11111111K')
        inst = mock(Instalacion)
        when(inst).get_instalacion_id().thenReturn('instprueba')
        fecha = datetime.strptime('01/01/07 07', '%d/%m/%y %H')
        reserva = Reserva(socio, fecha, mock(Instalacion))
        alquiler = Alquiler(reserva)
        alquiler.aniadir_instalacion(inst)
        con = ConexionAlquiler(mock(ConexionReserva),  mock(ConexionInstalacion))
        f = open('newFile.txt', 'w')
        con.guardar_alquiler_fichero(alquiler, f)
        f.close()
        f = open('newFile.txt', 'r')
        row = f.readlines()
        f.close()
        self.assertEqual(row[0], '11111111K\t01/01/07 07:00\tinstprueba\tFalse\n')
        os.remove('newFile.txt')
