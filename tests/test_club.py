from unittest import TestCase
from src.Club import Club
from src.Reserva import Reserva
from random import randrange
from datetime import *

__author__ = 'Ricardo'


class TestClub(TestCase):
    def crear_fecha_random(self):
        delta = datetime.strptime('1/1/00 15', '%d/%m/%y %H')
        random_second = randrange(999999999)
        return (delta + timedelta(seconds=random_second)).strftime('%d/%m/%y %H')

    def test_validarDNI(self):
        club = Club()
        self.assertTrue(club.validarDNI('12345678A'))
        self.assertTrue(club.validarDNI('12345678a'))
        self.assertFalse(club.validarDNI('olakase'))
        self.assertFalse(club.validarDNI('123456789'))
        self.assertFalse(club.validarDNI(''))
        self.assertFalse(club.validarDNI('12345678-a'))
        self.assertFalse(club.validarDNI('1234567a8'))

    def test_validarEmail(self):
        club = Club()
        self.assertTrue(club.validarEmail('olakase@hotmail.com'))
        self.assertFalse(club.validarEmail('noesunemail'))

    def test_validarInstalacion(self):
        club = Club()
        self.assertTrue(club.validarInstalacion('inst01'))
        self.assertTrue(club.validarInstalacion('luz'))
        self.assertTrue(club.validarInstalacion('pala3'))
        self.assertFalse(club.validarInstalacion('1234134'))
        self.assertFalse(club.validarInstalacion('inst1'))

    def test_validarTelefono(self):
        club = Club()
        self.assertTrue(club.validarTelefono('123456789'))
        self.assertFalse(club.validarTelefono('1234589'))
        self.assertFalse(club.validarTelefono('abcdefghi'))

    def test_validarFecha(self):
        club = Club()
        self.assertTrue(club.validarFecha('12/12/14 17'))
        self.assertFalse(club.validarFecha('12-12-14 17'))
        self.assertFalse(club.validarFecha('32/22/14 17'))
        self.assertFalse(club.validarFecha('12/20/14 17'))
        self.assertFalse(club.validarFecha('12/12/14 17:00'))

    def test_crear_reserva(self):
        fecha = self.crear_fecha_random()
        club = Club()
        self.assertIsInstance(club.crear_reserva('12345678A', fecha, 'inst01'), Reserva)
        res1 = club.crear_reserva('11111111A', '01/01/01 15', 'inst01')
        self.assertEqual(-1, res1)
        res2 = club.crear_reserva('12345678A', fecha, 'inst01')
        self.assertEqual(-1, res2)

    def test_consultar_reserva(self):
        club = Club()
        fecha = self.crear_fecha_random()
        self.assertIsInstance(club.consultar_reserva('12345678A', '27/04/01 22'), Reserva)
        self.assertEqual(-1, club.consultar_reserva('12345678A', fecha))
        self.assertEqual(-1, club.consultar_reserva('12223334A', fecha))
        self.assertEqual(-1, club.consultar_reserva('12223334A', '27/04/01 22'))

    def test_cancelar_reserva(self):
        fecha = self.crear_fecha_random()
        club = Club()
        club.crear_reserva('12345678A', fecha, 'inst02')
        self.assertIsInstance(club.cancelar_reserva('12345678A', fecha), Reserva)
        self.assertEqual(-1, club.cancelar_reserva('12345678A', fecha))
        self.assertEqual(-1, club.cancelar_reserva('12345555A',fecha))