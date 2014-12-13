from unittest import TestCase
from src.conexion_socio import ConexionSocio
from src.Socio import Socio
import time
import os

__author__ = 'alberto'


class TestConexionSocio(TestCase):
    """
    Clase con los test unitarios del modelo de socios
    """
    def test_guardar_socio(self):
        """
        Test unitario que verifica que se guarda un socio de forma permanente
        """
        con = ConexionSocio()
        socio = Socio("49116666Q", "Don Juan", "Tenorio", "634824490", "daswirdaendern@jetzt.de")
        con.guardar_socio(socio)
        link = os.path.dirname(__file__)
        link = link[:-5] + 'src/files/socios.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        tmp_file.close()
        self.assertEqual(lines[len(lines)-1], "49116666Q\tDon Juan\tTenorio\t634824490\tdaswirdaendern@jetzt.de\t" +
                         str(time.strftime("%d/%m/%y"))+"\tTrue\n")
        lines.pop()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)
        tmp_file.close()

    def test_sacar_socio(self):
        """
        Test unitario que verifica obtiene un socio del modelo
        """
        con = ConexionSocio()
        socio = Socio("49116666Q", "Don Juan", "Tenorio", "634824490", "daswirdaendern@jetzt.de")
        con.guardar_socio(socio)
        link = os.path.dirname(__file__)
        link = link[:-5] + 'src/files/socios.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        tmp_file.close()
        self.assertEqual(con.sacar_socio("socioInexistente"), -1)
        self.assertIsInstance(con.sacar_socio("49116666Q"), Socio)
        lines.pop()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)
        tmp_file.close()

    def test_dar_baja_socio(self):
        """
        Test unitario para dar de baja a un socio
        """
        con = ConexionSocio()
        socio = Socio("49116666Q", "Don Juan", "Tenorio", "634824490", "daswirdaendern@jetzt.de")
        con.guardar_socio(socio)
        con.dar_baja_socio(socio)
        link = os.path.dirname(__file__)
        link = link[:-5] + 'src/files/socios.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        tmp_file.close()
        self.assertEqual(lines[len(lines)-1], "49116666Q\tDon Juan\tTenorio\t634824490\tdaswirdaendern@jetzt.de\t"
                         + str(time.strftime("%d/%m/%y"))+"\tFalse\r\n")
        lines.pop()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)
        tmp_file.close()

    def test_cambiar_socio(self):
        """
        Test unitario que verifica que se editan los datos de un socio
        """
        con = ConexionSocio()
        socio = Socio("49116666Q", "Don Juan", "Tenorio", "634824490", "daswirdaendern@jetzt.de")
        con.guardar_socio(socio)
        con.cambiar_socio("49116666Q", "Juan", "Tenorio Valverde", "645636512", "daswirdaendern@morgen.de")
        link = os.path.dirname(__file__)
        link = link[:-5] + 'src/files/socios.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        tmp_file.close()
        self.assertEqual(lines[len(lines)-1], "49116666Q\tJuan\tTenorio Valverde\t645636512\tdaswirdaendern@morgen.de\t"
                         + str(time.strftime("%d/%m/%y"))+"\tTrue\r\n")
        lines.pop()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)
        tmp_file.close()
