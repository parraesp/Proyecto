from unittest import TestCase
from src.Instalacion import Instalacion
from src.conexion_instalacion import conexion_instalacion

__author__ = 'Ricardo'


class TestConexion_instalacion(TestCase):
    def test_sacar_instalacion(self):
        con = conexion_instalacion()
        self.assertIsInstance(con.sacar_instalacion('inst02'), Instalacion)
        self.assertEqual(-1, con.sacar_instalacion('olakase'))