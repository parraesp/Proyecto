from unittest import TestCase
from src.conexion_profesor import conexion_profesor
from src.Profesor import Profesor
import time
import os
__author__ = 'alberto'


class TestConexion_profesor(TestCase):
    def test_guardar_profesor(self):
        con = conexion_profesor()
        prof = Profesor("49116666Q", "Don Juan", "Tenorio", "634824490", "daswirdaendern@jetzt.de", 3000, "Completa")
        con.guardar_profesor(prof)
        link = os.path.dirname(__file__)
        link = link[:-6] + '/src/files/profesores.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        self.assertEqual(lines[len(lines)-1], "49116666Q\tDon Juan\tTenorio\t634824490\tdaswirdaendern@jetzt.de\t"+str(time.strftime("%d/%m/%y"))+"\tTrue\t3000\tCompleta\n")
        lines.pop()
        tmp_file.close()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)
        tmp_file.close()

    def test_sacar_profesor(self):
        con = conexion_profesor()
        prof = Profesor("49116666Q", "Don Juan", "Tenorio", "634824490", "daswirdaendern@jetzt.de", 3000, "Completa")
        con.guardar_profesor(prof)
        link = os.path.dirname(__file__)
        link = link[:-6] + '/src/files/profesores.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        self.assertEqual(con.sacar_profesor("profesorInexistente"), -1)
        self.assertIsInstance(con.sacar_profesor("49116666Q"), Profesor)
        lines.pop()
        tmp_file.close()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)
        tmp_file.close()

    def test_dar_baja_profesor(self):
        con = conexion_profesor()
        prof = Profesor("49116666Q", "Don Juan", "Tenorio", "634824490", "daswirdaendern@jetzt.de", 3000, "Completa")
        con.guardar_profesor(prof)
        con.dar_baja_profesor(prof.DNI)
        link = os.path.dirname(__file__)
        link = link[:-6] + '/src/files/profesores.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        self.assertEqual(lines[len(lines)-1], "49116666Q\tDon Juan\tTenorio\t634824490\tdaswirdaendern@jetzt.de\t"
                         + str(time.strftime("%d/%m/%y"))+"\tFalse\t3000\tCompleta\r\n")
        tmp_file.close()
        lines.pop()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)
        tmp_file.close()

    def test_cambiar_profesor(self):
        con = conexion_profesor()
        prof = Profesor("49116666Q", "Don Juan", "Tenorio", "634824490", "daswirdaendern@jetzt.de", 3000, "Completa")
        con.guardar_profesor(prof)
        con.cambiar_profesor("49116666Q","Juan","Tenorio Valverde","645636512","daswirdaendern@morgen.de",5000,"Media")
        link = os.path.dirname(__file__)
        link = link[:-6] + '/src/files/profesores.csv'
        tmp_file = open(link, 'r')
        lines = tmp_file.readlines()
        self.assertEqual(lines[len(lines)-1], "49116666Q\tJuan\tTenorio Valverde\t645636512\tdaswirdaendern@morgen.de\t"+str(time.strftime("%d/%m/%y"))+"\tTrue\t5000\tMedia\r\n")
        lines.pop()
        tmp_file.close()
        tmp_file = open(link, 'w')
        tmp_file.writelines(lines)
        tmp_file.close()
