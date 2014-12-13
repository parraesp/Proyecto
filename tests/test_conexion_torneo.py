from unittest import TestCase
from src.Socio import Socio
from src.Torneo import Torneo
from mockito import mock, when
from src.conexion_torneo import conexion_torneo
from src.conexion_socio import conexion_socio
import os
__author__ = 'Ricardo'


class TestConexion_torneo(TestCase):
    def test_guardar_torneo_fichero(self):
        socio = mock(Socio)
        when(socio).get_DNI().thenReturn('11111111K')
        socios = []
        for i in range(0, 8, 1):
            socios.append(socio)
        con = conexion_torneo(mock(conexion_socio))
        torneo = Torneo('torneoprueba', socios)
        f = open('newFile.txt', 'w')
        con.guardar_torneo_fichero(torneo, f)
        f.close()
        f = open('newFile.txt', 'r')
        row = f.readlines()
        f.close()
        self.assertEqual(row[0], "torneoprueba\t11111111K\t11111111K\t11111111K\t11111111K\t11111111K\t11111111K"
                                 "\t11111111K\t11111111K\tp2\t\tp3\t\tp1\t\tp6\t\tp7\t\tp4\t\tp5\t\t\n")
        os.remove('newFile.txt')

    def test_sacar_torneo(self):
        con = conexion_torneo(mock(conexion_socio))
        self.assertIsInstance(con.sacar_torneo('calidad'), Torneo)
        self.assertEqual(-1, con.sacar_torneo('probando'), Torneo)


    def test_borrar_torneo(self):
        socio = mock(Socio)
        socio = mock(Socio)
        when(socio).get_DNI().thenReturn('11111111K')
        socios = []
        for i in range(0, 8, 1):
            socios.append(socio)
        con = conexion_torneo(mock(conexion_socio))
        torneo = Torneo('torneoprueba', socios)
        con.guardar_torneo(torneo)
        con.borrar_torneo(torneo)
        link = os.path.dirname(__file__)
        link = link[:-5] + 'src/files/torneos.csv'
        tmp_file = open(link, 'r')
        row = tmp_file.readlines()
        self.assertNotEquals(row[0], "torneoprueba\t11111111K\t11111111K\t11111111K\t11111111K\t11111111K\t11111111K"
                                     "\t11111111K\t11111111K\tp2\t\tp3\t\tp1\t\tp6\t\tp7\t\tp4\t\tp5\t\t\n")
        tmp_file.close()