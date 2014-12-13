from unittest import TestCase
from src.conexion_reserva import conexion_reserva
from src.Reserva import Reserva
from src.Socio import Socio
from src.Instalacion import Instalacion
from mockito import mock, when
from datetime import *
from src.conexion_socio import conexion_socio
from src.conexion_instalacion import conexion_instalacion
import os
__author__ = 'Ricardo'


class TestConexion_reserva(TestCase):
    def test_guardar_reserva(self):
        socio = mock(Socio)
        con = conexion_reserva(mock(conexion_socio), mock(conexion_instalacion))
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
        con = conexion_reserva(conexion_socio(), mock(conexion_instalacion))
        fecha = datetime.strptime('02/05/24 16', '%d/%m/%y %H')
        fecha2 = datetime.strptime('02/05/23 16', '%d/%m/%y %H')
        self.assertIsInstance(con.sacar_reserva('12345678A', fecha), Reserva)
        self.assertEqual(-1, con.sacar_reserva('12222278A', fecha), Reserva)
        self.assertEqual(-1, con.sacar_reserva('12345678A', fecha2), Reserva)

    def test_verificar_reserva(self):
        con = conexion_reserva(mock(), mock())
        fecha = datetime.strptime('02/05/24 16', '%d/%m/%y %H')
        fecha2 = datetime.strptime('02/01/07 07', '%d/%m/%y %H')
        self.assertFalse(con.verificar_reserva(fecha))
        self.assertTrue(con.verificar_reserva(fecha2))

    def test_borrar_reserva(self):
        socio = mock(Socio)
        con = conexion_reserva(conexion_socio(), mock(conexion_instalacion))
        inst = mock(Instalacion)
        when(socio).get_DNI().thenReturn('12345678A')
        when(inst).get_instalacion_id().thenReturn('inst02')
        fecha = datetime.strptime('01/01/07 07', '%d/%m/%y %H')
        reserva = Reserva(socio, fecha, inst)
        con.guardar_reserva(reserva)
        con.borrar_reserva('12345678A', fecha)
        link = os.path.dirname(__file__)
        link = link[:-5] + 'src/files/reservas.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        self.assertNotEquals(lines[len(lines)-1], "11111111K\t01/01/07 07:00\tinst02\n")