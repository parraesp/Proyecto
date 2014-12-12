from unittest import TestCase
from src.conexion_reserva import conexion_reserva
from src.Reserva import Reserva
from src.Socio import Socio
from src.Instalacion import Instalacion
from mockito import mock, when
from datetime import *
import os
__author__ = 'Ricardo'


class TestConexion_reserva(TestCase):
    def test_guardar_reserva(self):
        socio = mock(Socio)
        con = conexion_reserva(mock(), mock())
        inst = mock(Instalacion)
        when(socio).get_DNI().thenReturn('11111111K')
        when(inst).get_instalacion_id().thenReturn('inst02')
        fecha = datetime.strptime('01/01/07 07', '%d/%m/%y %H')
        reserva = Reserva(socio, fecha, inst)
        con.guardar_reserva(reserva)
        link = os.path.dirname(__file__)
        link = link[:-5] + 'src/files/reservas.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        self.assertEqual(lines[len(lines)-1], "11111111K\t01/01/07 07:00\tinst02\n")
        lines.pop()
        tmp_file.close()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)

    def test_sacar_reserva(self):
        self.fail()

    def test_verificar_reserva(self):
        self.fail()

    def test_borrar_reserva(self):
        self.fail()