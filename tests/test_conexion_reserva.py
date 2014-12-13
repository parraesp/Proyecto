from unittest import TestCase
from src.conexion_reserva import ConexionReserva
from src.Reserva import Reserva
from src.Socio import Socio
from src.Instalacion import Instalacion
from mockito import mock, when
from datetime import *
from src.conexion_socio import ConexionSocio
from src.conexion_instalacion import ConexionInstalacion
import os
__author__ = 'Ricardo'


class TestConexionReserva(TestCase):
    """
    Clase con los test unitarios del modelo de reservas
    """
    def test_guardar_reserva(self):
        """
        Test unitario que verifica que se guarda una reserva de forma permanente
        """
        socio = mock(Socio)
        con = ConexionReserva(mock(ConexionSocio), mock(ConexionInstalacion))
        inst = mock(Instalacion)
        when(socio).get_dni().thenReturn('11111111K')
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
        """
        Test unitario que verifica que obtiene una reserva del modelo
        """
        con = ConexionReserva(ConexionSocio(), mock(ConexionInstalacion))
        fecha = datetime.strptime('02/05/24 16', '%d/%m/%y %H')
        fecha2 = datetime.strptime('02/05/23 16', '%d/%m/%y %H')
        self.assertIsInstance(con.sacar_reserva('12345678A', fecha), Reserva)
        self.assertEqual(-1, con.sacar_reserva('12222278A', fecha), Reserva)
        self.assertEqual(-1, con.sacar_reserva('12345678A', fecha2), Reserva)

    def test_verificar_reserva(self):
        """
        Test unitario para verificar una reserva existente
        """
        con = ConexionReserva(mock(), ConexionInstalacion())
        fecha = datetime.strptime('02/05/24 16', '%d/%m/%y %H')
        fecha2 = datetime.strptime('02/01/07 07', '%d/%m/%y %H')
        self.assertFalse(con.verificar_reserva(fecha, 'inst01'))
        self.assertTrue(con.verificar_reserva(fecha2, 'inst01'))

    def test_borrar_reserva(self):
        """
        Test unitario que verifica que se borra una reserva de forma permanente
        """
        socio = mock(Socio)
        con = ConexionReserva(ConexionSocio(), mock(ConexionInstalacion))
        inst = mock(Instalacion)
        when(socio).get_dni().thenReturn('12345678A')
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
        tmp_file.close()
