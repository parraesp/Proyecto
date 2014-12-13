from unittest import TestCase
from src.Instalacion import Instalacion
from src.conexion_instalacion import ConexionInstalacion

__author__ = 'Ricardo'


class TestConexionInstalacion(TestCase):
    """
    Clase con los test unitarios del modelo de instalaciones
    """
    def test_sacar_instalacion(self):
        """
        Test para obtener una instalacion del modelo
        """
        con = ConexionInstalacion()
        self.assertIsInstance(con.sacar_instalacion('inst02'), Instalacion)
        self.assertEqual(-1, con.sacar_instalacion('olakase'))
