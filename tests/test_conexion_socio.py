from unittest import TestCase
from src.conexion_socio import conexion_socio
from src.Socio import Socio
import time
import os

__author__ = 'alberto'


class TestConexion_socio(TestCase):
    def test_guardar_socio(self):
        con = conexion_socio()
        socio = Socio("49116666Q", "Don Juan", "Tenorio", "634824490", "daswirdaendern@jetzt.de")
        con.guardar_socio(socio)
        link = os.path.dirname(__file__)
        link = link[:-5] + 'src/files/socios.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        self.assertEqual(lines[len(lines)-1], "49116666Q\tDon Juan\tTenorio\t634824490\tdaswirdaendern@jetzt.de\t"+str(time.strftime("%d/%m/%y"))+"\tTrue\n")
        lines.pop()
        tmp_file.close()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)
        con.dar_baja_socio(socio)

    def test_sacar_socio(self):
        con = conexion_socio()
        socio = Socio("49116666Q", "Don Juan", "Tenorio", "634824490", "daswirdaendern@jetzt.de")
        con.guardar_socio(socio)
        link = os.path.dirname(__file__)
        link = link[:-5] + 'src/files/socios.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        self.assertEqual(con.sacar_socio("socioInexistente"), -1)
        self.assertIsInstance(con.sacar_socio("49116666Q"), Socio)
        lines.pop()
        tmp_file.close()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)

    def test_dar_baja_socio(self):
        con = conexion_socio()
        socio = Socio("49116666Q", "Don Juan", "Tenorio", "634824490", "daswirdaendern@jetzt.de")
        con.guardar_socio(socio)
        link = os.path.dirname(__file__)
        link = link[:-5] + 'src/files/socios.csv'
        tmp_file = open(link, 'r')
        con.dar_baja_socio(socio)
        lines = tmp_file.readlines()
        self.assertEqual(lines[len(lines)-1], "49116666Q\tDon Juan\tTenorio\t634824490\tdaswirdaendern@jetzt.de\t"+str(time.strftime("%d/%m/%y"))+"\tFalse\r\n")
        lines.pop()
        tmp_file.close()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)

    def test_cambiar_socio(self):
        con = conexion_socio()
        socio = Socio("49116666Q", "Don Juan", "Tenorio", "634824490", "daswirdaendern@jetzt.de")
        con.guardar_socio(socio)
        con.cambiar_socio("49116666Q","Juan","Tenorio Valverde","645636512","daswirdaendern@morgen.de")
        link = os.path.dirname(__file__)
        link = link[:-5] + 'src/files/socios.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        self.assertEqual(lines[len(lines)-1], "49116666Q\tJuan\tTenorio Valverde\t645636512\tdaswirdaendern@morgen.de\t"+str(time.strftime("%d/%m/%y"))+"\tTrue\r\n")
        lines.pop()
        tmp_file.close()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)